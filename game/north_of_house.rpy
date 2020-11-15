# Outdoors: Yard #north_of_house

label north_of_house_narrative:

    "It's just an empty yard."
    "Kind of ugly."
    "Bad smell coming from somewhere."
    "What's that thing on the ground?"

    menu:
        "Pick it up":
            jump invitation
        "Leave it alone":
            jump north_of_house_2

label invitation:

    #displays image of event invitation
    "I can't believe someone dropped this."
    "The paper feels almost like snakeskin."
    "The Future Ball..."
    "I guess I'm in the right place after all."
    #invitation added to inventory; has invitation == true

label north_of_house_2:

    menu:
        "Go right":
            jump east_of_house #back of house
        "Go left":
            jump west_of_house #front of house


