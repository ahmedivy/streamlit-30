import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

"Basic Trygnometric Functions"

x = np.linspace(-np.pi, np.pi, 1000)

st.radio("Select a function", ("sin", "cos", "tan"), key="func")

@st.cache_data
def get_y(func):
    if func == "sin":
        return np.sin(x)
    elif func == "cos":
        return np.cos(x)
    elif func == "tan":
        return np.tan(x)

y = get_y(st.session_state.func)

fig = go.Figure(data=go.Scatter(x=x, y=y))
st.plotly_chart(fig)

"Gapminder Data"

df = px.data.gapminder().query("continent == 'Asia'")
fig_2 = px.line(df, x='year', y='lifeExp', color='country', markers=True)
st.plotly_chart(fig_2)

