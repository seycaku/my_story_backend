from fastapi import FastAPI, HTTPException

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

@app.get("/tasks/{task_id}")
def get_task(task_id : int):
    find = False
    for item in tasks:
        if item["id"] == task_id:
            find = True
            return item
            
    if find == False:
        return HTTPException(status_code=404, detail="Task not found")