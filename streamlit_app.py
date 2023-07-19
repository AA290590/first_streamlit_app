import streamlit
import pandas
import requests
#snowflake-connector-python
import snowflake
import snowflake.connector

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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #writes the data to screen 


#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#take the json version of it and normalise
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it screen as table
streamlit.dataframe(fruityvice_normalized)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cnx = snowflake.connector.connect(
                user = "apoorva",
password = "Amol1#12",
account = "as58208.ca-central-1.aws" ,
warehouse = "PC_RIVERY_WH" ,
database = "PC_RIVERY_DB" ,
schema = "public",
role = "accountadmin"
                )
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("fruit load list contains")
streamlit.text(my_data_row)


#display the table
#streamlit.dataframe(fruits_to_show)

