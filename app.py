import streamlit as st
import random

# タイトル
st.title("🎯 ロト6 予測アプリ")

# 説明
st.write("ブラウザの翻訳機能をオフにしてご利用ください。")

# 入力欄
prev_input = st.text_input("前回の当選番号（カンマ区切り）", value="8,17,18,19,30,39")

# 実行ボタン
if st.button("予想する"):
    try:
        # 入力された文字を数字のリストに変える
        prev_nums = [int(x.strip()) for x in prev_input.split(",")]
        
        if len(prev_nums) < 6:
            st.warning("数字を6個以上入力してください。")
        else:
            st.subheader("次回の予想 5パターン")
            for i in range(5):
                # 予測ロジック
                res = set()
                # 1. 前回の数字から1つ選ぶ（ひっぱり）
                res.add(random.choice(prev_nums))
                # 2. 残りをランダムに埋める
                while len(res) < 6:
                    res.add(random.randint(1, 43))
                
                # 表示
                st.success(f"パターン {i+1}: {sorted(list(res))}")
    except Exception as e:
        st.error(f"入力にエラーがあります。半角数字とカンマで入力してください。")
