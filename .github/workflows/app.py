from fastapi import FastAPI
import wikipedia

app = FastAPI()

@app.get("/")
async def get_wikipedia_url(topic: str):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        return {"topic": topic, "url": page.url}
    except Exception:
        return {"topic": topic, "url": "https://en.wikipedia.org/wiki/Main_Page"}
