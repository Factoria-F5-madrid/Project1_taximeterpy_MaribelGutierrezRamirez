<p align="center">
  <img src="Texto.png" alt="Portada" width="1000"/>
</p>



¡Tu taxi ha llegado! Bienvenidos a **Familias en Movimiento**, la única empresa de transportes que ofrece servicio a familias con niños. 


<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />Este es un programa en Python que simula el funcionamiento básico de un taxímetro. 

##  Enlaces importantes: 

Conoce la presentacion realizada en Canva :eyes:
[Ver Presentación en Google Drive](https://drive.google.com/file/d/1hXzdEgHxsJMqbNMaI0rVr_g7Pn0-ZDBH/view?usp=sharing)


O si prefieres, puedes ver un **video** con la ejecución del código en el siguiente enlace: :point_down:

[Ver video en Google Drive](https://drive.google.com/file/d/1HqESXwPJFjO7tJJKtsm8tCtCQZmruRBi/view?usp=sharing)


¿Quieres ver cómo me organice? :point_down:

[Enlace a Projects](https://github.com/orgs/Factoria-F5-madrid/projects/9)

---

## **¿Cómo fue diseñado este código?** :construction_worker:
Este proyecto fue una experiencia completamente nueva para mí, ya que era la primera vez que trabajaba con Python. Tal vez te preguntes: ¿cómo logre sacarlo adelante sin experiencia previa?

Comencé investigando referencias sobre la lógica de funcionamiento de sistemas similares. A partir de ahí, desarrollé un código mínimo viable que permitiera calcular la tarifa en función del tiempo en movimiento, específicamente por segundo.

Desde el inicio, quise que el proyecto tuviera un fuerte enfoque en la atención al cliente. Esto se debe a mi experiencia profesional previa, donde aprendí la importancia de diseñar productos y servicios centrados en las personas. Por eso, incorporé interacciones con el usuario a través de funciones como input() y mensajes informativos con print(), solicitando datos como el nombre y detalles del viaje.

También incluí una condición en el código que permite ofrecer una silla para menores, pensando en brindar un servicio más inclusivo y adaptado a las necesidades familiares.

Para registrar de forma precisa los horarios de los viajes, utilicé la librería datetime, lo que permite obtener la hora real en que se ejecutan ciertas partes del código. Esto ayuda a generar registros más certeros y útiles para posibles análisis posteriores


## **Funcionalidades Principales:** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Oncoming%20Taxi.png" alt="Oncoming Taxi" width="40" height="40" />  


1. Simulación del flujo de un viaje con los comandos:

- start: inicia el trayecto

- stop: marca el estado detenido

- move: indica que el vehículo está en movimiento

- finish: finaliza el trayecto y calcula la tarifa

- exit: cierra el programa

2. Registro de datos del usuario (nombre del adulto y del niño/a).

3. Verificación de la necesidad de una silla para menores de 12 años.

4. Cálculo dinámico de la tarifa:

- Tarifa base: $2.50

- Costo por segundo en movimiento: $0.20

- Costo por segundo detenido: $0.50

5. Registro del trayecto en un archivo historial_trayectos.txt.

  
## **Estructura del Proyecto**

 - taximetro-cli/
     - taximetro.py              # Código principal del taxímetro
     - README.md                 # Este documento
     - Historial_proyectos.txt   # Texto plano para el registro histórico de los viajes


## **Estructura del Código**

calculate_fare(): Calcula el total de la tarifa con base en los tiempos registrados.

registrar_trayecto(): Guarda los datos del viaje en un archivo de texto.

solicitar_datos_usuario(): Interactúa con el usuario para capturar los datos necesarios.

taximeter(): Controla el flujo del viaje y los comandos disponibles.

Bloque if __name__ == "__main__": Inicia el programa llamando a taximeter().  




## **Fortalezas y Debilidades del Proyecto**

- ✅ Fácil de entender y mantener
- ✅ Lógica clara para calcular tarifas
- ✅ Guarda el  historial de trayectos en archivo de texto plano
- ✅ Respuestas personalizadas con nombre de usuario y su hijo o hija

- ⚠️ No tiene pruebas unitarias 
- ⚠️ No controla errores avanzados de entrada
- ⚠️ Es solo CLI, sin interfaz gráfica (más adelante haré este desarrollo)


  Y si tú también estás empezando en Python, te dejo este mensaje: :ok_woman:

  <img src="https://user-images.githubusercontent.com/74038190/236544207-c4f427b3-be04-4cfe-a3d2-2eabb0d2de73.gif" width="400">
<br><br>

¡Hasta el próximo proyecto! :wave:




