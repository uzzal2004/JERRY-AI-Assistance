import streamlit as st
from jerry.assistant import jerryAssistant
from jerry.gemini_engine import GeminiEngine
from jerry.prompt_controller import PromptController
from jerry.memory import Memory
from config.settings import Settings

# Page configuration
st.set_page_config(
    page_title="jerry AI Assistant",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for jerry theme
st.markdown("""
    <style>
    .main {
        background-color: #0a0e27;
        color: #00d9ff;
    }
    .stChatMessage {
        background-color: #1a1f3a;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title(" ")
    
    # Initialize Session State for authentication
    if 'database' not in st.session_state:
        st.session_state.database = {}  # Format: {email: {'name': name, 'password': password}}
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

    # Initialize jerry only once
    if 'jerry' not in st.session_state:
        try:
            settings = Settings()
            api_key = settings.load_api_key()
            
            engine = GeminiEngine(api_key)
            memory = Memory()
            prompt_controller = PromptController()
            
            st.session_state.jerry = jerryAssistant(engine, prompt_controller, memory)
            st.session_state.messages = memory.get_history()
        except Exception as e:
            st.error(f"Initialization Error: {str(e)}")
            st.stop()

    # Sidebar for Navigation / Auth
    with st.sidebar:
        st.header("Navigation")
        if not st.session_state.logged_in:
            option = st.radio("Choose Option", ["Login", "Register"])
        else:
            st.success(f"Welcome, {st.session_state.database[st.session_state.current_user]['name']}!")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.current_user = None
                st.rerun()

    # Main Content Area
    if not st.session_state.logged_in:
        if option == "Register":
            st.subheader("Create a New Account")
            with st.form("register_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Register")

                if submit:
                    if email in st.session_state.database:
                        st.error("Email already exists!")
                    elif name and email and password:
                        st.session_state.database[email] = {'name': name, 'password': password}
                        st.success("Registration successful! Please login.")
                    else:
                        st.warning("Please fill in all fields.")

        elif option == "Login":
            st.subheader("Login to your Account")
            with st.form("login_form"):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")

                if submit:
                    if email in st.session_state.database:
                        if st.session_state.database[email]['password'] == password:
                            st.session_state.logged_in = True
                            st.session_state.current_user = email
                            st.success("Login Successful!")
                            st.rerun()
                        else:
                            st.error("Incorrect Password")
                    else:
                        st.error("Email not found. Please register first.")

    else:
        # Logged in - Show jerry interface
        # Sidebar controls
        with st.sidebar:
            st.title("⚙️ jerry Controls")
            
            # Assistant role selection
            role = st.selectbox(
                "Select Assistant Role",
                ["General Assistant", "Tutor", "Coding Assistant", "Career Helper"]
            )
            
            st.session_state.jerry.prompt_controller.set_role(role)
            
            st.divider()
            
            # Clear memory button
            if st.button("🗑️ Clear Memory", use_container_width=True):
                st.session_state.jerry.memory.clear()
                st.session_state.messages = []
                st.rerun()
            
            st.divider()
            
            # Stats
            st.metric("Total Messages", len(st.session_state.messages))
            
            st.divider()
            
            st.info("💡 **Tip:** jerry remembers your conversation context!")

        # Main chat interface
        st.title("🧠 jerry – Your Personal AI Assistant")
        st.caption("Powered by Google Gemini API")

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if user_input := st.chat_input("Ask jerry anything..."):
            # Display user message
            with st.chat_message("user"):
                st.markdown(user_input)
            
            # Add to session state
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Get jerry response
            with st.chat_message("assistant"):
                with st.spinner("jerry is thinking..."):
                    try:
                        response = st.session_state.jerry.respond(user_input)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    except Exception as e:
                        error_msg = f"⚠️ Error: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})


if __name__ == "__main__":
    main()