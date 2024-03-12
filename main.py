from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
# Paso 2: Aplicación FastAPI
app = FastAPI()

# Paso 3: Configuración de plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Lista inicial de comentarios
comentarios = []

# Paso 3: Endpoints
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def leer_raiz(request: Request):
    return templates.TemplateResponse("index_comments.html", {"request": request, "comentarios": comentarios})

@app.post("/agregar_comentario")
async def agregar_comentario(request: Request, nuevo_comentario: str = Form(...)):
    comentarios.append(nuevo_comentario)
    return templates.TemplateResponse("index_comments.html", {"request": request, "comentarios": comentarios})

@app.get("/ver_comentarios")
async def ver_comentarios():
    return {"comentarios": comentarios}

@app.post("/redirect_comentarios")
async def redirect_comentarios():
    return RedirectResponse(url="/ver_comentarios")

# Paso 4: Ejecutar la aplicación
if __name__ == "__main__":
    # Importamos Uvicorn solo si estamos ejecutando el script directamente
    import uvicorn
    
    # Ejecutamos la aplicación en el puerto 8000
    uvicorn.run(app, port=8000)
