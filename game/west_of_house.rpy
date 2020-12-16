#Outdoors: Front of house #label west_of_house

define neighbor = DynamicCharacter(
    "neighbor_name",
    who_color="#880022",
    image="neighbor",
    what_color="#ffcccc",
)

image neighbor good = "foebuck_good.png"
image neighbor indignant = "foebuck_indignant.png"
image neighbor oops = "foebuck_oops.png"

default front_door_open = False


define technologist = Character(
    "Technologist",
    image="technologist",
    what_color="#ffaacc",
    who_color="#ff44cc")

image technologist action  = "technologist_action.png"

label front_door:
    if front_door_open:
        if has_invitation:
            jump west_of_house_invitation
        else:
            jump west_of_house_no_invitation
    else:
        jump try_front_door

label try_front_door:

    "I can hear music inside though."
    "What are they listening to in there?"
    "That music inside is super loud."
    "How will I get in if no one can hear me?"

    menu:
        "Call friend inside" if not called_friend:
            jump call_yes
        "Knock on door":
            jump knock_door
        "Shout" if not shouted_out:
            jump shout_out


label call_yes:
    "It's ringing."
    "Is she seriously not going to pick up?"
    "{i}The number you have dialed is out of service. Please try again later.{/i}"
    "I hope she's OK..."

    $ called_friend = True

    jump west_of_house_control

label knock_door:
    "Waiting."
    "Still waiting."
    "This is ridiculous."
    "Why am I even here?"
    "Maybe I should never have come..."
    "Well, I guess I already drove three hours. Might as well have a look around."

    jump west_of_house_control

label shout_out:
    "Hello!"
    "I'm here for the workshop!"
    "Can someone let me in?"
    "Might as well look around."

    $ shouted_out = True

    jump west_of_house_control


label hello_neighbor:
    show neighbor oops

    narrate "A man comes around the corner."

    $ met_neighbor = True
    $ neighbor_name = ""

    neighbor "Good luck getting anyone to answer."
    "Why's that?"
    neighbor "Weird people..."
    neighbor "I don't mind them, but some folks around here really do."
    neighbor "They invite you to one of their get-togethers?"

    menu:
        "Yeah. There's a friend of mine in there.": # consider other options...
            jump neighbor_yeah

label neighbor_yeah:
    show neighbor good

    neighbor "Word of advice?"
    neighbor "Keep an eye on your things."

    $ neighbor_name = "Neighbor"

    neighbor "These people...my neighbors..."
    neighbor "They are not accountable."
    neighbor "Do you consider yourself accountable?"

    menu:
        "More or less.": ## option for a different personality trait...
            jump neighbor_accountable
        # "I wouldn't go that far.":
        #    jump neighbor_not_accountable

label neighbor_accountable:
    neighbor "Hmm, in that case..."
    neighbor "Would you mind, if you get in...?"
    neighbor "A couple months ago one of them..."
    neighbor "Maybe you know his name."
    neighbor "The man, with the shirts and the braces."
    "I don't think so."

    show neighbor indignant

    neighbor "Anyway, he wanted to borrow my vacuum cleaner."
    neighbor "I think, what's the harm, it's not like I don't know where he lives."
    neighbor "A week goes by. A month."
    neighbor "I'm starting to wonder are they ever going to return it?"
    neighbor "You can guess what happened next."

    menu:
        "They gave it back?":
            call neighbor_vacuum_back from _call_neighbor_vacuum_back
        "Why don't you tell me.":
            call neighbor_vacuum from _call_neighbor_vacuum

    menu:
        "Sure.":
            call neighbor_vacuum_yes from _call_neighbor_vacuum_yes
        "I don't know...":
            call neighbor_vacuum_no from _call_neighbor_vacuum_no

    jump west_of_house

label neighbor_vacuum_back:
    show neighbor indignant
    # log PC as sarcastic?
    neighbor "You're pretty naive if you'd believe that."
    jump neighbor_vacuum

label neighbor_vacuum:
    show neighbor oops
    neighbor "I call and I call and then I go over and knock on the door exactly like you're doing."
    "And?"
    neighbor "And no one answers. I can't get a word out of them."
    neighbor "They've had my vacuum since March."
    neighbor "They have that crazy music on all the time."
    neighbor "Strange people...and I'm sorry but it's true..."
    neighbor "Strange people stopping by day and night."
    "What were you going to ask me?"
    neighbor "Yes, right, well..."
    neighbor "When and if you do somehow manage to get inside, could you try and find my vacuum cleaner?"
    neighbor "And then return it to me back here?"
    return

label neighbor_vacuum_yes:
    show neighbor indignant
    neighbor "I'll make it worth your time, I promise."
    neighbor "And unlike some people, I keep my word."

    hide neighbor indignant

    narrate "The man leaves abruptly, going north."

    $ accepted_neighbor_quest = True
    return

label neighbor_vacuum_no:
    show neighbor good
    neighbor "Looks like you'll fit in with this bunch just fine."
    neighbor "Maybe I'll see you out here later."
    neighbor "Good luck breaking and entering."
    return

define cook = Character("Cook", image="cook", what_color="#aaffcc")


label west_of_house_invitation:

    ## technologist welcome here....

    show technologist action at top
    technologist "Hello. I see you've been invited."
    technologist "Right this way, shoes off, thank you."

    menu:
        "Enter Cult HQ":
            screen black
            jump victory
        "Leave":
            jump credits

define librarian = Character("", image="librarian", what_color="#ccaaff")

label west_of_house_no_invitation:
    librarian "Who is it?"
    "I'm here to see my friend."
    librarian "We have no friends of anyone's here."
    "Come on, just let me in already."
    librarian "Are your papers in order?"
    "Umm..."
    librarian "I'm afraid without the proper documentation you cannot proceed."

    jump west_of_house_control

