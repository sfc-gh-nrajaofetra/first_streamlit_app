
import streamlit
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Favorites  - Petit Dejeuner')
streamlit.text('🫕 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍵 Kale, Spnach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥒 🍞 Cuncumber Toast')


streamlit.header('🍌🍓Build your Own Fruit Smoothie 🍇🥝')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
