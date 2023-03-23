import streamlit as st
import math

pi = math.pi

# 第一个页面：公制全螺纹螺栓计算器
st.set_page_config(page_title="公制全螺纹螺栓计算器", page_icon="📈")
st.header("公制全螺纹螺栓计算器")
st.sidebar.header("公制全螺纹螺栓计算器")
diameter = st.number_input("请选择公制全螺纹螺栓的直径（单位：英寸）：M")
pitch_options = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
pitch = st.selectbox("请选择美制制全螺纹螺栓的牙距：", pitch_options)
length = st.number_input("请输入全螺纹螺栓的长度（单位）：")


def metric_full_threadedrod_calculator():
    calculated_diameter =  diameter - 0.7 * pitch
    metric_full_threaded_rod_weight = ((calculated_diameter / 2) ** 2
                                       * pi * length * 0.00001 * 0.785)

    st.write("<head><style>body {font-family: 宋体; font-size: 20px;} "
             "span {font-weight: bold; background: linear-gradient(to right, #B46060, #FFBF9B); color: white; padding: 2px 5px;} </style></head>",
             unsafe_allow_html=True)

    st.write(
        f"您输入的规格为<span style='color:white;'>     M {diameter}        </span>长度为<span style='color:white;'>   {length}   </span>"
        f"<br>对应公制<span style='color:white;'>   M{diameter}   </span>。"
        f"<br>实际落料尺寸为<span style='color:white;'>   {calculated_diameter:.3f}   </span>"
        f"<br>该尺寸重量为<span style='color:white;'>   {metric_full_threaded_rod_weight:.3f}Kg    </span>",
        unsafe_allow_html=True)


if __name__ == "__main__":
    metric_full_threadedrod_calculator()
# @Time:2023/3/23 5:10 PM
# @Artuher: Daniel
# @File: 公制全螺纹螺柱.py
# @Software: PyCharm
