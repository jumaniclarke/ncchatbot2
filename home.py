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
        try:
            st.login("google")
        except Exception as e:
            import traceback
            st.error("Login failed: " + str(e))
            st.text(traceback.format_exc())
            # Safe diagnostics (do not print secret values)
            google = auth.get("google") if auth else None
            st.write("google type:", type(google))
            if google:
                st.write("client_id present:", bool(google.get("client_id")))
                st.write("client_kwargs type:", type(google.get("client_kwargs")))

st.write(st.user)
st.write("You are logged in as " + st.user.name if st.user.is_logged_in else "You are not logged in.")

