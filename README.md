
# 🔎 Proyecto de Visualización y Análisis de Grafos Genealógicos

Este proyecto permite construir, visualizar y analizar árboles genealógicos mediante grafos dirigidos. Además, compara el rendimiento de algoritmos de búsqueda por **anchura** y **profundidad**, aplicados sobre estructuras de grafo.

---

## 📦 **Estructura del Proyecto**

```
├── algoritmos.py           # Implementación de BFS y DFS personalizados
├── grafo_genealogico.py    # Carga de datos, construcción y visualización del grafo
├── benchmark.py            # Script para comparar el rendimiento de BFS y DFS
├── data.csv                # Archivo de entrada con relaciones padre-hijo
├── grafo_familiar.png               # Imagen generada del grafo genealógico
├── benchmark.png           # Gráfico comparativo de tiempos de ejecución
└── README.md               # Documentación del proyecto
```

---

## 🛠️ **Requisitos**

- Python 3.8+
- Librerías:
  - pandas
  - networkx
  - matplotlib

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

> **Nota:** Crea un archivo `requirements.txt` con:
> ```
> pandas
> networkx
> matplotlib
> ```

---

## 📂 **Entrada de Datos**

El archivo `data.csv` debe tener el siguiente formato:

```csv
padre,hijo
A,B
A,C
B,D
C,E
...
```

Cada fila representa una relación padre-hijo que se transforma en una arista del grafo.

---

## 📊 **Ejemplos de Salida**

### 🔵 Grafo Genealógico

Visualización generada tras construir el árbol genealógico:

![grafo_familiar](https://github.com/user-attachments/assets/7fd1a715-109d-4f64-b0b3-03f0669de227)

---

### ⏱️ Benchmark Comparativo

Gráfico que muestra el rendimiento en tiempo de los algoritmos de búsqueda por **anchura** y **profundidad**, en función de la cantidad de nodos o iteraciones:

![benchmark](https://github.com/user-attachments/assets/1d46bc7d-532c-4c1c-827b-517145a0eb3b)

---


## 🚀 **Ejecutar el Proyecto**

Para visualizar el grafo:

```bash
python app.py
```

---

## 📄 **Licencia**

Este proyecto se distribuye bajo la licencia MIT.

---

## 👨‍💻 **Autores**

Desarrollado por ["Pablo Vargas", "Ariel Salas", "Jaime Sepúlveda"].















