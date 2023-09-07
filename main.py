import pyglet;

import pyglet.media as media;


gif_path = 'assets/gif/startGame.gif';
background_animation = pyglet.resource.animation(gif_path);

window = pyglet.window.Window(
    width=background_animation.get_max_width(), 
    height=background_animation.get_max_height(), 
    caption="Jogo da Forca - MasterGames m3_Power");

background_sprite = pyglet.sprite.Sprite(img=background_animation);

## Trilha inicial

audio_path = 'assets/sounds/music_track/initial.mp3';
initial_audio = media.load(audio_path, streaming=False);
player = pyglet.media.Player();
player.queue(initial_audio);

def on_player_eos():
    player.seek(0);

player.on_eos = on_player_eos;

player.play();

#Botão iniciar do jogo

button_img = pyglet.image.load('assets/components/buttons/button_iniciar.png');
button_sprite = pyglet.sprite.Sprite(button_img, x=150, y=100);

button_y = 150
button_sprite.x = 450
button_sprite.y = button_y

button_pressed = False;
initial_scale_button = 1;

@window.event
def on_mouse_press(x, y, button, modifiers):
    global button_pressed
    if button_sprite.x <= x <= button_sprite.x + button_sprite.width and button_y <= y <= button_y + button_sprite.height:
        button_pressed = True
        button_sprite.scale = initial_scale_button * 0.9

@window.event
def on_mouse_release(x, y, button, modifiers):
    global button_pressed
    if button_pressed and button_sprite.x <= x <= button_sprite.x + button_sprite.width and button_y <= y <= button_y + button_sprite.height:
        event_click(x, y)
    button_pressed = False
    button_sprite.scale = initial_scale_button  # Restaura o tamanho original)

def event_click(x, y):
    print("O botão foi clicado nas coordenadas (x={}, y={})".format(x, y))

@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    button_sprite.draw()
pyglet.app.run()