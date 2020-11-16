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

label west_of_house:

    scene bg west_of_house

    if not visited_west_of_house:
        "Is this the right place?"
        "It doesn't look like anyone's home."
        $ visited_west_of_house = True

    # TODO: Front door label
    control "You are west of a house with a {a=call:front_door}front door{/a}. There is a small {a=jump:mailbox}mailbox{/a} here. You may go {a=jump:north_of_house}north{/a} or {a=jump:south_of_house}south{/a}."

    pass

label mailbox:

    show testimonial

    narrate "Opening the small mailbox reveals a leaflet."

    "Sounds like someone had a bad time..."

    hide testimonial

    jump west_of_house



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

    control "You are north of the house. You may go {a=jump:east_of_house}east{/a} or {a=jump:west_of_house}west{/a}."


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

label east_of_house:

    scene bg back_door

    control "You are east of the house. There is a {a=call:back_door}back door{/a} here. ___ ___ {a=jump:meet_newcomer}newcomer{/a} description _____ _______ ______ _____ ____. You may go {a=jump:north_of_house}north{/a} or {a=jump:south_of_house}south{/a}."


#
# SNAKE: See snake. (eyes) (tongue) (fang?) 
#     Turn the tongue around to let it speak
#     Intercom with somebody inside.
#     The ask you which door you want to come through.
#     <east> <west>
#
image bg yuxta = "bg_yuxa-white.jpg"

label south_of_house:

    # unusually, the neighbor will block you from moving at first
    if call_out and not met_neighbor:
        call hello_neighbor
        jump west_of_house

    scene bg yuxta

    control "You are south of the house. There is an enormous {a=call:snake}snake{/a} here. You may go {a=jump:east_of_house}east{/a} or {a=jump:west_of_house}west{/a}."

