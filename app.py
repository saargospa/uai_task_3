import pandas as pd
import networkx as nx
import warnings
import matplotlib.pyplot as plt
import random
import time
import os
import timeit

# Importa funciones personalizadas de algoritmos de búsqueda
from algoritmos import busqueda_por_anchura_aristas, busqueda_por_profundidad_aristas


def buscar_por_anchura(grafo, nodo_inicial, neighbors=None, depth_limit=None):
    """
    Realiza una búsqueda en anchura (BFS) sobre el grafo, comenzando desde el nodo especificado.
    
    Parámetros:
    ------------
    grafo | networkx.DiGraph | Grafo dirigido sobre el que se realizará la búsqueda.
    nodo_inicial | string | Nodo desde el cual comenzará la búsqueda.
    neighbors | callable | Función para obtener vecinos de un nodo. Por defecto se usa grafo.neighbors.
    depth_limit | int | Límite de profundidad de búsqueda.

    Salida:
    -------
    Imprime en consola el tiempo de ejecución y la lista de aristas exploradas.
    """
    resultado_bfs = busqueda_por_anchura_aristas(grafo, nodo_inicial)

    # print("Aristas encontradas mediante búsqueda por anchura:\n")
    # print(list(resultado_bfs), "\n")
    
    
    

def buscar_por_profundidad(grafo, nodo_inicial, neighbors=None, depth_limit=None):
    """
    Realiza una búsqueda en profundidad (DFS) sobre el grafo, comenzando desde el nodo especificado.
    
    Parámetros:
    ------------
    grafo | networkx.DiGraph |Grafo dirigido sobre el que se realizará la búsqueda.
    nodo_inicial | str |Nodo desde el cual comenzará la búsqueda.
    neighbors | callable | Función para obtener vecinos de un nodo. Por defecto se usa grafo.neighbors.
    depth_limit | int | Límite de profundidad de búsqueda.

    Salida:
    -------
    Imprime en consola el tiempo de ejecución y la lista de aristas exploradas.
    """
    resultado_dfs = busqueda_por_profundidad_aristas(grafo, nodo_inicial)
    # print("Aristas encontradas mediante búsqueda por profundidad:\n")
    # print(list(resultado_dfs), "\n")


def calcular_posicion_jerarquica(grafo, nodo_raiz=None, ancho_total=1.0, separacion_vertical=0.2, altura_inicial=0, centro_horizontal=0.5):
    """
    Calcula posiciones (x, y) para visualizar un árbol de manera jerárquica.

    Parámetros:
    ------------
    grafo | networkx.Graph |Grafo que debe ser un árbol (sin ciclos).
    nodo_raiz | nodo |Nodo desde donde se estructura la jerarquía. Si no se especifica, se selecciona aleatoriamente.
    ancho_total | float | Ancho total disponible para distribuir los nodos.
    separacion_vertical | float | Distancia vertical entre los niveles.
    altura_inicial | float |Coordenada vertical inicial.
    centro_horizontal | float |Coordenada horizontal inicial.

    Retorna:
    --------
    dict | Diccionario con las posiciones (x, y) de cada nodo.
    """
    if not nx.is_tree(grafo):
        raise TypeError("El grafo debe ser un árbol para utilizar esta función.")

    if nodo_raiz is None:
        if isinstance(grafo, nx.DiGraph):
            nodo_raiz = next(iter(nx.topological_sort(grafo)))
        else:
            nodo_raiz = random.choice(list(grafo.nodes))

    return _calcular_posicion_jerarquica_recursiva(grafo, nodo_raiz, ancho_total, separacion_vertical, altura_inicial, centro_horizontal)


def _calcular_posicion_jerarquica_recursiva(grafo, nodo_actual, ancho_total, separacion_vertical, altura_actual, centro_horizontal, posiciones=None, nodo_padre=None):
    """
    Función auxiliar recursiva para calcular posiciones jerárquicas de un árbol.

    Parámetros:
    ------------
    grafo | networkx.Graph | Grafo que debe ser un árbol.
    nodo_actual | nodo |Nodo actualmente procesado.
    ancho_total | float |Ancho disponible para distribuir los nodos hijos.
    separacion_vertical | float |Distancia vertical entre los niveles.
    altura_actual | float | Coordenada vertical actual.
    centro_horizontal | float | Coordenada horizontal del nodo actual.
    posiciones | dict |Diccionario acumulativo de posiciones.
    nodo_padre | nodo | Nodo padre, para evitar ciclos en grafos no dirigidos.

    Retorna:
    --------
    dict | Diccionario con las posiciones (x, y) de cada nodo.
    """
    if posiciones is None:
        posiciones = {nodo_actual: (centro_horizontal, altura_actual)}
    else:
        posiciones[nodo_actual] = (centro_horizontal, altura_actual)

    hijos = list(grafo.neighbors(nodo_actual))
    if not isinstance(grafo, nx.DiGraph) and nodo_padre is not None:
        hijos.remove(nodo_padre)

    if len(hijos) > 0:
        ancho_por_hijo = ancho_total / len(hijos)
        siguiente_x = centro_horizontal - ancho_total / 2 - ancho_por_hijo / 2
        for hijo in hijos:
            siguiente_x += ancho_por_hijo
            posiciones = _calcular_posicion_jerarquica_recursiva(
                grafo, hijo, ancho_por_hijo, separacion_vertical, 
                altura_actual - separacion_vertical, siguiente_x, 
                posiciones, nodo_actual
            )
    return posiciones


####### EJECUCIÓN PRINCIPAL #######

if __name__ == "__main__":
    # Carga el archivo CSV con las relaciones de parentesco
    ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")
    tabla_parentesco = pd.read_csv(ruta_archivo)

    # Obtiene nodos únicos de padres e hijos
    lista_padres = tabla_parentesco["padre"].unique().tolist()
    lista_hijos = tabla_parentesco["hijo"].unique().tolist()

    # Crea grafo dirigido y añade nodos y aristas
    grafo_familiar = nx.DiGraph()
    grafo_familiar.add_nodes_from(lista_padres)
    grafo_familiar.add_nodes_from(lista_hijos)

    for _, fila in tabla_parentesco.iterrows():
        grafo_familiar.add_edge(fila["padre"], fila["hijo"])

    print("Estructura del grafo generado:")
    print(grafo_familiar)

    # Ejecuta algoritmos de búsqueda
    buscar_por_anchura(grafo_familiar, "A")
    buscar_por_profundidad(grafo_familiar, "A")

    # Visualiza el grafo en formato jerárquico
    # fig, ax = plt.subplots(figsize=(5, 4))
    # posiciones = calcular_posicion_jerarquica(grafo_familiar, nodo_raiz="A")
    # nx.draw(grafo_familiar, pos=posiciones, with_labels=True, ax=ax)

    # Guardar imagen
    #plt.savefig("grafo_familiar.png", bbox_inches="tight", dpi=300)
    #plt.show()


    ######## BENCHMARK ########

    # Series de repeticiones 
    repeticiones = [1, 10, 100, 1000, 10000, 100000, 1000000]

    # Listas para guardar los tiempos
    tiempos_anchura = []
    tiempos_profundidad = []

    # Realiza el benchmark para cada cantidad de repeticiones
    for r in repeticiones:
        tiempo_1 = timeit.timeit(lambda: buscar_por_anchura(grafo_familiar, "A"), number=r)
        tiempo_2 = timeit.timeit(lambda: buscar_por_profundidad(grafo_familiar, "A"), number=r)
        tiempos_anchura.append(tiempo_1)
        tiempos_profundidad.append(tiempo_2)

    # Mostrar resultados
    # print(f"Tiempo de funcion_1: {tiempo_1:.10f} segundos")
    # print(f"Tiempo de funcion_2: {tiempo_2:.10f} segundos")

    # Graficar los resultados
    plt.plot(repeticiones, tiempos_anchura, marker='o', label='fn_anchura')
    plt.plot(repeticiones, tiempos_profundidad, marker='o', label='fn_produndidad')
    plt.xscale('log')  # Escala logarítmica en el eje X
    plt.yscale('log')  # Escala logarítmica en el eje Y
    plt.xlabel('Cantidad de iteraciones (log)')
    plt.ylabel('Tiempo en segundos (log)')
    plt.title('Benchmark comparativo por cantidad de iteraciones')
    plt.legend()
    plt.grid(True)

    plt.savefig("benchmark.png", bbox_inches="tight", dpi=300)
    plt.show()


    