# Character definitions
define narrator = Character("Narrator", color="#ffffff")
define mystery = Character("???", color="#ffffff")
define mc = Character("[mcname]", color="#ffffff")
define end = Character("End", color="#ffffff")
define smc = Character("Shadow Milk Cookie", color="#4b88dd")

# Character sprite definitions
image smc pleased = "characters/smc_pleased.png"
image smc happy = "characters/smc_happy.png"

# Default name
default mcname = "MC"

# Story begins
label start:
    # Introductory scene
    scene black
    window hide
    pause 1.0

    # Ask player for character name
    $ mcname = renpy.input("Enter the name of your character:", length=20)
    if mcname.strip() == "":
        $ mcname = "MC"

    # Transition to bedroom scene
    play music "audio/morningwakeup.mp3" fadein 1.0 volume 0.5
    scene bedroom with fade
    pause 2.0

    window show
    narrator "You weren't particularly an outside person. You always preferred to stay in your room, playing games or reading books until your eyes started watering."
    narrator "It didn’t help that your job was a stay-at-home job. Lately though, you’ve been so BOOOORED that you needed to get outside and get some fresh air."
    mc "But there are so many people I don't recall."
    narrator "TOO BAD! YOU NEED FRESH AIR!"

    stop music
    window hide
    pause 1.0

    # [Choices]
    menu:
        "Stay in bed":
            jump stay_in_bed

        "Go outside":
            jump go_outside

# [Choice] Stay in bed - Sweet Dreams Ending
label stay_in_bed:
    play music "audio/morningwakeup.mp3" fadein 1.0 volume 0.5
    pause 1.0
    mc "Wait what am I doing? Why am I listening to a voice in my head?? Am I going crazy??? Eh ill sleep it off."
    narrator "Maybe today isn't the day for adventure after all."
    # Fade to black
    scene black with fade
    end "Sweet Dreams."
    stop music
    return

# [Choice] Go outside
label go_outside: 
    # Fade to black
    scene black with fade 
    play sound "audio/footsteps.mp3" volume 0.5 
    queue sound "audio/opendoor.mp3" volume 0.5
    pause 6.0 
play music "audio/dreamscape.mp3" fadein 1.0 volume 0.5

# Transition to outside scene
scene outsidefront with fade

narrator "You decided to go outside, finally soaking in that MUCH needed sunlight. Your neighbors almost mistaken you for a ghost."
narrator "How antisocial can one person be... no seriously what is wrong with you."  
mc "That was unnecessary."

play sound "audio/pavementfootsteps.mp3" fadein 1.0 volume 2.0 loop

narrator "You found yourself wandering, getting distracted by your phone instead of focusing on your surroundings. It isn't much of a difference from being inside."
narrator "You didn't notice, but something was wrong… someone was following you… Someone... or rather something... had their eyes on you…"

stop sound

mc "..."
mc "...something's off."

narrator "You then started to notice the lack of people around you and that the area is suddenly empty."
mc "Where is everyone?"

stop music
window hide
pause 1.0

# [Choices]
menu:
    "Go back home":
        jump go_back_home

    "Keep walking":
        jump keep_walking


# [Choice] Stay in bed - Sweet Dreams Ending
label keep_walking:
    # Transition to outsidefrontending scene
    scene outsidefrontending
    play music "audio/lostcause.mp3" fadein 1.0 volume 0.5
    pause 1.0
    narrator " You start walking aimlessly, hoping to get whatever that’s watching off your tail, not realizing that there would be nowhere to go."
    scene black with fade
    end "Lost cause."
    stop music
    return

# [Choice] Go back home
label go_back_home:
    scene outsidefront with Dissolve(1.5)
    play music "audio/dreamscape.mp3" fadein 1.0 volume 0.5
    narrator "Feeling reluctant to continue, you stop your journey and decide to head back home. However, the longer you walk… the more confused you feel."
    
    mc "I swear I should be home by now… what is going on…"
    
    pause 0.5
    # Fade to black
    scene black with fade
    play sound "audio/pavementfootsteps.mp3" volume 0.5 fadein 1.0
    pause 6.0
    # Transition to distortedoutside scene
    scene distortedoutside with Dissolve(2.0)
    mc "Okay now I know I’ve seen this corner before…."
    
    narrator "The paths start to twist and turn, taking you somewhere unrecognizable."
    
    pause 1.0
    scene black with fade
    stop music
    play sound "audio/pavementfootsteps.mp3" volume 0.5 fadein 1.0
    queue sound "audio/bodycollapse.mp3" volume 0.5

    pause 9.0

    mc "It's no use..."
    narrator "The further you went, the darker it became. You start to feel nauseous. Your legs felt heavier, your head swinging, until suddenly you collapsed."

pause 5.0
play sound "audio/circusmusic.mp3" fadein 2.0 volume 2.0 loop
# Transition to circusinterior scene
scene circustentinterior with fade

show smc pleased at center with Dissolve(1.0)

smc "Ladies, gents and everybody in between! Welcome to the show, entry fee, you! Today it seems like we have a lovely new face in the audience."

mc "What."

show smc happy at center

smc "Yes you, what's your name my little spectator, my darling marionette!"

return
