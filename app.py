import streamlit as st
import pandas as pd
import plotly.express as px
import random

# 1. アプリの設定
st.set_page_config(page_title="Loto6分析ツール", layout="wide")
st.title("📊 ロト6 2等・3等 ターゲット分析")

# 2. 直近の当選データ（サンプル）
# 本来はCSVから読み込みますが、まずは直近5回分を入力
history_data = {
    "回号": ["2084回", "2083回", "2082回", "2081回", "2080回"],
    "当選番号": [
        [8, 17, 18, 19, 30, 39],
        [8, 10, 13, 17, 26, 29],
        [5, 11, 14, 19, 25, 40],
        [14, 31, 32, 37, 41, 42],
        [6, 12, 30, 36, 37, 38]
    ]
}

# 3. 分析：出現頻度の集計
all_nums = [n for sublist in history_data["当選番号"] for n in sublist]
freq = pd.Series(all_nums).value_counts().reset_index()
freq.columns = ["数字", "出現回数"]

# 4. グラフ表示
st.subheader("📈 直近の出現傾向")
fig = px.bar(freq, x="数字", y="出現回数", color="出現回数", height=400)
st.plotly_chart(fig, use_container_width=True)

# 5. 予測エンジン
def predict_next(prev_nums):
    patterns = []
    for _ in range(5):
        nums = set()
        # セオリー：ひっぱり(1個)
        nums.add(random.choice(prev_nums))
        # セオリー：スライド(1個)
        nums.add(random.choice([n-1 for n in prev_nums if n > 1] + [n+1 for n in prev_nums if n < 43]))
        # 残りを埋める
        while len(nums) < 6:
            nums.add(random.randint(1, 43))
        patterns.append(sorted(list(nums)))
    return patterns

# 6. UI操作
st.divider()
prev_input = st.text_input("前回の当選番号（カンマ区切り）", "8,17,18,19,30,39")
if st.button("期待値重視で5パターン生成"):
    prev_nums = [int(x.strip()) for x in prev_input.split(",")]
    results = predict_next(prev_nums)
    for i, res in enumerate(results):
        st.info(f"パターン {i+1}: {res}")
