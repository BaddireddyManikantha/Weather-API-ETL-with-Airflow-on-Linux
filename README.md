# Weather API ETL with Airflow on Linux
This ETL (Extract, Transform, Load) process automates the task of fetching real-time weather data from an API and saving it as a CSV file on a Linux server using Apache Airflow
# Technologies 
`python`
`airflow`
`pandas`
`bash`
# airflow
Airflow was used in this project to streamline the workflow by managing task scheduling, automation, and monitoring
# ETL
- **Extract**: Weather data is fetched from a weather API for multiple cities using the API's endpoint.
- **Transform**: The API response is processed to extract relevant weather information (e.g., temperature, humidity, location, and conditions).
- **Load**: The cleaned data is saved as a CSV file on the Linux filesystem for further use or analysis.

## API
([http://api.weatherapi.com/v1/](https://www.weatherapi.com/docs/))

# Features
- Fetches real-time weather data for multiple cities.
- Transforms and stores data in a structured CSV file.
- Automates the entire process using Airflow DAGs.
- Handles task scheduling and retries efficiently with Airflow.

# Airflow Windows Installation
**Windows subsystem for Linux**

Run this in windows search

Turn Windows features on or off

Run this in command prompt

wsl --install

Step 1: Update Your System

sudo apt update

Step 2: Install Python and Virtual Environment

sudo apt install python3 python3-pip

Install virtualenv:

sudo pip3 install virtualenv

Step 3: Create and Activate a Virtual Environment

mkdir airflow_project

cd airflow_project

Create a virtual environment:

virtualenv airflow_venv

source airflow_venv/bin/activate

Step 4: Install Apache Airflow with Constraints

Set Airflow constraints:

AIRFLOW_VERSION=2.10.4

PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

Install Apache Airflow using constraints:

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

Step 5: Initialize the Database

Set the Airflow home directory:

export AIRFLOW_HOME=~/airflow

Initialize the database:

airflow db init

Step 6: Start Airflow

Start the web server:

airflow webserver --port 8085

source ~/airflow_project/airflow_venv/bin/activate

airflow scheduler

Accessing Airflow

http://localhost:8085

Additional Steps

Set up the Airflow user (Optional):

airflow users create
--username admin
--firstname gowtham
--lastname sb
--role Admin
--email test@admin.com




