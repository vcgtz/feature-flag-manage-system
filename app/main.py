from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Welcome to the Feature Flag Manage System"}
