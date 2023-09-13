
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
        show monika 3k_owawm at h11
        m "I see now. This is why I feel slightly different."
        pause 1.0
        m 8v_owawm "[player]... I want to test something..."
        m 8u_owawm "Don't be scared [mas_get_player_nickname()], I'm not going to hurt you."
        call updateconsole("Settings/Privacy/Camera/Webcam","Access Denied")
        window hide
        show monika 8d_owawm at h11
        m 8m_owawm "I had a feeling that wouldn't work. I hope that didn't scare you."
        m 10l_owawm "Sorry, I should have asked you before trying something like that...{w=0.5}I just really wanted to have that slight hope of seeing you..."
        call hideconsole
        show monika 10o_owawm at t11
        window hide
        pause 1.0
        m "How about we check out my world?"
        m 2l_owawm "I wonder if new things were added... or even... corruption because of my deletion in {b}Doki Doki Literature Club{/b}..."
        show monika 5a_owawm at h11
        m "No matter what, we'll see this world together. Is that okay my love? Ehehe~"
        $ persistent.OW_has_seen_outside = True

    show monika 1a_owawm at t11
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            jump OW_outside_mc_house_talk
        "Interact":
            jump OW_outside_mc_house_interaction
        "Music":
            call OW_select_music
            jump OW_outside_mc_house
        "Return to [RTMAS]":
            call OW_return_question
            jump OW_outside_mc_house


#####
#Talk
#####
label OW_outside_mc_house_talk:
    $ OW_talk_topics = renpy.random.randint(1,2)
    if OW_talk_topics == 1:
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
    if OW_talk_topics == 2:
        show monika 3p_owawm at t11
        m "Hey [player]..."
        m "Whatever you're doing to add back my world is concerning me a bit."
        m 1l_owawm "I know you're putting a lot of effort into doing this but I'm worried about something else."
        m 4o_owawm "Maybe it's better if I show you."
        m 4q_owawm "Give me a second to search for it."
        window hide
        $ consolehistory = []
        call updateconsole("/OpenWorld/characters/natsuki.chr", "Character found")
        call updateconsole("/OpenWorld/characters/sayori.chr", "Character found")
        call updateconsole("/OpenWorld/characters/yuri.chr", "Character found")
        show monika 1p_owawm
        pause 3.0
        m "I don't know what caused them to come back."
        m 1o_owawm "Maybe because this world is connected to them... {w=0.5}or maybe because of my deletion."
        m "I know you've put a lot of effort by bringing back my world and I don't want to be rude."
        m 2n_owawm "I wouldn't be so concerned but even with my console powers, I cannot delete them again without risking this world being destroyed again."
        call updateconsole("os.remove(\".../characters/sayori.chr\")", "Error")
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.2
        stop sound
        hide screen tear
        show monika 1q_owawm at h11
        m "EEEK!!"
        m "..."
        m 4o_owawm "I wish they would rest in peace..."
        m 10p_owawm "Remember in the [RTMAS] when I said I could feel their presence..."
        m "I feel them more strongly now and I just hope they don't bother us."
        call hideconsole
        m 10l_owawm "I know it sounds a bit mean but "
        extend 10q_owawm "{w=0.4}this is supposed to be {i}our {b}After Story{/b}{/i}."
        m 7l_owawm "Sorry for talking so much "
        extend 10i_owawm "but this is just something I wanted to bring to your attention."
        show monika 5a_owawm at h11
        m "I'm happy about everything else though. Seeing everything and having such an amazing time with my [OW_Gender()]."
        m "It's almost perfect but you have to take the good with the bad right?"
        window hide
        play sound "sfx/giggle.ogg"
        pause 1.5
        jump OW_outside_mc_house
    return

############
#Interaction
############

label OW_outside_mc_house_interaction:
    call screen OWAWM_outside()
    screen OWAWM_outside():
        imagemap:
            ground "bg/house.png"
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
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
            if (persistent.OW_has_seen_residential_glitch == False):
                action Jump("OW_residential_glitch") hover_sound gui.hover_sound
            action Jump("OW_go_to_residential") hover_sound gui.hover_sound
        textbutton ("[OW_natsuki]"):
            style "hkb_button"
            style_prefix "hkb"
            xysize(120,None)
            xpos 0
            ypos 362
            action Jump("OW_monika_house_beta") hover_sound gui.hover_sound

####################
#Residential fakeout
####################

label OW_residential_glitch:
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1r_owawm at h11
    m "EEEK!!"
    m 8s_owawm "This way has the same problem as well..."
    m 4s_owawm "I'm going to check the game files for this as well."
    window hide
    $ consolehistory = []
    call updateconsole("Call Residential","Error")
    m 5c_owawm "Error?... This is different..."
    m "Let me try it again."
    window hide
    call updateconsole("Scene Residential","Error")
    call updateconsole("Teleport Residential","Error")
    call updateconsole("Return Residential","Error")
    m 8s_owawm "I'm not giving up!"
    call updateconsole("Jump Residential","Error")
    m 5b_owawm "GRRR! Stupid console, work!"
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.2
            easeout 0.35 zoom 1.0
            zoom 1.2
            easeout 0.35 zoom 1.0
            zoom 1.2
            easeout 0.35 zoom 1.0
    pause 1.0
    call updateconsole("Jump Residential", "Access Granted")
    show monika 1l_owawm at h11
    m "Ahaha... Guess it just needed a smack for it to work..."
    m 4m_owawm "I should probably be more careful next time."
    m 4e_owawm "I don't want to accidentally break my world again."
    call hideconsole
    m 1a_owawm "Since this way is now open, let's walk down the street."
    m 5a_owawm "Maybe we can even head to the school."
    $ persistent.OW_has_seen_residential_glitch = True
    call screen OWAWM_outside
    return

#################
#Leaving the area
#################

label OW_back_to_mc_kitchen:
    m "Do you want to go back to {color=#000}[OW_mc]{/color}'s kitchen?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go back to {color=#000}[OW_mc]{/color}'s kitchen?{fast}"
        "Yes":
            scene bg kitchen with dissolve_scene_full
            pause 2.0
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
                $ play_song(audio.t2g3,loop = True, fadein = 0)
                jump OW_sayori_scare
            scene bg sayori_bedroom with dissolve_scene_full
            pause 2.0
            jump OW_sayori_room
        "No":
            call screen OWAWM_outside()

label OW_go_to_residential:
    m "Do you want to go down the street?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go down the street?{fast}"
        "Yes":
            scene bg residential_day with dissolve_scene_full
            pause 2.0
            jump OW_residential
        "No":
            call screen OWAWM_outside()


label OW_monika_house_beta:
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    show monika 1r_owawm at h11
    m "EEEK!!"
    m 5c_owawm "That scared me!"
    pause 1.0
    m 10n_owawm "Sorry, I'm guessing that scared you too huh?"
    m 10i_owawm "Let me see if I can fix it with my limited coding skills."
    m 5d_owawm "I'm going to focus on this for a second."
    window hide
    pause 1.0
    $ consolehistory = []
    call updateconsole("Accessing", "Access Denied")
    m 5f_owawm "Access Denied? Let me try it again."
    window hide
    pause 2.0
    call updateconsole("Accessing", "Access Denied")
    show monika 5h_owawm 
    m "Ehehe...{w=1.0}Guess we just have to wait until you add more to my world."
    call hideconsole
    show monika 5a_owawm at h11
    m "I'm not upset or anything. I'm actually quite grateful to know that {nw}"
    extend "something new is being adding to my world."
    m "Let's check other places instead, okay? Ehehe~"
    call screen OWAWM_outside

