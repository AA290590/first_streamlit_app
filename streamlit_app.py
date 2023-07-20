import streamlit
import pandas
import requests
#snowflake-connector-python
import snowflake
import snowflake.connector
from urllib.error import URLError

streamlit.title("My MOM's New Healtiest Diner")
streamlit.header('Breakfast Specials 🥣 🥗 🐔 🥑🍞')
streamlit.text('🥣 🥗 Blueberry Oatmeal')
streamlit.text('🥑🍞 Oats avacado sandwich')
streamlit.text('🥗 🐔Banana oats pancakes')
streamlit.text('🥗 Spinach Roll')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#CREATING A FUNCTION
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized



streamlit.header("Fruityvice Fruit Advice!")
#new to display in api##
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select the fruit to get information.")
  else:
    #moved to function
   #  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
   # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   # streamlit.dataframe(fruityvice_normalized)
      back_from_function= get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.header("fruit load list contains:")
#snowflake related function
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
        
   #add button to load   
if streamlit.button('fruit load list contains'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    streamlit.dataframe(my_data_rows)



