import uvicorn
from fastapi import FastAPI
from routers.users import router as users
from routers.items import router as items

app = FastAPI()

app.include_router(users)
app.include_router(items)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Router Example"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
