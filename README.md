QR Generator & Weather App

This project is a web application that combines two main functionalities:

QR Code Generator: Generate QR codes for any input text or URLs.

Weather App: Retrieve real-time weather data for any location.

The application is built using Django and Django REST Framework (DRF) for the backend.

Features

1. QR Code Generator

Create QR codes for text or URLs.

Download the generated QR code as an image file.

2. Weather App

Search for weather information by city name.

Displays temperature, humidity, and weather conditions in real-time.

Technologies Used

Django: Backend framework.

Django REST Framework (DRF): For creating APIs.

Python: Core programming language.

API Integration: Weather data is fetched using an external API (e.g., OpenWeatherMap).

QR Code Library: Python libraries to generate QR codes.

Installation & Setup

Clone the Repository

git clone https://github.com/parvez-k0/QR_generator-Weather_app.git
cd QR_generator-Weather_app

Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows

Install Dependencies

pip install -r requirements.txt

Run Database Migrations

python manage.py makemigrations
python manage.py migrate

Run the Development Server

python manage.py runserver

Open your browser and navigate to:

http://127.0.0.1:8000/

API Endpoints

QR Code Generator

Endpoint: /api/generate-qr/

Method: POST

Payload:

{
  "text": "Your text or URL here"
}

Response: Returns a QR code image.

Weather App

Endpoint: /api/get-weather/

Method: GET

Parameters:

city: Name of the city

Example:

/api/get-weather/?city=London

Screenshots

Add screenshots of your app here, if available.

Future Enhancements

Add user authentication for saving QR code and weather searches.

Enable caching to improve API response time.

Add more detailed weather forecasts (e.g., 7-day forecast).

License

This project is open-source and available under the MIT License.

Author

Mohd Parvez KhanFeel free to connect with me for feedback or suggestions!

