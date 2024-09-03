
```
WeatherNotifier

WeatherNotifier is a FastAPI-based web application that sends daily weather reports to registered users. The application uses PostgreSQL for database management and integrates with the OpenWeatherMap API to fetch weather data.

 Features

- User registration with email and city.
- Daily weather report sent via email.
- Easy-to-use web interface with FastAPI and Jinja2Templates.

 Technologies Used

- FastAPI: Web framework for building the API.
- Jinja2: Templating engine for HTML rendering.
- SQLAlchemy: ORM for database interactions.
- PostgreSQL: Database management system.
- SMTP: Email sending protocol.
- OpenWeatherMap API: Weather data provider.
- Google Geocoding API: Geolocation data provider.

 Setup and Installation

```

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/WeatherNotifier.git
   cd WeatherNotifier
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add the following variables:

   ```env
   SMTP_SERVER=smtp.mail.yahoo.com
   SMTP_PORT=587
   EMAIL_USER=your_email@yahoo.com
   EMAIL_PASSWORD=your_email_password
   WEATHER_API_KEY=your_openweathermap_api_key
   GEOCODING_API_KEY=your_google_geocoding_api_key
   ```

5. **Run the Application**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the Application**

   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

- **Register a User**: Go to the home page and register with your email and city.
- **Receive Weather Reports**: Registered users will receive daily weather reports via email.

## Contributing

Feel free to open issues or submit pull requests to contribute to the development of WeatherNotifier.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```




