# Outdoors: Yard #north_of_house


define friend = Character(
    "Friend",
    who_color="#888888",
    image="friend",
    what_color="#cccccc",
)

image invitation = "invitation.png"

label empty_yard:

    if not has_invitation and accepted_neighbor_quest:
        jump pick_up_invitation
    elif front_door_open and called_friend:
        jump friend_calls
    else:
        narrate "The yard is empty."

        jump north_of_house_control

label friend_calls:

    "It's a nice night."

    $ location = "Pittsburgh" # ideally randomly choose between Pittsburgh, Bridgeport, etc.

    "Funny to drive three hours only to be hanging out alone in an empty yard."
    "How did I wind up here?"
    "I was looking for answers."
    "My friend said that she had found some."
    "She invited me to an event at someone's house near [location]."
    "I was hesitant at first."
    "My friend had a history of unreliability."
    "And in two months I was getting married."
    "There were competing claims for my attention."
    "Life goes on or answers--that was how it broke down for me."
    "I was hungry for mentorship."

    friend "Come out for a weekend and meet my friends"
    friend "They’re cool people. I think you’d really like them."

    "And I'd get to meet the guru?"

    friend "Oh, there's no guru."

    "Then who has the answers?"

    friend "We share them."

    "Sometimes my friend called it a cult."

    friend "More like an Ancient Greek cult than a Waco, Texas cult."

    friend "I'm kidding!"

    friend "It's not really a cult. That's a joke."

    "She told me to join a workshop the group was running at a big house outside [location]"

    friend "Come to the Future Ball!"

    "..."

    "I'm here. Where are you?"

    "{i}Phone rings{/i}"   # best to have a sound effect

    "Huh. She finally called back!"

    friend "Hi! You're here!"

    menu:
        "Hi hi! So excited to be here!":
            pass
        "Took you long enough...":
            pass

    friend "I'm so sorry I missed your call earlier!"
    friend "We have to turn our phones off when bathing in lustrations."

    "Bathing in what?"

    friend "You'll have to experience that for yourself."

    friend "First, let's get you inside."

    friend "Have you tried the front door?"

    "Yeah. Somebody told me to piss off because I didn't have the right paperwork."

    friend "Oh, the Librarian. Don't mind him. He's a robot."

    "Huh? You mean he's got aspergers or something?"

    friend "No! Of course not. I mean he's actually a robot."
    friend "He can get stuck on the formal rules and procedures sometimes."
    friend "You'll get used to him though."
    friend "Hey, come around the back. I'll open the door for you there."
    friend "See you soon!"

    $ back_door_open = True

    "Sometimes a scene just sucks you in if you’re open to it."
    "Before you know it you’re part of the cult too."

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


