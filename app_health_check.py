import requests
import logging

# Configure logging
logging.basicConfig(filename="app_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Application URL
APP_URL = "http://your-app-url.com"

def check_application_health():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP - Status Code: {response.status_code}")
            logging.info("Application is UP")
        else:
            print(f"Application might be DOWN - Status Code: {response.status_code}")
            logging.warning("Application might be DOWN")
    except requests.exceptions.RequestException:
        print("Application is DOWN or not reachable")
        logging.error("Application is DOWN or not reachable")

if __name__ == "__main__":
    check_application_health()
