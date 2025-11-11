import streamlit as st
import pandas as pd

with open("20025 mount.csv", "r", encoding="utf-8", errors="ignore") as f:
    df = pd.read_csv(f, sep="\t")

st.title("藥品查詢介面")
ingredient = st.text_input("請輸入主成分")

if ingredient:
    if "藥品名稱" in df.columns:
        filtered = df[df["藥品名稱"].str.contains(ingredient, case=False, na=False)]
        result = filtered.groupby(["藥品代碼", "藥品名稱"], as_index=False)["數量"].sum()
        st.dataframe(result)
    else:
        st.error("找不到『藥品名稱』欄位，請檢查 CSV 檔案格式")
    
    # 依藥品代碼與名稱加總數量
    result = filtered.groupby(['藥品代碼', '藥品名稱'], as_index=False)['數量'].sum()
    
    # 顯示結果表格
    st.dataframe(result)
    
    # 顯示總數量
    total = result['數量'].sum()
    st.write(f"👉 主成分 **{ingredient}** 的總數量：{total}")









