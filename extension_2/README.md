Añadimos el nuevo tipo_plato para poder especificar de que tipo son los platos.

Para poder especificar el tipo necesitamos un predicado que nos conecte un plato a un tipo, otro predicado para poder unificar los tipos de platos que tiene un menu de un dia especifico. Para finalizar necesitamos dos predicados para construir el orden que tienen los dias de la semana entre ellos, el primer dia de la semana y su siguiente.

Comprobamos que en la precondicion los tipos de plato no se repitan con el anterior si el dia a servir no es el primero y en el efecto ponemos los tipos de plato al menu que hemos servido al dia.
