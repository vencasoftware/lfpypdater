import pandas as pd

class datahandler:
    
    def __init__(self, file_route):
        self.file = file_route
        self.df = pd.read_csv(self.file)

    # Cambio il valore di alcohol status
    def __alcoholConvert(self, alcohol_status):
        if alcohol_status == 'Never':
            return 1
        elif alcohol_status == 'Occasionally':
            return 2
        elif alcohol_status == 'Regularly':
            return 3

    # Cambio il valore di diabetic status
    def __diabetesConvert(self, diabetes_status):
        if diabetes_status == 'Non-diabetic':
            return 1
        elif diabetes_status == 'Diabetic':
            return 2

    # Creo un array di json con i dati che mi servono nel csv
    def getDataReady(self):
        data = []

        for rownum in range(len(self.df)):
            data.append(
                {
                    'waist_unit':       self.df.iloc[rownum]['waist_unit'],
                    'waist':            self.df.iloc[rownum]['waist'],
                    'weight_unit':      self.df.iloc[rownum]['weight_unit'],
                    'weight':           self.df.iloc[rownum]['weight'],
                    'height_unit':      self.df.iloc[rownum]['height_unit'],
                    'height':           self.df.iloc[rownum]['height'],
                    'alcohol_status':   self.__alcoholConvert(self.df.iloc[rownum]['alcohol_status']),
                    'diabetes_status':  self.__diabetesConvert(self.df.iloc[rownum]['diabetes_status']),
                    'sbp':              self.df.iloc[rownum]['sbp'],
                    'dbp':              self.df.iloc[rownum]['dbp'],
                    'alt_unit':         self.df.iloc[rownum]['alt_unit'],
                    'alt':              self.df.iloc[rownum]['alt'],
                    'ast_unit':         self.df.iloc[rownum]['ast_unit'],
                    'ast':              self.df.iloc[rownum]['ast'],
                    'tg_unit':          self.df.iloc[rownum]['tg_unit'],
                    'tg':               self.df.iloc[rownum]['tg'],
                    'hba1c_unit':       self.df.iloc[rownum]['hba1c_unit'],
                    'hba1c':            self.df.iloc[rownum]['hba1c'],
                    'glu_unit':         self.df.iloc[rownum]['glu_unit'],
                    'fasting_glu':      self.df.iloc[rownum]['fasting_glu'],
                    'ins_unit':         self.df.iloc[rownum]['ins_unit'],
                    'fasting_ins':      self.df.iloc[rownum]['fasting_ins'],
                    'fl-submit': 'Submit'
                    })
        return data

    def exportResults(self, prob, prob_level, errs):
        self.df['probabilty'] = pd.Series(prob)
        self.df['probabilty_level'] = pd.Series(prob_level)
        self.df['errors'] = pd.Series(errs)

        results_route = self.file[:-4] + '_RESULTS.csv'
        self.df.to_csv(results_route, index=False)

def main():
    print(datahandler('../DOCS/EXAMPLE.CSV').getDataReady())

if __name__ == '__main__':
    main()