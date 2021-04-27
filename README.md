# Locations

The features directory contains all the features used for machine learning. Included in the features directory are the raw GFA data "MDF_DMREF_Metallic_Glasses_v5.csv" before feature processing.

The plots directory contains the figures used throughout the paper and their data in either a json lines or pickle form.

The model directory contains the final XGBoost model fit to build the shapley value summary plot.

```
├── README.md
├── features
│   ├── MDF_DMREF_Metallic_Glasses_v5
│   │   ├── MDF_DMREF_Metallic_Glasses_v5.csv
│   │   └── update_metallic_glasses.py
│   ├── features_dmax_cts
│   │   ├── features_dmax_cts.csv
│   │   ├── features_dmax_cts.json
│   │   └── upload.py
│   ├── features_gfa_cts
│   │   ├── features_gfa_cts.csv
│   │   ├── features_gfa_cts.json
│   │   ├── requirements.txt
│   │   └── upload.py
│   └── prsd_features_gfa_cts
│       └── prsd_features_gfa_cts.csv
├── model
│   ├── features_gfa_cts.csv
│   ├── run.py
│   ├── shap.pickle
│   ├── shap.png
│   └── xgboost_model.pickle
└── plots
    ├── classification
    │   ├── original
    │   │   ├── PR_positive.png
    │   │   └── PR_positive_data.csv
    │   └── prsd
    │       ├── PRSD_PR_positive_data.csv
    │       └── PR_positive_PRSD.png
    ├── regression
    │   ├── parity.jsonl
    │   ├── parity.png
    │   ├── parity_cv.pickle
    │   └── parity_cv.png
    ├── tgm
    │   ├── tgm.jsonl
    │   └── tgm.png
    ├── tprime
    │   ├── desktop.ini
    │   ├── tprime.jsonl
    │   └── tprime.png
    ├── tstar
    │   ├── tstar.jsonl
    │   └── tstar.png
    ├── viscosity
    │   ├── plot.py
    │   ├── visc_cu50zr50_set_1-run_1_1100K.csv
    │   └── visc_cu50zr50_set_1-run_1_1100K.png
    └── xgb_select_class
        ├── shap.pickle
        └── shap.png
```
