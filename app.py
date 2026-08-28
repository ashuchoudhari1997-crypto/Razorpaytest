import streamlit as st
import requests

st.title("Simple Calculator")

num1 = st.number_input("Number 1")

num2 = st.number_input("Number 2")

if st.button("Calculate"):
    st.success(num1 + num2)

st.divider()

st.subheader("Premium Calculator")

st.write("Price : ₹10")

if st.button("Unlock Premium"):

    response = requests.get(
        "http://127.0.0.1:8000/create-order"
    )

    st.json(response.json())