import pyglet
import pyglet.media as media
from gamestate import GameState
from initial import InitialScreen
from register import RegisterScreen

current_state = GameState.INITIAL

window = pyglet.window.Window(1150, 620, caption="Jogo da Forca - MasterGames m3_Power")

initial_screen = InitialScreen(window)
register_screen = RegisterScreen()

initial_screen.player.play()

def update_state():
    global current_state
    current_state = GameState.REGISTER

@window.event
def on_draw():
    window.clear()
    if current_state == GameState.INITIAL:
        initial_screen.draw()
    elif current_state == GameState.REGISTER:
        register_screen.draw()

@window.event
def on_key_press(key, modifiers):
    global current_state
    if key == pyglet.window.key.I:
        current_state = GameState.INITIAL
        initial_screen.player.play()
    elif key == pyglet.window.key.ENTER:
        update_state()

@window.event
def on_mouse_press(x, y, button, modifiers):
    initial_screen.on_mouse_press(x, y, button, modifiers)

@window.event
def on_mouse_release(x, y, button, modifiers):
    initial_screen.on_mouse_release(x, y, button, modifiers)

if __name__ == '__main__':
    pyglet.app.run()
