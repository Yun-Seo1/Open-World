#Mall area
    
#YUN ONLY
#TESTING AREA
#WILL BE REMOVED IN BETA/FIRST RELEASE

label OW_Start_Area:
    stop music
    hide black
    scene bg TEST
    pause 0.75
    $ is_sitting = False
    show monika 5a_owawm at t11
    m "Testing Hub"
    menu:
        "MC's Room":
            m "Oh! I forgot you don't actually have anything in this world."
            m 8t_owawm "Maybe...{w=0.5} we can change that one day~"
            m "Ahaha... guess you'll just have to use MC's house."
            scene bg bedroom with dissolve_scene_full
            hide TEST
            pause 2.0
            play music audio.MC_Room
            jump OW_Go_To_MC_Room
        "Scare Phazeee ehehe~":
            jump OW_Phazeee
        "Test new Monika sprites":
            jump OW_Sprite_Test
        "MC's Kitchen":
            #call screen dialog(message="Error:Next to be added", ok_action=Return())
            scene bg kitchen with dissolve_scene_full
            jump OW_Go_To_MC_Kitchen
        "MC's Livingroom":
            call screen dialog(message="Error:Might be MC's or Monika's living room",ok_action=Return())
            jump OW_Start_Area
        "Outside":
            scene bg house with dissolve_scene_full
            pause 1.0
            jump OW_outside_mc_house
        "Monika's house":
            call screen dialog(message="Error:Monika's house in progress", ok_action=Return())
            jump OW_Start_Area
        "Monika's bedroom":
            call screen dialog(message="Error:Monika's room in progress", ok_action=Return())
            #call screen dialog(message="Error: No Talk options have been added", ok_action=Return())
            jump OW_Start_Area
        "OW Test Talk":
            show monika 5a_owawm at h11
            m "[OW_random_talk()]"
            jump OW_Start_Area
        "Secret Area 1":
            call screen dialog(message="Error: Secret Area in progress", ok_action=Return())
            jump OW_Start_Area
        "School Gate":
            scene bg school gate with dissolve_scene_full
            show monika 5a_owawm at t11
            pause 2.0
            jump OW_Start_Area
        "Return":
            call OW_Go_Back_To_Classroom
            

#Will Remove or replaced in the Beta/First Release
label OW_Phazeee:
    window hide
    scene bg noise1 with wipeleft_scene
    show monika 1h_owawm at t11
    play music audio.t10y
    pause 2.0
    m 1h_owawm "Discord User Phazeee. We're watching you. Don't think you can steal my [player] plans"
    pause 3.0
    m 3g_owawm "..."
    m "At least listen to [player]'s Monika, okay?"
    pause 4.0
    m 2k_owawm "Ahaha, did I scare you? Sorry if I did. I can be a bit protective of my player sometimes..."
    extend "{w=0.5}And you should know that better than anyone, ehehe~"
    pause 1.5
    jump OW_Start_Area

