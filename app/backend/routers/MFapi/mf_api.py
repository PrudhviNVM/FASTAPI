import requests
from fastapi import APIRouter, HTTPException

API_URL = "https://api.mfapi.in/mf?limit=100&offset=0" 

HISTORY_URL = "GET https://api.mfapi.in/mf/125497?startDate=2023-01-01&endDate=2023-12-31"
data = requests.get(HISTORY_URL).json()

print(data)