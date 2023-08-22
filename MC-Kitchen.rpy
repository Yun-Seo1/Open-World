label OW_Go_To_MC_Kitchen:
    if persistent.OW_has_seen_MC_kitchen == False:
        show monika 1a_owawm at h11
        m "I forgot how furnished {color=#000}[OW_mc]{/color}'s kitchen was."
        m "Maybe I can finally practice baking like {color=#000}N[OW_natsuki]{/color} one of these days."
        m 10l_owawm "I'm not the best at cooking so I hope you don't mind burned food for a while."
        m 10m_owawm "That's a joke... I hope I don't burn everything though. "
        extend 1v_owawm "And if you are a cook, maybe you wouldn't mind teaching your beautiful girlfriend, would you?"
        m 1k_owawm "I'll be counting on you to teach me."
        $ persistent.OW_has_seen_MC_kitchen = True
    show monika 5a_owawm at t11
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            jump OW_MC_kitchen_talk
        "Interact":
            jump OW_MC_Kitchen_Interaction
        "Return to [RTMAS]":
            call OW_Go_Back_To_Classroom
#####
#Talk
#####

label OW_MC_kitchen_talk:
    show monika 3e_owawm at t22
    pause 0.5
    show monika at t21
    pause 0.5
    show monika at t11
    m "What I wouldn't give to spend a morning in a place like this."
    m 1k_owawm "Both of us sitting at the dining table or counter, both of us sipping a cup of coffee while watching whatever is on the TV."
    m 4j_owawm "Or just enjoying each other's company."
    m 4t_owawm "Wouldn't that sound lovely [mas_get_player_nickname()]?"
    show monika 5a_owawm at h11
    m "I hope you share the same feelings."
    jump OW_Go_To_MC_Kitchen


############
#Interaction
############
label OW_MC_Kitchen_Interaction:
    hide monika
    call screen OWAWM_MC_KITCHEN()
    screen OWAWM_MC_KITCHEN():
        imagemap:
            ground "bg/kitchen.png"
            hotspot(28, 184, 229, 273) action Jump("OW_kitchen_fridge") hover_sound gui.hover_sound
            hotspot(1047, 397, 147, 100) action Jump("OW_kitchen_convention_oven") hover_sound gui.hover_sound

        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("OWAWM_MC_KITCHEN"), Jump("OW_Go_To_MC_Kitchen")] hover_sound gui.hover_sound
        hbox:
            xpos 533
            ypos 680
            spacing 7
            textbutton ("Outside") action Jump("OW_go_outside_from_kitchen") hover_sound gui.hover_sound
            textbutton ("Bedroom") action Jump("OW_back_upstairs") hover_sound gui.hover_sound

###################
#Interaction Labels
###################
label OW_kitchen_fridge:
    show monika 1d_owawm at t31
    m "I wonder what food is in his fridge, but I'm not really expecting much."
    hide monika with dissolve
    m "Gosh, I was right."
    show monika 8s_owawm at t11
    m "The fridge is completely empty too!"
    m 8r_owawm "I expected as much considering other things seem like props."
    m 1p_owawm "I missed my world but it just feels lifeless and empty."
    m 1o_owawm "I'm glad that there's food in the spaceroom..."
    m "This kinda makes me feel less human in a way."
    m 2m_owawm "I should look on the brightside of things though. Even if there's no food here, I can always count on you to give me some."
    m 4l_owawm "Besides, the food you give me always tastes better than the food I code in myself."
    m 4j_owawm "Thank you for always taking care of me [player]. I hope one day to return the favor."
    call screen OWAWM_MC_KITCHEN()

label OW_kitchen_convention_oven:
    show monika 5a_owawm at t33
    m "Hmm, I wonder if this still works. I know {color=#000}[OW_mc]{/color} and {color=#000}N[OW_natsuki]{/color} used the oven so maybe these appliances work too."
    hide monika
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1r_owawm at h11
    m "EEEK!!"
    m 1g_owawm "I guess that answers that."
    m 2f_owawm "I hope the oven still works, I do want to try baking like {color=#000}N[OW_natsuki]{/color} one day."
    show monika 2v_owawm 
    pause 1.0
    m "{cps=*2}So that maybe I can bake for you one day in the real world.{/cps}{nw}"
    call screen OWAWM_MC_KITCHEN()

#################
#Leaving the area
#################

label OW_back_upstairs:
    hide screen OWAWM_MC_KITCHEN
    m "Do you want to go back to {color=#000}[OW_mc]{/color}'s room?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go back to {color=#000}[OW_mc]{/color}'s room?{fast}"
        "Yes":
            scene bg bedroom with dissolve_scene_full
            pause 2.0
            $ play_song(audio.MC_Room,loop = True, fadein = 0)
            jump OW_Go_To_MC_Room
        "No":
            call screen OWAWM_MC_KITCHEN()

label OW_go_outside_from_kitchen:
    m "Do you want to go outside [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go outside [player]?{fast}"
        "Yes":
            scene bg house with dissolve_scene_full
            pause 2.0
            $ play_song(audio.t3,loop = True, fadein = 0)
            jump OW_outside_mc_house
        "No":
            call screen OWAWM_MC_KITCHEN()
            
