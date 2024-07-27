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


**Setup Instructions**
1. Installation
Clone the repository: Go to GitHub and create a new repository named weather-monitoring. Clone the repository to your local machine
Command:
git clone https://github.com/vanshika-pahuja/weather-monitoring.git
cd weather-monitoring

2. Create a virtual environment and install dependencies: Create and activate a virtual environment:
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

5. Testing
Run tests:
Ensure that all components are working as expected by running the unit tests:
Command:
python -m unittest discover tests

