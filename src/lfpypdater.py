import requests, easygui, sys, os, datahandler
from bs4 import BeautifulSoup


# Apre la finestra per scegliere il file di importazione
def openFile():
    file = easygui.fileopenbox(title="Seleziona un file CSV", default="*.csv")
    if file == None:
        sys.exit(0)
    else:
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".csv" or ".CSV":
                    return file
        else:
            if easygui.ccbox(msg="Devi selezionare un file con estensione .csv!", title="ERRORE!"):
                openFile()
            else:
                sys.exit(0)
        

def main():

    # Scelgo il file
    file_route = openFile()

    # Ottengo un array di json pronto per il request
    data = datahandler.readCSV(file_route)

    # interrogo il sito
    probabilility, probability_level, errors = [], [], []
    for riga in data:
        res = requests.post('https://www.predictliverfat.org/check-liver-models.php', data=riga)

        model_info = BeautifulSoup(res.text, 'html5lib').find("span", class_="model-info").text
        if model_info.split()[-1][-2:].isnumeric():
            probabilility.append(model_info.split()[0])
            probability_level.append(model_info.split()[-1])
            errors.append(None)
        else:
            probabilility.append(None)
            probability_level.append(None)
            errors.append(model_info)
    
    print (probabilility, probability_level, errors)

if __name__ == "__main__":
    main()