import requests, easygui, sys, os
from bs4 import BeautifulSoup
from datahandler import datahandler


# Apre la finestra per scegliere il file di importazione
def openFile():
    file = easygui.fileopenbox(title="Seleziona un file CSV", default="*.csv")
    if file == None:
        sys.exit(0)
    else:
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".csv" or file_extension == ".CSV":
                    return file
        else:
            if easygui.ccbox(msg="Devi selezionare un file con estensione .csv!", title="ERRORE!"):
                openFile()
            else:
                sys.exit(0)

def avanzanmento(r):
    barra = {
        '0.0' : '[          ]',
        '0.1' : '[=         ]',
        '0.2' : '[==        ]',
        '0.3' : '[===       ]',
        '0.4' : '[====      ]',
        '0.5' : '[=====     ]',
        '0.6' : '[======    ]',
        '0.7' : '[=======   ]',
        '0.8' : '[========  ]',
        '0.9' : '[==========]',
        '1.0' : 'Operazione terminata!'
    }

    print(str(int(r * 100)) + "% " + barra['{:.1f}'.format(r)], end='\r')

def main():

    # Scelgo il file
    file_route = openFile()

    # Ottengo un array di json pronto per il request
    dataobj = datahandler(file_route)
    data = dataobj.getDataReady()

    # interrogo il sito
    probabilility, probability_level, errors = [], [], []

    # necessari per la barra di avanzamento
    lunghezza, i = len(data), 0
    for riga in data:
        avanzanmento(i / lunghezza)
        i += 1
        res = requests.post('https://www.predictliverfat.org/check-liver-models.php', data=riga)

        # Faccio il parsing del risutato e seleziono le parole che mi indicano la 
        # probabilità e il livello di probabilità.
        # Se la stringa che dovrebbe indicare la probabilità non è un numero
        # vuol dire che c'è un errore con i dati inseriti dunque aggiungo uno spazio
        # vuoto agli array di probabilità e stampo tutto il risultato
        # nell'array dell'errore
        model_info = BeautifulSoup(res.text, 'html5lib').find("span", class_="model-info").text
        if model_info.split()[-1][-2:].isnumeric():
            probabilility.append(model_info.split()[0])
            probability_level.append(model_info.split()[-1])
            errors.append(None)
        else:
            probabilility.append(None)
            probability_level.append(None)
            errors.append(model_info)
    
    avanzanmento(1.0)

    # Esporto i risultati
    dataobj.exportResults(probabilility, probability_level, errors)
    
    

if __name__ == "__main__":
    main()