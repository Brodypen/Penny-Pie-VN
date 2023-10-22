define blue_character = Character("Penny", color = "#0000ff", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
$ answer = False
label blue_start:
    blue_character "Hi, I'm [blue_character]! It's so great to meet you!!"
    blue_character "Today, we're going to learn about want vs. need. So here's a story about me:"
    blue_character "Penny is at the store picking up some things when she sees a squishmellow."
    blue_character "She really wants to add one to her collection, but she needs to stack up on food. Should I have..."
    menu:
        "Bought food":
            jump rightDecision
        "Bought the squishmellow":
            jump wrongDecision

    label rightDecision:
        $ answer = True
        blue_character "That's correct! *we could give reasons here???*"
        jump blue_ending

    label wrongDecision:
        blue_character "Uh Oh! That isn't right. Here's why:"
        blue_character "When learning to manage money, it is good to distinguish between what you want and what you need."
        blue_character "It is important to invest in your necessities such as food, paying rent, etc."
        jump blue_ending

label blue_ending:
    blue_character "Thank you and have a good day!!"

    # set blue to true to indicate blue's ending was completed.
    $ persistent.blue = True
    "THE END"
    return
 