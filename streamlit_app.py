import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Mi padres hacen comida saludable')
streamlit.header('Menú de desayuno')
streamlit.text('🥣 Omega 3 y avena con arándanos')
streamlit.text('🥗Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔Huevo de gallinas camperas hervidas')
streamlit.text('🥑🍞Tostada de aguacate')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')


my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')



# Pongamos una lista de selección aquí para que puedan escoger la fruta que quieren incluir 
fruits_selected=streamlit.multiselect("Pick some fruots:", list(my_fruit_list.index), ['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Mostrar la tabla en la página.

streamlit.dataframe(fruits_to_show)



# create block
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice: 
    streamlit.error("Please select a fruit to get information.")
  else: 
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e: 
  streamlit.error()
    
    


streamlit.header("the fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    return my_cur.fetchall()

#ADD a button to load the fruit
if streamlit.button('GET FRUIT LOAD LIST'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)



def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.excute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES('from streamlit')")
    return "Thanks for adding "+new_fruit
    
 
add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)


