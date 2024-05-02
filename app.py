import duckdb
import streamlit as st
import pandas as pd

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

answer_str = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

# solution_df = duckdb.sql(answer_str).df()


st.write("Hello World !")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

with st.sidebar:
    theme = st.selectbox(
        "What topic are you interested in ?",
        ("cross_joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a topic...",
    )
    st.write("You have selected : ", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

input_text = st.text_area(label="Entrez votre input")
st.write(f"Vous avez entré : {input_text}")
# result = duckdb.query(input_text).df()
# st.write(result)
#
# try:
#     result = result[solution_df.columns]
#     st.dataframe(result.compare(solution_df))
# except KeyError as e:
#     st.write("Il manque des colonnes.")
#
# nb_lignes_diff = result.shape[0] - solution_df.shape[0]
# if nb_lignes_diff != 0:
#     st.write(f"Le résultat a une différence de {nb_lignes_diff} avec la solution.")
#
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("Table : beverages")
#     st.dataframe(beverages)
#     st.write("Table : food_items")
#     st.dataframe(food_items)
#     st.write("Expected :")
#     st.dataframe(solution_df)
#
# with tab3:
#     st.write(answer_str)
#
