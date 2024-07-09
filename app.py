import streamlit as st
from dbhelper import Dbhelper


class Flipkart:
    def __init__(self):
        self.db = Dbhelper()
        self.main()

    def main(self):
        st.title("Flipkart Registration and Login System")

        menu = ["Home", "Login", "Register"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Home":
            st.subheader("Home")
        elif choice == "Login":
            self.login()
        elif choice == "Register":
            self.register()

    def register(self):
        st.subheader("Create New Account")
        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type='password')

        if st.button("Register"):
            response = self.db.register(name, email, password)
            if response:
                st.success("Registration successful")
            else:
                st.error("Registration failed")

    def login(self):
        st.subheader("Login to Your Account")
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type='password')

        if st.button("Login"):
            user_details = self.db.search(email, password)
            if user_details:
                st.success("Login successful")
                st.subheader("User Details")
                for detail in user_details:
                    st.write(detail)
            else:
                st.error("Login failed")


if __name__ == "__main__":
    Flipkart()
