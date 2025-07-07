def busqueda_por_anchura_aristas(grafo, nodo_inicial, obtener_vecinos=None, limite_profundidad=None):
    """
    Genera las aristas descubiertas en un recorrido de búsqueda por anchura (BFS) sobre un grafo.

    Parámetros:
    ------------
    grafo | networkx.Graph o networkx.DiGraph | Grafo sobre el que se realiza la búsqueda.
    nodo_inicial | nodo | Nodo desde el cual comienza la búsqueda.
    obtener_vecinos | callable | Función personalizada para obtener los vecinos de un nodo. Si no se especifica, se usa grafo.neighbors.
    limite_profundidad | int | Profundidad máxima hasta la que se explorará el grafo. Si no se especifica, se recorre todo el grafo.

    Yields:
    -------
    tuple | Pares de nodos representando las aristas descubiertas durante la búsqueda.
    """
    if obtener_vecinos is None:
        obtener_vecinos = grafo.neighbors
    if limite_profundidad is None:
        limite_profundidad = len(grafo)

    nodos_visitados = {nodo_inicial}
    total_nodos = len(grafo)
    profundidad_actual = 0
    cola_nodos = [(nodo_inicial, obtener_vecinos(nodo_inicial))]

    while cola_nodos and profundidad_actual < limite_profundidad:
        nodos_actuales = cola_nodos
        cola_nodos = []
        for nodo_padre, vecinos in nodos_actuales:
            for vecino in vecinos:
                if vecino not in nodos_visitados:
                    nodos_visitados.add(vecino)
                    cola_nodos.append((vecino, obtener_vecinos(vecino)))
                    yield nodo_padre, vecino
            if len(nodos_visitados) == total_nodos:
                return
        profundidad_actual += 1


def busqueda_por_profundidad_aristas(grafo, nodo_inicial, limite_profundidad=None, ordenar_vecinos=None):
    """
    Genera las aristas descubiertas en un recorrido de búsqueda por profundidad (DFS) sobre un grafo.

    Parámetros:
    ------------
    grafo | networkx.Graph o networkx.DiGraph | Grafo sobre el que se realiza la búsqueda.
    nodo_inicial | nodo | Nodo desde el cual comienza la búsqueda. Si es None, se exploran todos los nodos no visitados.
    limite_profundidad | int | Profundidad máxima permitida para la búsqueda. Si no se especifica, se recorre todo el grafo.
    ordenar_vecinos | callable | Función que define el orden en que se exploran los vecinos. Si no se especifica, se usa el orden por defecto.

    Yields:
    -------
    tuple | Pares de nodos representando las aristas descubiertas durante la búsqueda.
    """
    if nodo_inicial is None:
        nodos_iniciales = grafo
    else:
        nodos_iniciales = [nodo_inicial]

    if limite_profundidad is None:
        limite_profundidad = len(grafo)

    obtener_vecinos = (
        grafo.neighbors if ordenar_vecinos is None 
        else lambda n: iter(ordenar_vecinos(grafo.neighbors(n)))
    )

    nodos_visitados = set()

    for nodo_raiz in nodos_iniciales:
        if nodo_raiz in nodos_visitados:
            continue
        nodos_visitados.add(nodo_raiz)
        pila = [(nodo_raiz, obtener_vecinos(nodo_raiz))]
        profundidad_actual = 1

        while pila:
            nodo_padre, vecinos = pila[-1]
            for vecino in vecinos:
                if vecino not in nodos_visitados:
                    yield nodo_padre, vecino
                    nodos_visitados.add(vecino)
                    if profundidad_actual < limite_profundidad:
                        pila.append((vecino, obtener_vecinos(vecino)))
                        profundidad_actual += 1
                        break
            else:
                pila.pop()
                profundidad_actual -= 1
