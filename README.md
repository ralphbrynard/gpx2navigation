# Strava2RideWithGPS Documentation

## Overview
This document outlines the process and components for building the Strava2RideWithGPS iOS shortcut. Each function will be a separate shortcut integrated to work together seamlessly. 

## Shortcut Descriptions

### Core Features

#### Download Routes (Shortcut #1)
This shortcut downloads route GPX files from the "My Routes" section on Strava via API.

**Functionalities:**
- **Siri Command:** "Download my rides."
- **Fetch Latest Routes:** Downloads the latest saved routes.
- **Cache Management:**
  - Cache a list of locally saved routes.
  - Track how frequently certain routes are used (`Number of Rides`).
  - Categorize routes based on time and distance in the cache.

**Steps:**
1. **API Request to Strava:**
   - Use Strava API to fetch routes.
   - Store API credentials as secret values.
2. **Select Latest Routes:**
   - Identify the latest saved routes.
3. **Download GPX Files:**
   - Download the GPX files of the selected routes.
4. **Update Cache:**
   - Save the route information locally.
   - Track the usage frequency (`Number of Rides`).
   - Categorize by time and distance.

#### Start Bike Ride (Shortcut #2)
This shortcut uses downloaded GPX files to start a bike ride.

**Functionalities:**
- **Siri Command:** "Start my ride."
- **Route Selection:**
  - Prompt for distance or time.
  - Match routes based on closest time or distance value.
  - Select routes with the lowest `Number of Rides` from the matched group.
- **RideWithGPS and Apple Music Integration:**
  - Open the selected GPX file in the RideWithGPS app.
  - Simultaneously play the "Cycling" playlist on Apple Music.
  - Ensure RideWithGPS takes priority on the display.

**Steps:**
1. **Prompt User:**
   - Ask for desired ride duration or distance.
2. **Match Routes:**
   - Find routes that match the provided time or distance.
   - Group matching routes and prioritize those with the lowest `Number of Rides`.
3. **Open in RideWithGPS:**
   - Open the selected route's GPX file in RideWithGPS.
4. **Play Music:**
   - Start playing the "Cycling" playlist on Apple Music.

#### Random Bike Ride (Shortcut #3)
This shortcut selects a random bike ride based on user preferences.

**Functionalities:**
- **Siri Command:** "Random bike ride."
- **Prompt for Preferences:**
  - Ride type (mountain, road, gravel).
  - Distance or time.
- **Find and Download Route:**
  - Fetch a new route from Strava matching the criteria.
  - Download the GPX file.
  - Proceed with the `Start Bike Ride` shortcut.

**Steps:**
1. **Prompt User:**
   - Ask for ride type and duration or distance.
2. **API Request to Strava:**
   - Use Strava API to find a new route matching the criteria.
3. **Download GPX File:**
   - Download the selected route's GPX file.
4. **Start Ride:**
   - Use the `Start Bike Ride` shortcut functionalities to open the route and start the ride.

### Requirements
- **Python Code:**
  - Any bespoke code should be written in Python.
  - Python code should run in Pythonista 3.
- **Compatibility:**
  - Must work with iOS 17.5.
- **Security:**
  - Store Strava API credentials as secret values.

## Next Steps
1. **Set up Strava API Credentials:**
   - Securely store the API credentials.
2. **Develop and Test Individual Shortcuts:**
   - Create, test, and debug each shortcut separately.
3. **Integrate and Automate:**
   - Ensure seamless integration between the shortcuts.
4. **Final Testing:**
   - Test the complete workflow with Siri commands and app integrations. 

Feel free to reach out if you need any specific coding examples or further assistance in setting up the shortcuts!