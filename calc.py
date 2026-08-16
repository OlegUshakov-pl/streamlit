import streamlit as st
import math


st.title("Calculator for angles")

tab1, tab2 = st.tabs(["Anlge","Cont" ])

with tab1:
    a=st.number_input("a channel", value=0)
    b=st.number_input("b channel", value=0)
    up=st.number_input("up tol", value=0.0)
    down=st.number_input("down tol", value=0.0)

    c=(a**2 + b**2)**0.5
    if st.button("Calculate", type="primary"):
        if c == 0:
            st.write("Введите ненулевые значения а или b")
        else:
            up_c = b - up
            down_c = b + down
            alpha_up = math.degrees(math.asin(up_c / c))
            alpha_down = math.degrees(math.asin(down_c / c))

            alpha = math.degrees(math.asin(a / c))
            up_angle=round(alpha_up - alpha,2)
            down_angle=round(alpha_down - alpha,2)

            st.latex(f"{round(alpha,2)}_{{{round(alpha_down,2)}}}^{{{round(alpha_up,2)}}}")


with tab2:
    st.title("Calculator\n")
    st.write("Enter angle")

    angle=st.number_input("a = ",value=0.0)

    def calc_angle(a):
        if angle == 0:
            st.write("Введите ненулевые значения a")

        else:
            x = (angle*math.pi)/180
            st.write(f'Angle radian {round(x,2)}')
            calc_angle(angle)
            st.button("Angle", on_click=calc_angle, args=(angle,), type="primary")
