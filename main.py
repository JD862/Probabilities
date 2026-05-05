import random
import streamlit as st


def roll_prob(sum):

    possibles = 0
    for dice_a in range (6):
        for dice_b in range (6):
            if dice_a + dice_b == sum:
                possibles += 1

    return possibles / 36 * 100

def catan():

    if "num_inputs" not in st.session_state:
        st.session_state.num_inputs = 2

    if st.button("(+) Add input"):
        st.session_state.num_inputs += 1


    with st.form ("Catan"):
        st.write("Catan Probabilities")


        tiles = {}
        for i in range(st.session_state.num_inputs):
            col1, col2 = st.columns(2)


            with col1:
                options = ["Sheep", "Wheat", "Ore", "Brick", "Wood"]
                resource = st.selectbox("Resource Type", options, key=f"res_{i}")
            with col2:
                value = st.text_input(f"Win sum", key=f"win_{i}")

            tiles[resource] = value

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
