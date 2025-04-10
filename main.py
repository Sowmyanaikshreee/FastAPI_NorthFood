from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
 
app = FastAPI()
 
# Mount the static directory (for CSS and images)
app.mount("/static", StaticFiles(directory="static"), name="static")
 
# Read the HTML file
html_path = Path("index.html")
html_content = html_path.read_text(encoding="utf-8")
 
# Replace href and src to use /static
html_content = html_content.replace('href="styles.css"', 'href="/static/styles.css"')
html_content = html_content.replace('src="images/', 'src="/static/images/')
 
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=html_content, status_code=200)
 