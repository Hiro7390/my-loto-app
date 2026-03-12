import streamlit as st
import pandas as pd
import random

# シンプルな設定
st.title("🎯 ロト6 予測アプリ")

# 前回の番号入力
prev_input = st.text_input("前回の当選番号（カンマ区切り）", "8,17,18,19,30,39")

if st.button("予測する"):
    prev_nums = [int(x.strip()) for x in prev_input.split(",")]
    
    st.subheader("次回の予想 5パターン")
    for i in range(5):
        # 簡易的なロジック
        res = set()
        res.add(random.choice(prev_nums)) # ひっぱり
        while len(res) < 6:
            res.add(random.randint(1, 43))
        st.success(f"パターン {i+1}: {sorted(list(res))}")

# 簡易的な表を表示（グラフの代わりにまずはこれ）
st.write("---")
st.write("※ブラウザの翻訳機能をオフにしてお使いください。")
