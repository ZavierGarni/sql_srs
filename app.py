import duckdb
import pandas as pd
import streamlit as st
import io

csv = '''
beverages, prices
orange juice, 2.5
expresso, 4
tea, 3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item, food_price
cookie, 4
chocolatine, 2.5
muffin, 3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()



st.write("Hello World !")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

with st.sidebar:
    option = st.selectbox(
        "What topic are REALLYYY you interested in ?",
        ("Joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a topic..."
    )
    st.write("You have selected : ", option)

input_text = st.text_area(label='Entrez votre input')
st.write(f"Vous avez entré : {input_text}")
result = duckdb.query(input_text).df()
st.write(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("Table : beverages")
    st.dataframe(beverages)
    st.write("Table : food_items")
    st.dataframe(food_items)
    st.write("Expected :")
    st.dataframe(solution)

with tab3:
    st.write(answer)