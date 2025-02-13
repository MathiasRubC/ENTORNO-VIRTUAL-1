from flask import Flask, url_for
import random

app = Flask(__name__)

# Lista de hechos aleatorios sobre entretenimiento, cine y videojuegos
facts_list = [
    "El personaje de Yoda en Star Wars fue originalmente diseñado con piel de melocotón.",
    "El videojuego Pac-Man fue diseñado para atraer a las mujeres, ya que está inspirado en comer bocadillos.",
    "El director Alfred Hitchcock nunca ganó un Oscar competitivo a lo largo de su carrera.",
    "Super Mario Bros. fue creado inicialmente como un juego de plataformas para que los desarrolladores probaran nuevas ideas.",
    "La película Avatar utilizó cámaras especialmente diseñadas para capturar las expresiones faciales de los actores en CGI.",
]

# Lista de nombres de imágenes en la carpeta 'imagenes'
images_list = [
    "5.jpg",
    "cobra kai.jpg",
    "god.jpg",
    "gta.jpg",
    "msn.jpg",
]

# Página principal
@app.route("/")
def home():
    return '''
    <h1>Bienvenido a la página de entretenimiento</h1>
    <ul>
        <li><a href="/random_fact">¡Ver un dato aleatorio sobre entretenimiento!</a></li>
        <li><a href="/coin_flip">¡Lanzar una moneda!</a></li>
        <li><a href="/password_generator">¡Generar una contraseña segura!</a></li>
        <li><a href="/random_image">¡Ver una imagen aleatoria!</a></li>
    </ul>
    '''

# Página de hecho aleatorio
@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

# Página de lanzamiento de moneda
@app.route("/coin_flip")
def coin_flip():
    result = random.choice(["Cara", "Cruz"])
    return f'<h1>¡Resultado del lanzamiento de moneda: {result}!</h1>'

# Página de generador de contraseñas
@app.route("/password_generator")
def password_generator():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = "".join(random.choices(characters, k=12))
    return f'<h1>Tu nueva contraseña segura es: {password}</h1>'

# Página de imagen aleatoria
@app.route("/random_image")
def random_image():
    # Selecciona un nombre de imagen aleatorio de la lista
    image_name = random.choice(images_list)
    image_url = url_for('static', filename=f'imagenes/{image_name}')
    return f'<h1>¡Aquí tienes una imagen aleatoria!</h1><img src="{image_url}" alt="Imagen aleatoria" />'

if __name__ == "__main__":
    app.run(debug=True)

