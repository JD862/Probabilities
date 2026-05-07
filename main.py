import random
import streamlit as st


def roll_prob(sum):

    possibles = 0
    for dice_a in range (1, 7):
        for dice_b in range (1, 7):
            if dice_a + dice_b == sum:
                possibles += 1

    return possibles / 36 * 100

def catan():

    if "num_inputs" not in st.session_state:
        st.session_state.num_inputs = 3

    col1, col2 = st.columns(2)

    with col1:
        if st.button("(+) Add input"):
            st.session_state.num_inputs += 1

    with col2:
        if st.button("Reset inputs"):
            st.session_state.num_inputs = 3


    with st.form ("Catan"):
        st.write("Catan Probabilities")


        tiles = []
        for i in range(st.session_state.num_inputs):
            col1, col2 = st.columns(2)


            with col1:
                options = ["Sheep", "Wheat", "Ore", "Brick", "Wood"]
                resource = st.selectbox("Resource Type", options, key=f"res_{i}")
            with col2:
                value = st.text_input(f"Win sum", key=f"win_{i}")

            tiles.append(resource + "/" + value)

        wanted = st.multiselect("Wanted options", options, key="wanted_options")

        submit = st.form_submit_button("Done")

        if submit:
            st.write(tiles)
            prob = 0

            for i in range (len(tiles)):
                if (tiles[i].split("/"))[0] in wanted:
                    prob += roll_prob(int((tiles[i].split("/"))[1]))
                    st.write(prob)

            st.write(f"Prob = {round(prob, 2)}%")


def main():

    st.title("Probabilities")
    options = ["Catan"]
    game = st.selectbox("Game", options)

    if game == "Catan":
        catan()

if __name__ == "__main__":
    main()
