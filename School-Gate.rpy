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
    menu:
        m "[OW_random_talk()]{fast}"
        "Talk":
            call screen dialog(message="Error: No Talk options have been added", ok_action=Return())
            jump OW_school_gate
        "Interact":
            call screen dialog(message="Error: No Interaction options have been added", ok_action=Return())
            jump OW_school_gate
        "Return to [RTMAS.title()]":
            call OW_Go_Back_To_Classroom


#####
#Talk
#####
label OW_school_gate_talk:
    $ OW_talk_topics = renpy.random.randint(1,2)
    if OW_talk_topics == 1:
        pass
