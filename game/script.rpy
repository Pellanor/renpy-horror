# The script of the game goes in this file.

image phone = "phone.png"

screen phone_menu:
    tag menu 
    frame:
        xpadding 10
        ypadding 10
        xpos 50
        ypos 100
        background "images/phone.png"

        imagebutton idle "phoneIcon.png" action Jump("phone_menu") xpos 15 ypos 25 

screen contacts_menu:
    tag menu 
    frame:
        xpadding 10
        ypadding 10
        xpos 50
        ypos 100
        background "images/phone.png"

        imagebutton idle "momButton.png" action Jump("mom_convo") xpos 14 ypos 50


# The game starts here.

label start:
    "phone" "..."
    call screen phone_menu


label phone_menu:
    "Player-kun" "Who should I call...?"
 
    call screen contacts_menu

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
