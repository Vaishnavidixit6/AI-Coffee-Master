import warnings

warnings.filterwarnings(
    "ignore"
)

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from src.core.planner import CoffeePlanner
from src.utils.logger import get_logger

logger = get_logger(__name__)


st.set_page_config(page_title="Coffee Master", layout="wide")
st.title("☕ Create Your Own Coffee Recipe")

with st.form("coffee_form"):
    coffee_type = st.text_input("☕ Coffee Type (e.g., Latte, Espresso)")
    strength = st.slider("🔥 Strength Level", 1, 5, 3)
    flavors = st.text_input("🍫 Flavor Preferences (comma-separated)")
    milk = st.selectbox("🥛 Milk Type", ["None", "Regular", "Almond", "Oat", "Soy"])
    sweetness = st.selectbox("🍯 Sweetness Level", ["No Sugar", "Low", "Medium", "High"])
    temperature = st.selectbox("🌡️ Temperature", ["Hot", "Iced"])

    submitted = st.form_submit_button("✨ Generate Recipe")

if submitted:
    if coffee_type and flavors:
        planner = CoffeePlanner()

        recipe = planner.create_recipe(
            coffee_type=coffee_type,
            strength=strength,
            flavors=[f.strip() for f in flavors.split(",")],
            milk=milk,
            sweetness=sweetness,
            temperature=temperature
        )

        st.subheader("📄 Your Coffee Recipe")
        st.markdown(recipe)

        logger.info("COFFEE RECIPE GENERATED")
    else:
        st.warning("Please enter coffee type and flavor preferences")