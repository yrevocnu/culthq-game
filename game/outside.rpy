# Outside

#init python:
#    renpy.register_bmfont("mono", 22, filename="Ubuntu-M.ttf")

define control = Character("", advance=False, what_font="LiberationMono-Regular.ttf")
define narrate = Character("", what_font="LiberationMono-Regular.ttf")

image testimonial = "anonymous-testimonial.png"

#
# FRONT: muffled sounds. (try) (knock) (call friend) (call neighbor)
#                        <west> <north> <south>
#    - neighor gossips about cult, asks for a favor
#
#
# WEST OF HOUSE: mailbox.
#   - in mailbox, the anonymous testimonial
#  <east>
#

image bg west_of_house = "bg_culty_door.png"

# flag for having visited west_of_house
default visited_west_of_house = False

# flag for having called out at the front door
default call_out = False

# flag for having met the neighbor
default met_neighbor = False

# flag for holding an invitation
default has_invitation = False

label west_of_house:

    scene bg west_of_house

    if not visited_west_of_house:
        "Is this the right place?"
        "It doesn't look like anyone's home."
        $ visited_west_of_house = True

    jump west_of_house_control

label west_of_house_control:

    # TODO: Front door label
    control "You are west of a house with a {a=call:front_door}front door{/a}. There is a small {a=call:mailbox}mailbox{/a} here. You may go {a=jump:north_of_house}north{/a} or {a=jump:south_of_house}south{/a}."

    return

default has_testimonial = False

label mailbox:

    if not has_testimonial:
        show testimonial

        narrate "Opening the small mailbox reveals a leaflet."

        "Sounds like someone had a bad time..."

        hide testimonial

        narrate "You pocket the anonymous testimonial."

        $ has_testimonial = True

    else:
        narrate "The mailbox is empty."

    jump west_of_house_control



# 
# YARD: nothing. <west> <east>
#

image yard = "yard_NO_RIGHTS.jpg"

label north_of_house:

    # unusually, the neighbor will block you from moving at first
    if call_out and not met_neighbor:
        call hello_neighbor
        jump west_of_house

    scene bg disassociate3

    show yard at top

    "TODO: Yard background scene."

    jump north_of_house_control

label north_of_house_control:

    control "You are north of the house. There is only an {a=call:empty_yard}empty yard{/a} here. You may go {a=jump:east_of_house}east{/a} or {a=jump:west_of_house}west{/a}."
    return

#
# BACK: Back door.
#    - Encounter Newcomer
#    - introduction and pick option about self.
#       - talking about snake: reveals it didn't talk to him
#    - if enter through back door, Newcomer comes it with.
#   
#     <north><south>
#

image bg back_door = "bg_back_door_scrubbed.jpg"

# If the back door is open
default back_door_open = False

label east_of_house:

    scene bg back_door

label east_of_house_control:

    control "You are east of the house. There is a {a=call:back_door}back door{/a} here. ___ ___ {a=jump:meet_newcomer}newcomer{/a} description _____ _______ ______ _____ ____. You may go {a=jump:north_of_house}north{/a} or {a=jump:south_of_house}south{/a}."
    return

label back_door:
    if not back_door_open:
        narrate "The back door is locked shut."
        jump east_of_house_control
    else:
        jump east_of_house_snake_permission

#
# SNAKE: See snake. (eyes) (tongue) (fang?) 
#     Turn the tongue around to let it speak
#     Intercom with somebody inside.
#     The ask you which door you want to come through.
#     <east> <west>
#
image bg yuxa = "bg_yuxa-white.jpg"
image bg yuxa_resurrected = "bg_yuxa_resurrected.jpg"

default yuxa_alive = False

label south_of_house:

    # unusually, the neighbor will block you from moving at first
    if call_out and not met_neighbor:
        call hello_neighbor
        jump west_of_house

    if not yuxa_alive:
        scene bg yuxa
    else:
        scene bg yuxa_resurrected

    control "You are south of the house. There is an enormous {a=call:snake}snake{/a} here. You may go {a=jump:east_of_house}east{/a} or {a=jump:west_of_house}west{/a}."
    return
