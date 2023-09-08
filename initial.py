import pyglet
import pyglet.media as media
from gamestate import GameState

class InitialScreen:
    def __init__(self, window):

        self.window = window
        self.current_state = GameState.INITIAL

        gif_path = 'assets/gif/startGame.gif'
        background_animation = pyglet.resource.animation(gif_path)
        self.background_sprite = pyglet.sprite.Sprite(img=background_animation)

        self.elements_to_draw = [self.background_sprite]

        ## SOUND ##

        audio_path = 'assets/sounds/music_track/initial.mp3'
        initial_audio = media.load(audio_path, streaming=False)
        self.player = pyglet.media.Player()
        self.player.queue(initial_audio)
        self.player.play()

        ## BUTTON ##
        self.button_image = pyglet.resource.image('assets/components/buttons/button_iniciar.png')
        self.button_sprite = pyglet.sprite.Sprite(img=self.button_image, x=200, y=100)
        self.button_y = 150
        self.button_sprite.x = 450
        self.button_sprite.y = self.button_y

        self.button_pressed = False
        self.initial_scale_button = 1

        self.elements_to_draw.append(self.button_sprite)

    def on_mouse_press(self, x, y, button, modifiers):
        global current_state  # Certifique-se de declarar como global
        if self.button_sprite.x <= x <= self.button_sprite.x + self.button_sprite.width and self.button_y <= y <= self.button_y + self.button_sprite.height:
          self.button_pressed = True
          self.button_sprite.scale = self.initial_scale_button * 0.9
          current_state = GameState.REGISTER  # Altera o estado global
        print("teste1")

    def on_mouse_release(self, x, y, button, modifiers):
        if self.button_pressed and self.button_sprite.x <= x <= self.button_sprite.x + self.button_sprite.width and self.button_y <= y <= self.button_y + self.button_sprite.height:
          self.button_pressed = False
          self.button_sprite.scale = self.initial_scale_button

    def draw(self):
      for element in self.elements_to_draw:
          element.draw()

def on_player_eos(self):
    self.player.seek(0)
    self.player.play()

if __name__ == "__main__":
    window = pyglet.window.Window(1150, 620, caption="Jogo da Forca - MasterGames m3_Power")

    initial_screen = InitialScreen(window)

    @window.event
    def on_draw():
        window.clear()
        initial_screen.draw()

    pyglet.app.run()