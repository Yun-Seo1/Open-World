<<<<<<< Updated upstream
#Version 0.0.X
=======
#Version 0.0.2
label OW_residential:
    show monika 1a_owawm at t11
    $ OW_talk = renpy.random.choice(OW_random_talk)
    menu:
        m "[OW_talk]{fast}"
        "Talk":
            call screen dialog(message="Error: No Talk options have been added", ok_action=Return())
            jump OW_residential
        "Interact":
            call screen dialog(message="Error: No Interaction options have been added", ok_action=Return())
            jump OW_residential
        "Return to [RTMAS.title()]":
            call OW_Go_Back_To_Classroom
>>>>>>> Stashed changes
