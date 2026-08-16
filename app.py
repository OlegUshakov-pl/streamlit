import streamlit as st

st.title("My Streamlit App")

st.write("Welcome to my Streamlit application! This is a simple app to demonstrate the capabilities of Streamlit.")

st.markdown("""
### Welcome to my Streamlit **application**! This is a simple app to demonstrate the capabilities of Streamlit. You can use this app to display text, images, and interactive widgets.
""")

st.text("You can also use Streamlit to create interactive data visualizations and dashboards.")

name=st.text_input("Enter your name:", "")

if button := st.button("Submit"):
    st.markdown(f"Hello, **{name}**! Welcome to the app.") 

age=st.slider("Select your age:", 0, 120, 1)

if age==0:
    st.write(f"There is no age.")
elif age<100:
    st.write(f"You are living {age}.")
else:
    st.write(f"Stupid {age}.")

st.divider()

# st.sidebar.title("Sidebar")
# st.sidebar.write("This is the sidebar where you can add additional information or controls.")

# cont = st.container(border=True, horizontal_alignment="center")

# col1, col2 = cont.columns(2)

# col1.write("This is column 1.")

# col2.write("This is column 2.")

# st.divider()

# tab1, tab2, tab3 = st.tabs(["Chart", "Data", "Settings"])

# with tab1:
#     st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
# with tab2:
#     st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
# with tab3:
#     st.checkbox("Show gridlines")

# st.divider()

# st.latex(r"""
# E = mc^2
# """)

st.divider()

num=st.number_input("Enter a length:", value=0)
up=st.number_input("Enter a up:", value=0)
down=st.number_input("Enter a down:", value=0)


if st.button("Show"):
    st.latex(f"{num}_{{{down}}}^{{{up}}}")
  
