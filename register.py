import pyglet

class RegisterScreen:
    def __init__(self):
        self.label = pyglet.text.Label(
            'Tela de Registro',
            font_name='Arial',
            font_size=36,
            x=400, y=300,
            anchor_x='center', anchor_y='center'
        )

    def draw(self):
        self.label.draw()

# Criar uma instância da tela de registro
register_screen = RegisterScreen()
