import os
import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="homesync", description="Local file synchronization service", docs_url="/"
)


@app.get("/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080, reload=os.getenv("ENV") == "DEV")
