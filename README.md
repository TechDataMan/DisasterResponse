## Project "Disaster Response Pipeline"

This project is part of my Udacity´s Data Scientist Nanodegree Program. 

### Table of Contents
 
1. [Project Motivation](#motivation)
2. [Data](#data)
3. [Files](#files)
4. [Libraries](#libraries)
5. [Results](#results)
6. [Licensing](#licensing)

## Project Motivation <a name="motivation"></a>

Writing a data science blog post is one of the projects within the Udacity Data Scientist Nanodegree Program. The StackOverflow Annual Developer Survey from 2024 was chosen as the data basis.

## Data
The data files associated with this project are from [Figure Eight](https://www.figure-eight.com/dataset/combined-disaster-response-data/)

- messages.csv: 
- categories.csv: 

## Files <a name="files"></a>

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
