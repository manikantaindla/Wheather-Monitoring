**Weather Monitoring Application**

**Objective**
The objective of this project is to develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates.

**Tech Stack**:
1. Programming Language: Python
2. API: OpenWeatherMap
3. Database: SQLite (via SQLAlchemy)
4. Visualization: Matplotlib
5. Web Framework: Flask (if web interface is required)

**Features**
1. Real-time weather data retrieval
2. Data processing and conversion
3. Daily summaries and aggregates
4. Alerting based on user-defined thresholds
5. Visualization of weather data

**Prerequisites**
1. Python 3.x
2. Git
3. Visual Studio Code (VS Code)

**Requirements:**
﻿1. certifi==2024.7.4
2. charset-normalizer==3.3.2
3. idna==3.7
4. numpy==2.0.1
5. pandas==2.2.2
6. python-dateutil==2.9.0.post0
7. pytz==2024.1
8. requests==2.32.3
9. six==1.16.0
10. tzdata==2024.1
11. urllib3==2.2.2
12. requests
13. pandas
14. SQLAlchemy


**Setup Instructions**
1. Installation
Clone the repository: Go to GitHub and create a new repository named weather-monitoring. Clone the repository to your local machine

   Command:
   
   git clone https://github.com/vanshika-pahuja/weather-monitoring.git
   cd weather-monitoring

3. Create a virtual environment and install dependencies: Create and activate a virtual environment:

   Command:
   
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux

   Install the required packages:
   
   Command:
   pip install -r requirements.txt

3. Configure the application: Update the src/config.py file with your OpenWeatherMap API key and other settings.

4. Run the application:
   
   Command:
   
   python src/app.py

6. Testing
   Run tests:
   
   Ensure that all components are working as expected by running the unit tests:
   Command:
   
   python -m unittest discover tests


**Project Structure**
The project directory structure is as follows:
weather-monitoring/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── weather_api.py
│   ├── data_processing.py
│   ├── aggregates.py
│   ├── database.py
│   └── visualizations.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── requirements.txt
└── README.md

**Contributing**
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

**Key Features**
1. Real-time Weather Data Retrieval: Continuously fetches weather data for multiple cities at specified intervals.
2. Data Processing and Conversion: Converts raw data into meaningful metrics, such as temperature in Celsius.
3. Daily Summaries and Aggregates: Aggregates weather data on a daily basis to provide summaries like average, maximum, and minimum temperatures, as well as dominant weather conditions.
4. Threshold-Based Alerts: Monitors temperature thresholds and generates alerts if certain conditions are met.
5. Data Storage: Uses SQLite for storing historical weather data.
6. Visualization: Generates visual representations of the weather data for better insights.
   
**License**
This project is licensed under the MIT License.

