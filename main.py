from fastapi import FastAPI
import uvicorn
api = FastAPI()
a = {
    "player1":2000,
    "player2":4000
}

@api.get("/player")
def apid(name:str):
    if not a[name]:
        return None
    return a[name]


uvicorn.run(api)
