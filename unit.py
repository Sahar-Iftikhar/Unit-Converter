import streamlit as st

# Define conversion logic
def convert_units(value, unit_from, unit_to):
    conversions = {
        # Length
        "meters_kilometers": lambda v: v * 0.001,
        "kilometers_meters": lambda v: v * 1000,

        # Weight
        "grams_kilograms": lambda v: v * 0.001,
        "kilograms_grams": lambda v: v * 1000,

        # Temperature
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,

        # Volume
        "liters_milliliters": lambda v: v * 1000,
        "milliliters_liters": lambda v: v * 0.001,

        # Time
        "seconds_minutes": lambda v: v / 60,
        "minutes_seconds": lambda v: v * 60,
        "minutes_hours": lambda v: v / 60,
        "hours_minutes": lambda v: v * 60,
        "seconds_hours": lambda v: v / 3600,
        "hours_seconds": lambda v: v * 3600,
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return conversions[key](value)
    elif unit_from == unit_to:
        return value
    else:
        return "❌ Conversion not supported"

# Unit categories
unit_categories = {
    # Length
    "meters": "Length",
    "kilometers": "Length",

    # Weight
    "grams": "Weight",
    "kilograms": "Weight",

    # Temperature
    "celsius": "Temperature",
    "fahrenheit": "Temperature",

    # Volume
    "liters": "Volume",
    "milliliters": "Volume",

    # Time
    "seconds": "Time",
    "minutes": "Time",
    "hours": "Time",
}

# Streamlit UI
st.title("🔄 Universal Unit Converter")

with st.form("conversion_form"):
    value = st.number_input("Enter value:", value=0.0, step=1.0)

    unit_from = st.selectbox("Convert from:", list(unit_categories.keys()))

    # Filter compatible units based on category
    compatible_units = [
        u for u in unit_categories if unit_categories[u] == unit_categories[unit_from]
    ]

    # Prevent self-conversion
    if unit_from in compatible_units:
        compatible_units.remove(unit_from)

    unit_to = st.selectbox("Convert to:", compatible_units)

    submitted = st.form_submit_button("Convert")

# Show result
if submitted:
    result = convert_units(value, unit_from, unit_to)

    if isinstance(result, str):  # Error message
        st.error(result)
    else:
        st.success(f"✅ {value} {unit_from} = {round(result, 4)} {unit_to}")
