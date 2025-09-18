import pandas as pd # leer archivos cvs, calcular media, moda, mediana, regresion, etc.
import matplotlib.pyplot as plt #graficar
import seaborn as sns #mapas de calor

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", None)


    # 1) Cargar datos

#Leemos el csv con los datos del caso (15 tiendas, variables explicitas)
df = pd.read_csv("escenario_tiendas_15.csv", encoding="utf-8-sig") # df = data frame

#Vistazo rapido al tamaño de la tabla y a los tipos de datos
print("Forma (filas, columnas):", df.shape)
print("\nTipos de datos:\n", df.dtypes)

#Conteo de valores faltantes (NaN (not a number)) por columna
print("\nValores faltantes por columna:\n", df.isna().sum())

    # 2) Estadistica descriptiva basica

# describe() nos da conteo, medio, std, min, cuartiles y max para varibales numericas
desc = df.select_dtypes("number").describe()
print("\nDescripcion numerica:\n", desc)

    # 3) Mediana, media y moda para variables clave

def calcular_tendencia(var):
    media = df[var].mean()
    mediana = df[var].median()
    moda = df[var].mode().iloc[0] if not df[var].mode().empty else None
    return media, mediana, moda

#Elegimos dos variables para ejemplificar: Ventas_Mensuales y Precio_Promedio
var1 = "Ventas_Mensuales"
var2 = "Precio_Promedio"

media1, mediana1, moda1 = calcular_tendencia(var1)
media2, mediana2, moda2 = calcular_tendencia(var2)

print("\nIndicadores de tendencia central:")
print(f"{var1} -> media: {media1:.2f}, mediana: {mediana1:.2f}, moda: {moda1}")
print(f"{var2} -> media: {media2:.2f}, mediana: {mediana2:.2f}, moda: {moda2}")

    # 4) Gráficos simples

# 4.1) Boxplot (caja y bigotes) de Ventas_Mensuales

def mostrar_boxplot(variable):
    plt.figure()
    sns.boxplot(x=df[variable])
    plt.title(f"Boxplot - {variable}")
    plt.show()
    
# 4.2) Histograma de Ventas_Mensuales
def mostrar_histograma(variable, bins=10):
    plt.figure()
    sns.histplot(df[variable], bins=bins, kde=True)
    plt.title(f"Histograma - {variable}")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.show()
    
mostrar_boxplot(var1)
mostrar_histograma(var1)
mostrar_boxplot(var2)

    # 5) Matriz de correlación y heatmap

# Calculamos la matriz de correlaciones solo con columnas numéricas
corr = df.select_dtypes("number").corr()
print("\nMatriz de correlación:\n", corr)

# Heatmap para visualizar de forma gráfica las correlaciones
plt.figure()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Heatmap de correlaciones (variables numéricas)")
plt.show()

    # 6) Correlaciones más fuertes con la variable objetivo

if var1 in corr.columns:
    top_corr = corr[var1].dropna().abs().sort_values(ascending=False).head(6)
    print(f"\nCorrelaciones más fuertes (absolutas) con {var1}:\n", top_corr)

print("\nAnalisis completo.")

