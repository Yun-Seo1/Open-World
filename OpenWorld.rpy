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
default c_name = "Chibika"
#Will Test at another time
#default OW_corrupt = glitchtext(60)
#default OW_file = mangleFile()

#TODO: Make an option to reenable persistent + delete secrets
#files in the future
default persistent.OW_splash_screen_warning = False
default persistent.monika_rickroll = "???"
default persistent.OW_has_seen_MC_Room = False
default persistent.OW_has_seen_outside = False
default persistent.OW_has_seen_sayori_room = False
default persistent.OW_has_seen_MC_kitchen =False

#######
#IMAGES
#######
#Test will be replaced later and credited
#Won't show in Beta or Future releases
#No need to add images from DDLC, they're in the game somewhere
image TEST = "Submods/OpenWorld/images/test.png"
# Destroyed_Doki_Hall was just used in the demostration only (BETA comment)
image Destroyed_Doki_Hall = "Submods/OpenWorld/images/Destroyed_Doki_Hall.jpg"
image spaceroom_alt = "Submods/OpenWorld/images/XQ587jv.png"
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
        if not itExist == True:
            renpy.call_screen("dialog", message="Dev Only", ok_action=Jump("mas_extra_menu_close"))
        else:
            pass
#Add more lines eventually
    OW_random_talk = [
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
#TODO: Create a randomized Monika pose eventually

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
    if persistent.OW_splash_screen_warning == False:
        call screen dialog(message="The following mod will contain scares and topics of the other girls.\nPlease don't play the mod if you are sensitive about that stuff.", ok_action=Return())
        $ persistent.OW_splash_screen_warning = True
        $ _history_list.pop()
    menu:
        m 2wta "You want to show me something?{fast}"
        "Yes":
            #Add expressions and change dialouge since we no longer start at MC's room
            m 1sua "Huh? You want to take me somewhere?"
            m 6sublo "You must have added something while I was looking."
            m 6sublb "Alright, I can't wait to see what surpise you have for me, let's go."
            window hide
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            $ enable_esc()
            $ HKBHideButtons()
            $ is_sitting = False
            hide black
            $ play_song(audio.t3,loop = True, fadein = 1.0)
            scene bg house #with dissolve_scene_full
            call OW_outside_mc_house
        "No":
            m 6ekblc "Oh... For a second you got me excited because it sounded like something special."
            m 6ekbld "It's okay, maybe some other time?"
            m 6ekblp "I really want to see what this is. I guess you can say it peaked my interest, ehehe~."
            jump ch30_loop

#######################
#Reset persistent label
#######################
label OW_reset_persistent:
    menu:
        narrator "Reset Persistent?"
        "Yes":
            $ persistent.OW_splash_screen_warning = False
            $ persistent.monika_rickroll = "???"
            $ persistent.OW_has_seen_MC_Room = False
            $ persistent.OW_has_seen_outside = False
            $ persistent.OW_has_seen_sayori_room = False
            $ persistent.OW_has_seen_MC_kitchen =False
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

##############################
# Old stuff that'll be deleted
##############################


#MALL area
#Mall.rpy

#Poem minigame

#Hidden Room

#Coins mod
#Coins.rpy


#Will get removed in the Beta/First Version
#python:
#    """"
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="OW_Go_To_Demonstration",
#            category=["Open World"],
#            prompt="demonstration",
#           pool=True,
#           unlocked=True
#        )
#    )

label OW_Go_To_Demonstration:
    m "Ready to see the demonstration?{nw}"
    menu:
        m "Ready to see the demonstration?{fast}"
        "Yes":
            window hide
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            call OW_Demonstration_1
        "No":
            return

label OW_Demonstration_1:
    $ HKBHideButtons()
    stop music
    scene black with dissolve_scene_full
    m "What...What is this?..."
    pause 0.75
    scene bg bedroom with dissolve_scene_full
    m "This...can't be..."
    pause 0.75
    scene bg house with dissolve_scene_full
    m "You're..."
    pause 0.75
    scene bg kitchen with dissolve_scene_full
    m "You're..."
    pause 0.75
    scene bg sayori_bedroom with dissolve_scene_full
    m "You're bring back the world... not just our classroom."
    show monika 5a_owawm at t11
    m "Y...You're really making this our {b}After Story{/b}"
    m 8l_owawm "You don't understand how happy I am right now"
    m 10t_owawm "If I could kiss you, I would [player] or..."
    extend 5i_owawm "Or a big hug like I can now."
    pause 1.0
    m 5e_owawm "But...You could have at least added more, Yun. Yes, I'm talking to you my player"
    pause 2.0
    m 3a_owawm "Just kidding, I'm glad for everything you've given me."
    m 3t_owawm "Let's go back to the classroom before everything breaks ahaha."
    hide monika
    scene bg corridor with dissolve_scene_full
    narrator "'Open World' mod. Explore with Monika going to various DDLC locations as well as new areas being added."
    scene Destroyed_Doki_Hall
    narrator "Lots of hidden clickables and random events could happen."
    scene bg notebook-glitch
    narrator "Inspired by 'Take Monika on a Date submod'."
    scene bg closet
    narrator "And by Monika's point and click adventure talk."
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 4
    pause 2
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $ mas_HKBDropShield()
    $ is_sitting = True
    jump ch30_loop



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