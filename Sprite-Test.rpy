label OW_Sprite_Test:
    m "Welcome to the sprite test area{nw}"
    menu:
        m "Welcome to the sprite test area. Please pick an option{fast}"
        "Mad expression":
            m 1s_owawm ""
            pause 1.0
            m 2s_owawm ""
            pause 1.0
            m 3s_owawm ""
            pause 1.0
            m 4s_owawm ""
            pause 1.0 
            jump OW_Sprite_Test
        "Confused":
            m 5c_owawm ""
            jump OW_Sprite_Test
        "Wink":
            m 1t_owawm ""
            m 2t_owawm ""
            m 3t_owawm ""
            m 4t_owawm ""
            jump OW_Sprite_Test
        "Crossed arms":
            m 5d_owawm ""
            m 5e_owawm ""
            m 5f_owawm ""
            m 5g_owawm ""
            m 5h_owawm ""
            jump OW_Sprite_Test
        "Testing Menu":
            jump Testing_scroll_menu
            jump OW_Sprite_Test
        "r/place":
            m 5d_owawm "You guys better not give on me!"
            m 5a_owawm "Just kidding, I can't be mad. I'm happy for all of your efforts"
            m 5i_owawm "Come here"
            window hide 
            pause 3.0
            jump OW_Sprite_Test
        "Moving Monika Test":
            show monika 5a_owawm at t41
            pause 1.0
            show monika 5a_owawm at t31
            pause 1.0
            show monika 5a_owawm at t21
            pause 1.0
            show monika 5a_owawm at t42
            pause 1.0
            show monika 5a_owawm at t11
            pause 1.0
            show monika 5a_owawm at t43
            pause 1.0
            show monika 5a_owawm at t22
            pause 1.0
            show monika 5a_owawm at t33
            pause 1.0
            show monika 5a_owawm at t41
            pause 1.0
            jump OW_Sprite_Test
        "Testing hop":
            #Makes Monika hop
            show monika 5c_owawm at hop
            pause 1.0
            show monika 5c_owawm at hop
            pause 1.0
            jump OW_Sprite_Test
        "Test Monika hug":
            show monika 5i_owawm at t11
            show screen OW_monika_hug
            m "Okay, thanks"
            hide screen OW_monika_hug
            jump OW_Sprite_Test
        "Monika glitch 1":
            show monika g1 at t11
            pause 1.0
            hide monika
            show monika 1a_owawm at t11
            jump OW_Sprite_Test
        "Monika glitch 2":
            show monika g2 at t11
            pause 1.0
            hide monika
            show monika 1a_owawm at t11
            jump OW_Sprite_Test
        "Chibika":
            show chibika 1_owawm at t11
            c "Hello"
            pause 1.0
            show chibika 2_owawm at t11
            show chibika at hop
            #show chibika at t21
            c "Goodbye"
            hide chibika
        "Go back":
            jump OW_Start_Area


#    Positions list containing Monika's table positions from leftmost [0] to
#    rightmost [9]. Items are usable with renpy.show(..., at=list[]) call.
#    Positions=[
#        t41 = 0
#        t31 = 1
#        t21 = 2
#        t42 = 3
#        t11 = 4
#        t32 = 5 (unused)
#        t43 = 6
#        t22 = 7
#        t33 = 8
#        t44 = 9
#    ]
#     play sound "sfx/giggle.ogg" Monika giggle
#     play sound "sfx/monikapound.ogg" Screen Pound



label Testing_scroll_menu:
    show monika 5d_owawm at t21
    python:
        testing_menu = [
            ("Testing console call", 'OW_console_test'),
            ("Music Test", 'OW_music_test'),
            ("Sayori Glitch", 'OW_glitched_sayori'),
            ("Sitting Test", 'OW_sitting_test'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Testing", 'OW_text'),
            ("Return", 'OW_Sprite_Test'),
        ]
    call screen OW_gen_list(testing_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA)
    return
label OW_text:
    jump OW_Sprite_Test

label OW_console_test:
    $ consolehistory = []
    call updateconsole("Test", "This is a test")
    m "Seems like the test works"
    call hideconsole
    jump Testing_scroll_menu

label OW_music_test:
    $ play_song(audio.deep_breaths,loop = False)
    narrator "Test"
    $ play_song(audio.alone_time, loop = False)
    narrator "Test"
    jump Testing_scroll_menu

label OW_glitched_sayori:
        hide monika
        show sayori 1_owawm at t11
        pause 1.0
        hide sayori
        jump Testing_scroll_menu

label OW_sitting_test:
    $ temp_clothing
    $ is_sitting = True
    show monika 1eua at ls32 zorder MAS_MONIKA_Z
    pause 1.0
    show monika 1eua at rs32 with dissolve_monika
    pause 1.0
    hide monika
    pause 2.0
    $ is_sitting = False
    show monika 5a_owawm at ls32
    pause 1.0
    jump Testing_scroll_menu