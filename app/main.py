from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Welcome to the Feature Flag Manage System"}


@app.get("/feature-flags")
async def get_feature_flags():
    return {"message": "List of the available feature flags"}


@app.get("/feature-flags/{slug}")
async def get_feature_flag(slug: str):
    return {"message": "Get one feature flag by the slug: " + slug}


@app.post("/feature-flags")
async def create_feature_flag():
    return {"message": "Create a new feature flag"}


@app.put("/feature-flags/{slug}")
async def update_feature_flag(slug: str):
    return {"message": "Update the existing feature flag: " + slug}


@app.delete("/feature-flags/{slug}")
async def delete_feature_flag(slug: str):
    return {"message": "Delete existing feature flag: " + slug}
