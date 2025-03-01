import streamlit as st

def calculate_tax(salary, deductions):
    # Define the income tax slabs for the old regime
    tax_slabs = [(250000, 0.05), (500000, 0.1), (750000, 0.15), (1000000, 0.2), (1250000, 0.25), (1500000, 0.3)]

    # Calculate taxable income after deductions
    taxable_income = salary - deductions

    # Initialize tax amount
    tax_amount = 0

    # Calculate tax based on slabs
    for slab_limit, slab_rate in tax_slabs:
        if taxable_income <= slab_limit:
            tax_amount += taxable_income * slab_rate
            break
        else:
            tax_amount += slab_limit * slab_rate
            taxable_income -= slab_limit

    return tax_amount

# Streamlit app
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Dwaipayan's Tax Calculator</h1>
        <h2>Income Tax Calculator (Old Regime)</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

salary = st.number_input("Enter your total salary received:", min_value=0.0, step=1000.0)
investment_80c = st.number_input("Enter the amount invested in 80C:", min_value=0.0, step=1000.0)
investment_80d = st.number_input("Enter the amount invested in 80D:", min_value=0.0, step=1000.0)
investment_80ccd = st.number_input("Enter the amount invested in 80CCD:", min_value=0.0, step=1000.0)
home_loan_interest = st.number_input("Enter the interest paid for home loan:", min_value=0.0, step=1000.0)

total_deductions = investment_80c + investment_80d + investment_80ccd + home_loan_interest

if st.button("Calculate Tax"):
    final_tax = calculate_tax(salary, total_deductions)
    st.write(f"The final tax amount is: ₹{final_tax}")
