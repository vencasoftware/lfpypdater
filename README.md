# LFPYPDATER
Codice per inserimenti massivi di dati sul sito per la [Predizione del grasso nel fegato](https://www.predictliverfat.org/#prediction_models)

## Request + Response
Utilizzo la libreria *requests* per interpellare la pagina https://www.predictliverfat.org/check-liver-models.php adibita al calcolo dell'algoritmo.

1. Invio una Richiesta di tipo POST con la seguente formattazione di dati
```json
{
    'waist_unit': 'cm',
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
    'fl-submit': 'Submit'   }
```

2. Ricevendo come risposta:
```html
<h4>Submitted values, converted to default units</h4><dl id="submitted"><dt>Waist circumference <span class="unit">(cm)</span></dt><dd>70</dd><dt>Weight <span class="unit">(kg)</span></dt><dd>40</dd><dt>Height <span class="unit">(cm)</span></dt><dd>140</dd><dt>Systolic blood pressure <span class="unit">(mm Hg)</span></dt><dd>22</dd><dt>Diastolic blood pressure <span class="unit">(mm Hg)</span></dt><dd>33</dd><dt>Alanine transaminase <span class="unit">(U/L)</span></dt><dd>5</dd><dt>Aspartate transaminase <span class="unit">(U/L)</span></dt><dd>5</dd><dt>Triglyceride 
levels <span class="unit">(mmol/L)</span></dt><dd>5</dd><dt>HbA1C <span class="unit">(mmol/mol)</span></dt><dd>11</dd><dt>Fasting insulin <span class="unit">(pmol/L)</span></dt><dd>5</dd><dt>Fasting glucose <span class="unit">(mmol/L)</span></dt><dd>5</dd><dt>Alcohol consumption </dt><dd>Regularly</dd><dt>Diabetes status </dt><dd>Non-diabetic</dd></dl><h4>Prediction by the best matching model for the variables in use</h4><ul><li><span class="model-label">Model 3: </span><span class="model-info">Low risk of fatty liver, probability: 0.30</span></li></ul>
```
3. Dalla risposta non resta che estrarre la stringa con classe "_model-info_" usando la libreria *beautifulsoup4*