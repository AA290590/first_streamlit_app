import streamlit
import pandas
streamlit.title("My MOM's New Healtiest Diner")
streamlit.header('Breakfast Specials 🥣 🥗 🐔 🥑🍞')
streamlit.text('🥣 🥗 Blueberry Oatmeal')
streamlit.text('🥑🍞 Oats avacado sandwich')
streamlit.text('🥗 🐔Banana oats pancakes')
streamlit.text('🥗 Spinach Roll')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.dataframe(my_fruit_list)

#pick the fruits they want to
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.multiselect("pick some fruit's:",list(my_fruit_list.index),['Apple','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table
streamlit.dataframe(fruits_to_show)

