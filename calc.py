import streamlit as st
import math


st.title("Calculator for degrees")

tab1, tab2, tab3= st.tabs(["Anlge","Radian" ,"Degerees" ])

with tab1:
    b=st.number_input("B channel", value=0.0)
    L=st.number_input("L channel", value=0.0)

    Up_tol=st.number_input("up tolerance", value=0.0)
    Down_tol=st.number_input("down tololerance", value=0.0)

    c=(L**2 + b**2)**0.5

    if st.button("Calculate", type="primary"):
        if c == 0:
            st.write("а or b must be not null")
        else:

            L_min=L+Up_tol
            L_max=L-Down_tol

            angle=math.degrees(math.asin(L/ c))
            angle_min = math.degrees(math.asin(L_min / c))
            angle_max = math.degrees(math.asin(L_max / c))

            tol_min=angle-angle_min
            tol_max=angle-angle_max

            st.divider()

            st.latex(f"Angle: {round(angle,2)}_{{{round(tol_min,2)}}}^{{{round(tol_max,2)}}}")


with tab2:
    st.markdown(f"### Calculator radian\n")
    st.write("Enter angle")

    angle=st.number_input("Degrees = ",value=0.0)


    if st.button("Degree", type="primary"):
        if angle == 0:
            st.write("Enter angle is not null\n")
        else:
            radian = (angle*math.pi)/180
            st.divider()
            st.markdown(f'Angle **{round(radian,3)}** radian')


with tab3:
    st.markdown(f"### Calculator degrees\n")

    st.title("Enter angle is not null \n")
    radian=st.number_input("Radian: ",value=0.0)

    if radian == 0:
        st.write("Enter angle is not null\n")
    else:
        deg = (radian*math.pi)/180
        st.divider()
        st.markdown(f'Angle: **{round(deg,2)}** radian')
