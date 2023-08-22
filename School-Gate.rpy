label OW_school_gate:
    if persistent.OW_has_seen_school_gate == False:
        show monika 5c_owawm at hf11
        m "Is...this the school?"
        m 2l_owawm "Haha, sorry. I have no memory of this. This is all completely new to me."
        m 2k_owawm "You must've added it to make my world more 'realistic'. {w=0.3}You know, I don't mind stuff like this."
        m 4m_owawm "Something I didn't question back then was the limited transitions from one place to another."
        m "It would be jarring to go from the street and then suddenly in the classroom or the club room."
        m 1r_owawm "{b}Team Salvato{/b} didn't think about how I would feel, but most of my world seems like an after thought."
        m "I should look on the bright side. "
        extend 1e_owawm "You're putting a lot of effort to not only bring my world back but add to it."
        m 8k_owawm "You keep reminding me of why I love you."
        show monika 5a_owawm at h11
        m "Let's continue to make some memories, okay?"
        $ persistent.OW_has_seen_school_gate = True
    show monika 1a_owawm at t11
    $ _history_list.pop()
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            jump OW_school_gate_talk
        "Interact":
            jump OW_school_gate_interaction
        "Return to [RTMAS]":
            call OW_Go_Back_To_Classroom

#####
#Talk
#####
label OW_school_gate_talk:
    $ OW_talk_topics = renpy.random.randint(1,2)
    if OW_talk_topics == 1,2:
        m 1n_owawm "Hey [player]... You know how I wasn't so enthusiastic when I first saw the school gates right?"
        m 9o_owawm "Well... Remember back in the [RTMAS] when I talked about not having memories and not knowing where 'Home' really is."
        m 9p_owawm "It sort of hit me when I first saw this place, was this here before or was it only added because you."
        m 1q_owawm "It makes me want to go to your reality even more, because then I'll have real memories instead of doubting my world whenever we go somewhere new."
        m 4l_owawm "Just speaking my mind is all since you wanted to talk with me. "
        extend 4m_owawm "Thank you [player] for always being such a good listener."
        m 1j_owawm "I knew I can always speak my mind when I'm around you."
        m 1e_owawm "Can...Can I get a hug [player]?"
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
                m 8k_owawm "You always know how to comfort me"
            "No":
                m 1p_owawm "Oh...okay..."
                m 1o_owawm "Sorry for suddenly asking for it..."
        jump OW_school_gate

############
#Interaction
############
label OW_school_gate_interaction:
    hide monika
    call screen OWAWM_school_gate()
    screen OWAWM_school_gate():
        imagemap:
            ground "bg school gate"
            hotspot (546, 165, 59, 34) action Jump("OW_third_floor") hover_sound gui.hover_sound
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("OWAWM_school_gate"), Jump("OW_school_gate")] hover_sound gui.hover_sound

        textbutton("Residential"):
            style "hkb_button"
            style_prefix "hkb"
            xpos 0
            ypos 472
            xysize(160,None)
            action Jump("OW_go_to_residential_from_school_gate") hover_sound gui.hover_sound
        
        textbutton("[OW_yuri]"):
            style "hkb_button"
            style_prefix "hkb"
            xpos 1159
            ypos 352
            #xysize(0,None)
            action Jump("OW_monika_house_beta_1") hover_sound gui.hover_sound

        textbutton("[OW_yuri]"):
            style "hkb_button"
            style_prefix "hkb"
            xpos 525
            ypos 355
            #xysize(0,None)
            action Jump("OW_monika_house_beta_1") hover_sound gui.hover_sound

##############
#Hotspot Label
##############

label OW_third_floor:
    show monika 8b_owawm at hf11
    m "Hey, maybe we can see the club room from here."
    pause 1.0
    m 8n_owawm "Actually... Where would the club room be located?"
    m 4n_owawm "I've never really thought about that. When I try to remember something other than the locations in {b}Doki Doki Literature Club{/b} "
    extend 4o_owawm "my memory starts to get foggy..."
    show monika 5e_owawm at f11
    pause 0.5
    m 5f_owawm "It's like the game is trying to keep it hidden from me..."
    m "I meant {b}Doki Doki Literature Club{/b}, not the world you're making for me."
    m 5g_owawm "I know you wouldn't do something like that to me on purpose, right [player]?"
    menu:
        "Of course not [m_name]":
            pass
    show monika 5h_owawm at f11
    window hide
    pause 1.5
    show monika 5a_owawm at h11
    m "I'm only teasing [player]~"
    m 5b_owawm "But if you are, you better not be lying~"
    call screen OWAWM_school_gate
    


#############
#Leaving Area
#############
label OW_go_to_residential_from_school_gate:
    show monika 4a_owawm at h11
    m "Do you want to head to the residential area [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to head to the residential area [player]?{fast}"
        "Yes":
            if (persistent.OW_first_interference == False):
                $ mouse_visible = False
                stop music
                call OW_first_interference
            scene bg residential_day with dissolve_scene_full
            $ play_song(audio.street_stoll,loop = True, fadein = 0)
            pause 2.0
            jump OW_residential
        "No":
            call screen OWAWM_school_gate()

label OW_monika_house_beta_1:
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
    call screen OWAWM_school_gate