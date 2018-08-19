# The script of the game goes in this file.

# list of images
image phone = "phone.png"

# list of styles
# text message from player
style windowStyle:
     background "#fff"
     xmaximum 180
     padding (5,5)
     top_margin 10

# text message from other
style windowStyle2:
     background "#000"
     xmaximum 180
     padding (5,5)
     top_margin 10

style windowText is text:
     color "#000"
     size 10

style windowText2 is text:
     color "#fff"
     size 10

# screens
screen phone_menu:
    tag menu 
    frame:
        xpadding 10
        ypadding 10
        xpos 50
        ypos 100
        background "images/phone.png"

        imagebutton idle "phoneIcon.png" action Jump("phone_menu") xpos 15 ypos 25 
        imagebutton idle "textIcon.png" action Jump("message_menu") xpos 75 ypos 25

screen contacts_menu:
    tag menu 
    frame:
        xpadding 10
        ypadding 10
        xpos 50
        ypos 100
        background "images/phone.png"

        imagebutton idle "momButton.png" action Jump("mom_convo") xpos 14 ypos 50

screen message_menu: 
    tag menu 
    frame:
        xpadding 10
        ypadding 10
        xpos 50
        ypos 100
        background "images/phone.png"

        imagebutton idle "momButton.png" action Jump("mom_text") xpos 14 ypos 50

screen message_mom:
    tag menu
    frame:
        area (1,0,280,600)
        xpadding 10
        ypadding 10
        xpos 50
        ypos 100
        background "images/phone.png"

        vbox:
            xpos 15
            ypos 35
            window:
                style "windowStyle"
                text "Hey mom, im testing this out, i'm going to talk a bit" style "windowText"


            window:
                style "windowStyle2"
                text "Good lord, leave me be." style "windowText2"




# message queue
python: 
    message_queue = 0



# The game starts here.

label start:
    "phone" "..."
    call screen phone_menu


label phone_menu:
    "Player-kun" "Who should I call...?"
 
    call screen contacts_menu

label message_menu:
    "Player-kun" "Text menu..."

    call screen message_menu

label mom_text:
    "Player-kun" "Text my mom..."

    call screen message_mom

label mom_convo:
    "Mom" "Hello?"
    "Player-kun" "Mom? It's me, Player-kun."
    "Mom" "...nobody else to call, huh..."
    "Player-kun" "...uh?"
    "Mom" "Look... I'm not here to entertain you, Player-kun. I have a very vital and entertaining life outside of you." 
    "Player-kun" "Mom..."
    "Player-kun" "..."
    "Player-kun" "...she hung up."
    call screen phone_menu
    
  
    return
