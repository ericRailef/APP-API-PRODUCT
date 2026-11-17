import requests 

# API de Productos

BASE_URL = "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    #Muestra el codigo HTTP y los datos recibidos
    print("Codigo HTTP:", respuesta.status_code)
    
    if respuesta.text:
        print("Respuesta JSON")
        print(respuesta.json())
    else:
        print("La respuesta no tiene datos")
        
        
try:
    
    
    # =====================================
    #     1-GET -CONSULTAR UN PRODUCTO
    # =====================================

    print("\n --- GET: Consultar un producto ---")
    
    respuesta = requests.get(
        f"{BASE_URL}/19",
        timeout=10
    )
    
    #Captura el error si es 4XX - 5XX
    respuesta.raise_for_status()
    producto = respuesta.json()
    
    print("Producto", producto["title"])
    print("Precio", producto["price"])
    print("Categoria", producto["category"])
    
    # =====================================
    #     2-POST -CREAR UN PRODUCTO
    # =====================================
    
    print("\n --- POST: Crear un producto ---")
    
    nuevo_producto = {
        "title": "Teclado mecanico gamer",
        "price": 50000,
        "descripcion": "Teclado para jugar",
        "category": "electronics"
    }
    
    respuesta = requests.post(
        f"{BASE_URL}/add",
        json=nuevo_producto,
        timeout=10
    )
    
    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)
    
    
    # =====================================
    #     3-PATCH -MODIFICAR SOLO EL PRECIO
    # =====================================
    print("\n --- PATCH: Modificar el Precio ---")
    
    respuesta = requests.patch(
        f"{BASE_URL}/1",
        json={"price": 549990},
        timeout=10
    )
    
    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)
        
    
except requests.exceptions.Timeout:
    print("Error: Se agoto el tiempo de espera")


