from talon import imgui, Module, speech_system, actions, app
from talon.ui import _SEAN_sorted_screens as sorted_screens


# We keep command_history_size lines of history, but by default display only
# command_history_display of them.
mod = Module()
setting_command_history_size = mod.setting("command_history_size", int, default=50)
setting_command_history_display = mod.setting(
    "command_history_display", int, default=10
)

hist_more = False
history = []

screen = sorted_screens()[0]

def parse_phrase(word_list):
    return " ".join(word.split("\\")[0] for word in word_list)


def on_phrase(j):
    global history

    try:
        val = parse_phrase(getattr(j["parsed"], "_unmapped", j["phrase"]))
    except:
        val = parse_phrase(j["phrase"])

    if val != "":
        history.append(val)
        history = history[-setting_command_history_size.get() :]


# todo: dynamic rect?
@imgui.open(x=screen.visible_rect.left, y=screen.visible_rect.height)
def previous_command_gui(gui: imgui.GUI):
    global history
    if len(history) > 0:
        gui.text(history[-1])
    else:
        gui.text('No history')

# todo: dynamic rect?
@imgui.open(x=screen.visible_rect.x, y=screen.visible_rect.y)
# @imgui.open(x=-700, y=0)
# @imgui.open(screen=monitor)
def gui(gui: imgui.GUI):
    global history
    gui.text("Command History")
    gui.line()
    text = (
        history[:] if hist_more else history[-setting_command_history_display.get() :]
    )
    for line in text:
        gui.text(line)


speech_system.register("phrase", on_phrase)


@mod.action_class
class Actions:
    def previous_command_toggle():
        """Toggles viewing the previous command"""
        if previous_command_gui.showing:
            previous_command_gui.hide()
        else:
            previous_command_gui.show()

    def history_toggle():
        """Toggles viewing the history"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()

    def history_enable():
        """Enables the history"""
        gui.show()

    def history_disable():
        """Disables the history"""
        gui.hide()

    def history_clear():
        """Clear the history"""
        global history
        history = []

    def history_more():
        """Show more history"""
        global hist_more
        hist_more = True

    def history_less():
        """Show less history"""
        global hist_more
        hist_more = False

    def history_get(number: int):
        """returns the history entry at the specified index"""
        num = (0 - number) - 1
        return history[num]

# Talon starts faster if you don't use the `talon.ui` module during launch
def on_ready():
    # TODO (Sean): Where is gui coming from? Why is it in scope?
    previous_command_gui.show()


# NOTE: please update this from "launch" to "ready" in Talon v0.1.5
app.register("launch", on_ready)
