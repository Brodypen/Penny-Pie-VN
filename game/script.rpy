# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

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
        jump flags

    label choice_b:
        e "Awww okay!"
        jump flags

    label flags:
        if answer:
            e "I cant wait to play!!"
        else:
            e "Hope we can play again soon!"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
