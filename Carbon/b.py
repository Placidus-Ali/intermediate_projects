import pandas as pd
import streamlit as st

# Load datasets
def load_emission_factors():
    csv_url = "https://raw.githubusercontent.com/keanyaoha/Final_Project_WBS/main/emission_factor_formated.csv"
    return pd.read_csv(csv_url)

def load_per_capita_data():
    return pd.read_csv("per_capita_filtered.csv")

emission_factors = load_emission_factors()
per_capita_data = load_per_capita_data()

# Extract country lists
emission_countries = emission_factors.columns[1:].tolist()
per_capita_countries = per_capita_data["Country"].unique().tolist()

# Common countries
common_countries = set(emission_countries).intersection(set(per_capita_countries))

# Streamlit UI
st.title("Carbon Footprint & Per Capita CO₂ Emissions Calculator")

# Country selection
selected_country = st.selectbox("Select a country:", sorted(set(emission_countries + per_capita_countries)))

if selected_country:
    if selected_country not in emission_countries and selected_country not in per_capita_countries:
        st.warning(f"{selected_country} not found in both datasets.")
    else:
        # Fetch per capita CO2 data
        if selected_country in per_capita_countries:
            country_per_capita = per_capita_data.loc[
                per_capita_data["Country"] == selected_country, "PerCapitaCO2"
            ].item()
            eu_27_per_capita = per_capita_data.loc[
                per_capita_data["Country"] == "European Union (27)", "PerCapitaCO2"
            ].item()
            world_per_capita = per_capita_data.loc[
                per_capita_data["Country"] == "World", "PerCapitaCO2"
            ].item()

            st.write(f"Per capita CO₂ emissions for {selected_country}: **{country_per_capita}** tons")
            st.write(f"Per capita CO₂ emissions for European Union (27): **{eu_27_per_capita}** tons")
            st.write(f"Per capita CO₂ emissions for the World: **{world_per_capita}** tons")
        else:
            st.warning(f"Per capita CO₂ emissions data for {selected_country} is not available.")

        # Fetch emission factors data
        if selected_country in emission_countries:
            activities = emission_factors['Activity'].tolist()
            emission_values = {}
            for activity in activities:
                activity_row = emission_factors[emission_factors['Activity'] == activity]
                factor = activity_row[selected_country].values[0] if not activity_row.empty else None
                if factor is not None:
                    user_input = st.number_input(
                        f"{activity.replace('_', ' ').capitalize()}", min_value=0, step=1, key=activity
                    )
                    emission_values[activity] = user_input * factor
            
            # Calculate total emissions
            if st.button("Calculate Carbon Footprint"):
                total_emission = sum(emission_values.values())
                st.subheader(f"Your Carbon Footprint is: {total_emission:.4f} tons")
        else:
            st.warning(f"Emission factor data for {selected_country} is not available.")
print("Completed")



