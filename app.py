import streamlit as st
from savings_account import SavingsAccount
from current_account import CurrentAccount

# 1. Home Page Header and Logo
st.set_page_config(page_title="Pentagon Bank", layout="centered")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Emblem-money.svg/1200px-Emblem-money.svg.png", width=100)
st.title("🏦 PENTAGON BANK")

# 2. Account Selection
account_type = st.sidebar.selectbox("Select Account Type", ["Savings", "Current"])

# 3. Account Initialization
if account_type == "Savings":
    st.subheader("Savings Account")
    savings = SavingsAccount(2000000)

    with st.form("savings_form"):
        operation = st.selectbox("Choose operation", ["Deposit", "Withdraw"])
        amount = st.number_input("Enter amount", min_value=1)
        submit = st.form_submit_button("Submit")

        if submit:
            with st.spinner("Processing..."):
                if operation == "Withdraw":
                    savings.withdraw(amount)
                elif operation == "Deposit":
                    savings.deposit(amount)
                st.success(f"Updated Balance: ₦{savings.get_balance():,.2f}")

elif account_type == "Current":
    st.subheader("Current Account")
    current = CurrentAccount(2000000)

    with st.form("current_form"):
        operation = st.selectbox("Choose operation", ["Deposit", "Withdraw"])
        amount = st.number_input("Enter amount", min_value=1)
        submit = st.form_submit_button("Submit")

        if submit:
            with st.spinner("Processing..."):
                if operation == "Withdraw":
                    current.withdraw(amount)
                elif operation == "Deposit":
                    current.deposit(amount)
                st.success(f"Updated Balance: ₦{current.get_balance():,.2f}")




