#I am just copy pasting what i need from regular MAS music selector
#Most of the code is from them, I take no credit

init -1 python in OWmusic:
    import os
    import mutagen.mp3 as muta3
    import mutagen.oggvorbis as mutaogg
    import store

    #MUSICAL CONSTANTS
    #DDLC SONG NAMES
    MAIN_THEME_TITLE = "Doki Doki Literature Club!"
    SAYORI_THEME = "Ohayou Sayori!"
    MAIN_GAME_THEME = "DDLC Main Theme"
    POEM_MINIGAME = "Dreams of Love and Literature"
    # Might add the other versions if asked
    SHARING_POEMS = "Okay, Everyone!"
    SHARING_POEMS_M = "Okay, Everyone! (Monika)"
    SHARING_POEMS_N = "Okay, Everyone! (Natsuki)"
    SHARING_POEMS_Y = "Okay, Everyone! (Yuri)"
    SHARING_POEMS_S = "Okay, Everyone! (Sayori)"
    YURI_NATUSKI_THEME = "Play with Me"
    CAUSING_TROUBLE = "Poem Panic!"
    TROUBLE_RESOLVED = "Daijoubu!"
    EMOTIONAL = "My Feelings"
    CONFESSION = "My Confession"
    JUST_MONIKA = "Just Monika."
    I_STILL_LOVE = "I Still Love You"
    NO_MUSIC = "No Music"

    # DDLC SONG FILEPATHS
    FP_MAIN_THEME_TITLE = "<loop 22.073>bgm/1.ogg"
    FP_SAYORI_THEME = "<loop 4.499>bgm/2.ogg"
    FP_MAIN_GAME_THEME = "<loop 4.618>bgm/3.ogg"
    FP_POEM_MINIGAME = "<loop 19.451>bgm/4.ogg"
    FP_SHARING_POEMS = "<loop 4.444>bgm/5.ogg"
    FP_SHARING_POEMS_M = "<loop 4.444>bgm/5_monika.ogg"
    FP_SHARING_POEMS_N = "<loop 4.444>bgm/5_natsuki.ogg"
    FP_SHARING_POEMS_Y = "<loop 4.444>bgm/5_yuri.ogg"
    FP_SHARING_POEMS_S = "<loop 4.444>bgm/5_sayori.ogg"
    FP_YURI_NATUSKI_THEME = "<loop 10.893>bgm/6.ogg"
    FP_CAUSING_TROUBLE = "<loop 2.291>bgm/7.ogg"
    FP_TROUBLE_RESOLVED = "<loop 9.938>bgm/8.ogg"
    FP_EMOTIONAL = "<loop 3.172>bgm/9.ogg"
    FP_CONFESSION = "<loop 5.861>bgm/10.ogg"
    FP_JUST_MONIKA = "bgm/m1.ogg"
    FP_I_STILL_LOVE = "<loop 6.424>bgm/monika-end.ogg"
    FP_NO_MUSIC = None

    # MOD SONG NAMES
    #ALONE_TIME = "Alone Time"
    DEEP_BREATHS = "Deep Breaths Inst."
    DUMB_DATING = "Dumb Dating Sim"
    IDKSOMETHING = "Idk Something DDLC"
    MAIN_STREET_STROLL = "Main Street Stroll"
    MAIN_STREET_STROLL_MIX = "Main Street Stroll Remix"
    MONIKA_CONFESSION = "Monika's Confession" #Might be removed

    # MOD SONG FILEPATHS
    FP_DEEP_BREATHS = "Submods/OpenWorld/music/Deep Breaths inst.ogg"
    FP_DUMB_DATING = "Submods/OpenWorld/music/dumb_dating_sim_loop.ogg"
    FP_IDKSOMETHING = "Submods/OpenWorld/music/idksomethingddlc.ogg"
    FP_MAIN_STREET_STROLL = "Submods/OpenWorld/music/main_street_stroll.ogg"
    FP_MAIN_STREET_STROLL_MIX = "Submods/OpenWorld/music/main_street_stroll_new_mix.ogg"
    FP_MONIKA_CONFESSION = "Submods/OpenWorld/music/Monikas_confession.ogg"

    def adjustVolume(channel="music",up=True):
        #
        # Adjusts the volume of the given channel by the volume bump value
        #
        # IN:
        #   channel - the channel to adjust volume
        #       (DEFAULT: music)
        #   up - True means increase volume, False means decrease
        #       (DEFAULT: True)
        direct = 1
        if not up:
            direct = -1

        # volume checks
        new_vol = _sanitizeVolume(getUserVolume(channel)+(direct*vol_bump))
        setUserVolume(new_vol, channel)

    def OW_getplayingmusicname():
        ################################
        #Get's current playing song name
        ################################
        
        OW_current_filename = renpy.music.get_playing()

        # Checks for brackets
        if OW_current_filename:
            bracket_endex = OW_current_filename.find(">")

            if bracket_endex >= 0:
                OW_current_filename = OW_current_filename[bracket_endex:]
            
            # goes through music choices to match
            for name,music in OW_music_choices:

                # braket check
                if music: # None check
                    bracket_endex = OWmusic.find(">")

                    if bracket_endex >= 0:
                        check_song = music[bracket_endex:]
                    else:
                        check_song = music
                else:
                    check_song = music

                if OW_current_filename == check_song:
                    return name
        return None

    def initOWmusicchoices():

        ########################
        #Sets music choices list
        ########################
        global OW_music_choices
        global OW_music_pages
        OW_music_choices = list()
        # Creating a tuple to add the music and their filepaths
        # [0] = Title
        # [1] = File Path
        OW_music_choices.append((MAIN_THEME_TITLE,FP_MAIN_THEME_TITLE))
        OW_music_choices.append((SAYORI_THEME,FP_SAYORI_THEME))
        OW_music_choices.append((MAIN_GAME_THEME,FP_MAIN_GAME_THEME))
        OW_music_choices.append((POEM_MINIGAME,FP_POEM_MINIGAME))
        OW_music_choices.append((SHARING_POEMS,FP_SHARING_POEMS))
        OW_music_choices.append((SHARING_POEMS_M,FP_SHARING_POEMS_M))
        OW_music_choices.append((SHARING_POEMS_N,FP_SHARING_POEMS_N))
        OW_music_choices.append((SHARING_POEMS_Y,FP_SHARING_POEMS_Y))
        OW_music_choices.append((SHARING_POEMS_S,FP_SHARING_POEMS_S))
        OW_music_choices.append((YURI_NATUSKI_THEME,FP_YURI_NATUSKI_THEME))
        OW_music_choices.append((CAUSING_TROUBLE,FP_CAUSING_TROUBLE))
        OW_music_choices.append((TROUBLE_RESOLVED,FP_TROUBLE_RESOLVED))
        OW_music_choices.append((EMOTIONAL,FP_EMOTIONAL))
        OW_music_choices.append((CONFESSION,FP_CONFESSION))
        OW_music_choices.append((JUST_MONIKA,FP_JUST_MONIKA))
        OW_music_choices.append((I_STILL_LOVE,FP_I_STILL_LOVE))
        OW_music_choices.append((DEEP_BREATHS,FP_DEEP_BREATHS))
        OW_music_choices.append((DUMB_DATING,FP_DUMB_DATING))
        OW_music_choices.append((IDKSOMETHING,FP_IDKSOMETHING))
        OW_music_choices.append((MAIN_STREET_STROLL,FP_MAIN_STREET_STROLL))
        OW_music_choices.append((MAIN_STREET_STROLL_MIX,FP_MAIN_STREET_STROLL_MIX))
        OW_music_choices.append((MONIKA_CONFESSION,FP_MONIKA_CONFESSION))
        #OW_music_choices.append((NO_MUSIC,FP_NO_MUSIC))
        #OW_music_choices.append((,))

        OW_music_pages = __OWpageinate(OW_music_choices)


    def getVolume(channel):
        """
        Gets the volume of the given audio channel.
        NOTE: gets the real volume, not user-defined slider volume.

        IN:
            channel - audio channel to get volume for (string)

        RETURNS: volume of the audio channel as double/float
        """
        return renpy.audio.audio.get_channel(channel).context.secondary_volume


    def getUserVolume(channel):
        """
        Gets user-defined slider volume of the given channel.
        NOTE: this is indepenent of the actual channel volume.
            Using set_volume will NOT affect this.

        IN:
            channel - audio channel to get volume for (string)

        RETURNS: value of the user slider for the audio channel (double/float)
        """
        return renpy.game.preferences.volumes.get(
            renpy.audio.audio.get_channel(channel).mixer,
            0.0
        )


    def hasMusicMuted():
        """
        Checks if the player has the music channel muted or the 'Mute All' option enabled.

        RETURNS: True if the music channel is muted or the 'Mute All' option is enabled, False otherwise
        """
        return renpy.game.preferences.mute["music"] or getUserVolume("music") == 0.0

    def setUserVolume(value, channel):
        """
        Sets user volume to the given value.
        NOTE: this does a preference edit, so there's no delay options.
        NOTE: this changes mixer volume, so it may affect other channels.

        IN:
            value - value to set volume to. Should be between 0.0 and 1.0.
            channel - channel to set.
        """
        chan = renpy.audio.audio.get_channel(channel)
        if chan.mixer in renpy.game.preferences.volumes:
            renpy.game.preferences.volumes[chan.mixer] = _sanitizeVolume(value)


    def _sanitizeVolume(value):
        """
        Santizes the given value as if it were a volume.
        NOTE: does not check if its a number.

        IN:
            value - value to sanitize

        RETURNS: valid volume value
        """
        if value < 0.0:
            return 0.0
        elif value > 1.0:
            return 1.0
        return value


    def __OWpageinate(music_list):
        ###########################################################
        #music list - list of the music tuples in initOWmusicchoice
        ###########################################################
        
        # Returns number of pages
        # [0]: first page
        # [1]: second page
        # ...
        # [n]: last page
        pages_dict = dict()
        page = 0
        leftovers = music_list
        while len(leftovers) > 0:
            music_page, leftovers = __OWgenpage(leftovers)
            pages_dict[page] = music_page
            page +=1
        
        return pages_dict

    def __OWgenpage(music_list):
        ################
        #Renerates pages
        ################

        # Returns tuple
        # [0]: pages
        # [1]: remaining items
        return (music_list[:PAGE_LIMIT], music_list[PAGE_LIMIT:])

    def _OWgetaudiofile(filepath):
        ######################################################
        #Attempts to get the correct audio, based on extension
        ######################################################

        # Returns tuple in the following format:
        # [0]: Audio object that we want
        # [1]: Correct Extension
        if filepath.endswith(EXT_MP3):
            return (_OWgetMP3(filepath), EXT_MP3)

        elif filepath.endswith(EXT_OGG):
            return (_OWgetOgg(filepath), EXT_OGG)

        # Failure otherwise
        return (None, None)

    def _OWgetdisplayname(_audio_file, _ext, _filename):
        ############################################################################
        #Attemps to get displayname, if failure,  it'll use filename minus extension
        ############################################################################
        
        #In:
        #   _audio_file: audio object
        #   _ext: extension of the audio file
        #   _filename: name of audio file

        #Returns name of the song
        # if fails, returns filename without extension

        display_name = None

        if _audio_file.tags is not None:
            if _ext == EXT_MP3:
                display_name = _OWgetMP3Name(_audio_file)
            
            elif _ext == EXT_OGG:
                display_name = _OWgetOggName(_audio_file)

        #Failure
        if not display_name:
            return _filename[:-(len(_ext))]

        return display_name

    def _OWgetloopdata(_audio_file, _ext):
        ######################################
        #Attempts to get the audio's file name
        ######################################

        #In:
        # _audio_file: audio object
        # _ext: extension of the audio file

        # Returns: loop string or empty if failed

        if _audio_file.tags is None:
            return ""

        if _ext == EXT_MP3:
            #NOTE: Test if I should loop mp3
            return ""
        if _ext == EXT_OGG:
            return _getoggloop(_audio_file, _ext)

        #Failsafe ?
        return ""
        
    def _OWgetMP3(filepath):
        ##############################################################
        #Attempts to retrieve the MP3 object from the given audio path
        ##############################################################

        #In: filepath: full filepath for the mp3 file
        
        # Returns: mutagen.mp3.EasyMP3 object or None if failure

        try:
            return muta3.EasyMP3(filepath)
        except:
            return None
    
    def _OWgetMP3Name(_audio_file):
        ################################################
        #Attempts to get the song's name from the MP3 ID
        ################################################

        #In: _audio_file: audio object

        # Returns: Display name for the song or None if failure

        return _OWgetoggname(_audio_file)

    def _OWgetogg(filepath):
        #########################################################
        #Attempts to get the ogg object from the given audio path
        #########################################################

        #In: filepath: full filepath for the ogg file
        
        # Returns: mutagen.ogg.OggVorbis object or None if failure

        try:
            return mutaogg.OggVorbis(filepath)
        except:
            return None

    def _OWgetoggname(_audio_file):
        ################################################
        #Attempts to get the song's name from the ogg ID
        ################################################

        #In: _audio_file: audio object

        # Returns: Display name for the song or None if failure

        song_names = _audio_file.tags.get(MT_TITLE,[])
        #song_artists = _audio_file.tags.get(MT_ARTIST, [])

        if not song_names:
            #If song name can't be obtained
            return None

        # select the first item by default
        # NOTE: Test if this can be removed
        sel_name = song_names[0]

        # If Artist is recognized, Add it to the Song title
        #NOTE: Not Nessessary for the mod. They're all credited
        #   in credits.txt
        #   Also I don't songs to have long names and go through
        #   the hassel of trying to squeeze them properly
        #   Ehehe~
        #if song_artists:
        #    sel_art = song_artists[0]
        #    return sel_art + "  -  " + sel_name
        
        return sel_name

    def _getoggloop(_audio_file, _ext):
        #############################################
        #Attempts to retreive loop data from Ogg tags
        #############################################

        #In:
        # _audio_file - audio object
        # _ext - audio file extension

        # Return: loop string or " " if no loop

        # First, try OpenWorld tags
        loopstart = _audio_file.tags.get(MT_LSTART,[])
        loopend = _audio_file.tags.get(MT_LEND, [])

        if loopstart or loopend:
            return _getOggLoopOW(loopstart, loopend, _audio_file)

        # if not found, check if this is ogg
        if _ext != EXT_OGG:
            return ""

        # if ogg, we can try RPGMaker sample tags
        loopstart = _audio_file.tags.get(MT_LSSTART, [])
        looplen = _audio_file.tags.get(MT_LSEND, [])

        if loopstart:
            return _getOggLoopRPG(loopstart, looplen, _audio_file)

        return ""

    def _getOggLoopOW(loopstart, loopend, _audio_file):
        ######################################################
        #Attempts to retrieve OW-based loop data from Ogg tags
        ######################################################

        #In:
        # loopstart: list of loopstart tags
        # loopend: list of loopend tags
        # _audio_file: audio object

        # Returns: loop string we could use or "" if no loop

        # Start with float for these values

        try:
            if loopstart:
                loopstart = float(loopstart[0])

            else:
                loopstart = None

            if loopend:
                loopend = float(loopend[0])

            else:
                loopend = None
        
        except:
            # Error, assume invalid
            return ""

        # now we have floats
        # Validate with values

        if loopstart is not None and loopstart < 0:
            loopstart = 0
        
        if loopend is not None and loopend > _audio_file.info.length:
            loopend = None

        #NOTE: should have at least one of these tags by now
        #   we can now build the tag

        _tag_elems = [RPY_START]

        if loopstart is not None:
            _tag_elems.append(RPY_FROM)
            _tag_elems.append(str(loopstart))

        if loopend is not None:
            _tag_elems.appened(RPY_TO)
            _tag_elems.append(str(loopend))

        _tag_elems.append(RPY_END)

        return " ".join(_tag_elems)

    def _getOggLoopRPG(loopstart, looplen, _audio_file):
        ######################################################
        #Attempts to use RPGMaker-based loop data for ogg tags
        ######################################################


        # NOTE: unlike MAS tags, loopstart is Required

        #In:
        # loopstart: list of loopstart tags
        # looplen: list of loop length
        # _audio_file: audio object

        # Returns: loop string or "" if no loop

        try:
            loopstart = int(loopstart[0])

            if looplen:
                looplen = int(looplen[0])
            
            else:
                looplen = None

        except:
            # Error in parsing tags
            return ""

        # they've been turned into ints
        # converting these into seconds

        _sample_rate = float(_audio_file.info.sample_rate)
        loopstart = loopstart / _sample_rate

        if looplen is not None:
            looplen = looplen / _sample_rate
        
        #validations
        if loopstart < 0:
            loopstart = 0
        
        loopend = None
        if looplen is not None:

            # calculating endpoint
            loopend = loopstart + looplen

            if loopend > _audio_file.info.length:
                loopend = None

        # now build the tag

        _tag_elems = [
            RPY_START,
            RPY_FROM,
            str(loopstart)
        ]

        if loopend is not None:
            _tag_elems.append(RPY_TO)
            _tag_elems.append(str(loopend))

        _tag_elems.append(RPY_END)

        return " ".join(_tag_elems)

    def isValidExt(filename):
        ##############################################
        #checks if the files have the proper extension
        ##############################################

        for ext in VALID_EXT:
            if filename.endswith(ext):
                return True
        
        return False

    def cleanGUIText(unclean):
        #######################################################
        #Cleans the given text so its applicable for gui useage
        #######################################################

        # In:
        # unclean - unclean text

        # Returns: cleaned text

        # bad text needing to be removed
        bad_text = ("{","}", "[", "]")

        #NOTE: For bad test, they're replaced with an empty space
        cleaned_text = unclean
        for bt_el in bad_text:
            cleaned_text = cleaned_text.replace(bt_el, "")
        
        return cleaned_text

    def isInMusicListOW(filepath):
        ########################################################################
        #Checks if the song with the given path will be in the music choice list
        ########################################################################

        #In:
        # filepath - filepath of the song to check

        #Return: True if filepath is in OW_music_choice list
        #otherwise, fail

        for name,fpath in OW_music_choices:
            if filepath == fpath:
                return True
        
        return False

    PAGE_LIMIT = 10
    OW_current_track = "<loop 4.618>bgm/3.ogg"
    OW_selected_track = OW_current_track
    menu_open = False
    
    #enabled / disable the music menu
    #NOTE: Not really sure if mine should have this
    enabled = True

    vol_bump = 0.1 #how much to increase volume by

    #contains the music lists
    OW_music_choices = list()
    OW_music_pages = dict()

    EXT_OGG = ".ogg"
    EXT_MP3 = ".mp3"
    VALID_EXT = [
        EXT_MP3,
        EXT_OGG
    ]

    MT_TITLE = "title"
    #MT_ARTIST = "artist"

    #NOTE: default looping, so think of it as a loop start and loop end

    #seconds to start playback
    MT_LSTART = "OWloopstart"

    #seconds to end playback
    MT_LEND = "OWloopend"

    #for RPGMaker support
    #samples to start playback
    MT_LSSTART = "loopstart"

    #length of loop
    MT_LSEND = "looplength"

    #renpy audio tags
    RPY_START = "<"
    RPY_FROM = "loop"
    RPY_TO = "to"
    RPY_END = ">"

    #some post screen init is setting volume to current settings
init 10 python in OWmusic:

    #for muting
    music_volume = getVolume("music")

init 10 python:

    store.OWmusic.initOWmusicchoices()

    #checks if song exists
    if not store.OWmusic.isInMusicListOW(persistent.OW_current_track):
        #not existing song becomes No Music
        persistent.OW_current_track = None

    #sets up start song
    store.OWmusic.OW_current_track = persistent.OW_current_track
    store.OWmusic.OW_selected_track = store.OWmusic.OW_current_track


#################
#MUSIC MENU STUFF
#################

transform animated_music_menu:
    on show:
        xoffset -1500
        easein 1 xoffset 0
    on hide:
        xoffset 0
        easeout 1 xoffset -1500

screen OW_music_menu(music_page, page_num = 0, more_pages = False):
    modal True
    add "menu_particles"
    add "menu_particles"

    $ import store.OWmusic as music

    #logic to ensure Return works
    if music.OW_current_track is None:
        $ return_value = music.NO_MUSIC
    else:
        $ return_value = music.OW_current_track

    zorder 200

    vbox:
        style_prefix "music_menu"
        xpos 431
        ypos 68
        spacing 10
        # wonderful loop so we can dynamically add songs
        for name,song in music_page:
            textbutton _(name) action Return(song)

    #Dynamic previous text
    if page_num > 0:
        textbutton _("<< Prev"):
            xpos 430
            ypos 592
            style "music_menu_prev_button"
            action Return(page_num - 1)

    else:
        textbutton _(""):
            style "music_menu_prev_button"
            xsize 126
            sensitive False
            
    if more_pages:
        textbutton _("Next >>"):
            xpos 789
            ypos 592
            style "music_menu_return_button"
            action Return(page_num + 1)

    textbutton _(music.NO_MUSIC):
        xpos 430
        ypos 642
        style "music_menu_return_button"
        action Return(music.NO_MUSIC)

    textbutton _("Return"):
        xpos 430 
        ypos 682
        style "music_menu_return_button"
        action Return(return_value)


label OW_display_music_menu:
    # set var so we can block multiple music menus
    show menu_logo zorder 100:
        xpos 200
    show music_screen at animated_music_menu
    pause 1.0
    #show menu_logo
    python:
        import store.OWmusic as music
        music.menu_open = True
        music_selected = False
        curr_page = 0
    $ choose = random.randint(1,4)
    if choose == 1:
        show m_sticker at sticker_mid
    elif choose == 2:
        show n_sticker at sticker_mid
    elif choose == 3:
        show y_sticker at sticker_mid
    else:
        show s_sticker at sticker_mid
        
    while not music_selected:

        #setup pages
        $ music_page = music.OW_music_pages.get(curr_page, None)

        if music_page is None:
            #this shouldn't happen, but as a backup
            return music.NO_MUSIC

        #otherwise, continue formatting into *args
        $ next_page = (curr_page + 1) in music.OW_music_pages

        call screen OW_music_menu(music_page, page_num=curr_page, more_pages=next_page)

        #obtaining results
        $ curr_page = _return
        $ music_selected = _return not in music.OW_music_pages
    $ music.menu_open = False
    hide music_screen
    hide menu_logo
    if choose == 1:
        hide m_sticker
    elif choose == 2:
        hide n_sticker
    elif choose == 3:
        hide y_sticker
    else:
        hide s_sticker
    pause 1.0
    return _return

init python:
    import store.OWmusic as music

    def dec_musicvol():
        """
        Decreases the volume of the music channel by the value defined in songs.vol_bump

        ASSUMES:
            persistent.playername
        """
        # sayori cannot make the volume quieter
        music.adjustVolume()

    def inc_musicvol():
        """
        increases the volume of the music channel by the value defined in songs.vol_bump
        """
        music.adjustVolume()

    def mute_music(mute_enabled=True):
        """
        Mutes and unmutes the music channel

        IN:
            mute_enabled - True means we are allowed to mute.
                False means we are not
        """
        curr_volume = music.getUserVolume("music")
        
        music.setUserVolume(music.music_volume, "music")

    def OW_play_song(song, fadein=0.0, loop=True, set_per=False, fadeout=0.0, if_changed=False):
        ############################################
        #Just plays the song + sets the current song
        ############################################

        #In:
        #   music: music to play, if none then stops
        #   fadein: number of seconds to fade into the song
        #   fadeout: number of seconds to fade out the song
        #   set_per: True if we should set persistent track, false otherwise (default: false)
        #   loop: True if the song should loop
        #   if_changed: whether or not to set the song without restarting

        if song is None:
            song = music.FP_NO_MUSIC
            renpy.music.stop(channel="music", fadeout=fadeout)

        else:
            renpy.music.play(
                song,
                channel="music",
                loop=loop,
                synchro_start=True,
                fadein=1.0,
                fadeout=1.0,
                if_changed=if_changed
            )
        music.OW_current_track = song
        music.OW_selected_track = song
        
        if set_per:
            persistent.OW_current_track = song

label OW_select_music:
    python:
        import store.OWmusic as music
        if music.enabled and not music.menu_open:
            OW_selected_track = renpy.call_in_new_context("OW_display_music_menu")
            if OW_selected_track == music.NO_MUSIC:
                OW_selected_track = music.FP_NO_MUSIC
        
        if OW_selected_track != music.OW_current_track:
            OW_play_song(OW_selected_track, set_per=True)

