screen choose_route:
    add "bg/bg_choose.png"
    # This button will delete any persistent variable
    button:
        text "Clear Persistence": 
            idle_color "#fff"
            hover_color "#c0c0c0"
        action Function(renpy.game.persistent._clear)
        # horizontal box containing the 5 image buttons
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30  
        spacing 20

        imagebutton:
            auto "choices/red%s.png"
            action Jump("left_start")
        imagebutton:
            auto "choices/yellow%s.png"
            action Jump("right_start")
            sensitive persistent.left == True
            # The imagebutton will be enabled if blue, red and yellow are true and disabled when at least one is false.