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
streamlit.dataframe(my_fruit_list)


