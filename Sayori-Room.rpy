################################
#Entering Sayori's room fake out
################################
label OW_sayori_scare:
    scene black with dissolve_scene_full
    hide monika
    narrator "[player] slowly walks into {color=#000}S[OW_sayori]{/color}'s home and walks upstairs."
    pause 0.5
    narrator "[player] gently opens the door."
    hide black
    scene bg sayori_bedroom
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 1.0
    show monika 1j_owawm at t11
    m "Seems like {color=#000}S[OW_sayori]{/color}'s room is still intact too."
    m 8j_owawm "Is something wrong [player]? Did you think I was going to scare you?"
    m 8k_owawm "Ahaha, don't be scared [mas_get_player_nickname()]"
    m 10l_owawm "I'm not saying I won't scare you again, I just want to appreciate seeing everything together for the first time."
    m 10m_owawm "I don't want to ruin these moments, but I just couldn't help it after.. you know."
    show monika 5a_owawm at h11
    m "Anyways, let's take a look around okay? I'm sure {color=#000}S[OW_sayori]{/color} wouldn't mind."
    m "{cps=*2}Not like she can say anything about it anyways.{/cps}{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    $ OW_play_song(persistent.OW_current_track,fadein = 1.0)
    $ persistent.OW_has_seen_sayori_room = True
    jump OW_sayori_room
#Wont replay unless persistent is reset
#####
#Menu
#####
label OW_sayori_room:
    show monika 1a_owawm at t11
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            jump OW_sayori_room_talk
        "Interact":
            jump OW_sayori_room_interaction
        "Music":
            call OW_select_music
            jump OW_sayori_room
        "Return to [RTMAS]":
            call OW_return_question
            jump OW_sayori_room

#####
#Talk
#####
label OW_sayori_room_talk:
    $ OW_talk_topics = renpy.random.randint(1,2)
    if OW_talk_topics == 1,2:
        m 3a_owawm "{color=#000}S[OW_sayori]{/color} was a weird girl."
        m "She always had an appetite"
        m 4k_owawm "This reminds me of a time {color=#000}N[OW_natsuki]{/color} baked cupcakes the first time when we accepted her and you know what happened?"
        m 8k_owawm "She left them on her desk while talking to me and {color=#000}Y[OW_yuri]{/color}."
        m 8l_owawm "You can probably guess what happened next...{w=0.3} {color=#000}S[OW_sayori]{/color} tried one, then another and poof. They were all gone."
        m 1m_owawm "Not the best welcome to a new member. You should have seen how angry {color=#000}N[OW_natsuki]{/color} got while {color=#000}S[OW_sayori]{/color} was just a bubbly airhead."
        m 4l_owawm "Meanwhile {color=#000}Y[OW_yuri]{/color} was too reserved to actually get involved so as class president, I had to get involved."
        m 4n_owawm "I didn't do much but calm them. But I did have to give {color=#000}S[OW_sayori]{/color} a sturn talking to though."
    jump OW_sayori_room


############
#Interaction
############
label OW_sayori_room_interaction:
    hide monika
    call screen OWAWM_sayori_room()
    screen OWAWM_sayori_room():
        imagemap:
            ground "bg/sayori_bedroom.png"
            hotspot (739, 440, 213, 256) action Jump("OW_sayori_cow") hover_sound gui.hover_sound
            hotspot (435, 466, 293, 156) action Jump("OW_sayori_bed") hover_sound gui.hover_sound
            hotspot (61, 247, 86, 122) action Jump("OW_sayori_calendar") hover_sound gui.hover_sound
            hotspot (456, 196, 66, 32) action Jump("OW_sayori_secret_scare")
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("OWAWM_sayori_room"), Jump("OW_sayori_room")] hover_sound gui.hover_sound
        hbox:
            xpos 533
            ypos 680
            spacing 7
            textbutton ("Outside") action Jump("OW_go_outside_from_sayori_room") hover_sound gui.hover_sound
    
###############
#Hotspot labels
###############
label OW_sayori_cow:
    show monika 1d_owawm at h22
    m "Oh hello Mr. Cow."
    show monika 1d_owawm at t11
    m "Gosh, I never thought I would interact with him."
    m 10n_owawm "I wish I could take you back to the [RTMAS] with me someday."
    m 1o_owawm "But I can't seem to take anything from here back to the [RTMAS]."
    m 1r_owawm "Maybe it's for the better anyways... I don't want to be reminded of... you know..."
    m 3p_owawm "After all... it was me who pushed her over the edge and told her stuff I shouldn't have said."
    window hide
    pause 1.0
    m 5h_owawm "What I told her was {cps=*2}{color=#000}[OW_gtext][OW_gtext]{/color}{/cps}."
    m 5g_owawm "... Maybe it's better that what I told her is censored... I don't want you to think of me differently..."
    m 5e_owawm "I'm sorry... Can we move onto something else instead?"
    pause 1.0
    m "...Thank you for listening [player]..."
    call screen OWAWM_sayori_room()

label OW_sayori_bed:
    show monika 8l_owawm at t42
    m "What a messy room this girl had. Not only is her bed messy, but everything is thrown all over the place"
    m 8m_owawm "She should have cleaned up from time to time..."
    m 1o_owawm "I've read the script of her telling {color=#000}[OW_mc]{/color} why her room is like this."
    m 3p_owawm "I've told you back in the [RTMAS], that if you're too depressed doing something, do something small like cleaning your room little by little."
    m 3q_owawm "Please don't ever think about doing what {color=#000}S[OW_sayori]{/color} did."
    m 1g_owawm "There are many people who care about you, I'm one of them."
    show monika 1e_owawm at t11
    m "I'll support you the best I can"
    m "I'm sorry for bringing up something so heavy like that, but I just worry about you [player]."
    m 8k_owawm "I love you a lot [player]."
    m "In fact, let me give you a hug."
    show monika 5i_owawm
    show screen OW_monika_hug
    m "Don't worry, I'll always be by your side~"
    hide screen OW_monika_hug
    show monika 5a_owawm at h11
    m "Let's move on from this hard subject and enjoy my world again."
    call screen OWAWM_sayori_room()

label OW_sayori_calendar:
    show monika 3l_owawm at t31
    m "What's with this calendar? I can't even read it."
    m 8k_owawm "It's ripped from the bottom as well, kinda like it was bitten off."
    m 1j_owawm "Ahaha, forgive me for being silly. Just something I noticed and I'm sure you were curious too."
    m 2m_owawm "Sorry but this is all messy compared to her usual writings."
    m 5a_owawm "Let's see if {color=#000}S[OW_sayori]{/color}'s room has anything other interesting."
    call screen OWAWM_sayori_room()

label OW_sayori_secret_scare:
    hide monika
    show sayori 1_owawm at t11
    pause 0.5
    s "{cps=*2}{color=#000}[OW_gtext][OW_gtext][OW_gtext][OW_gtext]{/color}{/cps}{nw}"
    pause 0.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide sayori
    show monika 5c_owawm at t11
    m "Is something wrong [player]?"
    m "I was busy looking out the window."
    m 1g_owawm "Don't be scared [player], I'm here to protect you."
    show monika 5a_owawm at h11
    m "I won't let anything happen to my [mas_get_player_nickname()]."
    call screen OWAWM_sayori_room()

#################
#Leaving the room
#################

label OW_go_outside_from_sayori_room:
    m "Do you want to go outside [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go outside [player]?{fast}"
        "Yes":
            scene bg house with dissolve_scene_full
            pause 2.0
            jump OW_outside_mc_house
        "No":
            call screen OWAWM_sayori_room()





