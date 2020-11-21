#Outdoors: Back of house #label east_of_house

define newcomer = DynamicCharacter(
    "newcomer_name",
    image="newcomer",
    who_color="#002288",
    what_color="#ccccff"
    )
default newcomer_name = "Newcomer"

image newcomer face = "newcomer.png"

default met_newcomer = False
default took_newcomer_deal = True
default newcomer_inside = False

define technologist = Character("", image="technologist")

label encounter_newcomer:
    if not met_newcomer:
        jump meet_newcomer
    else:
        jump revisit_newcomer


label meet_newcomer:

    show newcomer face at left
    $ met_newcomer = True

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
        "Oh yeah, no, I am, I just misunderstood you.":
            jump newcomer_lie
        "I'm just trying to get in to see my friend.":
            jump newcomer_friend

label newcomer_lie:

    newcomer "Got it. Got it."
    newcomer "Just keep it down, please."
    newcomer "And remember I was here first."
    jump east_of_house_control

label newcomer_friend:

    newcomer "Well, nice to meet you or whatever."
    newcomer "Hey, do you think your friend could get me inside too?"

    menu:
        "Sure. For something in return.":
            call newcomer_bargain
        "Forget it.":
            call newcomer_annoy

    hide newcomer face

    jump east_of_house_control

label newcomer_bargain:

    $ took_newcomer_deal = True

    newcomer "OK, so you want a taste of mine, is that it?"
    newcomer "Fair enough, fair enough."
    newcomer "I'll tell you what."
    newcomer "If you get me through that front door, I'll give you as much as you like."
    return

label newcomer_annoy:

    newcomer "Screw you!"
    newcomer "You think you're, like, above me?"
    newcomer "You can go in but I can't, is that it?"
    newcomer "That seem fair to you?"
    newcomer "Fine. I don't need your friend's invitation anyway."
    newcomer "I've got friends inside too."
    newcomer "You'll see."
    newcomer "We're all gonna be best friends before we know it."
    return

label east_of_house_snake_permission:

    if met_newcomer:
        show newcomer face at left
        newcomer "Back already?"
        "Someone's coming to let us in."
        newcomer "So you pulled it off!"
        newcomer "Well, thanks, buddy."

    show technologist at right
    
    technologist "Quick, both of you, come in fast so nobody sees you."
    technologist "Right this way, shoes off, thank you."

    $ newcomer_inside = True
    narrate "The [newcomer_name] slips in ahead of you through the back door."

    menu:
        "Go inside":
            screen black
            jump victory
        "Run away":
            jump credits

default newcomer_visits = 0

label revisit_newcomer:

    if newcomer_visits == 0:

        jump revisit_newcomer_0

    elif newcomer_visits == 1:

        jump revisit_newcomer_1

    elif newcomer_visits == 2:

        jump revisit_newcomer_2

    else:

        jump revisit_newcomer_end

label revisit_newcomer_0:

    $ newcomer_visits = 1

    show newcomer face at left

    "Still waiting, huh?"

    newcomer "Better here than out there."

    newcomer "These are some pretty crazy times."

    newcomer "Corporate Evil, World at war, Famine."

    newcomer "Greed, racism, bigotry, baddy fucking bad us La Di Da Doomdaying Da."

    newcomer "It sounds like some absurd zombie apocalypse b-movie."

    newcomer "Every beaten to death dystopian cliche out there."

    "Yeah, we are pretty fucked."

    newcomer "And yet here we are."

    "Here we are. In front of this door."

    narrate "The house murmurs a thumping bass line while the night grows colder."

    hide newcomer face

    jump east_of_house_control

label revisit_newcomer_1:

    $ newcomer_visits = 2

    show newcomer face at left

    newcomer "Hey, do you remember that old show with the big walking, talking bird?"

    "Yeah, that old TV show."

    newcomer "That bird isn't real. It's a man in a suit."

    "Haha. Yeah, I guess it's a not a real huge talking bird."

    newcomer "Fucking child abuse, putting kids through that shit."

    "Haha. Yeah... totally."

    newcomer "I'll never forget the day. Mom took me to the studio to see it."

    newcomer "I was going to meet the bird."

    newcomer "Then there it is, skinned, gutted, head chopped off."

    "Devastating."

    newcomer "Mom told me it was OK, that they could find somebody to wear the skin and head."

    newcomer "Somebody who could walk and dance {i}wearing{/i} it."

    newcomer "Sick."

    "Yeah, really sick, now that you say it like that."

    hide newcomer face
    jump east_of_house_control


label revisit_newcomer_2:

    $ newcomer_visits = 3

    show newcomer face at left

    newcomer "It's not just the talking bird. We're all wearing suits."

    "Huh?"

    newcomer "Ever just get exhausted being whoever the fuck you are?"

    "Uhh ..."

    newcomer "The simple things of you."
    newcomer "How to stand in a room when there are other people there."
    newcomer "How to assert oneself into one’s own life without being a dick to others."

    "You're saying that's wearing a bird suit?"

    newcomer "I don't care what you believe I'm saying. It's irrelevant to me. You can't prove anything about me."

    "Oh."

    newcomer "Maybe you are looking for a way out of this shithole world."

    newcomer "This shithole life."

    newcomer "To something so much more..."

    newcomer "Something."

    menu:
        "I'm looking for answers and inspiration.":
            newcomer "How to find solace in one’s own fault lines, how to howl at the moon and mean it, how to embrace today as fuel for tomorrow."
            pass
        "I'm looking for true belonging.":
            newcomer "How to choose friends beyond convenience, how to laugh openly, How to be compassionate without it devolving into cowardice..."
            pass
        "I'm looking for an escape from the mundane.":
            newcomer "How to stop the autopilot self and unleash the interconnected system of superself that understands fear is just another tool in the belt... That one is definitely straight forward enough."
            pass
        "I'm looking for the real talking bird.":
            newcomer "Exactly. The real talking bird."
            narrate "The newcomer begins to weep."
            pass

    newcomer "It’s exhausting. To the bone. The body, the spirit, all of it. Weary planet exhaustion to the core of all fcking things tired..."
    newcomer "The relentless haunting that there is more to it all than 'just this'."
    newcomer "While you fit in as best you can, a spy now trapped behind the enemy lines of your own life praying you won’t be discovered."

    narrate "Silence again. The newcomer lights a cigarette."

    hide newcomer face
    jump east_of_house_control


label revisit_newcomer_end:
    show newcomer face at left

    newcomer "But what if I were to tell you there’s a group of people: engineers, scientists, educators, designers, artists."
    newcomer "Doctors and lawyers and tinkers and tailors too, all come together to figure a way forward."
    newcomer "All driven by that same small voice of many voices."
    newcomer "People of like spirit if not like mind, driven by that same haunting spy movie thrill kind of sense - That there really is more than Just This."
    newcomer "Something to be found, deep within it all. Deep within US all. Something to be unleashed - uncovered"
    newcomer "What if I were to tell you there was a planet wide band of misfits and miscreants, wide eyed and wide open, broken hearted believers in humanity come together to harness that autopilot fear - to wield as both tool and weapon."
    newcomer "To assert that raging storm of slapstick dreaming we call life as way to define the very age we live in - Not the new age - let’s be real there’s nothing new under the sun - but The Next Age."

    $ newcomer_name = "Nextgoer"

    narrate "The Nextgoer drops the butt of his cigarette and grinds it with his heel."

    newcomer "Yeah. Of course. You’d know I was totally full of shit."

    hide newcomer face

    jump east_of_house_control