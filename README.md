## Project "Disaster Response Pipeline"

This project is part of my Udacity´s Data Scientist Nanodegree Program. 

### Table of Contents
 
1. [Project Motivation](#motivation)
2. [Data](#data)
3. [Provided Files](#files)
4. [Libraries](#libraries)
5. [Results](#results)
6. [Licensing](#licensing)

## Project Motivation <a name="motivation"></a>

Writing a data science blog post is one of the projects within the Udacity Data Scientist Nanodegree Program. The StackOverflow Annual Developer Survey from 2024 was chosen as the data basis.

## Data <a name="data"></a>
The Appen (former Figure Eight) dataset includes around 25k messages of disaters all around the world. The focus of the project ist to classify the incoming messages correctly to the corresponding categories. </br>
The data contains of the following two CSV files:

<ul>
  <li>messages.csv: Contains around 25k messages
  <li>categories.csv: Contains the 36 categories 
</ul>

Further information about the original dataset can be found at [Appen](https://www.appen.com/) former Figure Eight.

## Provided Files <a name="files"></a>

```
├── README.md          
│
├── models                     <- Trained models and ML pipeline
│   ├── classifier.pkl         <- Saved model
│   └── train_classifier.py    <- Script to train model
│
├── data                       <- Raw, processed Data and ETL pipeline
│   ├── messages.csv           <- Raw data messages
│   ├── categories.csv         <- Raw data categories
│   ├── DisasterResponse.db    <- SQL database with processed data
│   └── process_data.py        <- Script to process the data
│
├── JupyterNotebook            <- Jupyter notebooks with ML and ETL pipelines
│
└── App                        <- Source code for use in this project.
    ├── templates              <- Flask html templates 
    └── run.py                 <- Scripts to create start Flask server. 
```

## Full Instructions

- Installation
    Install Python 3.5+
    Run ```pip install -r requirements.txt```
- Prepare data
    1. Clone or download the repo
    2. Open terminal and navigate to the project folder
    3. Run ```python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db```
- Train model
    5. Run ```python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl```

- Start Web app
    6. Run ```cd app```
    7. Run ```python run.py```
    8. Open web browser and go to http://loclhost:3001 or http://0.0.0.0:3001

## Results <a name="results"></a>


## Licensing <a name="licensing"></a>
Thanks to Appen and Udacity for providing the data.
