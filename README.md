# 📚 API de Libros - Django

Este proyecto es una **API REST de gestión de libros** desarrollada con **Django y Django REST Framework**, que permite realizar operaciones de **CRUD** sobre libros (Crear, Leer, Actualizar, Eliminar).  
Es compatible con la aplicación Flutter **`app_libros`**, la cual consume los datos desde esta API.

---

## 🔹 Tecnologías usadas

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- SQLite (base de datos por defecto, puede cambiarse)  
- Virtualenv (para gestión de dependencias)

---

## 🔹 Instalación

1. **Clonar el repositorio:**

   ```
   git clone https://github.com/Harryata/lab016_flutter_api_django.git
   cd lab016_flutter_api_django
   ```

2. **Crear y activar el entorno virtual:**

   ```
   python -m venv venv
   ```

   **Windows:**
   ```
   venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```
   source venv/bin/activate
   ```

3. **Instalar dependencias:**

   ```
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones:**

   ```
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo:**

   ```
   python manage.py runserver
   ```

El servidor estará disponible en:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔹 Uso de la API

### Obtener lista de libros  
**GET** `/libros/`

### Obtener detalle de un libro  
**GET** `/libros/<id>/`

### Crear un libro  
**POST** `/libros/`

**Ejemplo de body JSON:**
```
{
  "titulo": "El Principito",
  "autor": "Antoine de Saint-Exupéry",
  "fecha": "1943",
  "isbn": "1234567890"
}
```

### Actualizar un libro  
**PUT** `/libros/<id>/`

### Eliminar un libro  
**DELETE** `/libros/<id>/`

Estas rutas funcionan correctamente con la aplicación Flutter **`app_libros`**, la cual consume los datos desde la API local.

---

## 🔹 Capturas de pantalla

![Lista de libros](1_api.png)
![Detalle de libro](2_api.png)
![Crear / editar libro](3_api.png)
