import streamlit as st

def get_session_state(**kwargs):
    session_state = getattr(st.session_state, "_state", None)
    if session_state is None:
        session_state = st.session_state._state = {}
    for key, default_value in kwargs.items():
        if key not in session_state:
            session_state[key] = default_value
    return session_state

def set_session_state(**kwargs):
    # Save the user inputs in session state
    session_state = kwargs.copy()
