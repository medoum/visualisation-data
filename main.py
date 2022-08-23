import streamlit as st
import os
import pandas as pd


st.set_page_config(page_title="Tableau de bord", page_icon=":bar_chart:",
                   layout="wide")


# Path to the folder
path = "/Users/med/Desktop/test-python1/visualisation/data"

# To get the files from the dir
files = os.listdir(path)

# Extract filenames
files_list = [os.path.splitext(file)[0].lower() for file in files]
st.write(files_list)

# Extract unique alphabets of first letter of filename
files_alpha = set([filename[0] for filename in files_list])

filtered_files = [file for file in files_list]
sel_filtered_file = st.selectbox("Choisissez le fichier", filtered_files)

if sel_filtered_file:
    st.write()
    df = pd.read_csv(f"{path}/{sel_filtered_file}.csv")
    st.dataframe(df)

    # --------SIDEBAR -------
    st.sidebar.header("Please Filter Here:")
    name = st.sidebar.selectbox(
        "Select the Product Name:",
        options=df["name"].unique(),
    )
    lien = st.sidebar.selectbox(
        "Select the Product Link:",
        options=df["lien"].unique(),
    )
    tagline = st.sidebar.selectbox(
        "Select the Product Tagline:",
        options=df["tagline"].unique(),
    )
    dates = st.sidebar.multiselect(
        "Select the Product Dates:",
        options=df["dates"].unique(),
    )
    price = st.sidebar.multiselect(
        "Select the Product Price:",
        options=df["price"].unique(),
    )

# ----- MAINPAGE -------

st.title(":bar_chart: Tableau de bord des produits")
# st.markdown("##")


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Prix cher:")
with middle_column:
    st.subheader("Prix moins cher:")
with right_column:
    st.subheader("Prix moyen:")
