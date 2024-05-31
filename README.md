# Project Management System (PMS) Streamlit Dashboard

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)

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
