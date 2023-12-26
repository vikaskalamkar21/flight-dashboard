import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px


db = DB()

st.sidebar.title('Flight Analytics')

user_option = st.sidebar.selectbox('Menu',['select one','check Flights','Analytics'])


if user_option == 'check flights':
    st.title('Check For Flights')

    col1,col2 = st.columns(2)

    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('source',sorted(city))

    with col2:
        destination = st.selectbox('destination', sorted(city))

    if st.button('search'):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)

elif user_option == 'analytics':
    airline,frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig1 = px.bar(
        x=city,
        y=frequency1,
    )

    st.plotly_chart(fig1,theme="streamlit",use_container_width=True)

    date, frequency2 = db.daily_frequency()
    fig1 = px.line(
        x=date,
        y=frequency2,
    )

    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)


else:
    st.title('Welcome to the Flight Dashboard')
    st.write("""a game-changer in aviation
                 Our initiative redefines cockpit interfaces, 
                 seamlessly integrating crucial flight data for enhanced safety and efficiency. 
                 Using cutting-edge tech, we empower pilots with real-time insights, 
                 reducing workload and elevating situational awareness.
                 Explore the features and benefits propelling this innovation forward, 
                 setting a new standard in aviation precision""")


