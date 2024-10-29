import requests as re
import pandas as pd

def extract(api_key, cities):
    # List to store weather data for all cities
    all_data = []

    # Loop through each city and fetch weather data
    for city in cities:
        print(f"Fetching data for: {city}")
        res = re.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")
        
        if res.status_code == 200:  # Check if the request was successful
            data = res.json()
            # Extract relevant information
            info = {
                "city": data["location"]["name"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "lat": data["location"]["lat"],
                "lon": data["location"]["lon"],
                "localtime": data["location"]["localtime"],
                "condition": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "feelslike_c": data["current"]["feelslike_c"]
            }
            all_data.append(info)  # Add city data to the list
        else:
            print(f"Failed to fetch data for: {city}")

    return all_data

def dataframe_creation():
    api_key = '8d0e4c0679ba4618b5d130954240810'
    cities = ['kakinada', 'london', 'goa', 'pune', 'hyderabad','chicago','Jerusalem']
    
    # Fetch weather data for all cities
    data = extract(api_key, cities)

    # Create a DataFrame from the collected data
    df = pd.DataFrame(data)

    return df
def transform(df):
    filtered_df = df[df["country"] == 'India']
    return filtered_df

def write_to_file(df):
    from datetime import datetime
    import os
    path="/home/mani/extract"
    day=datetime.now().strftime('%y%m%d_%H%M%S')
    file=f"weather_{day}.csv"
    full_path=os.path.join(path,file)
    df.to_csv(full_path,index=False)
    print(f"Data saved at: {full_path}")

# Run the code
def etl_process():
    df=dataframe_creation()
    clean_df=transform(df)
    write_to_file(clean_df)
if __name__=='__main__':
    etl_process()
