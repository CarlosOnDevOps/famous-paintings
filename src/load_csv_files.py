#########################################################################
# Connect to your database
#########################################################################
import pandas as pd
from sqlalchemy import create_engine

# 1. create a variable to store the connection details to the PostgreSQL database
# syntax: database://username:password@host/database_name
# Note that you should already have created your database in PostgreSQL first, before importing any data
connection_string = "postgresql://postgres:admin@localhost/famous_paintings"

# 2. create the database engine
db = create_engine(connection_string)

# 3. create the connection and store it in a variable
connection = db.connect()

# Note lines 2-13 is the only code you need to connect to your PostgreSQL database

#########################################################################
# Load the data into dataframes (SINGLE FILE)
#########################################################################
# 1. load in CSV files
df = pd.read_csv("references/artist.csv")
df.head()
df.info()

# 2. load data from the DataFrame to an SQL table
df.to_sql(
    "artist", con=connection, if_exists="replace", index=False
)  # creates table named artist
# Note, these are the only 4 arguments you need to provide when loading DataFrames into SQL tables
# Note, lines 24-29 are used when working with 1 single file

#########################################################################
# Load the data into dataframes (MULTIPLE FILES)
#########################################################################
# 1. create a list to store your files
csv_files = [
    "artist",
    "canvas_size",
    "image_link",
    "museum_hours",
    "museum",
    "product_size",
    "subject",
    "work",
]

# 2. open a loop
for file in csv_files:
    df = pd.read_csv(f"references/{file}.csv")
    df.to_sql(file, con=connection, if_exists="replace", index=False)
