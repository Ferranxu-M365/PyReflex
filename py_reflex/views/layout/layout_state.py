from ...app_state import AppState

# Layout controls some state vars to make a communication between the Header and the Footer
class LayoutState(AppState):
  github_header_btn_disabled: bool = True