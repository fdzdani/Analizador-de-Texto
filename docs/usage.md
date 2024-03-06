# Uso
## Instrucciones de ejecucion
Para la ejecucion del programa simplemente debemos introducir los articulos que queremos procesar en la carpeta de entrada, tambien tenemos que [activar el servidor de grobid](https://grobid.readthedocs.io/en/latest/Grobid-service/), y por ultimo activar el entorno virtual si no lo tenemos activado ya. 
Tras esto y si no lo hemos hecho nos movemos a la carpeta principal del proyecto haciendo un:

````
cd Analizador-de-Texto
````

Una vez hecho todo lo anterior corremos el script principal mediante el comando:

````
python3 main.py
````

Que se ocupara de correr todos los otros scripts. Despues de esto podremos consultar los resultados de la ejecucion en el subdirectorio de salida correspondiente.
### Posibles errores durante la ejecucion
Este es un posible error que puede salir durante la ejecucion del programa:

````
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

Aborted (core dumped)
````

Una posible solucion para este problema es instalar el siguiente plugin en Ubuntu:

````
sudo apt install qtwayland5
````
