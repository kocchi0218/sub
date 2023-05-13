import streamlit as st
import pandas as pd

# エクセルファイルの読み込み
uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=["xlsx", "xls"])

if uploaded_file is not None:
    with open('temp_file.xlsx', 'wb') as f:
        f.write(uploaded_file.getbuffer())

    data = pd.read_excel('temp_file.xlsx')

    # 特定の項目を取り出す
    selected_data = data[['ライン名', '品目略称', '出来高数']]  # 取り出したい列名を指定

    # 取り出したデータを表示
    st.write(selected_data)

    condition = st.text_input("抽出する条件を入力してください")

    if condition:
        filtered_data = data[data["ライン名"].str.contains(condition)]  # 条件に基づいてデータを抽出
        st.write("抽出されたデータ")
        st.dataframe(filtered_data)  # 抽出されたデータを表示
