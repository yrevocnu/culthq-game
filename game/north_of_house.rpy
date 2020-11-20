# Outdoors: Yard #north_of_house

image invitation = "invitation.png"

label empty_yard:

    if not has_invitation and accepted_neighbor_quest:
        jump pick_up_invitation
    else:
        narrate "The yard is empty."

        jump north_of_house_control

label pick_up_invitation:

    show invitation

    $ has_invitation = True

    "I can't believe someone dropped this."
    "The paper feels almost like snakeskin."
    "The Future Ball..."
    "I guess I'm in the right place after all."

    hide invitation

    jump north_of_house_control


