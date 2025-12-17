import streamlit as st

st.title("Authentication")

# Debug: check presence of auth secrets without exposing values
auth = st.secrets.get("auth")
st.write("auth present:", auth is not None)
if auth:
    try:
        st.write("auth keys:", list(auth.keys()))
        google = auth.get("google")
        st.write("auth.google present:", google is not None)
        if google:
            st.write("auth.google keys:", list(google.keys()))
    except Exception:
        st.write("Could not enumerate auth secrets keys")

if not st.user.is_logged_in:
    if st.button("Authentication"):
        st.login("google")

st.write(st.user)
st.write("You are logged in as " + st.user.name if st.user.is_logged_in else "You are not logged in.")

