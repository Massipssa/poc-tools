from google.cloud import storage
import requests
from requests.auth import HTTPBasicAuth

from src.gcp.composer.util import read_variables_file_from_bucket

BUCKET_NAME = "testmkeimport"
BASE_DIR = "data"
FILE_NAME = "var_file_1.json"

if __name__ == '__main__':
    # read file from bucket
    gcs_client = storage.Client()
    variables_content = read_variables_file_from_bucket(gcs_client, BUCKET_NAME, BASE_DIR, FILE_NAME)
    print(variables_content)

    # Define the Airflow API endpoint
    # Replace "your-airflow-server" with the actual Composer url.
    airflow_api_url = "https://04fa8d1bb18f4aff8d2744bbd3b79b0a-dot-northamerica-northeast1.composer.googleusercontent.com/api/v1"
    username = "kerrache.massipssa@gmail.com"
    password = "Mes4casesouioui!"

    # Create a session with Basic Authentication
    session = requests.Session()
    session.auth = HTTPBasicAuth(username, password)

    # Define the request headers
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    # Make the POST request to set the variables
    for key, value in variables_content.items():
        data = {
            "key": key,
            "value": value
        }
        #response = session.post(f"{airflow_api_url}/variables",
        response = session.post("https://04fa8d1bb18f4aff8d2744bbd3b79b0a-dot-northamerica-northeast1.composer.googleusercontent.com/api/v1/variables",
                                json=data,
                                headers=headers)

        # Check the response
        if response.status_code == 200:
            print("Variables set successfully.")
        else:
            print(f"Failed to set variables. Status code: {response.status_code}, Response: {response.text}")
