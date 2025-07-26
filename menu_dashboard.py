
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("Skywalk_Engineering_Dataframe.csv", index_col=0)


#dashboard UI
st.title("Menu Engineering Dashboard")
st.write("Analyze item performance by profitability and popularity.")

category = st.selectbox("Select Category", options=df['POS Group'].unique())
filtered_df = df[df["POS Group"] == category]

subcategory = st.selectbox("Select a POS SubGroup", options=filtered_df["POS Subgroup"].unique())

filtered_df = filtered_df[filtered_df["POS Subgroup"] == subcategory]

mycategory = st.selectbox("Select the final group", options=filtered_df["My Group"].unique())
filtered_df = filtered_df[filtered_df["My Group"] == mycategory]

st.dataframe(filtered_df[["POS ITEM", 'PRICE', 'COST', 'QTY', 'Group Rating', 'Subgroup Rating', 'My Group Rating']])

# Scatter Plot
fig = px.scatter(
    filtered_df,
    x="QTY",
    y="PROFIT",
    color="My Group Rating",
    hover_name="POS ITEM",
    hover_data={
        'PRICE': True,
        "COST" : True,
        "TOTAL PROFIT" : True,
        "Group Rating" : True,
        "Subgroup Rating" : True,
        "My Group Rating" : True,
        "QTY" : False,
        "PROFIT" : False
    },
    title="Menu Engineering Matrix (Hover for Details)",
    labels={"QTY": "Popularity", "PROFIT": "Profitability"},
    size_max=60
)

fig.update_traces(marker=dict(size=15, line=dict(width=1, color='DarkSlateGrey')))

st.plotly_chart(fig, use_container_width=True)
