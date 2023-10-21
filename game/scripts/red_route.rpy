define red_character = Character("Red", color = "#ff0000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

label red_start:
    red_character "Yo. I'm [red_character]."
    jump red_scene1

label red_scene1:
    # This is where red's route will be.
    jump red_ending

label red_ending:
    red_character "Will you marry me?"
    
    # set red to true to indicate red's ending was completed.
    $ persistent.red = True
    "THE END"
    return
 