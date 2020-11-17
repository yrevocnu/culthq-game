# Outdoors: Yard #north_of_house

image invitation = "invitation.png"

label empty_yard:

    if has_invitation:
        narrate "The yard is empty."

        jump north_of_house_control

    else:
        jump pick_up_invitation

label pick_up_invitation:

    show invitation

    $ has_invitation = True

    "I can't believe someone dropped this."
    "The paper feels almost like snakeskin."
    "The Future Ball..."
    "I guess I'm in the right place after all."

    hide invitation

    jump north_of_house_control

label north_of_house_2:

    menu:
        "Go right":
            jump east_of_house #back of house
        "Go left":
            jump west_of_house #front of house


