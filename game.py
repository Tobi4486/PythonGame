import glfw
from OpenGL.GL import *

if not glfw.init():
    raise Exception("GLFW Could not be initialised, please check your configuration.")

window = glfw.create_window(1280,720,"Game Window", None, None)

glfw.make_context_current(window)
glClearColor(0,0.1,0.1,1)

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]


#Main Loop
while not glfw.window_should_close(window):
    ##You need to poll events, otherwise it will show as not responding.
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)



#Close Window and Free Resources
glfw.terminate()