import streamlit as st

# D2
# st.write('Hello world!')

# D3
# st.header('st.button')
# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

# D4
# import numpy as np
# import altair as alt
# import pandas as pd

# st.header('st.write')
# # Example 1
# st.write('Hello, *World!* :sunglasses:')

# # Example 2
# st.write(1234)

# # Example 3
# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4
# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# # Example 5
# df2 = pd.DataFrame( np.random.randn(200, 3), columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

# D8
# from datetime import time, datetime
# st.header('st.slider')
# Example 1
# st.subheader('Slider')
# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')

# # Example 2
# st.subheader('Range slider')
# values = st.slider(
#      'Select a range of values',
#      0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)

# # Example 3
# st.subheader('Range time slider')
# appointment = st.slider(
#      "Schedule your appointment:",
#      value=(time(11, 30), time(12, 45)))
# st.write("You're scheduled for:", appointment)

# # Example 4
# st.subheader('Datetime slider')
# start_time = st.slider(
#      "When do you start?",
#      value=datetime(2020, 1, 1, 9, 30),
#      format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)

# D9
# import pandas as pd
# import numpy as np

# st.header('Line chart')

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# st.write(chart_data)
# st.line_chart(chart_data)


# D10
# st.header('st.selectbox')

# option = st.selectbox(
#      'What is your favorite color?',
#      ('Blue', 'Red', 'Green'))

# st.write('Your favorite color is ', option)

# D11
# st.header('st.multiselect')
# options = st.multiselect(
#      'What are your favorite colors',
#      ['Green', 'Yellow', 'Red', 'Blue'],
#      ['Yellow', 'Red'])
# st.write('You selected:', options)

# D12
# st.header('st.checkbox')
# st.write ('What would you like to order?')
# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')
# if icecream:
#      st.write("Great! Here's some more 🍦")
# if coffee: 
#      st.write("Okay, here's some coffee ☕")
# if cola:
#      st.write("Here you go 🥤")

# D14
# import pandas as pd
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report

# st.header('`streamlit_pandas_profiling`')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# pr = df.profile_report()
# st_profile_report(pr)

# D15
st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
