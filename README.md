# Rick and Morty challenge

### Este Rick and Morty challenge es mi solución a modo de back end, a través de una API, para el desafío planteado por [Chipax](https://www.notion.so/Rick-and-Morty-Challenge-84a1b794dc09429fb3178c2a24e7c217).

![](https://i.kym-cdn.com/photos/images/newsfeed/001/666/080/25a.jpg)

### El desafío consta de dos tareas, basandose en la [API](https://rickandmortyapi.com/) de Rick and Morty. El cual se puede consultar la solucion en este endpoint (https://ram-challenge-chipax.herokuapp.com/)

**1.** Char counter: Contar las letras 'c' dentro de todos los characters, las letras l dentro de todas las locations y las letras 'e' dentro de todos los episodes.

**2.** Para cada episode, indicar la cantidad y un listado con las location (origin) de todos los character que aparecieron en ese episode (sin repetir).

## Installation

Esta solución fue hecha en Python usando Funtional Programming y exponiendola en una API gracias a FastAPI. 

Los pasos a seguir para poder correr el código localmente son (asumiendo que ya tienes instalado Python en tu PC y lo estás corriendo en un terminal adecuada como Anaconda Prompt
o Cmder):

1. Crear un ambiente virtual (por buenas pácticas). Por ejemplo podrías crear un ambiente llamado rickandmorty usando el comando `py -m venv rickandmorty`.

2. Activar el ambiente virtual corriendo el archivo activate `rickandmorty\Scripts\activate.bat`

3. Instalar las dependencias a través del archivo `requirements.txt` usando el comando `pip install -r requirements.txt`

4. Ejecutar el servidor unicorn con el comando `uvicorn main:app --reload` y visitar `http://127.0.0.1:8000`

5. Fin :) 

