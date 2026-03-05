init python:
    class GameScreen:
        """
        Clase base para pantallas (POO: Abstracción y herencia).
        Atributos: title (str), background (str).
        Métodos: show() - abstracto, para subclases.
        """
        def __init__(self, title, background):
            self.title = title
            self.background = background
        
        def show(self):
            # Método base: muestra fondo y título
            renpy.scene()
            renpy.show(self.background)
            renpy.say(None, self.title)  # Placeholder para texto
            # Subclases sobrescriben esto (polimorfismo)

    class SplashScreen(GameScreen):
        """
        Subclase para Splash (herencia).
        Agrega efecto glitch (composición: usa un Transform objeto).
        """
        def __init__(self, title, background):
            super().__init__(title, background)
            self.glitch_effect = Transform(matrixcolor=InvertMatrix(0.1))  # Objeto compuesto
        
        def show(self):
            super().show()  # Llama al base
            renpy.show(self.background, at_list=[self.glitch_effect])  # Aplica glitch
            renpy.pause(2.0)  # Espera antes de menú
            renpy.transition(dissolve)