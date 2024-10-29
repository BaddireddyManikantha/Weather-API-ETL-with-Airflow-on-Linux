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
