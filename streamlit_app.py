import streamlit
import pandas
import requests
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

#pick the fruits they want to
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#fruits_selected=streamlit.multiselect("pick some fruit's:",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json()) #writes the data to screen 

#take the json version of it and normalise
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it screen as table
streamlit.dataframe(fruityvice_normalized)




#display the table
#streamlit.dataframe(fruits_to_show)

