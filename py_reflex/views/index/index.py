import reflex as rx

from ...app_state import AppState

class IndexState(AppState):
  pass

def index() -> rx.Component:
  return rx.text("index")