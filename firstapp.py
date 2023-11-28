import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
def add_data(name,age):
    conn = sqlite3.connect("sharawy.db")
    cursor=conn.cursor()
    data=[(name,age)]
    cursor.executemany('insert into users(name,age) values(?,?)',data)
    conn.commit()
    conn.close()

def read_data():
    conn=sqlite3.connect("sharawy.db")
    query='select * from users'
    df=pd.read_sql_query(query,conn)
    return df
def clear_db():
    conn=sqlite3.connect("sharawy.db")
    cursor=conn.cursor()
    cursor.execute('DELETE FROM users')
    conn.commit()
    conn.close()
st.bar_chart(data=read_data(),x='name',y='age')
title = st.text_input('Movie title', 'Life of Brian')
if st.button('insert'):
    clear_db()
    add_data('momom',15)

    

