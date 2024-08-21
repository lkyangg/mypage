import streamlit as st
import streamlit.components.v1 as components

# 设置为宽页面
st.set_page_config(layout="wide", page_title="lkyangg's page")
st.title("lkyangg's page")


with open('./html/wherever.html', encoding='utf-8') as f:
    components.html(f.read(), height=1800)

st.write('---')
with open('./html/gdkfq_0.html', encoding='utf-8') as p:
    components.html(p.read(), height=800)
