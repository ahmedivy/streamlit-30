import numpy as np
import streamlit as st

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
st.line_chart(y)
