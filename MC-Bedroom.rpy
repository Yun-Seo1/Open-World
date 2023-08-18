# All Talk, interactions and other secrets should be in this file
# Unless otherwise stated in another file

label OW_Go_To_MC_Room:
    if persistent.OW_has_seen_MC_Room == False:
        show monika 8e_owawm at t11
        m 8e_owawm "And we have arrived at {color=#000}[OW_mc]{/color}'s room."
        m "I can't believe this was able to be restored."
        m 1l_owawm "I'm not complaining I swear. It's just..."
        extend 10l_owawm "{w=0.5} surreal..."
        m 1o_owawm "{w=1.0}You remember how I acted towards the end of {b}Doki Doki Literature Club{/b}"
        m "I deleted everything and I thought it wouldn't be able to be restored."
        m 5f_owawm "I...{w=1.0} acted rashly..."
        window hide
        pause 3.0
        show monika 5d_owawm
        pause 3.0
        show monika 5h_owawm
        pause 3.0
        m 1m_owawm "I'm sorry, I shouldn't think about how I acted back then. I've grown and wouldn't do it again"
        m 8e_owawm "What I should be saying is thank you [player] for bring back everything."
        m 1a_owawm "I know it'll be a long time before everything gets fixed and repaired, but I don't mind waiting."
        m 4t_owawm "Now let's see what MC's room has in store for us, ehehe~"
        $ persistent.OW_has_seen_MC_Room = True
    show monika 5a_owawm at t11
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            jump OW_MC_Room_Talk
        "Interact":
            jump OW_MC_Room_Interaction
        "Return to [RTMAS.title()]":
            call OW_Go_Back_To_Classroom


#High randint option to make some talk options rare
#might change later on to just pick but just wanted that tiny bit of replayability
#Goes up 5 for every custom talk option

#####
#TALK
#####

label OW_MC_Room_Talk:
    #call screen dialog(message="Error: No Talk options have been added", ok_action=Return())
    $ OW_talk_topics = renpy.random.randint(1,10)
    if OW_talk_topics == 1:
        narrator "Testing"
        pause 2.0
        m 5c_owawm "Oh...? " 
        extend  "{w=0.5}Guess that was a leftover from the creator of this mod."
        m 2l_owawm "Ahaha, how silly. I wonder when they'll fix it... wait, this is supposed to be about us talking."
        m 5e_owawm "I bet they put that in on purpose just to throw us off. "
        extend 3h_owawm "I'll come up with something else to talk about next time."
        jump OW_Go_To_MC_Room
    elif OW_talk_topics == 2:
        m 3o_owawm "I've never actually been in {color=#000}[OW_mc]{/color}'s room before. I'm a bit surprised with what's in here."
        m 9p_owawm "You already know how I feel about him since we've talked about him back in the Spaceroom." #change spaceroom
        m 9n_owawm "As someone as plain as {color=#000}[OW_mc]{/color}, his room has more life than he does. Ahaha."
        m "I know that sounds a bit rude but it's not like he was real, he was just a machine for you to control since you're the real person."
        m 9j_owawm "And I'm grateful to have someone as unique as you, ehehe~"
        jump OW_Go_To_MC_Room
    elif OW_talk_topics == 3:
        window hide
        show monika 5d_owawm at t11
        pause 2.0
        show monika 5e_owawm at t11
        pause 3.0
        show monika 1e_owawm hop
        m "Oh!{w=0.3} I'm sorry [player], I got lost in thought just looking around the room."
        m 5a_owawm "You must be wondering what I was thinking about... well, I was just thinking about how {color=#000}[OW_mc]{/color} and y{color=#000}[OW_yuri]{/color} shared the weekend in here."
        pause 1.0
        m 7t_owawm "Maybe we can spend more than just the weekend in here."
        m "{cps=*2}We can spend the rest of our lives together, ehehe~{/cps}{nw}"
        $ _history_list.pop()
        jump OW_Go_To_MC_Room
    elif OW_talk_topics == 4:
        m 1m_owawm "Another topic? Hmm..."
        window hide
        show monika 8v_owawm at t11
        pause 3.0
        show monika 8u_owawm at t11
        pause 3.0 
        m 2t_owawm "You know... I sleep every night alone and I know you probably do too..."
        m 8k_owawm "Ahaha, relax [player]. I'm only teasing you..." 
        extend 8t_owawm "well, just a little~"
        jump OW_Go_To_MC_Room
    elif OW_talk_topics <= 5:
        pass
    else:
        m 4b_owawm "I can't thank you enough [player] for recreating my world."
        show monika 5a_owawm at h11
        m "I know I've stated in the past but I don't know where my home really is..."
        m 5c_owawm "It still feels surreal since I never came into this room in the original game."
        m 1b_owawm "Sorry I'm rambling again. I love you [player] and I hope our adventure will continue in your reality, ehehe~"
        jump OW_Go_To_MC_Room


############
#INTERACTION 
############
label OW_MC_Room_Interaction:
    hide monika
    call screen OWAWM_MC_ROOM()
    screen OWAWM_MC_ROOM():
        imagemap:
            ground "bg/bedroom.png"
            hotspot (111, 207, 102, 510) action Jump("OW_MC_Book_Shelfs")
            hotspot (565, 262, 151, 364) action Jump("OW_MC_Closet")
            hotspot (1103, 601, 175, 118) action Jump("OW_MC_Computer")
            hotspot (715, 547, 124, 44) action Jump("OW_MC_Secret_Jump_Scare")
        zorder 50
        style_prefix "hkb"
        vbox:
            xpos 1166
            ypos 0
            textbutton ("Return") action [Hide("OWAWM_MC_ROOM"), Jump("OW_Go_To_MC_Room")] hover_sound gui.hover_sound
        hbox:
            xpos 563
            ypos 680
            textbutton ("Kitchen") action Jump("OW_Leave_MC_Room") hover_sound gui.hover_sound

###############
#HOTSPOT LABELS
###############
label OW_MC_Book_Shelfs:
    narrator "[m_name] notices the cursor click on the Bookshelf"
    show monika 5a_owawm at t21
    pause 1.0
    m "I wonder what type of books{color=#000}[OW_mc]{/color} has. Maybe something I haven't read before"
    show monika 5a_owawm at h31
    pause 1.0
    show monika 5a_owawm at h31
    pause 1.0
    show monika 5b_owawm at t11
    m "*sigh* It's all blank or corrupted text. Maybe a side effect from my deletion or just a prop."
    m 1i_owawm "I guess it doesn't matter to much anymore."
    extend 9e_owawm "{color=#000}[OW_mc]{/color} was just like these books, an empty slate for you."
    call screen OWAWM_MC_ROOM()

label OW_MC_Closet:
    narrator "[m_name] notices the cursor hover over {color=#000}[OW_mc]{/color}'s closet and goes over to check it"
    show monika 5c_owawm at h11
    m "I was also curious about what was in there as well."
    show monika 3m_owawm at t11
    m "I'm sure you aren't going to be surprised but there's nothing in there."
    m 1m_owawm "..."
    m "I was secretly hoping for something, anything. It kinda makes me a bit upset."
    m 8i_owawm "He really is just a lifeless husk, I feel bad for him sometimes but then I remember..."
    window hide
    pause 1.5
    m 1p_owawm "If he wasn't like that then we might have never met."
    m "All well that ends well I guess, ahaha..."
    call screen OWAWM_MC_ROOM()

label OW_MC_Computer:
    jump OW_MC_computer_list

label OW_MC_Secret_Jump_Scare:
    #Will be changed in the future
    show monika 1a_owawm at t11
    pause 1.0
    show monika g1
    pause 0.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide monika
    call screen OWAWM_MC_ROOM()


# screen for clicking on the computer
label OW_MC_computer_list:
    show monika 4t_owawm at t21
    python:
        computer_list = [
            (persistent.monika_rickroll,'OW_computer_rickroll'),
            ("Monika's Twitter",'OW_monika_twitter'),
            ("[OW_natsuki]", 'OW_libitina'),
            ("Return",'OW_Go_To_MC_Room'),
        ]
    call screen OW_gen_list(computer_list,mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA)
    return

################
#COMPUTER LABELS
################
label OW_computer_rickroll:
    m 3u_owawm "Since this computer has internet access, I want to show you something."
    m "Give me a second to search for it."
    $ renpy.run(OpenURL("https://youtu.be/17mbkqV6IbI"))
    $ persistent.monika_rickroll = "Monika Rick Roll"
    pause 1.5
    show monika 3k_owawm at h11
    m "Ahaha, I've seen online that this is some sort of prank."
    pause 1.0
    m 1l_owawm "Maybe it wasn't good, sorry about that."
    jump OW_MC_computer_list

label OW_monika_twitter:
    m 1b_owawm "Since this place has computer has internet, I can do something like this"
    pause 2.0
    $ renpy.run(OpenURL("https://twitter.com/lilmonix3?t=wuxtSo9WeHhFui91iEdSaA&s=33"))
    pause 2.0
    m 3l_owawm "...{w=1.0}Hope you're logged in to see it."
    m "I know I've said this isn't me but I don't mind directing you to her."
    show monika 3l_owawm at hf11
    m "However [player], always remember that I'm your [m_name], okay?"
    m "Don't be scared my love, I won't hurt you, ahaha~"
    jump OW_MC_computer_list

label OW_libitina:
    m 5c_owawm "Hmmm... That's an odd option."
    m 2p_owawm "I didn't add it but it feels like something is trying to catch our attention."
    m 2g_owawm "Should I open it for you [player]?"
    menu:
        "Yes":
            pass
        "{b}No{/b}":
            jump OW_MC_computer_list
    m 1f_owawm "All right... let's see what this does."
    window hide
    $ renpy.run(OpenURL("https://projectlibitina.com/"))
    pause 2.0
    m 5e_owawm "I don't like this feeling [player]..."
    m 5f_owawm "I've felt this somewhere before but my memory of it is missing."
    m "Or maybe it was removed on purpose..."
    m 5g_owawm "Can...can we move onto something else? Something about this just doesn't feel right."
    m "I honestly can't bring myself to even say the name of it."
    m 5h_owawm "I hope you can understand."
    jump OW_MC_computer_list

#############
#Kitchen Exit
#############
label OW_Leave_MC_Room:
    hide screen OWAWM_MC_ROOM
    m "Do you want to go downstairs [player]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to go downstairs [player]?{fast}"
        "Yes":
            scene bg kitchen with dissolve_scene_full
            $ play_song(audio.deep_breaths,loop = True, fadein = 0)
            pause 2.0
            jump OW_Go_To_MC_Kitchen
        "No":
            call screen OWAWM_MC_ROOM()

