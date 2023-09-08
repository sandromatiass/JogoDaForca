import pyglet

pyglet.options['audio'] = ('openal', 'pulse', 'silent')

from gamestate import GameState
from initial import InitialScreen
from register import RegisterScreen

current_state = GameState.INITIAL

window = pyglet.window.Window(1150, 620, caption="Jogo da Forca - MasterGames m3_Power")

initial_screen = InitialScreen(window)
register_screen = RegisterScreen()

initial_screen.player.play()

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
    elif key == pyglet.window.key.PLUS:
        initial_screen.increase_volume()
    elif key == pyglet.window.key.MINUS:
        initial_screen.decrease_volume()

def update_state():
    global current_state
    current_state = GameState.REGISTER

if __name__ == '__main__':
    pyglet.app.run()
