import streamlit as st

tab1, tab2 = st.tabs(['tab1',"tab2"])
with tab1:
    st.write("this is tab1")
with tab2:
    st.write("this is tab2")