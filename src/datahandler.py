import pandas as pd

def readCSV(file):
    df = pd.read_csv(file)
    data = []

    for rownum in range(len(df)):

        # Cambio il valore di alcohol status
        if df.iloc[rownum]['alcohol_status'] == 'Never':
            alcohol_status = 1
        elif df.iloc[rownum]['alcohol_status'] == 'Occasionally':
            alcohol_status = 2
        elif df.iloc[rownum]['alcohol_status'] == 'Regularly':
            alcohol_status = 3

        # Cambio il valore di diabetic status
        if df.iloc[rownum]['diabetes_status'] == 'Non-diabetic':
            diabetic_status = 1
        elif df.iloc[rownum]['diabetes_status'] == 'Diabetic':
            diabetic_status = 2
        data.append(
            {
                'waist_unit':       df.iloc[rownum]['waist_unit'],
                'waist':            df.iloc[rownum]['waist'],
                'weight_unit':      df.iloc[rownum]['weight_unit'],
                'weight':           df.iloc[rownum]['weight'],
                'height_unit':      df.iloc[rownum]['height_unit'],
                'height':           df.iloc[rownum]['height'],
                'alcohol_status':   alcohol_status,
                'diabetes_status':  diabetic_status,
                'sbp':              df.iloc[rownum]['sbp'],
                'dbp':              df.iloc[rownum]['dbp'],
                'alt_unit':         df.iloc[rownum]['alt_unit'],
                'alt':              df.iloc[rownum]['alt'],
                'ast_unit':         df.iloc[rownum]['ast_unit'],
                'ast':              df.iloc[rownum]['ast'],
                'tg_unit':          df.iloc[rownum]['tg_unit'],
                'tg':               df.iloc[rownum]['tg'],
                'hba1c_unit':       df.iloc[rownum]['hba1c_unit'],
                'hba1c':            df.iloc[rownum]['hba1c'],
                'glu_unit':         df.iloc[rownum]['glu_unit'],
                'fasting_glu':      df.iloc[rownum]['fasting_glu'],
                'ins_unit':         df.iloc[rownum]['ins_unit'],
                'fasting_ins':      df.iloc[rownum]['fasting_ins'],
                'fl-submit': 'Submit'
                })
    return data

def main():
    readCSV('../DOCS/EXAMPLE.CSV')

if __name__ == '__main__':
    main()