# Outside

define block = Character("", advance=False)

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

image bg disassociate3 = "bg_disassociate3.jpg"

image front_door_1 = "front-door-1.jpeg"

label west_of_house:

    scene bg disassociate3

    show front_door_1 at top

    # TODO: Front door label
    block "You are west of a house with a {a=call:neighbor}front door{/a}. There is a small {a=jump:mailbox}mailbox{/a} here. You may go {a=jump:north_of_house}north{/a} or {a=jump:south_of_house}south{/a}."

    pass

label mailbox:

    show testimonial

    "Opening the small mailbox reveals a leaflet."

    hide testimonial

    jump west_of_house

define nb = Character("", image="neighbor")

image neighbor good = "foebuck_good.png"
image neighbor indignant = "foebuck_indignant.png"
image neighbor oops = "foebuck_oops.png"

label neighbor:
    show neighbor indignant
    nb "I'll never forgive what you've done to me!"
    show neighbor oops
    nb "Oh I mistook you for somebody else"
    show neighbor good
    nb "Have a nice day!"
    hide neighbor good
    jump west_of_house

# 
# YARD: nothing. <west> <east>
#

label north_of_house:

    scene bg disassociate3

    "TODO: Yard background scene."

    block "You are north of the house. You may go {a=jump:east_of_house}east{/a} or {a=jump:west_of_house}west{/a}."


#
# BACK: Back door.
#    - Encounter Newcomer
#    - introduction and pick option about self.
#       - talking about snake: reveals it didn't talk to him
#    - if enter through back door, Newcomer comes it with.
#   
#     <north><south>
#

image bg cultydoor = "bg_culty_door.png"

label east_of_house:

    scene bg cultydoor

    block "You are east of the house. There is a {a=call:back_door}back door{/a} here. ______{a=jump:newcomer}newcomer{/a} description___________________________. You may go {a=jump:north_of_house}north{/a} or {a=jump:south_of_house}south{/a}."


#
# SNAKE: See snake. (eyes) (tongue) (fang?) 
#     Turn the tongue around to let it speak
#     Intercom with somebody inside.
#     The ask you which door you want to come through.
#     <east> <west>
#
image bg yuxta = "bg_yuxa-white.jpg"

label south_of_house:

    scene bg yuxta

    block "You are south of the house. There is an enormous {a=call:snake}snake{/a} here. You may go {a=jump:east_of_house}east{/a} or {a=jump:west_of_house}west{/a}."

