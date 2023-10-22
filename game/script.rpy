# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Penny")
image Penny_idle = "bg/WaveCinna.png"
image bg store = "bg/store.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg store:
        zoom 2.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Penny_idle with moveoutright:
        xpos 100
        ypos 50
        zoom 2.0


    # These display lines of dialogue.
    $ answer = False

    e "You've created a new Ren'Py game."
    label choices:
        e "Do you want to play this game?"
    menu:
        "yes":
            jump choice_a
        "no":
            jump choice_b

    label choice_a:
        $ answer = True
        e "Yay!"
        e "I can't wait to play!"
        jump flags

    label choice_b:
        e "Awww okay!"
        jump flags

    label flags:
        if answer:
            label startRoute:
                call screen choose_route
            return

        else:
            e "Hope we can play again soon!"
    # This ends the game.

    return
