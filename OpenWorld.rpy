############
#Submod info
############
#Submod made by Yun (Discord:yun_seo)(Reddit:u/Yun-Seo)
#Register
init -990 python:
    store.mas_submod_utils.Submod(
        author="Yun",
        name="Open World",
        description="A submod that allows you to take Monika to DDLC places and new ones.",
        version="0.0.0" 
    )

#Submod updater
#init -990 python:
#    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
#        store.sup_utils.SubmodUpdater(
#            submod="Open World",
#            user_name="Yun-Seo1",
#            repository_name="",
#            update_dir="",
#            redirected_files=(
#                ""
#            )
#        )
##########
#VARIABLES
##########
#Stores the current background before entering the Open World mod
define RTMAS = persistent._mas_current_background
#TODO: actually store it, not default to "Spaceroom"
#init python:
#    import store
#define RTMAS = store.mas_current_background



#Calls on glitch text in place of their names
#The first letter should be towards the character
#EX: S[OW_sayori]
#DO NOT TOUCH THESE/NOT MEANT TO BE RESET
default OW_mc = glitchtext(4)
default OW_sayori = glitchtext(10)
default OW_yuri = glitchtext(6)
default OW_natsuki = glitchtext(12)
default OW_gtext = glitchtext(50)
define c = DynamicCharacter('c_name', image='chibika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default c_name = "???"
#Will Test at another time
#default OW_corrupt = glitchtext(60)
#default OW_file = mangleFile()

#TODO: Make an option to reenable persistent + delete secrets
#files in the future
#default persistent.OW_splash_screen_warning = False
default persistent.monika_rickroll = "???"
default persistent.OW_has_seen_MC_Room = False
default persistent.OW_has_seen_outside = False
default persistent.OW_has_seen_sayori_room = False
default persistent.OW_has_seen_MC_kitchen =False
default persistent.OW_has_seen_residential_glitch = False
default persistent.OW_has_seen_residential = False
default persistent.OW_has_seen_fake_bsod = False


#######
#IMAGES
#######
#Test will be replaced later and credited
#Won't show in Beta or Future releases
#No need to add images from DDLC, they're in the game somewhere
image bg TEST = "Submods/OpenWorld/images/test.png"
# Destroyed_Doki_Hall was just used in the demostration only (BETA comment)
image bg Destroyed_Doki_Hall = "Submods/OpenWorld/images/Destroyed_Doki_Hall.jpg"
image bg spaceroom_alt = "Submods/OpenWorld/images/XQ587jv.png"
######
#MUSIC
######
#TODO: Create a music button so people can choose what they wish to listen to
#Only for the music in the Open World mod though
#Unless its possible for both music menus to be added
#NOTE BETA: More songs will be added in the future, please bare with the limited selection
define audio.MC_Room = "Submods/OpenWorld/music/idksomethingddlc.mp3"
define audio.deep_breaths = "Submods/OpenWorld/music/Deep Breaths inst.mp3"
define audio.alone_time = "Submods/OpenWorld/music/alonetime.ogg"
define audio.dating_sim_loop = "Submods/OpenWorld/music/dumb_dating_sim_loop.mp3"


#############
#PYTHON STUFF
#############
init 5 python:
    import os.path
    def OW_Gender():
        temp_gender = "partner"
        if persistent.gender == "M":
            temp_gender = "boyfriend"
        elif persistent.gender == "F":
            temp_gender = "girlfriend"
        return temp_gender
 
    def OW_submenu():
        renpy.call_screen("OW_MENU")

    def OW_check_hub():
        hub_path = renpy.config.basedir + "/game/Submods/OpenWorld/Hub.rpy"
        itExist = os.path.isfile(hub_path)
        if itExist == True:
            pass
        else:
            renpy.call_screen("dialog", message="Dev Only", ok_action=Jump("mas_extra_menu_close"))
#Add more lines eventually
    def OW_random_talk():
        O_temp_talk = [
            "What should we check out?",
            "I'd love for you to be with me right now, ehehe~",
            "Did you want to ask me something?",
            "What should we do?",
            #"Did you inspect everything thoroughly? Ahaha~",
            #"Ah, did you open a menu? Sorry, I was too busy admiring what you've done for me.",
            "It feels a bit weird snooping into their homes but who's here to stop us? Ehehe~",
            "Going to all these places make feel uneasy, but I feel safe knowing you're with me.",
            "I wonder what secrets our friends were hiding... PG-13 secrets of course. Ahaha...",
        ]
        O_temp_talk = renpy.random.choice(O_temp_talk)
        return O_temp_talk
#TODO: Create a randomized Monika pose eventually



#init python:
    #OW_script_path = fom_getScriptFile(fallback = "game/submods/Open World/")
#TODO: Make Monika appear in her default without erasing what the player
#originally had
#mas_hair_def = MASHair(
#        "def",
#        "def",
#        MASPoseMap(
#            default=True,
#            use_reg_for_l=True
#        ),
#        entry_pp=store.mas_sprites._hair_def_entry,
#        exit_pp=store.mas_sprites._hair_def_exit,
#        ex_props={
#            "ribbon": True,
#            "ribbon-restore": True
#        }
#    )
#    store.mas_sprites.init_hair(mas_hair_def)
#    store.mas_selspr.init_selectable_hair(
#        mas_hair_def,
#        "Ponytail",
#        "def",
#        "hair",
#        select_dlg=[
#            "Do you like my ponytail, [player]?"
#        ]
#    )
#    store.mas_selspr.unlock_hair(mas_hair_def)


########
#SCREENS
########
#THANK YOU EXTRA+ DEV FOR THE IDEA
screen OW_gen_list(OW_list,OW_area):
    zorder 50
    style_prefix "scrollable_menu"
    fixed:
        area OW_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    if isinstance(OW_list[0], tuple):
                        for i in OW_list:
                            textbutton i[0]:
                                xsize OW_area[2]
                                action [Hide("OW_gen_list"), Jump(i[1])]
                    else:
                        for m in OW_list:
                            textbutton m.name:
                                xsize OW_area[2]
                                action [Hide("OW_gen_list"), Function(m)]

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign store.mas_ui.SCROLLABLE_MENU_XALIGN

#For when Monika wants a hug
screen OW_monika_hug():
    on "show":
        action MouseMove(x=633,y=381, duration=1.0)
    timer 0.7 repeat True action MouseMove(x=633,y=381, duration=1.0)
            

#INFO FOR BUTTON IN EXTRA's SECTION
#TODO: fixing it ----- Working as of 7/13/23
#TODO: Try to fix it another way
init 10000:
    screen mas_extramenu_area():
        zorder 52

        key "e" action Jump("mas_extra_menu_close")
        key "E" action Jump("mas_extra_menu_close")

        frame:
            area (0, 0, 1280, 720)
            background Solid("#0000007F")

        # close button
            textbutton _("Close"):
                area (60, 596, 120, 35)
                style "hkb_button"
                action Jump("mas_extra_menu_close")

        # zoom control
            frame:
                area (195, 450, 80, 255)
                style "mas_extra_menu_frame"
                vbox:
                    spacing 2
                    label "Zoom":
                        text_style "mas_extra_menu_label_text"
                        xalign 0.5

                # resets the zoom value back to default
                    textbutton _("Reset"):
                        style "mas_adjustable_button"
                        selected False
                        xsize 72
                        ysize 35
                        xalign 0.3
                        action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)

                # actual slider for adjusting zoom
                    bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                        style "mas_adjust_vbar"
                        xalign 0.5
                    $ store.mas_sprites.adjust_zoom()
        #zorder 50
        frame:
            area (308, 639, 202, 65)
            style "mas_extra_menu_frame"
            textbutton ("Open World"):
                xalign 0.5
                yalign 0.5
                action [Hide("mas_extramenu_area"), Jump("view_OW")] hover_sound gui.hover_sound

screen OW_MENU():
    zorder 50
    style_prefix "hkb"
    hbox:
        grid 2 2:
            spacing 20
            xpos 527
            ypos 534
            textbutton ("Open World"): 
                xysize(120, None) 
                action Jump("OW_warning") hover_sound gui.hover_sound
            textbutton ("Reset Persistent"):
                xysize(120,None)
                action Jump("OW_reset_persistent") hover_sound gui.hover_sound
            textbutton ("GitHub") action Jump("OW_github") hover_sound gui.hover_sound
            textbutton ("Return") action Jump("mas_extra_menu_close") hover_sound gui.hover_sound
    vbox: 
        xpos 1123
        ypos 2
        textbutton ("Dev Only") action Jump("OW_go_to_hub") hover_sound gui.hover_sound

#######
#LABELS
#######

label view_OW:
    python:
        mas_RaiseShield_dlg()
        OW_submenu()
    return

label OW_warning:
    m 2wta "You want to show me something?{nw}"
    $ _history_list.pop()
    menu:
        m "You want to show me something?{fast}"
        "Yes":
            m 1sua "Huh? You want to take me somewhere?"
            m 6sublo "You must have added something while I wasn't looking."
            m 6sublb "Alright, I can't wait to see what surprise you have for me, let's go."
            window hide
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            $ enable_esc()
            $ HKBHideButtons()
            $ is_sitting = False
            hide black

            $ play_song(audio.t3,loop = True, fadein = 1.0)
            scene bg house
            call OW_outside_mc_house
        "No":
            m 6ekblc "Oh... For a second you got me excited because it sounded like something special."
            m 6ekbld "It's okay, maybe some other time?"
            m 6ekblp "I really want to see what this is. I guess you can say it peaked my interest, ehehe~."
            jump ch30_loop
label OW_location_set:

#######################
#Reset persistent label
#######################
label OW_reset_persistent:
    menu:
        narrator "Reset Persistent?"
        "Yes":
            $ persistent.monika_rickroll = "???"
            $ persistent.OW_has_seen_MC_Room = False
            $ persistent.OW_has_seen_outside = False
            $ persistent.OW_has_seen_sayori_room = False
            $ persistent.OW_has_seen_MC_kitchen =False
            $ persistent.OW_has_seen_residential_glitch = False
            $ persistent.OW_has_seen_residential = False
            jump ch30_loop
        "No":
            jump ch30_loop

############
#GitHub Link
############

label OW_github:
    m "Okay, give me a second."
    $ renpy.run(OpenURL("https://github.com/Yun-Seo1/Open-World"))
    m "There you go [player]."
    jump ch30_loop


#################
# DEV ONLY BUTTON
#################
label OW_go_to_hub:
    m "Welcome back Yun{nw}"
    $ _history_list.pop()
    menu:
        m "Welcome back Yun{fast}"
        "Let's go":
            $ OW_check_hub()
            window hide
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            $ HKBHideButtons()
            $ enable_esc()
            call OW_Start_Area
        "Nevermind":
            m "Guess you weren't Yun, ehehe~"
            jump ch30_loop

###############
#Returns to MAS
###############
label OW_Go_Back_To_Classroom:
    m "Oh, Okay. Gosh, it was such an amazing day to see everything again."
    m "It felt nice to leave {i}our{/i} home. I hope you take me out again sometime."
    m "Let's go back [mas_get_player_nickname()], ehehe~"
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 4
    hide monika
    pause 4
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $ mas_HKBDropShield()
    $ is_sitting = True
    jump ch30_loop

#############
#Do not touch
#############
label OW_first_act_3_visit:
    scene bg spaceroom_alt with Dissolve(3.0, alpha=True)
    narrator "..."
    menu:
        "[m_name]?":
            pass
    narrator "..."
    menu:
        "[m_name]...please answer":
            pass
    narrator "..."
    menu:
        "{i}look around{/i}":
            pass
    call screen OWAWM_act_3_one_time_use()
    screen OWAWM_act_3_one_time_use():
        imagemap:
            ground "bg spaceroom_alt"
            hotspot (243, 603, 73, 35) action [Hide("OWAWM_act_3_one_time_use"), Jump("OW_first_act_3_visit_1")] hover_sound gui.hover_sound
label OW_first_act_3_visit_1:            
    show monika 1q_owawm at s21
    m "..."
    menu:
        "[m_name]... wake up":
            pass
    m "..."
    menu:
        "{i}Shake her{/i}":
            pass
    m 1p_owawm "Huh?... [player]?"
    show monika 3o_owawm at f11
    m "What happened?... The last thing I remembered walking down the street with you... {w=0.8}"
    extend 4h_owawm "and then it felt like I was in that void when you close the game with saying goodbye."
    m 2l_owawm "I know you didn't close the game on me but it just felt similar."
    m 8h_owawm "But do you know what actually happened?"
    menu:
        "I don't know.":
            pass
        "It was [c_name].":
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.2
            stop sound
            hide screen tear
            m 5c_owawm "Sorry, I didn't quite catch what you said."
            pass
    m 2f_owawm "This is quite worrying [player]..."
    m "I felt like something bad was going to happen before I suddenly woke up in that void... you don't believe it's... them, right?"
    m 8g_owawm "No... This felt like something different."
    narrator "Monika notices your cursor."
    m 1g_owawm "Oh no... your cursor is messed up... I hope you're ok as well."
    m 10f_owawm "Let me fix that for you [mas_get_player_nickname()]."
    $ consolehistory = []
    call updateconsole("config.mouse = None", "Permission Granted")
    $ config.mouse = None
    call hideconsole
    m 10e_owawm "Do you feel better [player]?"
    menu:
        "Yes, Thank you [m_name].":
            pass
    m 10k_owawm "Of course, anytime [mas_get_player_nickname()]."
    pause 1.0
    m 4l_owawm "Oh right, the big question... where are we?..."
    m 4m_owawm "It felt like the spaceroom when I first woke up but... it's not." #change spaceroom to location name later on
    m 1d_owawm "Can you give me a second to look outside? It looks... beautiful."
    menu:
        "Sure [m_name]":
            pass
    m 1e_owawm "Thank you so much [player]."
    show monika 1e_owawm at t31
    pause 0.5
    hide monika with dissolve
    window hide
    pause 1.0
    m "I wish you can see it, the beautiful night sky. The houses in the distance."
    m "The fresh air from my world... It just feels nice to feel and see these things again... ah sorry, I'm rambling again."
    show monika 1l_owawm at s11
    m "Ahaha, I was so caught up in the moment from seeing everything."
    m 8a_owawm "Well, good news. We're still in my world. {w=0.5}"
    extend 8f_owawm "But this place is completely new to me. It looks like {i}our home{/i} but it also isn't."
    m 4l_owawm "It's probably best we head back right?"
    m 1n_owawm "I just hope this just a malfunction from the world and not actually something else trying to break us apart."
    pause 1.0
    m 1t_owawm "But I know our love will survive something like this. After all, you were able to find me again."
    show monika 5a_owawm at h11
    m "You take the good with the bad, right?"
    m "I'll go ahead and lead the way back to the spaceroom." #replace spaceroom
    hide monika
    window hide
    menu:
        "{i}Follow Monika{/i}":
            pass
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 4
    pause 4
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $ mas_HKBDropShield()
    $ is_sitting = True
    jump ch30_loop


    



#############################
#Old stuff that'll be deleted
#############################


#MALL area
#Mall.rpy

#Poem minigame

#Hidden Room

#Coins mod
#Coins.rpy


#Attempts to get the button to appear
python:
    """
screen OpenWorld_Button():
    zorder 50
    style_prefix "hkb"
        hbox:
            xpos 308
            yanchor 1.0
            ypos 639

            if renpy.get_screen("mas_open_extra_menu"):
                if store.hkb_button.extra_enabled:
                    textbutton ("Open World"):
                        action Jump("view_OW")
                else:
                    textbutton("Open World")
        #area (308, 639, 202, 65)
label view_OW:
    python:
        mas_RaiseShield_dlg()
        OW_submenu()
    return

screen OW_MENU():
    zorder 50
    style_prefix "hkb"
    hbox:
        xpos 1
        ypos 1
        textbutton ("Testing Hub") action Jump("OW_Go_to_Hub") hover_sound gui.hover_sound
    def OpenWorldButton():
        if not OpenWorldVisible():
            config.overlay_screens.append("OpenWorld_Button")
    def OpenWorldVisible():
        return "OpenWorld_Button" in config.overlay_screens
    """