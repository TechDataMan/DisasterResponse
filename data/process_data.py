import sys

# import libraries
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Load Messages and Categories from filepaths and merge them into a DataFrame
    
    Parameter:
        messages_filepath: Path to the CSV file containing messages
        categories_filepath: Path to the CSV file containing categories
    
    Return:
        df: Merged Dataset (Messages and Categories)
    """
    
    # Load messages dataset:
    messages =  pd.read_csv(messages_filepath)
    # Load categories dataset:
    categories = pd.read_csv(categories_filepath)
    # Merge datasets:
    df = pd.merge(messages, categories, on = 'id')

    return df

def clean_data(df):
    """ 
    The function cleans up the previously imported data. Data cleaning is carried out in four steps:
        1. Split categories into separate category columns.
        2. Convert category values to just numbers 0 or 1.
        3. Replace categories column in the DataFrame with new category columns.
        4. Remove duplicates from the dataframe.
        
    Parameter: 
        df (pandas.DataFrame): Dataframe which the merged message and categorie data.
        
    Return: 
        df (pandas.DataFrame): Cleaned DataFrame
    """    
    
    # STEP 1: Split categories into separate category columns:
    categories = df['categories'].str.split(pat=';', expand = True)
    # Select the first row of the categories dataframe:
    row = categories.iloc[0]
    # Extract a list of new column names for categories:
    category_colnames = row.str.split('-', expand=True)[0]
    # Rename the columns of `categories`:
    categories.columns = category_colnames
    
    # STEP 2: Convert category values to just numbers 0 or 1:
    # Define function for take/check the last character of the string and convert str2int:
    def replace_strings(x):
    # All values not equal to 0, 1 become NaN's:
        return 1 if '-1' in x else 0 if '-0' in x else np.nan 
    
    # Use function 'replace_strings' on the hole dataframe:
    categories = categories.applymap(replace_strings)
    # Find all rows with NaN's - save for further action after 'concat':
    rows_to_delete = categories[categories.isna().any(axis=1)].index.tolist()
    
    # STEP 3: Replace categories column in the DataFrame with new category columns.
    # Drop the original categories column from `df`:
    df.drop(['categories'], axis=1, inplace=True)
    # Concatenate the original dataframe with the new `categories` dataframe:
    df = pd.concat([df,categories], axis=1)
    # Delete the lines with the previously defined NaNs (rows_to_delete):
    df = df.drop(rows_to_delete)
    
    # STEP 4: Remove duplicates from the dataframe:
    # Drop duplicates:
    df.drop_duplicates(inplace=True)
    
    # Return cleaned dataframe:
    return df

def save_data(df, database_filename):
    """ 
    Function to save the cleaned dataframe in a SQLite database.
        
    Parameter: 
        df (pandas.DataFrame): Dataframe which includes the loaded and cleaned data.
        database_filename (string): Relative filename (path + database name) of the database where the data should be stored.
        
    Return: 
        !!! No Return !!!
    """    
    # Save the cleaned dataset as an sqlite database:
    engine = create_engine('sqlite:///'+database_filename)
    df.to_sql('tab_DisasterResponse', engine, index=False, if_exists='replace')
    
    return

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()