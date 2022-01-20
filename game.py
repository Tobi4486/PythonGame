from pyglet.gl import *

class Poly:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [-0.1,0.8,0.0, 1.0,0.75,0.0, 0.0,-0.5,0.0]),
                                                        ('c3B', [100,200,220, 200,100,118, 100,120,244]))

class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_minimum_size(400,200)
            glClearColor(0.1,0.1,0.3,1.0)

            self.triangle = Poly()

    def on_draw(self):
        self.clear()
        self.triangle.vertices.draw(GL_TRIANGLES)

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)


if __name__ == "__main__":
    window = gameWindow(1200,600,"Game Window", resizable = True)
    pyglet.app.run()