import reflex as rx

from .index_style import *
from ..layout.layout import layout
from ...shared_components.info_card.info_card import info_card
from ...app_state import AppState

class IndexState(AppState):
  pass

def index() -> rx.Component:
  return layout(
    rx.flex(
      rx.heading(
        rx.image(src="/profile_pic.png", style=profile_pic_style),
        "Hi! I am Ferran Ortega",
        size="md",
        style=heading_style,
      ),
      rx.text("I am a SharePoint Online and Power Platform developer. Currently, I have 1 year of experience on developing new solutions on the Microsoft 365 environment and 5 years of experience as a Microsoft 365 administrator.",
        style=bio_style,  
      ),
      rx.heading("SKILLS", size="sm"),
      rx.box(
        info_card("JavaScript", "white", "#F0DB4F"),
        info_card("TypeScript", "white", "#007acc"),
        info_card("React", "white", "#36dff8"),
        info_card("SharePoint Framework (SPFx)", "white", "#038387"),
        info_card("C# (Fundamentals)", "white", "#ac99ea"),
        info_card("Azure Functions (with C#)", "white", "#0078d4"),
        info_card("Power Automate", "white", "#3689f8"),
        info_card("PowerApps", "white", "#8f2c86"),
        info_card("SQL", "white", "grey"),
        style=card_list,
      ),
      direction="column",
      align="center",
      style=container,
    )
  )