image credits_image = "credits_image.png"

label credits:
    play music "music/Steve Morrell - Video Game.mp3"
    $ credits_speed = 25
    scene black
    show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)

    $ MainMenu(confirm=False)()