define blue_character = Character("Blue", color = "#0000ff", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])

label blue_start:
    blue_character "Yo. I'm [blue_character]."
    jump blue_scene1

label blue_scene1:
    # This is where blue's route will be.
    jump blue_ending

label blue_ending:
    blue_character "Will you marry me?"

    # set blue to true to indicate blue's ending was completed.
    $ persistent.blue = True
    "THE END"
    return
 