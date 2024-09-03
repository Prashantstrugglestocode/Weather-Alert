from fastapi import FastAPI, Depends, Request, Form, HTTPException, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette.responses import RedirectResponse
from .database import get_db, engine
from .models import User
from . import models
from .weather_service import get_weather
from .email_sender import send_email
import logging

# Ensure that tables are created
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get('/')
def home(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@app.post("/register/")
async def register(request: Request, db: Session = Depends(get_db), email: str = Form(...), city: str = Form(...)):
    try:
        user = User(email=email, city=city)
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    return RedirectResponse(url="/", status_code=303)

@app.get("/send_report/{user_id}")
def send_report(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        logging.info(f"Fetching weather data for {user.city}.")
        weather_data = get_weather(user.city)
        
        if not weather_data:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching weather data")

        # Extract weather information
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']

        weather_report = (f"Weather in {user.city}: {weather_description}, "
                          f"Temp: {temperature}°C")
        logging.info(f"Sending weather report to {user.email}.")
        send_email(user.email, "Daily Weather Report", weather_report)
        
        return {"message": f"Report sent to {user.email}"}

    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error sending report or fetching weather data")