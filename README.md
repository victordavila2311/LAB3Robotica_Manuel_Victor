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
En una segunda terminal se hizo aparecer la tortuga por primera vez con el siguiente comando
```console
rosrun turtlesim turtlesim_node
```
los errores que aparecen son debido a que al estar corriendo ubuntu en WSL no se tiene una interfaz grafica por lo que se necesito utilizar la aplicación externa Xming[https://sourceforge.net/projects/xming/] para poder obtener esas funcionalidades por lo que esos errores que aparecen solo se dan al inicio mientras se inicializa la visualización, pero no afectan de ninguna manera la ejecucion del codigo
### implementacion de matlab
debido a que el nodo maestro lo estabamos corriendo ya en ubuntu lo que necesitabamos era hacer que matlab fuera un nodo secundario por lo que al comando rosinit le pasamos como argumento la ip de donde se estaba ejecutando el nodo maestro ya que si pasamos el rosinit por si solo matlab crearia su propio nodo maestro
```matlab
rosinit("http://LAPTOP-B6O42SIN:11311/");
```

### implementacion python
En una tercera terminal se utilizo el siguiente comando para poder conocer la posicion inicial exacta de la tortuga, la cual seria usada para transportarse a ella con el teleport absolute con este
```console
rostopic echo turtle1/pose
```
El siguiente comando corre el codigo que hicimos en python
```console
python3 myTeleopKey.py
```
