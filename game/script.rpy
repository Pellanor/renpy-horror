# The script of the game goes in this file.

init python:
    import src.TestModule
    from src.SaveTest import SaveTest
    var = "undefined"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    $ e("Your random number is " + str(src.TestModule.get_random_number()) + "!")

    jump saveTest

label saveTest:
    $ e("State of Var is: " + str(var))
    menu:
        "Here's two options"
        "Enpty Constructor":
            jump optionA
        "Bool Constructor":
            jump optionB
        "Add Str to Var":
            jump optionC
        "Test Nesting":
            jump nest
        "Quit":
            jump end

label optionA:
    python:
        var = SaveTest()
    jump saveTest

label optionB:
    python:
        var = SaveTest(True)
    jump saveTest

label optionC:
    python:
        var.add("Monkey")
    jump saveTest

label nest:
    python:
        var.nested("Squirrel")
    jump saveTest

label end:

    # This ends the game.

    return
