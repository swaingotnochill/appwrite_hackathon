from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6969)
