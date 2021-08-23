import requests, easygui, sys, os, datahandler
from bs4 import BeautifulSoup

def openFile():
    file = easygui.fileopenbox(title="Seleziona un file CSV", default="*.csv")
    if file == None:
        sys.exit(0)
    else:
        filename, file_extension = os.path.splitext(file)
        if file_extension != ".csv" | ".CSV":
            if easygui.ccbox(msg="Devi selezionare un file con estensione .CSV!", title="ERRORE!"):
                openFile()
            else:
                sys.exit(0)
        elif file_extension == ".csv" | ".CSV":
            return file
            

def findprobability():
    res = requests.post('https://www.predictliverfat.org/check-liver-models.php', data={'waist_unit': 'cm',
                                                                                        'waist': '70',
                                                                                        'weight_unit': 'kg',
                                                                                        'weight': '40',
                                                                                        'height_unit': 'cm',
                                                                                        'height': '140',
                                                                                        'alcohol_status': '3',
                                                                                        'diabetes_status': '1',
                                                                                        'sbp': '22',
                                                                                        'dbp': '33',
                                                                                        'alt_unit': 'U/L',
                                                                                        'alt': '5',
                                                                                        'ast_unit': 'U/L',
                                                                                        'ast': '5',
                                                                                        'tg_unit': 'mmol/L',
                                                                                        'tg': '5',
                                                                                        'hba1c_unit': 'mmol/mol',
                                                                                        'hba1c': '11',
                                                                                        'glu_unit': 'mmol/L',
                                                                                        'fasting_glu': '5',
                                                                                        'ins_unit': 'pmol/L',
                                                                                        'fasting_ins': '5',
                                                                                        'fl-submit': 'Submit'})

    model_info = BeautifulSoup(res.text, 'html5lib').find("span", class_="model-info").text
    probability_level = model_info.split()[0]
    probability = model_info.split()[-1]

    print(probability + " " + probability_level)

def main():
    data_route = openFile()

if __name__ == "__main__":
    main()