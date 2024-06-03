import pyglet

# Define the on_draw function
def on_draw():
    window.clear()

# Create a Pyglet window
window = pyglet.window.Window()

# Set the on_draw function as the event handler for the on_draw event
window.on_draw = on_draw

# Run the Pyglet event loop
pyglet.app.run()
