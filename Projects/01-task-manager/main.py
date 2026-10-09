from fastapi import FastAPI

app = FastAPI()

tasks = [{"id": 1, "title": "Learn Python", "completed": True}, 
         {"id": 2, "title": "Learn FastAPI", "completed": False}, 
         {"id": 3, "title": "Learn PostgreSQL", "completed": False}]

@app.get("/")
def hello():
    return {"message" : "Welcome To Task Manager API"}

@app.get("/tasks")
def get_all_tasks():
    return tasks