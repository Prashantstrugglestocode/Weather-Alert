
```markdown
# WeatherNotifier

WeatherNotifier is a FastAPI-based web application that sends daily weather reports to registered users. The application uses PostgreSQL for database management and integrates with the OpenWeatherMap API to fetch weather data.

## Features

- User registration with email and city.
- Daily weather report sent via email.
- Easy-to-use web interface with FastAPI and Jinja2Templates.

## Technologies Used

- **FastAPI**: Web framework for building the API.
- **Jinja2**: Templating engine for HTML rendering.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database management system.
- **SMTP**: Email sending protocol.
- **OpenWeatherMap API**: Weather data provider.
- **Google Geocoding API**: Geolocation data provider.

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

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add the following variables:

   ```plaintext
   DATABASE_URL=your_database_url
   SMTP_SERVER=your_smtp_server
   SMTP_PORT=your_smtp_port
   EMAIL_USER=your_email
   EMAIL_PASSWORD=your_email_password
   WEATHER_API_KEY=your_weather_api_key
   GEOCODING_API_KEY=your_geocoding_api_key
   ```

5. **Run Database Migrations**

   Ensure the database tables are created:

   ```bash
   alembic upgrade head
   ```

6. **Run the Application**

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Usage

- **Register a New User**

  POST request to `/register/` with form data:
  
  - `email`: User's email address.
  - `city`: City for weather reports.

- **Send Weather Report**

  GET request to `/send_report/{user_id}` to manually trigger a weather report for a user.

## Contributing

Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact me at mishraprashant62@yahoo.in.
```

Feel free to modify the repository URL, license, and contact details according to your needs. If you need to add any additional setup or instructions, you can include them in the relevant sections.
