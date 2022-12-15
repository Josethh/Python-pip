import store 
from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 

app = FastAPI()

@app.get('/') # Suelen llamarlo Recurso ó endpoint
def get_list():
    return [1, 2, 3]

@app.get('/contact', response_class= HTMLResponse) # Suelen llamarlo Recurso ó endpoint
def get_list():
    return """
        <h1>Hola soy una página</h1>
        <p>Soy un parrafo</p>

    """

def run():
    store.get_categories() 


if __name__ == '__main__':
    run()