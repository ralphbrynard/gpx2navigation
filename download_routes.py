import requests
import json
import os

# Define the path for the configuration and cache files
config_path = os.path.expanduser('~/Documents/config.json')
cache_path = os.path.expanduser('~/Documents/strava_routes_cache.json')

# Function to load configuration
def load_config():
    with open(config_path, 'r') as file:
        return json.load(file)

# Load the configuration
config = load_config()
client_id = config['client_id']
client_secret = config['client_secret']
refresh_token = config['refresh_token']

# Function to get a new access token using the refresh token
def get_access_token():
    url = 'https://www.strava.com/oauth/token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

# Function to fetch routes from Strava
def fetch_routes(access_token):
    url = f'https://www.strava.com/api/v3/athlete/routes?access_token={access_token}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Function to download the GPX file for a route
def download_gpx(route_id, access_token):
    url = f'https://www.strava.com/api/v3/routes/{route_id}/export_gpx?access_token={access_token}'
    response = requests.get(url)
    response.raise_for_status()
    return response.content

# Function to save the GPX file locally
def save_gpx_file(route, gpx_content):
    filename = f"{route['name']}.gpx"
    filepath = os.path.join(os.path.expanduser('~/Documents'), filename)
    with open(filepath, 'wb') as file:
        file.write(gpx_content)
    return filepath

# Function to load the cache
def load_cache():
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as file:
            return json.load(file)
    return []

# Function to save the cache
def save_cache(cache):
    with open(cache_path, 'w') as file:
        json.dump(cache, file, indent=4)

# Main function
def main():
    # Get access token
    access_token = get_access_token()
    
    # Fetch routes from Strava
    routes = fetch_routes(access_token)
    
    # Select the latest route
    latest_route = routes[0]
    
    # Download the GPX file for the latest route
    gpx_content = download_gpx(latest_route['id'], access_token)
    
    # Save the GPX file locally
    gpx_filepath = save_gpx_file(latest_route, gpx_content)
    print(f"Downloaded and saved GPX file to {gpx_filepath}")
    
    # Load the cache
    cache = load_cache()
    
    # Check if the route is already cached
    for cached_route in cache:
        if cached_route['id'] == latest_route['id']:
            print("Route already cached.")
            return
    
    # Add the new route to the cache
    latest_route['number_of_rides'] = 0
    cache.append(latest_route)
    
    # Save the updated cache
    save_cache(cache)
    print("Updated cache with the new route.")

# Run the main function
if __name__ == "__main__":
    main()
