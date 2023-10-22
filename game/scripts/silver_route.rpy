define silver_character = Character("Silver", color = "#C0C0C0", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])

label silver_start:
    silver_character "Hey, I'm [silver_character]. Good to meet you!!"
    silver_character "Today we are going to learn about how I had to pick between saving and investing!"
    silver_character "With 20%% of her money in savings, Penny is feeling pretty good. When she meets up with one of her friends, he tells her about this stock he put all his savings into."
    silver_character "He explains how much money he is making and tries to convince her to do the same. Should she..."
    menu:
        "Keep her money in her savings":
            jump rightDecision
        "Invest all her money in the same stock":
            jump wrongDecision

    label rightDecision4:
        $ answer = True
        silver_character "That's correct! *we could give reasons here???*"
        jump silver_ending

    label wrongDecision4:
        silver_character "Uh Oh! That isn't right. Here's why:"
        silver_character "Stock investments can be a quick way to gain money but can be incredibly risky so it's best to keep your savings for emergencies."
        silver_character "If she really wants to try her hand at investing, she can invest a small portion of her savings into stocks or find a lower risk alternative such as real-estate or mutual funds. "
        jump silver_ending


label silver_ending:
    silver_character "Thank you and have a good day!!"

    # set gold to true to indicate gold's ending was completed.
    $ persistent.silver = True
    "THE END"
    return
 