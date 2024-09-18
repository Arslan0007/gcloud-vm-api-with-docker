from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import FileResponse
import requests
import json
import os

load_dotenv()

app = FastAPI(
    title="MyApp",
    description="Hello API dev",
    version="0.0.1"
)

api_key=os.getenv("WEATHER_TOKEN")

print(api_key)
url = f'https://api.openweathermap.org/data/2.5/weather?id=323786&appid={api_key}&cnt=5&units=metric&lang=en'


@app.get("/weather/")
async def root():
    response = requests.get(url)
    response_json = response.json()
    weather_temp = response_json["main"]["temp"]
    weather_location = response_json["name"]
    return weather_location, weather_temp


@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

print("test weather bro")