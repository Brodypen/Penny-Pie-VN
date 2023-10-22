define red_character = Character("Penny", color = "#E0D7FF", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

label red_start:
    red_character "Hey its [red_character]! We're back again with another story of mines!"
    red_character "Today we are going to learn about a time when I had to choose doing a DIY or spend money:"
    red_character "Penny is lounging at home and realizes she hasn't eaten anything today."
    red_character "There is a great restaurant near her house that she orders from all the time, but she also had the ingredients to make a filling lunch at home."
    red_character "Should she..."
    menu:
        "Make food":
            jump rightDecision2
        "Order food":
            jump wrongDecision2

    label rightDecision2:
        $ answer = True
        red_character "That's correct! *we could give reasons here???*"
        jump red_ending

    label wrongDecision2:
        red_character "Uh Oh! That isn't right. Here's why:"
        red_character "Food is obviously a necessity, but spending a lot on food is not."
        red_character "Although ordering food is okay once in a while, if there is the option of eating at home, it is more cost efficient."
        jump red_ending

label red_ending:
    red_character "Thank you and have a good day!!"
    
    # set red to true to indicate red's ending was completed.
    $ persistent.red = True
    "THE END"
    return
 