# Project Management System (PMS) Streamlit Dashboard

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [NOTE](#note)

## Project Overview
The Project Management System (PMS) Streamlit Dashboard is designed to provide a comprehensive overview of projects managed by government organizations across India. It includes interactive visualizations and metrics that allow users to track project progress, budget, timelines, and other key performance indicators.

## Features   
- Interactive dashboards with various project metrics
- Visualizations created with Altair and Streamlit
- Integration with a MySQL database to fetch real-time data

## Installation
To get started with the PMS Streamlit Dashboard, follow the steps below:

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/pms-streamlit-dashboard.git
    cd pms-streamlit-dashboard
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**
    - **Windows**
        ```sh
        venv\Scripts\activate
        ```
    - **macOS/Linux**
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**
    ```sh
    pip install -r requirements.txt

    ## Usage
To run the Streamlit application:

1. Ensure your MySQL database is running and properly configured.
2. Set the necessary environment variables as described in the [Configuration](#configuration) section.
3. Start the Streamlit app
    ```sh
    streamlit run app.py
    ```

Open your web browser and navigate to `http://localhost:8501` to view the dashboard.

## Configuration
Create a `.env` file in the root directory of your project and add the following environment variables:

```plaintext
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
SECRET_KEY=your_secret_key_for_authentication(if any )
```
## Dependencies
The key dependencies required for this project are listed in the requirements.txt file. Some of the main libraries include:

- Streamlit
- Pandas
- Altair
- MySQL Connector
- dotenv
To install all dependencies, run:
```
pip install -r requirements.txt
```
## NOTE 
- when connecting woth the databse , add the databse connector for the specific database and after fetching the data convert it into df as mentioned below:
   ```import mysql.connector
   import os
   from dotenv import load_dotenv

   load_dotenv()

   def get_db_connection():
       return mysql.connector.connect(
           host=os.getenv("DB_HOST"),
           user=os.getenv("DB_USER"),
           password=os.getenv("DB_PASSWORD"),
           database=os.getenv("DB_NAME")
       )
   ```

If the above code snippet creates error, replace it with the below given snippet if the credentials provided are correct  :
- Connect the databse
   ```mydb = mysql.connector.connect(
    host="your_host”,
    user="your_user",
    password="your_password",
    database="the name of yr database ",
    port = 3306( default)    connect it with the port your server is connected to.
)
 ```
 - Create the cursor after the database connection to fetch the data from database :
   ``` def fetch_data():
    db_connection = get_db_connection()
    mycursor = db_connection.cursor()
    mycursor.execute("SELECT * FROM flights;")
    data = mycursor.fetchall()
    column_names = [i[0] for i in mycursor.description]
    db_connection.close()
    return data,column_names
data,column_names= fetch_data()
df= pd.DataFrame(data,columns =column_names)
print(df)
 ```
- the fetch_data is provided as an example.
- Remember not to commit the .env file to your Git repository, especially if it contains sensitive information like passwords or API keys. You should add .env to your .gitignore file to ensure it's not accidentally included in your commits. If you haven't already created a .gitignore file, you can create one in the root directory of your project and add ".env" to it. This will prevent Git from tracking changes to the .env file.
- this can de done :
  ```.gitignore
  .env
   ```
   
