# QR Generator & Weather App

This project is a web application that combines two main functionalities:
1. **QR Code Generator**: Generate QR codes for any input text or URLs.
2. **Weather App**: Retrieve real-time weather data for any location.

The application is built using **Django** and **Django REST Framework (DRF)** for the backend.

---

## Features

### 1. QR Code Generator
- Create QR codes for text or URLs.
- Download the generated QR code as an image file.

### 2. Weather App
- Search for weather information by city name.
- Displays temperature, humidity, and weather conditions in real-time.

---

## Technologies Used
- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For creating APIs.
- **Python**: Core programming language.
- **API Integration**: Weather data is fetched using an external API (e.g., OpenWeatherMap).
- **QR Code Library**: Python libraries to generate QR codes.

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/parvez-k0/QR_generator-Weather_app.git
   cd QR_generator-Weather_app
   
# Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

# Run Database Migrations

python manage.py makemigrations
python manage.py migrate

# Run the Deployment Server

python manage.py runserver

# Future Enhancements

Add user authentication for saving QR code and weather searches.
Enable caching to improve API response time.
Add more detailed weather forecasts (e.g., 7-day forecast).

# License

This project is open-source and available under the MIT License.


Author
Mohd Parvez Khan
Feel free to connect with me for feedback or suggestions!

### How to Proceed:
1. Copy the above content into a `README.md` file in your repository.
2. Add screenshots of your app (if possible) to make it visually engaging.
3. Let me know if you'd like me to refine any part of it! 😊

























