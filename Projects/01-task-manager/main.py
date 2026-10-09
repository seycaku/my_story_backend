from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message" : "Welcome To Task Manager API"}