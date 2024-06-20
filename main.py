from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()


@app.get("/login/")
def login():
    with open('/home/danimir/LazyFront/login.html', 'r') as file:
        res = file.read()
    return HTMLResponse(res)

@app.get("/login/style.css", response_class=FileResponse)
def css():
    res = '/home/danimir/LazyFront/style.css'
    return res

@app.get("/login/background.jpg")
def background():
    res = '/home/danimir/LazyFront/background.jpg'
    return FileResponse(res)
