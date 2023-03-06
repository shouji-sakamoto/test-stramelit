import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("steamlit 入門")

st.write("プログレスバーの表示")
"start!!"

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f"ineration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"


left_column , right_column =st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ココは右カラム")

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせを書く")


text = st.text_input("あなたの趣味を教えてください。")
condition = st.slider("あなたの今の調子は？", 0 , 100 , 50)


"あなたの趣味は、",text,"です。"
"コンディション：", condition




#if st.checkbox("ShoW Image"):
#    img = Image.open("sakamoto.jpg")
#    st.image(img, caption="sakamoto shouji" , use_column_width=True)


#df = pd.DataFrame(
#   np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#   columns=["lat", "lon"]
#)
#st.map(df)

