define blue_character = Character("Penny", color = "#0000ff", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define clooney = Character("George Clooney", color = "#0000ff", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

$ answer = False
image store = "bg/store.png"
label blue_start:
    blue_character "Hi, I'm [blue_character]! It's so great to meet you!!"
    blue_character "Today, we're going to learn about want vs. need. So here's a story about me:"
    scene store
    show Penny_idle at truecenter with moveoutright:
        zoom 2.0
    blue_character "Penny is at the store picking up some things when she sees a squishmellow."
    blue_character "She really wants to add one to her collection, but she needs to stack up on food. Should I have..."
    menu:
        "Bought food":
            jump rightDecision
        "Bought the squishmellow":
            jump wrongDecision

    label rightDecision:
        $ answer = True
        show clooney at right:
            zoom 2.0
        clooney "That's correct! Thank you so much penny for getting the food. This is definitely how i got rich, and i hope you guys do too."
        blue_character "Thank YOU mr.George Clooney! I'm honored that you were able to make it here today, and i hoep to see you again in the future!!"
        jump blue_ending

    label wrongDecision:
        clooney "NOOOOOO"
        blue_character "HUH???"
        show clooney at right:
            zoom 2.0
        clooney "SQUISHMELLOWS ARE NOT MARSHMELLOWS!!! YOU CHOSE A PLUSHIE OVER SOME DAMN SUSTENANCE"
        blue_character "can you explain why that is wrong??"
        clooney "When learning to manage money, it is good to distinguish between what you want and what you need."
        clooney "It is important to invest in your necessities such as food, paying rent, etc."
        jump blue_ending

label blue_ending:
    blue_character "Thanks again mr.Clooney for helping us an see yall next time!!"

    # set blue to true to indicate blue's ending was completed.
    $ persistent.blue = True
    "THE END"
    return
 