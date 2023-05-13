import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'gender': ['female', 'male']
})

st.write(df)
st.dataframe(df)