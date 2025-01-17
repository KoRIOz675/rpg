from controller.setup import *

while run:
    # Quit game
    for events in event.get():
        if events.type == QUIT:
            run = False

    # Fill interface to clear it
    screen.fill(backgroundColor)

    # Display interface
    display.flip()
    clock.tick(fps)

quit()
