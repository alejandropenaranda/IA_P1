# ARS-IA
# cree una carpeta fuera del proyecto, python -m venv .
# cd hasta script activate y luego pip install pygame

To do
 
Falta 
Implementar el metodo que genera las posibles acciones o los operadores del problema.

Implementar el metodo que genera los nodos hasta que encuentra la solucion.

Implementar el movimiento de goku cuando se genera la solucion. (se planteo la base de una funcion que resive la lista de movimiento y a partir de esto va cambiando la posiciond de goku falta terminarla)
-Se creo un arreglo con los movimientos de goku y se termina la aplicacion cuando llega al ultimo movimiento.

Logica de cuando goku agarra una semilla, mata un freezer o cell y la bola del dragon.

Implementar los algoritmos de busqueda.

Generar la cola de acciones para guardar los operadores. (se creo la cola y se plantearon funciones que expanden la cola, expanden el nodo y se planteo dinamicamente para poder ingresar la logica de los demas algoritmos)

Comprobar cuando se gana. (ya esta la funcion esMeta en la clase nodo que comprueba si el nodo es una meta falta crear la funcion que haga lo demas que se debe hacer al expandir
un nodo).

Expandir los nodos. (se plateo la estructura de la funcion falta completar )

Evite devolverse, se puede devolver cuando cambia el estado entre casilla anterior y actual. (ya esta la funcion same_state 
en la clase nodo nodo que comprueba si el estado del nodo es igual al del padre falta la otra parte) 

Permitir escoger que algoritmo se quiere ejecutar. (se planteo la estructura de la funcion falta lo demas)
