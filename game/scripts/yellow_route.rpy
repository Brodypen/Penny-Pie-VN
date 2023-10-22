define yellow_character = Character("Yellow", color = "#FFFF00", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

label yellow_start:
    yellow_character "Hello, I'm [gold_character]. Nice to meet you!!"
    yellow_character "Today we are going to learn about monthly budgets! Here is my predicament:"
    yellow_character "Penny is reviewing her spending foe the past month and it's not looking good. She spent too much on going to events with her friends this month!"
    yellow_character "One of her co-workers suggested that she make a monthly budget at the beginning of the next month. Should she ..."
    menu:
        "Take her co-worker's advice":
            jump rightDecision
        "Ignore the advice and continue spending":
            jump wrongDecision

    label rightDecision3:
        $ answer = True
        yellow_character "That's correct! *we could give reasons here???*"
    
    label wrongDecision3:
        yellow_character "Uh Oh! That isn't right. Here's why:"
        yellow_character "When managing money, it is best to create a monthly budget so you don't overspend."
        yellow_character "There is a common budgeting technique called 50/30/20"
        jump yellow_ending



label yellow_ending:
    yellow_character "Thank you and have a good day!!"

    # set yellow to true to indicate yellow's ending was completed.
    $ persistent.yellow = True
    "THE END"
    return
 