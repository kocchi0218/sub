import streamlit as st
import pandas as pd

# データのアップロード
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    # データの抽出
    st.subheader('Extracted Data')
    select_line = st.selectbox('Select Line', data['ライン名'].unique())
    selected_data = data[data['ライン名'] == select_line]

    select_breed = st.selectbox('Select Breed', selected_data['品目略称'].unique())
    selected_data = selected_data[selected_data['品目略称'] == select_breed][['ライン名', '品目略称', '出来高数']]

    st.write(selected_data)

    st.subheader('Total Volume')
    total_volume = int(selected_data['出来高数'].sum())
    st.markdown(f"## {total_volume}")

