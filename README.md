## Project "Disaster Response Pipeline"

This project is part of my Udacity´s Data Scientist Nanodegree Program. 

### Table of Contents
 
1. [Project Motivation](#motivation)
2. [Data](#data)
3. [Provided Files](#files)
4. [Instructions](#instructions)
5. [Results](#results)
6. [Licensing](#licensing)

## Project Motivation <a name="motivation"></a>

Developing a "Disaster Response Pipeline" is one of the projects within the Udacity Data Scientist Nanodegree Program. The aim of this project is to optimize the process of message processing and forwarding during disasters to ensure that information gets to the right places quickly and efficiently.

This requires the use of natural language processing to classify these messages with the help of machine learning algorithms. Such an application can help to alert the right civil protection authorities as quickly as possible in the event of an emergency. 

## Data <a name="data"></a>
The Appen (former Figure8) dataset includes around 25k messages of disaters all around the world. The focus of the project ist to classify the incoming messages correctly to the corresponding categories. </br>
The data contains of the following two CSV files:

<ul>
  <li>messages.csv: Contains around 25k messages
  <li>categories.csv: Contains the 36 categories 
</ul>

Further information about the original dataset can be found at [Appen](https://www.appen.com/) former Figure8.

## Provided Files <a name="files"></a>

```
├── README.md          
│
├── models                          <- Trained models and ML pipeline
│   ├── classifier.pkl              <- Saved model
│   └── train_classifier.py         <- Script to train the model
│
├── data                            <- Raw, processed Data and ETL pipeline
│   ├── disaster_messages.csv       <- Raw data dto process (messages)
│   ├── disaster_categories.csv     <- Raw data dto process (categories)
│   ├── DisasterResponse.db         <- SQL database to save clean data to
│   └── process_data.py             <- Script to process the data
│
├── JupyterNotebook                 <- Jupyter notebooks with ML and ETL pipelines
│
└── App                             <- Source code for use in this project.
    ├── templates              
    │   ├── go.html                 <- Classification result page of web app
    │   └── master.html             <- Main page of web app
    └── run.py                      <- Flask file that runs app
```

## Instructions <a name="instructions"></a>

1. Clone or download the repo and Open terminal and navigate to the project folder

2. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database</br>
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves</br>
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

3. Go to `app` directory: `cd app`

4. Run your web app: `python run.py`

5. Click the `PREVIEW` button to open the homepage or go to http://loclhost:3001 or http://0.0.0.0:3001

## Results <a name="results"></a>


## Licensing <a name="licensing"></a>
Thanks to Appen (former Figure8) and Udacity for providing the data.
