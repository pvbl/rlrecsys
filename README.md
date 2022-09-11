rlrecsys
==============================

TFM idal UV - Análisis de modelos de RL para sistemas de recomendación tipo Slate.
En este proyecto se evalúan diferentes tipos de algoritmos de RL para esta tipología de entorno.

Instalación
------------
1. Instalar conda
2. conda env create -f conda.yml


Principal organización del proyecto
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── conda.yml   <- The requirements file for reproducing the analysis environment, e.g.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

Ejecución
---------------
Los principales notebooks del proyecto se encuentran en la carpeta notebooks.
- [01_tfm_rlrecsys-env_InterestEvol-models.ipynb](notebooks/01_tfm_rlrecsys-env_InterestEvol-models.ipynb): Contiene el desarrollo de los modelos utilizando el entorno de Interest Evolution.
- [02_tfm_rlrecsys-env_LTS-models.ipynb](notebooks/02_tfm_rlrecsys-env_LTS-models.ipynb): Contiene el desarrollo de los modelos utilizando el entorno de recsim de Long Term Satisfaction y una modificación del mismo.
- [03_tfm_rlrecsys-models_offline.ipynb](notebooks/03_tfm_rlrecsys-models_offline.ipynb): Contiene el desarrollo de los modelos offline generados a partir del dataset creado con la DQL del primer notebook.
- [04_tfm_rlrecsys-models_deploy.ipynb](notebooks/04_tfm_rlrecsys-models_deploy.ipynb): Ejemplo de puesta en producción de un modelo offline.

En todos los notebooks, las funciones que se van generando en el mismo son guardadas en scripts en la carpeta src/ por motivos de buenas prácticas.
