import streamlit as st
import pandas as pd

# データのアップロード
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    # 列名の確認
    st.write(data.columns.tolist())

    # 列の選択
    column_to_display = st.selectbox("Which column to display?", data.columns.tolist())

    # 選択した列のデータを表示
    st.write(data[column_to_display])

    # データの抽出
    st.subheader('Extracted Data')
    select_line = st.selectbox('Select Line', data['ライン名'].unique())
    selected_data = data[data['ライン名'] == select_line]
    st.write(selected_data)
