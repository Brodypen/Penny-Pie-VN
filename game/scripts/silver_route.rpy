define silver_character = Character("Penny", color = "#C0C0C0", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])
define beyonceChara = Character("Beyonce", color = "#C0C0C0", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ])
image beyonceImg = "bg/beyonce.png"
label silver_start:
    silver_character "Hey, I'm [silver_character]. Good to meet you!!"
    silver_character "Today we are going to learn about how I had to pick between saving and investing!"
    scene storeIMG
    show Penny_and_Friends at truecenter with moveoutright:
        zoom 2.0
    silver_character "With 20%% of her money in savings, Penny is feeling pretty good. When she meets up with one of her friends, he tells her about this stock he put all his savings into."
    silver_character "He explains how much money he is making and tries to convince her to do the same. Should she..."
    menu:
        "Keep her money in her savings":
            jump rightDecision4
        "Invest all her money in the same stock":
            jump wrongDecision4

    label rightDecision4:
        $ answer = True
        beyonceChara "HEY SINGLE LADY"
        show beyonceImg at right:
            zoom 2.0
        silver_character "BEYONCE??? IM YO COUSINNNN"
        beyonceChara "HEY BAE you are absolutely right!! We should NOT be investing this much money into a stock!! Especially since you dont know how it can end up."
        silver_character "I UNDERSTAND YOU QUEEN BEE!!!"
        jump silver_ending

    label wrongDecision4:
        beyonceChara "YOU SAID YOU MY COUSIN??"
        show beyonceImg at right:
            zoom 2.0
        silver_character "IM YO HUSBANDDDD"
        beyonceChara "YOU NOT MY HUSBAND WITH ALL THOSE RISKY STOCKS!!"
        silver_character "why?!"
        beyonceChara "Stock investments can be a quick way to gain money but can be incredibly risky so it's best to keep your savings for emergencies."
        beyonceChara "If she really wants to try her hand at investing, she can invest a small portion of her savings into stocks or find a lower risk alternative such as real-estate or mutual funds. "
        jump silver_ending


label silver_ending:
    silver_character "Thank you so much beyonce!!!"

    # set gold to true to indicate gold's ending was completed.
    $ persistent.silver = True
    "THE END"
    return
 