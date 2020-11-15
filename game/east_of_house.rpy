#Outdoors: Back of house #label east_of_house

define newcomer = Character("", image="newcomer")
define technologist = Character("", image="technologist")

label east_of_house:

    "There's some guy hanging out by that cool door."

    menu:
        "Approach him"
            jump meet_newcomer
        "Ignore him"
            jump east_of_house_2

label meet_newcomer:

    show newcomer

    "Hey, are you here for the workshop?"
    newcomer "Workshop?"
    newcomer "No, I'm meeting my guy here."
    newcomer "You know..."
    newcomer "For the stuff kids crave."
    "Are you talking about...?"
    newcomer "Shhh!"
    newcomer "Anyone could be listening."
    newcomer "But you're not here for...?"

    menu:
        "Oh yeah, no, I am, I just misunderstood you."
            jump newcomer_lie
        "I'm just trying to get in to see my friend."
            jump newcomer_friend

label newcomer_lie:

    newcomer "Got it. Got it."
    newcomer "Just keep it down, please."
    newcomer "And remember I was here first."

label newcomer_friend:

    newcomer "Well, nice to meet you or whatever."
    newcomer "Hey, do you think your friend could get me inside too?"

    menu:
        "Sure. For something in return."
            jump newcomer_bargain
        "Forget it."
            jump newcomer_annoy

label newcomer_bargain:

    newcomer "OK, so you want a taste of mine, is that it?"
    newcomer "Fair enough, fair enough."
    newcomer "I'll tell you what."
    newcomer "If you get me through that front door, I'll give you as much as you like."

label newcomer_annoy:

    newcomer "Screw you!"
    newcomer "You think you're, like, above me?"
    newcomer "You can go in but I can't, is that it?"
    newcomer "That seem fair to you?"
    newcomer "Fine. I don't need your friend's invitation anyway."
    newcomer "I've got friends inside too."
    newcomer "You'll see."
    newcomer "We're all gonna be best friends before we know it."

label east_of_house_2:

    menu:
        "Go left"
            jump south_of_house #snake
        "Go right"
            jump north_of_house #yard

label east_of_house_snake_permission:

    newcomer "Back already?"
    "Someone's coming to let us in."
    newcomer "So you pulled it off!"
    newcomer "Well, thanks, buddy."

    show technologist
    
    technologist "Quick, both of you, come in fast so nobody sees you."
    technologist "Right this way, shoes off, thank you."

    menu:
        "Go inside"
            jump map
        "Run away"
            jump credits