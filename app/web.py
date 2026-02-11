import os
import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

log = logging.getLogger("retail_sniper")
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Retail Sniper")

ui_dir = os.path.join(os.path.dirname(__file__), "ui")
if os.path.isdir(ui_dir):
    app.mount("/ui", StaticFiles(directory=ui_dir, html=True), name="ui")

@app.get("/")
async def root():
    return RedirectResponse("/ui")

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("APP_PORT", "8000"))
    uvicorn.run("app.web:app", host="0.0.0.0", port=port, reload=False)
