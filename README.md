## Laboratorio No. 3 - Robótica Industrial
### Integrantes: 
- Victor Manuel Dávila Castañeda.
- Manuel Felipe Carranza Montenegro.
## Descripción de la solución planteada
### iniciar turtlesim
Para iniciar la aplicación se corrio el siguiente comando que crea el nodo maestro en el que vamos a correr nuestros programas

```console
roscore
```

<div>
<p style = 'text-align:center;' align="center">
<img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/roscore.png" width="700px" height="300px" >
</p>
</div>

En una segunda terminal se hizo aparecer la tortuga por primera vez con el siguiente comando.

```console
rosrun turtlesim turtlesim_node
```

<div>
<p style = 'text-align:center;' align="center">
<img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/rosrun%20tortuga%20quieta.png" width="700px" height="300px" >
</p>
</div>
los errores que aparecen son debido a que al estar corriendo ubuntu en WSL no se tiene una interfaz grafica por lo que se necesito utilizar la aplicación externa Xming[https://sourceforge.net/projects/xming/] para poder obtener esas funcionalidades por lo que esos errores que aparecen solo se dan al inicio mientras se inicializa la visualización, pero no afectan de ninguna manera la ejecucion del codigo.

### implementacion de matlab
debido a que el nodo maestro lo estabamos corriendo ya en ubuntu lo que necesitabamos era hacer que matlab fuera un nodo secundario por lo que al comando rosinit le pasamos como argumento la ip de donde se estaba ejecutando el nodo maestro ya que si pasamos el rosinit por si solo matlab crearia su propio nodo maestro

```matlab
rosinit("http://LAPTOP-B6O42SIN:11311/");
```
Con el siguiente codigo nos suscribimos desde matlab al topico de pose y recibimos un mensaje con la informacion que envia el topico para conocer la posicion y orientacion actual de la tortuga 

```matlab
posesub = rossubscriber("/turtle1/pose","DataFormat","struct")
posedata = receive(posesub,10)
```
<div>
<p style = 'text-align:center;' align="center">
<img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/posesub%20matlab.png" width="700px" height="250px" >
</p>
</div>
<div>
<p style = 'text-align:center;' align="center">
<img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/posedata%20matlab.png" width="700px" height="250px" >
</p>
</div>
Conociendo la posicion actual de la tortuga y mandando una velocidad en x e y generamos un script donde la tortuga evite los bordes de la pantalla.

### resultado implementacion matlab

(dar click en la imagne para ir al video)

<div>
<p style = 'text-align:center;' align="center">
<a href="https://youtu.be/-qRDwdd-Kuo" target="_blank"><img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/implementacion%20turtlematlab.png" 
alt="IMAGE ALT TEXT HERE" width="600" height="300" border="10" /></a>
</p>
</div>

### implementacion python
En una tercera terminal se utilizo el siguiente comando para poder conocer la posicion inicial exacta de la tortuga, la cual seria usada para transportarse a ella con el teleport absolute con este

```console
rostopic echo turtle1/pose
```

<div>
<p style = 'text-align:center;' align="center">
<img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/rostopic%20echo%20pose.png" width="500px" height="200px" >
</p>
</div>

En python se uso rospy.publisher para enviar la velocidad lineal y angular segun la tecla que se oprimiera y tambien se uso para girar la tortuga 180 grados pasandole un argumento de pi/2 en la velocidad angular. Ademas de esto su utiliza /turtle1/teleport_absolute con el publisher para enviar a la tortuga a la posicion inicial que obtuvimos con el comando anterior. Junto con esto el script por consola nos dice que tecla se presiono.

Los siguientes comandos corren el codigo que hicimos en python despues de actualizar el espacio de trabajo de catkin para reconocer el paquete hello_turtle

```console
catkin build
rosrun hello_turtle myTeleopKey.py
```

### resultado implementacion python

(dar click en la imagne para ir al video)

<div>
<p style = 'text-align:center;' align="center">
<a href="https://youtu.be/-qRDwdd-Kuo" target="_blank"><img src="https://github.com/victordavila2311/LAB3Robotica_Manuel_Victor/blob/main/imagenes%20lab%203/implementacion%20python.png" 
alt="IMAGE ALT TEXT HERE" width="700" height="250" border="10" /></a>
</p>
</div>
