from __future__ import annotations
from tcod import libtcodpy
from typing import Optional
import color
import input_handlers
import tcod

# Load the background image and remove the alpha channel.
background_image = tcod.image.Image.from_file("death_stranding_menu_background.png")

def new_game() -> None:
    """Return a brand new game session as an Engine instance."""
    raise NotImplementedError()

def load_game(filename: str) -> None:
    """Load an Engine instance from a file."""
    raise NotImplementedError()

class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""
        tcod.image.Image.blit_2x(
            self=background_image,
            console=console,
            dest_x=0,
            dest_y=0
        )

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "DELIVERY RUNNER",
            fg=color.menu_title,
            alignment=libtcodpy.CENTER,
        )
        console.print(
            console.width // 2,
            console.height - 2,
            "By Jeff Li",
            fg=color.menu_title,
            alignment=libtcodpy.CENTER,
        )
        
        menu_width = 24
        for i, text in enumerate(
            ["[N] Play a new game", "[C] Continue last game", "[Q] Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=color.menu_text,
                bg=color.black,
                alignment=libtcodpy.CENTER,
                bg_blend=libtcodpy.BKGND_ALPHA(64),
            )

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        return None