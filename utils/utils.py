from datetime import datetime
from typing import Callable

import streamlit as st  # type:ignore


def time_count_down(timestamp_millis):
    """Display a countdown to a future timestamp (in milliseconds)."""
    try:
        future_time = datetime.fromtimestamp(timestamp_millis / 1000)
        now = datetime.now()
        remaining = future_time - now

        if remaining.total_seconds() <= 0:
            st.write("⏰ Time's up!")
            return

        hours, remainder = divmod(int(remaining.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)

        st.markdown(f"⏳ **{hours:02d}:{minutes:02d}:{seconds:02d}** remaining")

    except Exception as e:
        st.error(f"Countdown error: {e}")

def get_time_from_milis(timestamp_millis):
    date_s = timestamp_millis / 1000
    datetime_object = datetime.fromtimestamp(date_s)
    formatted_date = datetime_object.strftime("%d %B, %Y")
    return formatted_date


def create_confirm_dialog(state_key: str, title: str, message: str, on_confirm: Callable):
    @st.dialog(title)
    def dialog():
        st.warning(message)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Yes", key=f"{state_key}_yes"):
                on_confirm()
                st.session_state[state_key] = False
                st.rerun()  # Close the dialog

        with col2:
            if st.button("❌ No", key=f"{state_key}_no"):
                st.session_state[state_key] = False
                st.rerun()  # Close the dialog

    return dialog


def confirm_dialog(title: str, message: str, on_confirm: Callable, state_key: str):
    """
    Call this from your main page logic. If the session state flag is True,
    it invokes the dialog function created using create_confirm_dialog.
    """
    if st.session_state.get(state_key, False):
        dialog = create_confirm_dialog(state_key, title, message, on_confirm)
        dialog()
