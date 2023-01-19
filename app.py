import streamlit as st
import pandas as pd
import joblib

# Title
st.title("Life Expectancy APP")

# Add a text input
col1, col2 = st.columns(2)
with col1:
    st.header("Datos del país")
    pais = st.selectbox("País:",['Albania', 'Austria', 'Belarus', 'Belgium', 'Bulgaria',
                            'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia',
                            'Finland', 'France', 'Germany', 'Greece', 'Hungary',
                            'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
                            'Malta', 'Moldova', 'Montenegro', 'Netherlands',
                            'North Macedonia', 'Norway', 'Poland', 'Portugal',
                            'Romania', 'Russian Federation', 'Serbia', 'Slovak Republic',
                            'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine',
                            'United Kingdom'])
    anyo = st.number_input("Año:", 0)
    población = st.number_input("Población del país:", 0)

with col2:
    st.header("Datos per capita")
    emisiones_co2 = st.number_input("Emisiones CO2(m/tonelada per capita):")
    consumo_electrico = st.number_input("Consumo electrico per capita(kWh):")
    GDP_per_capita = st.number_input("PIB per capita:")
    consumo_cerveza = st.number_input("Consumo de cerveza:")

st.header("Índices generales")
gasto_salud = st.slider("Gasto en salud(%):", 0.0, 100.0)
area_forestal = st.slider("Area forestal(%):", 0.0, 100.0)
uso_internet = st.slider("Índice uso internet(%):", 0.0, 100.0)
gasto_militar = st.slider("Gasto militar(%):", 0.0, 100.0)
defecación_pública = st.slider("Índice defecación pública(%):", 0.0, 100.0)
servicio_agua = st.slider("Índice servicios de agua(%):", 0.0, 100.0)
obesidad_adultos = st.slider("Índice obesidad adulta(%):", 0.0, 100.0)
    

# Display the entered name
if st.button("Submit"):
    
    life_model = joblib.load("life.pkl")

    X = pd.DataFrame([[pais, anyo, población, emisiones_co2, gasto_salud, consumo_electrico, area_forestal,
                        GDP_per_capita, uso_internet, gasto_militar, defecación_pública,
                        servicio_agua, obesidad_adultos, consumo_cerveza]],
                        columns = ["Country", "Year", "Population", "CO2 emissions", "Health expenditure",
                        "Electric power consumption", "Forest area", "GDP per capita",
                        "Individuals using the Internet", "Military expenditure",
                        "People practicing open defecation", "People using at least basic drinking water services",
                         "Obesity among adults", "Beer consumption per capita"])

    X = X.replace(['Albania', 'Austria', 'Belarus', 'Belgium', 'Bulgaria',
                         'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia',
                         'Finland', 'France', 'Germany', 'Greece', 'Hungary',
                         'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
                         'Malta', 'Moldova', 'Montenegro', 'Netherlands',
                         'North Macedonia', 'Norway', 'Poland', 'Portugal',
                         'Romania', 'Russian Federation', 'Serbia', 'Slovak Republic',
                         'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine',
                         'United Kingdom'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                             11, 12, 13, 14, 15, 16, 17, 18, 19,
                                             20, 21, 22, 23, 24, 25, 26, 27, 28,
                                             29, 30, 31, 32, 33, 34, 35, 36, 37])

    prediction = life_model.predict(X)[0]
    
    st.text(f"La esperanza de vida es de {prediction}")