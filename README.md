# LFPYPDATER
Codice per inserimenti massivi di dati sul sito per la [Predizione del grasso nel fegato](https://www.predictliverfat.org/#prediction_models)

## File CSV in import

il file csv da cui verranno presi i dati dovrà avere ALMENO queste colonne:

* waist_unit     ( = Waist Unit )
* waist     ( = Waist )
* weight     ( = Weight )
* weight_unit     ( = Weight Unit )
* height     ( = Height )
* height_unit     ( = Height Unit )
* alcohol_status     ( = Alcohol consumption )
* diabetes_status     ( = Diabetes status )
* sbp     ( = Blood pressure (mm Hg) Systolic  )
* dbp     ( = Blood pressure (mm Hg) Diastolic  )
* alt_unit     ( = Alanine transaminase (ALT) Unit )
* alt     ( = Alanine transaminase (ALT) )
* ast_unit     ( = Aspartate transaminase (AST) unit )
* ast     ( = Aspartate transaminase (AST) )
* tg_unit     ( = Triglyceride levels (TG) Unit )
* tg     ( = Triglyceride levels (TG) )
* hba1c_unit     ( = HbA1C Unit )
* hba1c     ( = HbA1C )
* glu_unit     ( = Fasting glucose Unit )
* fasting_glu     ( = Fasting glucose )
* ins_unit     ( = Fasting insulin Unit )
* fasting_ins     ( = Fasting insulin )


: : : Vedi [CSV_TEMPLATE.csv](DOCS/TEMPLATE.csv) : : :


### Unità di misura

Le unità di misura dovranno essere PRECISAMENTE tra queste alternative elencate per i vari tipi di dato

* Waist Unit
    * cm
    * in
* Weight Unit
    * kg
    * lb
* Height Unit
    * cm
    * in
* Alanine transaminase (ALT) Unit
    * U/L
    * µkat/L
* Aspartate transaminase (AST) unit
    * U/L
    * µkat/L
* Triglyceride levels (TG) Unit
    * mmol/L
    * mg/dL
* HbA1C Unit
    * mmol/mol
    * %

_il sito presenta un errore per cui per questi due campi vale solo una unità di misura_
* Fasting glucose Unit
    * mmol/L
* Fasting insulin Unit
    * pmol/L








