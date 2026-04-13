import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "services", "lisbon.xlsx")


def render_dashboard(file):

    data = pd.read_excel(file)
    df = pd.DataFrame(data)

    st.set_page_config(layout="wide",page_title="Pogoda")

    st.title("Dashboard pogodowy")

    st.sidebar.header("Modyfikuj widok")
    show_table = st.sidebar.checkbox("Pokaż tabelę z danymi", value=False)
    selected_column = st.sidebar.selectbox(
        "Wybierz kolumnę do wykresu",
        ["humidity", "wind", "pressure"]
    )

    if df.empty:
        st.warning("Brak danych do wyświetlenia")


    # ostatni odczyt
    last_row = df.iloc[-1]

    st.subheader("Aktualna pogoda")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if "temp" in df.columns:
            col1.metric("Temperatura", f"{last_row["temp"]}°C")
    with col2:
        if "humidity" in df.columns:
            col2.metric("Wilgotność", f"{last_row["humidity"]}%")
    with col3:
        if "pressure" in df.columns:
           col3.metric("Ciśnienie", f"{last_row["pressure"]}hPa")
    with col4:
        if "wind" in df.columns:
            col4.metric("Wiatru", f"{last_row["wind"]}km/h")


    st.divider()

    stats_cols = st.columns(4)

    with stats_cols[0]:
        if "temp" in df.columns:
            stats_cols[0].info(
                    f"Średnia temperatura {df['temp'].mean():.2f}°C \n\n"
                    f"Minimalna: {df['temp'].min():.2f}°C \n\n"
                    f"Maksymalna: {df['temp'].max():.2f}°C \n\n"
            )
    with stats_cols[1]:
        if "humidity" in df.columns:
            stats_cols[1].warning(
                f"Średnia wilgotność: {df['humidity'].mean():.2f}% \n\n"
                f"Minimalna wilgotność: {df['humidity'].min():.2f}% \n\n"
                f"Maksymalna wilgotność: {df['humidity'].max():.2f}% \n\n"
            )

    with stats_cols[2]:
        if "pressure" in df.columns:
            stats_cols[2].error(
                f"Średnie ciśnienie: {df['pressure'].mean():.2f}hPa \n\n"
                f"Minimalne ciśnienie: {df['pressure'].min():.2f}hPa \n\n"
                f"Maksymalnie ciśnienie: {df['pressure'].max():.2f}hPa \n\n"
            )
    with stats_cols[3]:
        if "wind" in df.columns:
            stats_cols[3].info(
                f"Średnia prędkość wiatru: {df['wind'].mean():.2f}km/h \n\n"
                f"Minimalna prędkość wiatru: {df['wind'].min():.2f}km/h \n\n"
                f"Maksymalna prędkość wiatru: {df['wind'].max():.2f}km/h \n\n"
            )


    st.divider()

    st.subheader("Wykresy liniowe")

    line_charts = st.columns(2)

    with line_charts[0]:
        if "temp" in df.columns:
            st.markdown("**Temperatura w czasie**")
            st.line_chart(df, x="timestamp", y=["temp","feels_like"], color=["red","blue"])

    with line_charts[1]:
        if selected_column in df.columns:
            st.markdown(f"**{selected_column.capitalize()} w czasie**")
            st.line_chart(df, x="timestamp", y=selected_column)


    if show_table:
        st.subheader("Tabela danych")
        st.dataframe(df)

    st.subheader("Ostatnie 10 pomiarów")
    st.dataframe(df.tail(10), use_container_width=True)

    st.subheader("Opis statystyczny")

    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        st.dataframe(numeric_df.describe(), use_container_width=True)


    weather_counts = df["description"].value_counts()

    st.pyplot(
        weather_counts.plot.pie(
            autopct="%1.0f%%"
        ).figure
    )

if __name__ == "__main__":
    render_dashboard(file_path)
