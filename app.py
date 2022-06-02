# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:28:55 2022

@author: sowmu
"""

import streamlit as st
st.write("hello")

data_file = st.file_uploader("Upload CSV",type=["csv"])
if data_file is not None:
    file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
    st.write(file_details)
