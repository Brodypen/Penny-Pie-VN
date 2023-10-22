define yellow_character = Character("Penny", color = "#FFFF00", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])
define jackson = Character("Michael Jackson", color = "#FFFF00", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])
image Michaelimg = "bg/michaeljackson.png"
label yellow_start:
    scene bg home
    show Penny_coco at truecenter with moveoutright:
        zoom 2.0
    yellow_character "Hey, Its [yellow_character] again. Nice to meet you!!"
    yellow_character "Today we are going to learn about how I had to experience monthly budgeting and overspending!"
    yellow_character "Penny is reviewing her spending from the past month and it's not looking good. She spent too much on going to events with her friends this month!"
    scene work
    show Penny_idle at truecenter with moveoutright:
        zoom 2.0
    yellow_character "One of her co-workers suggested that she make a monthly budget at the beginning of the next month. Should she ..."
    menu:
        "Take her co-worker's advice":
            jump rightDecision3
        "Ignore the advice and continue spending":
            jump wrongDecision3

    label rightDecision3:
        $ answer = True
        jackson "HEEHEE"
        yellow_character "???"
        show Michaelimg at right:
            zoom 2.0
        jackson "HEEHEE that is correct HEEHEE overspending could put you in a really tight budget HEEHEE"
        jackson "HEEHEE smooth criminalll~"
        yellow_character "..."
        yellow_character "yeah thats correct i guess"
    
    label wrongDecision3:
        jackson "HEEHEE"
        yellow_character "???"
        show Michaelimg at right:
            zoom 2.0
        jackson "HEEHEE that is INCORECT!!!"
        yellow_character "HUH why mr. jackson?? why is that incorrect??"
        jackson "You need to look into the man in the mirror and tell her that creating a monthly budgeting plan can help reduce overspending."
        jackson "There is a common budgeting technique called 50/30/20 which goes as follows: 50%% -> goes towards needs such as groceries, rent, utilities, etc. 30%% -> goes towards wants such as going to the movies, restaurants, etc. 20%% -> goes towards savings such as emergency funds or investments"
        jump yellow_ending



label yellow_ending:
    yellow_character "I appreciate your time, Mr. Jackson!! Thank you"

    # set yellow to true to indicate yellow's ending was completed.
    $ persistent.yellow = True
    "THE END"
    return
 
