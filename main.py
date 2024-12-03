import streamlit as st


def calculate_partner_value(
    initial_sales,
    monthly_sales,
    price_initial,
    price_monthly,
    retention_initial,
    retention_monthly,
    cost_per_user,
):
    """
    Calculate Partner Value (Initial and Monthly) and the KPI.
    """
    pv_initial = initial_sales * price_initial * retention_initial
    pv_monthly = monthly_sales * retention_monthly * (price_monthly - cost_per_user)
    kpi = (pv_monthly / pv_initial) * 100
    return pv_initial, pv_monthly, kpi


def main():
    st.title("Partner Value Calculator")
    st.write("Adjust the values below to calculate Partner Value and KPI.")

    # Create two columns
    left_col, right_col = st.columns(2)

    # Input Section (Left Column)
    with left_col:
        st.header("Initial Values")
        initial_sales = st.number_input(
            "Nⁱ: Monthly Sales", min_value=0, value=100
        )
        price_initial = st.number_input(
            "Pⁱ: Product Price / Monthly Payment", min_value=0.0, value=10.0
        )
        retention_initial = st.number_input(
            "Rⁱ: Average Retention (Monthly)", min_value=0.0, value=12.0
        )

        st.header("Values post-mok")
        monthly_sales = st.number_input(
            "Nᵐ: Monthly Sales", min_value=0, value=120
        )
        price_monthly = st.number_input(
            "Pᵐ: Product Price / Monthly Payment", min_value=0.0, value=10.0
        )
        retention_monthly = st.number_input(
            "Rᵐ: Average Retention (Monthly)", min_value=0.0, value=11.0
        )
        cost_per_user = st.number_input(
            "C: Cost per User (Monthly)", min_value=0.0, value=2.0
        )

    # Results Section (Right Column)
    with right_col:
        st.header("Results")
        pv_initial, pv_monthly, kpi = calculate_partner_value(
            initial_sales,
            monthly_sales,
            price_initial,
            price_monthly,
            retention_initial,
            retention_monthly,
            cost_per_user,
        )

        st.metric("Partner Value (Initial)", f"${pv_initial:,.2f}")
        st.metric("Partner Value (Monthly)", f"${pv_monthly:,.2f}")
        st.metric("KPI", f"{kpi:.2f}%", delta=f"{kpi - 100:.2f}%")

        st.header("Interpretation")
        if kpi > 100:
            st.success("KPI is above 100%. This indicates a positive growth!")
        else:
            st.error(
                "KPI is below 100%. This indicates a potential issue in profitability."
            )


if __name__ == "__main__":
    main()