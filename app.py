import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page title and layout
st.set_page_config(page_title="Energy Consumption Visualization", layout="centered")

# Set the style for plots
sns.set(style="whitegrid")

# Hardcoded credentials for simplicity
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2"
}

# Comprehensive CSS to remove background and padding
st.markdown(
    """
    <style>
    /* General reset for container backgrounds and padding */
    .block-container {
        background-color: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Removing padding and margins in specific containers */
    .reportview-container, .css-18e3th9 {
        padding: 0 !important;
        margin: 0 !important;
        background-color: transparent !important;
    }

    /* Ensuring the main content block has no background or padding */
    .main {
        background-color: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Force the sidebar styling and remove any padding/margins */
    section[data-testid="stSidebar"] {
        background-color: #394867 !important;
        color: white;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Login container styling */
    .login-container {
        background-color: #1E1E1E;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        width: 60%;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Welcome message */
    .welcome-header {
        font-size: 32px;
        font-weight: bold;
        color: #56cfe1;
        margin-bottom: 10px;
    }

    /* Sub-header for login */
    .login-header {
        font-size: 24px;
        font-weight: bold;
        color: #f4a261;
        margin-bottom: 30px;
    }

    /* Input field styles */
    .stTextInput > div > input {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #d9d9d9;
        width: 100%;
    }

    /* Button styles */
    .stButton button {
        background-color: #56cfe1;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
    }

    /* Longer Login Button */
    .login-button {
        width: 100% !important;
        padding: 12px !important;
        font-size: 18px !important;
        border-radius: 5px !important;
    }

    /* Visualization headers */
    .viz-header {
        font-size: 24px;
        color: #56cfe1;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Chart titles */
    .chart-title {
        font-size: 18px;
        color: #d1d1d1;
        margin-bottom: 20px;
        font-weight: bold;
    }

    /* Forgot password text */
    .forgot-password {
        font-size: 14px;
        color: #f4a261;
        text-align: right;
        margin-top: 10px;
        cursor: pointer;
    }

    /* Custom style for the logout button */
    .logout-button {
        background-color: #f48c06; /* Change this to orange */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
        width: 100%; /* Full width for sidebar button */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to verify login credentials
def verify_login(username, password):
    return USER_CREDENTIALS.get(username) == password

# Function to handle "Forgot Password"
def forgot_password():
    st.warning("Password reset functionality is not implemented yet. Please contact support.")

# Main app layout
st.markdown('<div class="login-container">', unsafe_allow_html=True)
st.markdown('<div class="welcome-header">🔋 Welcome to the Energy Consumption App 🔋</div>', unsafe_allow_html=True)

# Login state management
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in:
    # Display login form with improved login header
    st.markdown('<div class="login-header">🔑 Please Log In</div>', unsafe_allow_html=True)
    
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("Login", key='login_button'):
        if verify_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username  # Store username in session state
            st.success(f"🎉 Welcome {username}! You are logged in.")
        else:
            st.error("🚫 Invalid username or password. Please try again.")
    
    # Forgot password button with action
    if st.button("Forgot Password?", key='forgot_password_button'):
        forgot_password()

else:
    st.success(f"🎉 Welcome back, {st.session_state.username}!")

    # Dataset load
    data_path = "C:\\Users\\ashmp\\OneDrive\\Desktop\\energy-consumption-2020-1.csv"
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"Error: The file at path {data_path} was not found. Please check the file path.")
        st.stop()  # Stops execution if the file is not found

    # Sidebar for visualization type selection
    st.sidebar.header("📊 Visualization Options")
    option = st.sidebar.radio("Choose Visualization Type", ["📈 Static Visualization", "📉 Dynamic Visualization"])

    # Sidebar content based on user selection
    if option == "📈 Static Visualization":
        st.sidebar.markdown('<div class="viz-header">📊 Static Visualization</div>', unsafe_allow_html=True)
    elif option == "📉 Dynamic Visualization":
        st.sidebar.markdown('<div class="viz-header">📉 Dynamic Visualization</div>', unsafe_allow_html=True)

    # Add About Us, User Guide, and Help & Support sections in the sidebar
    st.sidebar.markdown("### About Us")
    st.sidebar.markdown("We are dedicated to providing insights into energy consumption data to help improve sustainability.")
    st.sidebar.markdown("---")  # Line separator

    st.sidebar.markdown("### User Guide")
    st.sidebar.markdown("1. Log in with your credentials.\n2. Select a visualization type.\n3. Choose your desired columns and parameters for analysis.")
    st.sidebar.markdown("---")  # Line separator

    st.sidebar.markdown("### Help & Support")
    st.sidebar.markdown("For assistance, please contact us at: aishvipareek05@gmail.com\nPhone: +9158645236")
    st.sidebar.markdown("---")  # Line separator

    # Logout button in the sidebar
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("You have logged out successfully.")

    # Visualization Options
    if option == "📈 Static Visualization":
        st.markdown('<div class="viz-header">📊 Static Visualization</div>', unsafe_allow_html=True)
        st.write("Select one or more columns and view a static chart.")

        # Column selection for static visualization
        selected_static_columns = st.multiselect("Select columns for static visualization:", df.columns)

        if st.button("Show Static Visualization"):
            st.markdown(f'<div class="chart-title">Static Visualization for {", ".join(selected_static_columns)}</div>', unsafe_allow_html=True)
            plt.figure(figsize=(10, 5))
            
            for column in selected_static_columns:
                plt.plot(df[column], label=column)  # Plot each selected column
            plt.legend()  # Show legend for each column
            plt.title('Line Chart of Selected Columns')
            plt.xlabel('Index')
            plt.ylabel('Values')
            st.pyplot(plt)

    # Dynamic Visualization with two file uploads and comparison
    elif option == "📉 Dynamic Visualization":
        st.markdown('<div class="viz-header">📉 Dynamic Visualization</div>', unsafe_allow_html=True)

        # File upload widget for the user to upload two datasets
        uploaded_file_1 = st.file_uploader("Upload the first CSV file", type=["csv"])
        uploaded_file_2 = st.file_uploader("Upload the second CSV file", type=["csv"])

        if uploaded_file_1 is not None and uploaded_file_2 is not None:
            try:
                # Load both files
                df1 = pd.read_csv(uploaded_file_1)
                df2 = pd.read_csv(uploaded_file_2)

                # Display first few rows of both datasets
                st.write("📊 Data from the first uploaded file:")
                st.dataframe(df1.head())
                st.write("📊 Data from the second uploaded file:")
                st.dataframe(df2.head())

                # Select columns to compare
                selected_dynamic_columns_1 = st.multiselect("Select columns from the first file for comparison:", df1.columns)
                selected_dynamic_columns_2 = st.multiselect("Select columns from the second file for comparison:", df2.columns)

                if selected_dynamic_columns_1 and selected_dynamic_columns_2:
                    # Plot comparison of selected columns
                    st.markdown(f'<div class="chart-title">Comparison Chart</div>', unsafe_allow_html=True)
                    plt.figure(figsize=(10, 5))

                    # Plot from the first file
                    for column in selected_dynamic_columns_1:
                        plt.plot(df1[column], label=f"File 1 - {column}", color='orange')

                    # Plot from the second file
                    for column in selected_dynamic_columns_2:
                        plt.plot(df2[column], label=f"File 2 - {column}", color='blue')

                    plt.legend()
                    plt.title(f'Comparison of Selected Columns')
                    plt.xlabel('Index')
                    plt.ylabel('Values')
                    st.pyplot(plt)

            except Exception as e:
                st.error(f"Error reading the uploaded files: {e}")
