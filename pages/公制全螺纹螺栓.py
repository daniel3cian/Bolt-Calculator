import streamlit as st
import math

pi = math.pi

# 第一个页面：公制全螺纹螺栓计算器
st.set_page_config(page_title="公制全螺纹螺栓计算器", page_icon="📈")
st.header("公制全螺纹螺栓计算器")
st.sidebar.header("公制全螺纹螺栓计算器")
diameter = st.number_input("请选择螺栓的直径（单位：英寸）：M")
pitch_options = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
pitch = st.selectbox("请选择螺栓的牙距：", pitch_options)
k = st.number_input("请输入螺栓的头部厚度K: ")
s = st.number_input("请输入螺栓的头部对边S: ")
length = st.number_input("请输入螺栓的长度（单位）：")


def metric_hex_bolt_full_threaded():
        do = diameter - 0.7 * pitch
        heading_length = (1.1 * k * s * s )/ (do** 2)
        total_length = heading_length + length
        metric_hex_bolt_full_thread_weight = (do / 2) ** 2 * pi * 0.00001 * 0.785 * total_length

        st.write("<head><style>body {font-family: 宋体; font-size: 20px;} ", "span {font-weight: bold; background: linear-gradient(to right, #B46060, #FFBF9B); color: white; padding: 2px 5px;} </style></head>",
                 unsafe_allow_html=True)

        st.write(
        f"您输入的规格为<span style='color:white;'>     M {diameter}        </span>长度为<span style='color:white;'>   {length}   </span> 牙距为为<span style='color:white;'>   {pitch}   </span>，实际用料直径为<span style='color:white;'>   {do}   </span>"
        f"<br>头部加料为<span style='color:white;'>   {heading_length}   </span>。头部对边S为<span style='color:white;'>   {s}   </span>。头部厚度K为<span style='color:white;'>   {k}   </span>。"
        f"<br>料总长度为<span style='color:white;'>   {total_length}   </span>"
        f"重量为<span style='color:white;'>   {metric_hex_bolt_full_thread_weight:.3f}Kg    </span>",
        unsafe_allow_html=True)


if __name__ == "__main__":
    metric_hex_bolt_full_threaded()
# @Time:2023/3/23 6:09 PM
# @Artuher: Daniel
# @File: 公制全螺纹螺栓.py
# @Software: PyCharm
