import flet as ft
from syslibrary import get_all_sound_app
import time
from column_app_create import create_column_app  # Function to create ColumnApp instances

# Define a refresh interval in seconds
REFRESH_INTERVAL = 2  # Refresh every 2 seconds


def refresh_data(page):
    """
    Function to refresh application data periodically.

    Args:
        page (ft.Page): The Flet page instance to update.
    """
    apps = {}  # Dictionary to hold app instances

    while True:
        try:
            # Get updated audio applications info
            apps_infos = get_all_sound_app()

            # Remove existing apps by clearing the dictionary
            for app in apps.values():
                page.remove(app)
            apps.clear()

            # Add or update apps
            for key, value in apps_infos.items():
                sink_input = key
                app_name = value[0]
                media_name = value[1]
                volume = value[2]

                # Create or update ColumnApp instance
                app = create_column_app(
                    sink_input=sink_input,
                    app_name=app_name,
                    media_name=media_name,
                    volume=volume,
                    page_width=page.width,
                    page_height=page.height
                )
                apps[sink_input] = app
                page.add(app)

        except Exception as e:
            print(f"Error in refresh_data: {e}")

        # Sleep for the refresh interval
        time.sleep(REFRESH_INTERVAL)


def main(page: ft.Page):
    """
    Main function to initialize and run the application.

    Args:
        page (ft.Page): The Flet page instance to add the ColumnApp to.
    """

    refresh_data(page)  # Call refresh_data directly instead of using a thread

    # Set window properties
    page.title = "Audio Applications"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


if __name__ == "__main__":
    ft.app(main)
