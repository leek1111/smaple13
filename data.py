# -*- coding:utf-8 -*-
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from pathlib import Path
from utils import date_select

@st.cache_data
def load_data():
    comp_dir = Path('C:/Users/YONSAI/Desktop/csv')
    train = pd.read_csv(comp_dir / 'train_sample_201516.csv')
    stores = pd.read_csv(comp_dir / 'stores.csv')
    oil = pd.read_csv(comp_dir / 'oil.csv')
    transactions = pd.read_csv(comp_dir / 'transactions.csv')
    holidays_events = pd.read_csv(comp_dir / 'holidays_events.csv')
    return train, stores, oil, transactions, holidays_events
def run_data():
    train, stores, oil, transactions, holidays_events = load_data()

    menu = st.sidebar.selectbox("Submenu", ['Train','Stores', 'Oil', 'Transactions','Holidays_events'])

    if menu == 'Train':
            st.markdown("## Train 데이터")
            st.dataframe(train, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)

    elif menu == 'Stores':
            st.markdown("## Stores 데이터")
            st.dataframe(stores, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)

    elif menu == 'Oil':
            st.markdown("## Oil 데이터")
            st.dataframe(oil, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)

    elif menu == 'Transactions':
            st.markdown("## Transactions 데이터")
            st.dataframe(transactions, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)

    else:
            st.markdown("## Holiday Events 데이터")
            st.dataframe(holidays_events, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)