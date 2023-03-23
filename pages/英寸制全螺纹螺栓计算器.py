import streamlit as st
import math
pi = math.pi

# 第一个页面：英寸制全螺纹螺栓计算器
st.header("英寸制全螺纹螺栓计算器")
diameter_options = [1/2, 5/8, 3/4, 7/8, 1, 1 + 1/2, 1 +  3/4, 2]
diameter = st.selectbox("请选择英寸制全螺纹螺栓的直径（单位：英寸）：", diameter_options)
pitch_options = [4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
pitch = st.selectbox("请选择英寸制全螺纹螺栓的牙数（即一英寸几牙）：", pitch_options)
length = st.number_input("请输入螺栓的长度（单位毫米）：")

def inch_full_threadedrod_calculator():
    calculated_diameter = 25.4 * diameter - 0.7 * (25.4 / pitch)
    inch_full_threaded_rod_weight = ((calculated_diameter / 2) ** 2
                                     * pi * length * 0.00001 * 0.785)

    st.write("<head><style>body {font-family: 宋体; font-size: 20px;} "
             "span {font-weight: bold; background: linear-gradient(to right, #B46060, #FFBF9B); color: white; padding: 2px 5px;} </style></head>",
             unsafe_allow_html=True)

    st.write(
        f"您输入的规格为<span style='color:white;'>      {diameter}        </span>英寸长度为<span style='color:white;'>   {length}   </span>"
        f"<br>对应公制<span style='color:white;'>   M{25.4 * diameter:.3f}   </span>。"
        f"<br>实际落料尺寸为<span style='color:white;'>   {calculated_diameter:.3f}   </span>"
        f"<br>该尺寸重量为<span style='color:white;'>   {inch_full_threaded_rod_weight:.3f}Kg    </span>",
        unsafe_allow_html=True)

if __name__ == "__main__":
    inch_full_threadedrod_calculator()