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
            #call screen dialog(message="Error: No Interaction options have been added", ok_action=Return())
            jump OW_residential_interaction
        "Return to [RTMAS.title()]":
            call OW_Go_Back_To_Classroom

#MC's house button (18, 372)

#####
#Talk
#####



############
#Interaction
############
label OW_residential_interaction:
    hide monika
    call screen OWAWM_residential()
    screen OWAWM_residential():
        imagemap:
            ground "bg/residential.png"
            
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1123
            ypos 2
            textbutton ("Return") action [Hide("OWAWM_residential"), Jump("OW_residential")] hover_sound gui.hover_sound

        textbutton("Neighborhood"):
            style "hkb_button"
            style_prefix "hkb"
            xpos 0
            ypos 372
            xysize(160,None)
            action Jump("OW_go_to_neighborhood") hover_sound gui.hover_sound


#############
#Leaving Area
#############
label OW_go_to_neighborhood:
    m "Do you want to go outside {color=#000}[OW_mc]{/color}'s house [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go outside {color=#000}[OW_mc]{/color}'s house [player]?{fast}"
        "Yes":
            scene bg house with dissolve_scene_full
            $ play_song(audio.t3,loop = True, fadein = 1.0)
            pause 2.0
            jump OW_outside_mc_house
        "No":
            call screen OWAWM_residential()