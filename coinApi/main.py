from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests
import json
import os


app = FastAPI(
    title="MyApp",
    description="Hello API dev",
    version="0.0.1"
)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

@app.get("/{currency}/")
async def root(currency):
    # getting an information with requests
    response = requests.get(url)
    # converting them into a json
    response_json = response.json()
    # fetching a specific area to find related currency
    price_cur = response_json['bpi']
    # convert them to lowercase
    price_cur_lower = json.loads(json.dumps(price_cur).lower())
    # fetching the related rate of currency
    price_cur_rate = price_cur_lower[currency]['rate']
    # sending the result
    return {"message": price_cur_rate}

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

print("test coin bro")