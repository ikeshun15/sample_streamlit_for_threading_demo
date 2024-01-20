import streamlit as st
import time

from ..s_state import ThreadingWorkerSState
from controller import ThreadingWorkerEntity

class HomeComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(page_title="Threading Demo", page_icon="🏠")

    @staticmethod
    def init_session_state() -> None:
        ThreadingWorkerSState.init()

    @staticmethod
    def main_page() -> None:
        st.header(body="🍓 Threading Demo", divider="rainbow")
        worker = ThreadingWorkerSState.get()

        with st.container(border=True):
            button1, button2 = st.columns(2)
            if button1.button(label="🚶Start Worker", type="primary", use_container_width=True, disabled=worker is not None):
                worker = ThreadingWorkerEntity(daemon=True)
                ThreadingWorkerSState.set(value=worker)
                worker.start()
                st.rerun()
            if button2.button(label="🧍Stop Worker", use_container_width=True, disabled=worker is None):
                worker.should_stop.set()
                worker.join()
                ThreadingWorkerSState.set(value=None)
                st.rerun()
        
            if worker is None:
                st.markdown(body="No worker running.")
            else:
                st.markdown(body=f"Worker: {worker.getName()}")
                placeholder = st.empty()
                while worker.is_alive():
                    placeholder.markdown(body=f"Counter: {worker.counter}")
                    time.sleep(1)
        


    @classmethod
    def display_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.main_page()