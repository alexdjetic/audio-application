import flet as ft
from column_app import ColumnApp


def main(page: ft.Page):
    """
    Main function to initialize and run the application.

    Args:
        page (ft.Page): The Flet page instance to add the ColumnApp to.
    """
    app1: ColumnApp = ColumnApp(app="firefox", volume=50, page_width=page.width, page_height=page.height)
    app2: ColumnApp = ColumnApp(app="chrome", volume=50, page_width=page.width, page_height=page.height)
    app3: ColumnApp = ColumnApp(app="australia", volume=50, page_width=page.width, page_height=page.height)
    apps: list[ColumnApp] = [app1, app2, app3]

    def on_resized(e):
        """
        Event handler function for page resize events.
        Updates the layout of the ColumnApp.

        Args:
            e: Event object (not used).
        """
        for app in apps:
            app.update_layout(page.width, page.height)

    # window property
    page.title = "audio_app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_resized = on_resized
    page.add(app1, app2, app3)


ft.app(main)
