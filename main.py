#import random # Not used yet
import streamlit as st


def roll_prob(sum): # Totals all possible ways to get a sum

    possibles = 0
    for dice_a in range (1, 7):
        for dice_b in range (1, 7):
            if dice_a + dice_b == sum:
                possibles += 1

    return possibles / 36 * 100 # In present

def catan():

    if "num_inputs" not in st.session_state:
        st.session_state.num_inputs = 6 # Initial Tiles

    col1, col2 = st.columns(2)

    with col1:
        if st.button("(+) Add input"):
            st.session_state.num_inputs += 1 # Gain more tiles

    with col2:
        if st.button("Reset inputs"):
            st.session_state.num_inputs = 6 # New game


    with st.form ("Catan"):
        st.write("Catan Probabilities")


        tiles = []
        for i in range(st.session_state.num_inputs):
            col1, col2, col3, col4 = st.columns(4) # Divisions

            with col1:
                options = ["Sheep", "Wheat", "Ore", "Brick", "Wood"] # Choices
                resource = st.selectbox("Resource Type", options, key=f"res_{i}") # Different keys
            with col2:
                win_value = st.text_input(f"Win sum", key=f"win_{i}")
            with col3:
                amts = st.text_input(f"Number of settlements", key=f"amt_{i}")
            with col4:
                st.write("")
                st.write("")
                blocked = st.toggle("Blocked?", key=f"block_{i}")
                
            
            if amts.isdigit() == True:
                for i in range (int(amts)):
                    if blocked == False:
                        tiles.append(resource + "/" + win_value)
            else:
                tiles.append(resource + "/" + win_value)


        wanted = st.multiselect("Wanted options", options, key="wanted_options") # What player wants

        submit = st.form_submit_button("Done")

        if submit:
            prob = 0

            for i in range (len(tiles)):
                if (tiles[i].split("/"))[0] in wanted: # Resource type 
                    prob += roll_prob(int((tiles[i].split("/"))[1]))

            st.write(f"Prob = {round(prob, 2)}%") # Final


def main():

    st.title("Probabilities")
    options = ["Catan"]
    game = st.selectbox("Game", options)

    if game == "Catan":
        catan()

if __name__ == "__main__":
    main()
