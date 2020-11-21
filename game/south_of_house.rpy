#Outdoors: Snake #label south_of_house
define snake = Character("Snake", image="snake", what_color="#ccffcc")


label snake:

    if not yuxa_alive:

        "There's a huge snake here."
        "Who would put something like this in their backyard?"
        "I wonder what it's made of..."
        "Maybe I'll touch it."
        call dead_snake_menu
    else:
        call live_snake_menu

label dead_snake_menu:

    menu:
        "Touch the snake's eyes":
            call snake_eyes
        "Touch the snake's tongue":
            jump snake_tongue
        "Touch the snake's fangs":
            call snake_fangs
        "Touch the snake's skin":
            call snake_skin

    jump south_of_house

label snake_eyes:

    "They're wet."
    "And warm."
    "Ugh, and it got slime on my fingers."
    "What the hell is this thing?"
    jump south_of_house_control

label snake_fangs:

    "They feel sharp...like chef knives."
    "Some kind of metal."
    "I think my hand's going numb..."
    "Bizarre..."
    jump south_of_house_control

label snake_skin:

    "It's leathery and rough."
    "Cool, a little damp..."
    "Something's beating underneath."
    "Is it the music in the house?"
    "Or something...alive...?"
    jump south_of_house_control

label snake_tongue:

    "It smells horrible in here."
    "Like rotting meat."
    "There's a rumbling sound coming from inside."
    "The tongue's kind of loose."
    "I think I can move it."

    menu: 
        "Turn the tongue":
            jump snake_tongue_turned
        "Leave the tongue alone":
            jump south_of_house_control

label snake_tongue_turned:
    stop music fadeout 1.0
    "Whoa, the rumbling just got a lot louder."
    "I should probably get out of here."

    show bg yuxa_resurrected with dissolve

    $ yuxa_alive = True

    call live_snake_menu

label live_snake_menu:

    play music "music/Yrevocnu.mp3"

    snake "Who's there?"
    "It sounds like an intercom."
    "It's really crackly and hard to understand." 
    "Like an announcement over the school PA."
    snake "Are you here for someone?"

    menu:
        "Yeah, my friend's inside.":
            jump snake_friend
        "I'm actually looking for the workshop.":
            jump snake_workshop
        # SB: I think this one is too easy.
        # "I think I'm lost. Can you help me?": 
        #     jump snake_lost #

label snake_friend:

    snake "Interesting! Normally we don't let anybody in without an invitation."
    snake "Your friend didn't happen to give you an invitation, did she?"

    menu:
        "She did! I have it here somewhere...":
            jump snake_lie
        "She didn't tell me anything about that.":
            jump snake_truth
        "Wait, how do you know my friend's a she?":
            jump snake_friend_2

label snake_lie:

    snake "Excellent! Come right inside."
    snake "You'll just need to show your ticket at the front door."
    snake "Your friend has told us so much about you."
    snake "We're very excited to meet you."

    $ front_door_open = True

    jump south_of_house

label snake_truth:

    snake "I'm sorry, but without an invitation you're out of luck."
    snake "Maybe you can find some around!"
    jump south_of_house

label snake_friend_2:

    snake "Lucky guess."
    "Can you just put her on?"
    snake "We don't know your friend is our friend."
    snake "Dangerous world out there..."
    snake "Can't let in just any old stranger off the street."
    jump south_of_house

label snake_workshop:

    snake "Oh yes, one of our famous workshops."
    snake "You wouldn't happen to have an invitation to this workshop, would you?"

    menu:
        "I must have it here somewhere...":
            jump snake_lie
        "I don't know anything about that.":
            jump snake_truth

label snake_lost:

    snake "Lost your way, have you?"
    snake "Fortunately we take our hospitality very seriously."
    snake "If you go around to the back door someone will let you in."
    snake "Relax and make yourself comfortable."
    snake "Maybe stay a while."
    snake "Stay as long as you like."

    $ back_door_open = True

    jump south_of_house_control