define red_character = Character("Penny", color = "#ff0000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define kris = Character("Kris Jenner", color = "#ff0000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
image Jenner = "bg/jenner.png"
label red_start:
    red_character "Hey its [red_character]! We're back again with another story of mines!"
    red_character "Today we are going to learn about a time when I had to choose doing a DIY or spend money:"
    red_character "Penny is lounging at home and realizes she hasn't eaten anything today."
    scene restaurant
    show Penny_coco at truecenter with moveoutright:
        zoom 2.0
    red_character "There is a great restaurant near her house that she orders from all the time, but she also had the ingredients to make a filling lunch at home."
    red_character "Should she..."
    menu:
        "Make food":
            jump rightDecision2
        "Order food":
            jump wrongDecision2

    label rightDecision2:
        $ answer = True
        show Jenner at right:
            zoom 3.0
        kris "You're doing amazing sweetie!! You 4+4 ate that!"
        red_character "Thank you Mother!! We spending money cent for cent!!"
        jump red_ending

    label wrongDecision2:
        show Jenner at right:
            zoom 3.0
        kris "Absolutely not, I am disappointed in you sweetie."
        red_character "KRIS JENNER??? why??"
        kris "Food is obviously a necessity, but spending a lot on food is not."
        kris "Although ordering food is okay once in a while, if there is the option of eating at home, it is more cost efficient."
        red_character "omg thank you so much for teaching us this!!!"
        jump red_ending

label red_ending:
    red_character "We hope to see you again reader!!"
    
    # set red to true to indicate red's ending was completed.
    $ persistent.red = True
    "THE END"
    return
 