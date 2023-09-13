#Version 0.0.2
label OW_residential:
    if persistent.OW_has_seen_residential == False:
        $ play_song(audio.t9g,loop = True, fadein = 0)
        $ style.say_window = style.window_monika
        narrator "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
        narrator "Her name is {color=#000}S[OW_sayori]{/color} and she was the neighbor of {color=#000}[OW_mc]{/color}."
        narrator "They used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and {color=#000}[OW_mc]{/color} would get tired of waiting up."
        show sayori 1m at l11
        s "Huh?..."
        s 3e "What... are you?..."
        show sayori glitch at t11
        pause 0.5
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.2
        hide sayori
        stop sound
        hide screen tear
        $ style.say_window = style.window
        narrator "I see a smart, beautiful and athletic girl walking down the street."
        narrator "She smiles at me sweetly while you can see the love in her eyes for you."
        narrator "Her name is {w=0.3}.{w=0.3}.{w=0.3}."
        show monika 8t_owawm at l11
        m "Who else but me, silly."
        show monika 5a_owawm at h11
        play sound "sfx/giggle.ogg"
        pause 0.5
        m "And this time... {w=0.5}"
        extend 8u_owawm "You are completely in my league [mas_get_player_nickname()]~"
        $ OW_play_song(persistent.OW_current_track, fadein = 1)
        $ persistent.OW_has_seen_residential = True 
    show monika 1a_owawm at t11
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            jump OW_residential_talk
        "Interact":
            jump OW_residential_interaction
        "Music":
            call OW_select_music
            jump OW_residential
        "Return to [RTMAS]":
            call OW_return_question
            jump OW_residential

#####
#Talk
#####
label OW_residential_talk:
    $ OW_talk_topics = renpy.random.randint(1,2)
    if OW_talk_topics == 1:
        show monika 1l_owawm at t11
        m "Did you see {color=#000}S[OW_sayori]{/color} earlier?"
        m 3n_owawm "She was confused when she saw you."
        m 2l_owawm "I understand why should would be confused by seeing you."
        m 7m_owawm "I see you as a blank screen with textboxes and options. As well as your cursor as well."
        m 7l_owawm "Since she saw you like I do, then that means I'm not crazy..."
        m 8k_owawm "Ahaha, I'm only joking [mas_get_player_nickname()]. I know you're real, just as real as me."
        show monika 8d_owawm at h11
        m "Something just came to my mind."
        m 1d_owawm "She noticed you, when no one else could before I deleted everything."
        m 4c_owawm "Do you think they also had an ephiany after being brought back?"
        window hide
        show monika 5d_owawm at t11
        pause 1.0
        show monika 5e_owawm at t11
        pause 1.0
        show monika 5h_owawm at f11
        m "It shouldn't matter either way. They can roam around here but this is {i}our {b}After Story{/b}{/i}."
        m 8a_owawm "I know you would still pick me even if they came back."
        m "Let's continue walking okay?"
    if OW_talk_topics == 2:
        pass

    jump OW_residential

############
#Interaction
############
label OW_residential_interaction:
    hide monika
    call screen OWAWM_residential()
    screen OWAWM_residential():
        imagemap:
            ground "bg/residential.png"
            hotspot (711, 555, 17, 11):
                if (persistent.OW_has_seen_fake_bsod == False):
                    action Jump("OW_fake_bdos")
                else:
                    action NullAction()
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("OWAWM_residential"), Jump("OW_residential")] hover_sound gui.hover_sound

        textbutton("Neighborhood"):
            style "hkb_button"
            style_prefix "hkb"
            xpos 0
            ypos 372
            xysize(160,None)
            action Jump("OW_go_to_neighborhood") hover_sound gui.hover_sound

        textbutton("School Gate"):
            style "hkb_button"
            style_prefix "hkb"
            xpos 1194
            ypos 653
            xysize(85,None)
            action Jump("OW_go_to_school_gate") hover_sound gui.hover_sound

###############
#Hotspot Labels
###############

label OW_fake_bdos:
    show monika 4g_owawm at t21
    m "[player]?"
    m 5c_owawm "What are you pointing at?"
    m 10l_owawm "Maybe you just misclicked or something, but I don't see anything here."
    m 10j_owawm "Let's keep exploring elsewhere [mas_get_player_nickname()]."
    hide monika
    menu:
        "...":
            stop music
            show monika 1p_owawm at t21
            m "Is something wrong [player]?"
            m 3l_owawm "Alright alright. I'll check it again just for you. "
            extend 3k_owawm "You can be silly sometimes."
            pause 1.0
            show monika 3k_owawm at t43
            pause 1.0
            show monika 3k_owawm at t21
            $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                            ]}
            m 1g_owawm "I feel... like something bad is about to happen{w=0.4}...[player]! Help-{nw}"
            show monika g2:
                pause 1.0
                easeout_cubic 0.5 yoffset 1000
            pause 2.0
            hide monika
            show chibika 3_owawm at h22
            c "Oops, you're still here."
            show chibika 3_owawm at h22
            c "Bye bye"
            hide chibika
            $ mouse_visible = False
            if renpy.windows and renpy.game.preferences.fullscreen:
                scene bsod
                window hide
                pause 2.0
            else:
                show black zorder 100
                window hide
                pause 2.0
            $ mouse_visible = True
            $ play_song(audio.alone_time,loop = True)
            jump OW_first_act_3_visit
        "{i}Follow Monika{/i}":
            call screen OWAWM_residential



#############
#Leaving Area
#############
label OW_go_to_neighborhood:
    show monika 8b_owawm at h11
    m "Do you want to go outside {color=#000}[OW_mc]{/color}'s house [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go outside {color=#000}[OW_mc]{/color}'s house [player]?{fast}"
        "Yes":
            scene bg house with dissolve_scene_full
            pause 2.0
            jump OW_outside_mc_house
        "No":
            call screen OWAWM_residential()

label OW_go_to_school_gate:
    show monika 4a_owawm at h11
    m "Do you want to head to the school gates [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to head to the school gates [player]?{fast}"
        "Yes":
            if (persistent.OW_first_interference == False):
                $ mouse_visible = False
                stop music
                call OW_first_interference
            scene bg school gate with dissolve_scene_full
            pause 2.0
            jump OW_school_gate
        "No":
            call screen OWAWM_residential()