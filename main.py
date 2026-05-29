from fastapi import FastAPI

app = FastAPI(title="Fast-Blog", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Hello World"}
