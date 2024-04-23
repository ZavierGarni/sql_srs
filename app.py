import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World !")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

input_text = st.text_area(label='Entrez votre input')
st.write(f"Vous avez entré : {input_text}")
result = duckdb.query(input_text).df()
st.write(result)
