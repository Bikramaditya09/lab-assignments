from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from controllers.controller import router

app = FastAPI()
app.include_router(router)
app.mount('/static',StaticFiles(directory='static'),name='static')

# set the templates 
templates = Jinja2Templates(directory='templates')

@app.get("/")
async def homepage(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=5000)


