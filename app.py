import os
import logging
import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("Creating data folder")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

with st.sidebar:
    available_theme_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What topic are you interested in ?",
        available_theme_df["theme"].unique(),
        index=None,
        placeholder="Select a topic...",
    )
    st.write("You have selected : ", theme)

    exercise = (
        con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
        .df()
        .sort_values("last_reviewed")
        .reset_index()
    )
    st.write(exercise)

    try:
        exercise_name = exercise.loc[0, "exercise_name"]
    except KeyError as e:
        st.write("Aucune table trouvée pour cet exercice.")
    else:
        with open(f"answers/{exercise_name}.sql", "r") as f:
            answer = f.read()
            solution_df = con.execute(answer).df()

input_text = st.text_area(label="Entrez votre input")

if input_text != "":
    result = con.execute(input_text).df()
    st.write(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Il manque des colonnes.")

    nb_lignes_diff = result.shape[0] - solution_df.shape[0]
    if nb_lignes_diff != 0:
        st.write(f"Le résultat a une différence de {nb_lignes_diff} avec la solution.")

    tab2, tab3 = st.tabs(["Tables", "Solution"])

    with tab2:
        exercise_tables = exercise.loc[0, "tables"]
        for table in exercise_tables:
            st.write(f"table : {table}")
            df_tables = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(df_tables)

    with tab3:
        st.text(answer)
