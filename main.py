import random
import streamlit as st



def catan():
    with st.form ("Catan"):
        st.write("Catan Probabilities")


        submit = st.form_submit_button("Done")

        if submit:
            st.write("Prob = ")


def main():

    st.title("Probabilities")
    options = ["Catan"]
    game = st.selectbox("Game", options)

    if game == "Catan":
        catan()

if __name__ == "__main__":
    main()
