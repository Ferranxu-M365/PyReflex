import reflex as rx

from py_reflex.views.index.index import index
from py_reflex.views.about.about import about

# Add state and page to the app.
app = rx.App()

app.add_page(index, route="/")

app.add_page(about, route="/about")

app.compile()
