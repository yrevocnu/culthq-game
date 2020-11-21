image credits_image = "credits_image.png"

image bg people_love_you = "bg_hiding.png"

label victory:

    play music "music/Hallway.mp3"

    scene bg people_love_you

    narrate "You have won!"

    narrate "Thank you for playing the pilot of Yrevocnu CultHQ."

    narrate "What's inside the house?"

    narrate "To find out, look for the next installment of the game."

    jump credits

label credits:
    play music "music/Steve Morrell - Video Game.mp3"
    $ credits_speed = 25
    scene black
    show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)

    $ MainMenu(confirm=False)()