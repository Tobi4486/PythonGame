from pyglet.gl import *

##Simple 3 Colored Triangle
class Tri:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [-0.1,0.8,0.0, 1.0,0.75,0.0, 0.0,-0.5,0.0]),
                                                        ('c3B', [100,200,220, 200,100,118, 100,120,244]))

##First Way of Drawing Quads
class Quad:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0,1,2, 2,3,0],
                                                            ('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]),
                                                            ('c3f', [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,0.0,1.0]))

##Second Way of Drawing Quads
class Quad2:
    def __init__(self):
        self.indices = [0,1,2, 2,3,0]
        self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.color = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,0.0,1.0]
        self.vertices = pyglet.graphics.vertex_list_indexed(4, self.indices, ('v3f',self.vertex), ('c3f',self.color))

##Directly Drawing Quads
class Quad3:
    def __init__(self):
        self.indices = [0,1,2, 2,3,0]
        self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.color = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,0.0,1.0]
    def render(self):
        self.vertices = pyglet.graphics.draw_indexed(4, GL_TRIANGLES, self.indices, ('v3f',self.vertex), ('c3f',self.color))

class gameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_minimum_size(400,200)
            glClearColor(0.1,0.1,0.3,1.0)

            self.triangle = Tri()
            self.quad = Quad()
            self.quad3 = Quad3()

    def on_draw(self):
        self.clear()
        ##self.triangle.vertices.draw(GL_TRIANGLES)
        ##self.quad.vertices.draw(GL_TRIANGLES)
        ##self.quad2.vertices.draw(GL_TRIANGLES)
        self.quad3.render()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)


if __name__ == "__main__":
    window = gameWindow(1200,600,"Game Window", resizable = True)
    pyglet.app.run()