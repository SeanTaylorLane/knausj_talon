from talon import ui, Module, Context, actions

def sorted_screens():
    """Return screens sorted by their topmost, then leftmost, edge.

    Screens will be sorted left-to-right, then top-to-bottom as a tiebreak.

    """

    return sorted(
        sorted(ui.screens(), key=lambda screen: screen.visible_rect.top),
        key=lambda screen: screen.visible_rect.left,
    )

ui._SEAN_sorted_screens = sorted_screens
