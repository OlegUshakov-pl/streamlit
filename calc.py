import streamlit as st
import math


st.title("Calculator for angles")

tab1, tab2 = st.tabs(["Anlge","Cont" ])

with tab1:
    a=st.number_input("B channel", value=0.0)
    L=st.number_input("L channel", value=0.0)

    Up_tol=st.number_input("up tolerance", value=0.0)
    Down_tol=st.number_input("down tololerance", value=0.0)

    c=(l**2 + b**2)**0.5

    if st.button("Calculate", type="primary"):
        if c == 0:
            st.write("а or b must be not null")
        else:

            L_min=L+Up_tol
            L_max=L-Down_tol
            angle_up = math.degrees(math.asin(up_c / c))
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
