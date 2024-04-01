import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {
        "status":"ok",
        "msg": "Hello!"
    }

if __name__ == "__main__":
    uvicorn.run("main:app",
                port = 8989,
                host = "0.0.0.0")