from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai 
import os
import sqlite3

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_sql_conv(prompt,inputs):
    response = model.generate_content([prompt,input])
    return response.text 


def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

prompt = """
Given input in natural language, convert the input into 
sql language that can directly be used to query my db.
The name of my table is "STUDENT" and have 4 colums - 
[NAME,CLASS,SECTION,MARKS].\n for example, \n example 1 - 
how many entries of records are present. the sql command will be \n
SELECT COUNT(*) FROM STUDENT ;
\n the sql code should not have ''' in the beginning or end and sql word in the output\n

Input:

"""

st.set_page_config("Text to SQL")
st.header("Gemini Text2SQL")

input = st.text_input("Enter query", key=input)
submit = st.button("Execute")

if submit:
    response = get_sql_conv(prompt,input)
    st.write(response)
    rows = read_sql_query(response,"student.db")
    for row in rows:
        st.write(row)

