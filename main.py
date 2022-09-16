import streamlit as st
import os
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data
from datetime import datetime

st.set_page_config(
    page_title="Tableau de bord", page_icon="📊 ", layout="centered"
)


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
sel_filtered_file = st.selectbox("Choisissez le lien", filtered_files)

if sel_filtered_file:
    st.write()
    df = pd.read_csv(f"{path}/{sel_filtered_file}.csv")
    st.dataframe(df)
# --------SIDEBAR -------
st.sidebar.header("Veillez selectionner ici:")
name = st.sidebar.selectbox(
    "Selectionnez la marque du produit:",
    options=df["name"].unique(),
)
tagline = st.sidebar.selectbox(
    "Selectionner le produit:",
    options=df["tagline"].unique(),
)
dates = st.sidebar.multiselect(
    "Selectionner la date d'ajout du produit:",
    options=df["dates"].unique(),
)
price = st.sidebar.multiselect(
    "Selectionner le prix du produit:",
    options=df["price"].unique(),
)

# ----- MAINPAGE -------


measurements = df.drop(labels=["name"], axis=1).columns.tolist()




x_axis = st.sidebar.selectbox("X-Axis", measurements)
y_axis = st.sidebar.selectbox("Y-Axis", measurements, index=1)



if x_axis and y_axis:
    scatter_fig = plt.figure(figsize=(6,4))

    scatter_ax = scatter_fig.add_subplot(111)

    malignant_df = df[df["dates"] == "malignant"]
    benign_df = df[df["price"] == "benign"]

    malignant_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="tomato", alpha=0.6, ax=scatter_ax, label="Malignant")
    benign_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="dodgerblue", alpha=0.6, ax=scatter_ax,
                        title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()), label="Benign")

    
df = pd.DataFrame(
     np.random.randn(200, 5),
     columns=['tagline', 'price','name','lien','dates'])

hover = alt.selection_single(
        fields=["dates"],
        nearest=True,
        on="mouseover",
        empty="none",
    )
lines =  (alt.Chart(df, title="Evolution des prix")
            .mark_square()
            .encode(
                color = "tagline",
                x = "dates",
                y = "price",
                
)
    )
points = lines.transform_filter(hover).mark_circle(size=65)
tooltips = (
        alt.Chart(df)
        .mark_rule()
        .encode(
            x="dates",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                # alt.Tooltip("name", title="Name"),
                alt.Tooltip("price", title="Price (USD)"),
                ],
            )
            .add_selection(hover)
        )
chart = lines + points + tooltips.interactive()

st.altair_chart(
    chart.interactive(),
use_container_width=True
)
        
# st.subheader("Evolution des prix par marque")
# df = pd.DataFrame(
#      np.random.randn(200, 4),
#      columns=['tagline', 'price','name','lien'])

# tagline = alt.Chart(df).mark_circle().encode(
#      x='name', y='tagline', size='price', color='lien', tooltip=['tagline', 'price', 'name','lien'])

# st.altair_chart(tagline, use_container_width=True)


    
# @st.experimental_memo
    # def get_data(df):
#     source = data.
#     source = source[source.dates.gt("2022-09-01")]
#     return source

# source = get_data()

# # Define the base time-series chart.
# def get_chart(data):
#     hover = alt.selection_single(
#         fields=["dates"],
#         nearest=True,
#         on="mouseover",
#         empty="none",
#     )

#     lines = (
#         alt.Chart(data, title="Evolution of stock prices")
#         .mark_line()
#         .encode(
#             x="dates",
#             y="price",
#             color="symbol",
#         )
#     )

#     # Draw points on the line, and highlight based on selection
#     points = lines.transform_filter(hover).mark_circle(size=65)

#     # Draw a rule at the location of the selection
#     tooltips = (
#         alt.Chart(data)
#         .mark_rule()
#         .encode(
#             x="yearmonthdate(dates)",
#             y="price",
#             opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
#             tooltip=[
#                 alt.Tooltip("dates", title="Date"),
#                 alt.Tooltip("price", title="Price (USD)"),
#             ],
#         )
#         .add_selection(hover)
#     )
#     return (lines + points + tooltips).interactive()

# chart = get_chart(source)

