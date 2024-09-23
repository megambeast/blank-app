import streamlit as st

st.title("🎈 My Beginner App")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import pandas as pd
import numpy as np

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.DataFrame(np.random.randint(0, 100, size=(3, 3)), columns=['Column1', 'Column2', 'Column3'])

st.table(df)

