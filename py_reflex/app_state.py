import reflex as rx

class AppState(rx.State):
    """The app state."""
    @rx.var
    def current_page(self) -> str:
        return self.get_current_page()