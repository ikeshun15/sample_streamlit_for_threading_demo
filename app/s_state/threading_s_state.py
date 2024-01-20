import threading

from .base_s_state import BaseSState

    
class ThreadingWorkerSState(BaseSState[threading.Thread]):
    @staticmethod
    def get_name() -> str:
        return "threading_worker"
    
    @staticmethod
    def get_default() -> None:
        return None