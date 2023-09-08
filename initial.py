import pyglet;
from gamestate import GameState;

class InitialScreen:
    def __init__(self, window):
        self.window = window
        self.current_state = GameState.INITIAL

        gif_path = 'assets/gif/startGame.gif'
        background_animation = pyglet.resource.animation(gif_path)
        self.background_sprite = pyglet.sprite.Sprite(img=background_animation)

        self.elements_to_draw = [self.background_sprite]

        audio_path = 'assets/sounds/music_track/initial.mp3'
        initial_audio = pyglet.media.load(audio_path, streaming=False)
        self.player = pyglet.media.Player()
        self.player.queue(initial_audio)
        self.player.play()
        self.volume = 1.0 

    def on_key_press(self, key, modifiers):
        print(f"Tecla pressionada: {key}")
        if key == pyglet.window.key.PLUS:
            self.increase_volume()
        elif key == pyglet.window.key.MINUS:
            self.decrease_volume()

    def increase_volume(self):
        self.volume = min(1.0, self.volume + 0.1)  
        self.player.volume = self.volume
        print(f"Volume aumentado para {self.volume:.1f}")

    def decrease_volume(self):
        self.volume = max(0.0, self.volume - 0.1) 
        self.player.volume = self.volume
        print(f"Volume diminuído para {self.volume:.1f}")

    def draw(self):
        for element in self.elements_to_draw:
            element.draw()
