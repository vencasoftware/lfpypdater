import requests
from bs4 import BeautifulSoup

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