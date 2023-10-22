define gold_character = Character("Penny", color = "#FFD700", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

label gold_start:
    gold_character "Hello, I'm [gold_character]. Nice to meet you!!"
    gold_character "Today we are going to learn about credit card debt! Here is my predicament:"
    gold_character "When looking through her mail, Penny sees a letter from the bank regarding her credit card debt. After finalizing her monthly budget, she is looking at the 30%%, which interestingly is enough to pay off her credit card debt entirely with a tiny bit of cash left over. "
    gold_character "At the same time, she has been eyeing a brand new flat screen tv to put in her living room. Should she ..."
    menu:
        "Pay off the rest of her debt":
            jump rightDecision5
        "Buy the TV and continue to pay off the debt monthly":
            jump wrongDecision5

    label rightDecision5:
        $ answer = True
        gold_character "That's correct! *we could give reasons here???*"
        jump gold_ending

    label wrongDecision5:
        gold_character "Uh Oh! That isn't right. Here's why:"
        gold_character "Paying off your credit card monthly works but it is not the most ideal scenario. If presented with the opportunity to pay off the debt entirely, it's best to do so."
        gold_character "That way when the next paycheck comes in, you can spend the money on things you want while maintaining a decent credit card score."
        jump gold_ending


label gold_ending:
    gold_character "Thank you and have a good day!!"

    # set gold to true to indicate gold's ending was completed.
    $ persistent.gold = True
    "THE END"
    return
 