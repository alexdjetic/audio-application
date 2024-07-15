import flet as ft

class ColumnApp(ft.Container):
    """
    A custom container for displaying an application name and a volume slider.

    Args:
        app (str): The name of the application.
        volume (int, optional): The initial volume value (0-100). Defaults to 0.
        page_width (int, optional): The initial width of the page. Defaults to 800.
        page_height (int, optional): The initial height of the page. Defaults to 800.
    """

    def __init__(self, app: str, volume: int = 0, page_width: int = 800, page_height: int = 800) -> None:
        """
        Initializes the ColumnApp instance.

        Args:
            app (str): The name of the application.
            volume (int, optional): The initial volume value (0-100). Defaults to 0.
            page_width (int, optional): The initial width of the page. Defaults to 800.
            page_height (int, optional): The initial height of the page. Defaults to 800.
        """
        super().__init__()
        self._app: str = app
        self._volume: int = volume
        self._page_width: int = page_width
        self._page_height: int = page_height

        # Create UI elements
        self._create_app_text()
        self._create_slider()
        self._create_column()

    def _create_app_text(self) -> None:
        """
        Creates the text element displaying the application name.
        """
        self._text_app: ft.Text = ft.Text(value=self._app, size=16)

    def _create_slider(self) -> None:
        """
        Creates the volume slider element.
        """
        self._volume_slider: ft.Slider = ft.Slider(
            min=0,
            max=100,
            divisions=None,
            value=self._volume,
            label="{value}",
            on_change=self._change_slider_value,
            adaptive=True,
            inactive_color=ft.colors.BLUE,
            active_color=ft.colors.BLUE_200,
            expand=True
        )

    def _create_column(self) -> None:
        """
        Creates the column layout containing the application text and slider.
        """
        text_width: int = int(self._page_width * 0.3)
        slider_width: int = int(self._page_width * 0.7)

        text_container = ft.Container(
            content=self._text_app,
            width=text_width,  # Adjust as needed
            expand=True
        )

        slider_container = ft.Container(
            content=self._volume_slider,
            width=slider_width,  # Adjust as needed
            expand=True
        )

        self.content = ft.Row(
            [
                text_container,
                slider_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            width=self._page_width,
            expand=True
        )

    def _change_slider_value(self, e) -> None:
        """
        Handler function for when the slider value changes.
        Prints the current value of the slider.
        """
        print(f"value of slider: {int(self._volume_slider.value)}")

    def update_layout(self, page_width: int, page_height: int) -> None:
        """
        Updates the layout dimensions and refreshes the UI.

        Args:
            page_width (int): The new width of the page.
            page_height (int): The new height of the page.
        """
        print(f"new layout: {int(page_width)}x{int(page_height)}")
        self._page_width: int = int(page_width)
        self._page_height: int = int(page_height)
        self._create_column()
        self.update()


def main(page: ft.Page):
    """
    Main function to initialize and run the application.

    Args:
        page (ft.Page): The Flet page instance to add the ColumnApp to.
    """
    app = ColumnApp(app="firefox", volume=50, page_width=page.width, page_height=page.height)

    def on_resized(e):
        """
        Event handler function for page resize events.
        Updates the layout of the ColumnApp.

        Args:
            e: Event object (not used).
        """
        app.update_layout(page.width, page.height)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_resized = on_resized
    page.add(app)


if __name__ == "__main__":
    ft.app(target=main)
