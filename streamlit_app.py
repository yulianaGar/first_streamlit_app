import streamlit

streamlit.title('Mi padres hacen comida saludable')
streamlit.header('Menú de desayuno')
streamlit.text('🥣 Omega 3 y avena con arándanos')
streamlit.text('🥗Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔Huevo de gallinas camperas hervidas')
streamlit.text('🥑🍞Tostada de aguacate')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

mi_lista_de_frutas = mi_lista_de_frutas.set_index('Frutas')

# Pongamos una lista de selección aquí para que puedan escoger la fruta que quieren incluir 
streamlit.multiselect("Recoger algunas frutas:", list(my_fruit_list.index)) 

# Mostrar la tabla en la página.

streamlit.dataframe(my_fruit_list)
