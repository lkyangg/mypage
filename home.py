import streamlit as st
import streamlit.components.v1 as components

# 设置为宽页面
st.set_page_config(layout="wide", page_title="lkyangg's page")

st.title("lkyangg's page")
st.write("您好，欢迎来到此页面，以下是我的几个可视化效果图展示：")

with open('./html/wherever.html', encoding='utf-8') as f:
    components.html(f.read(), height=1200)

with open('./html/gdkfq_map.html', encoding='utf-8') as p:
    components.html(p.read(), height=800)

# st.write('---')
with open('./html/stars.html', encoding='utf-8') as p:
    components.html(p.read(), height=800)
