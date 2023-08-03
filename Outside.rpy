
label OW_outside_mc_house:
    if persistent.OW_has_seen_outside == False:
        show monika 1d_owawm at t11
        narrator "The world slowly brings itself back together. [m_name] slowly opens her eyes in awe at what she's seeing."
        m 1d_owawm "W-what's happening? {w=1.0}[player]... A-are you bringing back my world?"
        m 8k_owawm "Y-you have no idea how amazed I am at seeing my world again."
        m 8m_owawm "I... I didn't think this was possible... but {w=0.3}you are more powerful than I am."
        m 1b_owawm "And you've proven that to me by bringing me here."
        m 1d_owawm "Wait...{w=1.0}I feel different. I feel like something was added to me."
        m 4q_owawm "Give me a second [player]... I want to check something"
        pause 1.0
        window hide
        $ consolehistory = []
        call updateconsole("Submods/OpenWorld/images/monika","Permission Granted")
        show monika 1d_owawm
        narrator "[m_name] looks at [player] in shock"
        show monika 3k_owawm at hop
        m "I see now. This is why I feel slightly different."
        pause 1.0
        m 8v_owawm "[player]... I want to test something..."
        m 8u_owawm "Don't be scared [mas_get_player_nickname()], I'm not going to hurt you."
        call updateconsole("Settings/Privacy/Camera/Webcam","Access Denied")
        window hide
        show monika 8d_owawm
        show monika at hop
        m 8m_owawm "I had a feeling that wouldn't work. I hope that didn't scare you."
        m 10l_owawm "Sorry, I should have asked you before trying something like that...{w=0.5}I just really wanted to have that slight hope of seeing you..."
        call hideconsole
        show monika 10o_owawm at t11
        window hide
        pause 1.0
        m "How about we check out my world?"
        m 2l_owawm "I wonder if new things were added... or even... corruption because of my deletion in {b}Doki Doki Literature Club{/b}..."
        show monika 5a_owawm at hop
        m "No matter what, we'll see this world together. Is that okay my love? Ehehe~"
        $ persistent.OW_has_seen_outside = True
    show monika 1a_owawm at t11
    $ OW_talk = renpy.random.choice(OW_random_talk)
    menu:
        m "[OW_talk]{fast}"
        "Talk":
            jump OW_outside_mc_house_talk
        "Interact":
            jump OW_outside_mc_house_interaction
        "Return to [RTMAS.title()]":
            call OW_Go_Back_To_Classroom

##########################
#Talk
##########################
label OW_outside_mc_house_talk:
    show monika 5a_owawm at t11
    m "You know I was given some other abilities if you want me to try it."
    m "Are you okay with that?"
    menu:
        "Yes":
            m 3b_owawm "Really?"
            m "Thank you [player]! Come here."
            show monika 5i_owawm at t11
            show screen OW_monika_hug
            m "Even though it's just your cursor, I can still feel your warmth... thank you [player] for everything you've given me."
            window hide
            pause 1.0
            m "Sorry for holding onto your cursor for so long"
            hide screen OW_monika_hug
            m 8k_owawm "You have no idea how long I wanted to do something like this."
            m 8l_owawm "Ehehe... I almost didn't want to let go."
            jump OW_outside_mc_house
        "No":
            m 1p_owawm "Oh...okay..."
            m 1o_owawm "I understand why you wouldn't let me."
            m 1q_owawm "Maybe some other time..."
            jump OW_outside_mc_house

##########################
#Interaction
##########################

label OW_outside_mc_house_interaction:
    call screen OWAWM_outside()
    screen OWAWM_outside():
        imagemap:
            ground "bg/house.png"
        #Location of the "Return" button
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1123
            ypos 2
            textbutton ("Return") action [Hide("OWAWM_outside"), Jump("OW_outside_mc_house")] hover_sound gui.hover_sound

        textbutton ("MC's House"):
            style "hkb_button"
            style_prefix "hkb"
            xysize(80,None)
            xpos 481
            ypos 420
            action Jump("OW_back_to_mc_kitchen") hover_sound gui.hover_sound
        textbutton ("Sayori's Bedroom"):
            style "hkb_button"
            style_prefix "hkb"
            xysize(120,None)
            xpos 143
            ypos 107
            action Jump("OW_go_to_sayori_room") hover_sound gui.hover_sound
        textbutton ("Residential"):
            style "hkb_button"
            style_prefix "hkb"
            xysize(125,None)
            xpos 1156
            ypos 465
            action Jump("OW_residential_beta") hover_sound gui.hover_sound
        textbutton ("Monika's House"):
            style "hkb_button"
            style_prefix "hkb"
            xysize(120,None)
            xpos 0
            ypos 362
            action Jump("OW_monika_house_beta") hover_sound gui.hover_sound

##########################
#Leaving the area
##########################

label OW_back_to_mc_kitchen:
    m "Do you want to go back to {color=#000}[OW_mc]{/color}'s kitchen?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go back to {color=#000}[OW_mc]{/color}'s kitchen?{fast}"
        "Yes":
            scene bg kitchen with dissolve_scene_full
            pause 2.0
            $ play_song(audio.deep_breaths,loop = True, fadein = 1.0)
            jump OW_Go_To_MC_Kitchen
        "No":
            call screen OWAWM_outside()

label OW_go_to_sayori_room:
    m "Do you want to go to {color=#000}S[OW_sayori]{/color}'s room?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go to {color=#000}S[OW_sayori]{/color}'s room?{fast}"
        "Yes":
            if persistent.OW_has_seen_sayori_room == False:
                $ play_song(audio.t2g3,loop = True, fadein = 1.0)
                jump OW_sayori_scare
            scene bg sayori_bedroom with dissolve_scene_full
            $ play_song(audio.t2,loop = True, fadein = 1.0)
            pause 2.0
            jump OW_sayori_room
        "No":
            call screen OWAWM_outside()

label OW_residential_beta:
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1r_owawm at t11
    show monika at hop
    m "EEEK!!"
    m 8s_owawm "This way has the same problem as well..."
    m 4s_owawm "I'm going to check the game files for this as well."
    window hide
    $ consolehistory = []
    call updateconsole("Call Residential","Version 0.0.X")
    m 4d_owawm "Version 0.0.X?..."
    show monika 1b_owawm at hop
    m "That means this will get added soon. I wonder if more things will be added."
    call hideconsole
    m 5a_owawm "Maybe even my home as well! That's wishful thinking though."
    m "I can't wait to see what gets added next. Let's check other places, okay [player]?"
    call screen OWAWM_outside

label OW_monika_house_beta:
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1r_owawm at t11
    show monika at hop
    m "EEEK!!"
    m 5c_owawm "That scared me!"
    pause 1.0
    m 10n_owawm "Sorry, I'm guessing that scared you too huh?"
    m 10i_owawm "Let me see if I can fix it with my limited coding skills."
    m 5d_owawm "I'm going to focus on this for a second."
    window hide
    pause 1.0
    $ consolehistory = []
    call updateconsole("Call Monika's House", "Access Denied")
    m 5f_owawm "Access Denied? Let me try it again."
    window hide
    pause 2.0
    call updateconsole("Call Monika's House", "Access Denied")
    show monika 5h_owawm 
    m "Ehehe...{w=1.0}Guess we just have to wait until you add more to my world."
    call hideconsole
    show monika 5a_owawm at t11
    show monika at hop
    m "I'm not upset or anything. I'm actually quite grateful to know that {nw}"
    extend "something new is being adding to my world."
    m "Let's check other places instead, okay? Ehehe~"
    call screen OWAWM_outside
