from column_app import ColumnApp


def create_column_app(sink_input, app_name, media_name, volume, page_width, page_height):
    """
    Create a ColumnApp instance.

    Args:
        sink_input (str): Sink input identifier.
        app_name (str): Application name.
        media_name (str): Media name.
        volume (str): Volume percentage.
        page_width (int): Width of the page.
        page_height (int): Height of the page.

    Returns:
        ColumnApp: Instance of ColumnApp.
    """
    return ColumnApp(
        sink_input=int(sink_input),
        app=f"{app_name} : {media_name}",
        volume=int(volume),
        page_width=page_width,
        page_height=page_height
    )
