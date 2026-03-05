label splashscreen:
    $ splash = SplashScreen("Acceso a P.L.A.N.O.S. Iniciado", "bg_digital_glitch")  # Instancia objeto
    $ splash.show()  # Llama método
    return

label start:
    # Menú principal (usa otra subclase si expandimos)
    scene bg_main_menu_vertical  # Fondo chibi-surreal vertical
    menu:
        "Iniciar Sanación":
            jump intro_lore
        "Cargar Alma":
            "Próximamente..."
        "Salir":
