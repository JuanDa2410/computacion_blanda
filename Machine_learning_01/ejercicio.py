# Universidad Tecnologica de Pererira | Computación Blanda
# Juan David Castaño Vargas
# Codigo : 1007223922


# Se importa la libreria numpy
import numpy as np

# Se cra un vector con seis elementos
a = np.array([0,1,2,3,4,5])

# SE IMPRIME EL ARRAY ... a
print(a,'\n')

# Numero de dimensiones del array
print(a.ndim,'\n')

# Numero de elementos del array
print(a.shape,'\n')

# Se cambia la estructura del array
b = a.reshape((3,2),)
print(b, '\n')

# Se verifican los cambios
print(b.ndim, '\n')
print(b.shape,'\n')

# se modifica el primer elemento de la segunda fila
b[1][0] = 77

# se verifica el cambio
print(b,'\n')

# debido a que el array b se construyo con base en el arrya a, el cambio afecta tambien al array a
print(a,'\n')

# Se realiza una copia del array
c = a.reshape((3,2)).copy()
print(c,'\n')

# se cambia el primer valor de c
c[0][0] = -99

# el array a no se modifica
print(a,'\n')

# el arrat c queda modificado
print(c,'\n')

# las operaciones se propagan a lo largo del array
d = np.array([1,2,3,4,5])

# se multplican los elemntos por 2
print(d*2, '\n')

# se elevan al cuadrado los elementos del array
print(d**2,'\n')

# nueva definicion para el array a
a = np.array([1,2,3,4,5])

# itera sobre todos los elementos del array
print(a>4, '\n')
# se ejecuta la instruccion para los elementos que cunplan la condicion 

# se cambia el contrnido de los elementos mayores a 4
a[a>4] = 1
print(a , '\n')

# los elementos cuyo contenido es igual a 1, reciben como nuevo valor el numero 777
a[a==1] = 777
print(a,'\n')

# control de valores erróneos
c = np.array([1,2,np.NAN,3,4])
print(c,'\n')

# se verifica la existencia de valores nan
print(np.isnan(c),'\n')

# se eligen todos los valores que no son nan
print(c[~np.isnan(c)],'\n')

# se calcula el promedio de los valores que no son nan
print(np.mean(c[~np.isnan(c)]),'\n')

# ----------------- Segunda parte -------------------------

data = np.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10],'\n')

#numero de datos
print(data.shape)

# se divide el array en dos vectores columnas: x, y
x = data[:,0]
y = data[:,1]

# se muestran los valores x, y
print(x,'\n')
print(y,'\n')

# Dimension de los vectores x, y
print(x.ndim,'\n')
print(y.ndim,'\n')

#Elemntos contenidos en los vectores x , y
print(x.shape,'\n')
print(y.shape,'\n')

# invesitgamos el numero de valores nan que contiene el vector y
print(np.sum(np.isnan(y)),'\n')

# numero de elementos en x, y, antes de ser comprimidos
print(x.shape, '\n')
print(y.shape,'\n')

# se eleminan elementos nan
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

# se cuentan el numero de elemntos tanto de x como de y
print(x.shape,'\n')
print(y.shape,'\n')

# se importa la libreria para graficar
import matplotlib.pyplot as plt

# dibuja los puntos (x,y) con ciruclos de tamaño 19
plt.scatter(x, y, s=10)

# titulos de la grafica
plt.title("Trafico web en el ultimo mes")
plt.xlabel("Tiempo")
plt.ylabel("Accesos por hora")

plt.xticks([w*7*24 for w in range(10)],['Semana %i' % w for w in range(10)])
plt.autoscale(tight=True)

# dibuja una cuadricula punteada ligeramente opaca
plt.grid(True, linestyle='-', color='0.75')

# muestra el grafico
plt.show()
