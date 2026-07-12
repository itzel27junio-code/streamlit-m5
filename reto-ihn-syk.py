import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

### Leemos los datos de Employee_data
df = pd.read_csv("Employee_data.csv")

# i. Título y descripción
st.title("Análisis de desempeño de colaboradores de Marketing")
st.write(
    "Esta aplicación permite analizar el desempeño de los colaboradores de Socialize your Knowledge mediante diferentes filtros y gráficos."
)

# ii. Logotipo de la empresa Socialize your knowledge (syk)
# st.image("logo_syk.png", width=400)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_syk.png", width=400)


### Controles
st.sidebar.header("Filtros") 

# iii. Seleccionar el género del empleado 
genero = st.sidebar.selectbox( "Selecciona el género", ["Todos"] + list(df["gender"].unique()) ) 
# iv. Seleccionar un rango del puntaje de desempeño del empleado 
desempeno = st.sidebar.slider( "Rango del puntaje de desempeño", 1, 5, (1,5) ) 
# v. Seleccionar el estado civil del empleado # Cambiamos la columna marital_status para que los muestre en español 
# (en caso de que haya más estados civiles, agregarlos al diccionario) 
dict_estado_civil = { "Single": "Soltero(a)", "Married": "Casado(a)", "Divorced": "Divorciado(a)", "Separated": "Separado(a)", "Widowed": "Viudo(a)"} 
df["marital_status"] = df["marital_status"].replace(dict_estado_civil) 
estado_civil = st.sidebar.selectbox( "Estado civil", ["Todos"] + list(df["marital_status"].unique()) ) 

datos = df.copy() 
if genero != "Todos": 
    datos = datos[datos["gender"] == genero] 

datos = datos[ (datos["performance_score"] >= desempeno[0]) & (datos["performance_score"] <= desempeno[1]) ] 

if estado_civil != "Todos": 
    datos = datos[datos["marital_status"] == estado_civil]

# st.write(datos) 

### Gráficos
# vi. Gráfico en donde se visualice la distribución de los puntajes de desempeño
st.subheader("Distribución del puntaje de desempeño")
fig, ax = plt.subplots()
datos["performance_score"].value_counts().sort_index().plot(
    kind="bar",
    color="#23C5C8",
    ax=ax
)

ax.set_xlabel("Puntaje")
ax.set_ylabel("Número de empleados")
ax.tick_params(axis="x", rotation=0)

st.pyplot(fig)
# plt.close(fig)

# vii. Gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado
st.subheader("Promedio de horas trabajadas por género")
fig, ax = plt.subplots()
datos.groupby("gender")["average_work_hours"].mean().plot(
    kind="bar",
    color="#23C5C8",
    ax=ax
)

ax.set_ylabel("Horas promedio")
ax.tick_params(axis="x", rotation=0)

st.pyplot(fig)
# plt.close(fig)

# viii. Gráfico en donde se visualice la edad de los empleados con respecto al salario de los mismo
st.subheader("Edad de los empleados vs Salario")
fig, ax = plt.subplots()
ax.scatter(
    datos["age"],
    datos["salary"],
    color="#23C5C8",
)

ax.set_xlabel("Edad")
ax.set_ylabel("Salario")

st.pyplot(fig)
# plt.close(fig)

# ix. Gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño
st.subheader("Horas trabajadas vs Puntaje de desempeño")
fig, ax = plt.subplots()
ax.scatter(
    datos["average_work_hours"],
    datos["performance_score"],
    color="#23C5C8",
)

ax.set_xlabel("Horas promedio")
ax.set_ylabel("Puntaje")

st.pyplot(fig)
# plt.close(fig)


### Conclusión
st.subheader("Conclusión")
st.write("""
Este dashboard permite observar la distribución del desempeño de los empleados, comparar las horas promedio 
trabajadas entre hombres y mujeres, analizar la relación entre la edad y el salario, así como comparar las 
horas promedio trabajadas y los puntajes de desempeño obtenidos.
Los filtros facilitan visualizar únicamente los colaboradores que cumplen con las características seleccionadas.
""")