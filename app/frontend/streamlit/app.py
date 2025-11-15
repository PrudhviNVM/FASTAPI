import streamlit as st
import math

st.set_page_config(page_title="Mutual Fund SIP Calculator", page_icon="💰")

st.title("💰 Mutual Fund SIP Return Calculator")

st.write("Enter the following details to calculate your expected returns:")

with st.form("sip_form"):
    fund = st.text_input("Mutual Fund Name")

    sip_amount = st.number_input(
        "Monthly SIP Amount (₹)",
        min_value=100,
        max_value=1000000,
        step=100,
        value=1000
    )

    years = st.number_input(
        "Investment Duration (Years)",
        min_value=1,
        max_value=50,
        step=1,
        value=10
    )

    expected_return = st.slider(
        "Expected Annual Return (%)",
        min_value=5,
        max_value=25,
        value=12
    )

    submitted = st.form_submit_button("Calculate Returns")

if submitted:
    months = years * 12
    invested = sip_amount * months

    monthly_rate = expected_return / 100 / 12

    future_value = sip_amount * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)

    profit = future_value - invested

    st.subheader("📊 SIP Investment Summary")
    st.write(f"**Fund:** {fund}")
    st.write(f"**Total Invested:** ₹{invested:,.2f}")
    st.write(f"**Expected Value:** ₹{future_value:,.2f}")
    st.write(f"**Estimated Profit:** ₹{profit:,.2f}")

    st.success("Calculation Complete!")
