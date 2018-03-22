import glfw
from OpenGL.GL import *
import numpy as np

gComposedM = np.identity(3)

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv((T @ np.array([.0, .5, 1.]))[:-1])
    glVertex2fv((T @ np.array([.0, .0, 1.]))[:-1])
    glVertex2fv((T @ np.array([.5, .0, 1.]))[:-1])
    glEnd()


def key_callback(window, key, scancode, action, mods):
    global gComposedM
    M = np.identity(3)

    if action == glfw.PRESS :
        if key==glfw.KEY_Q :
            M = np.array([[1., 0., -.1],
                          [0., 1., 0.],
                          [0., 0., 1.]])
            gComposedM = M@gComposedM
        elif key == glfw.KEY_E :
            M = np.array([[1., 0., .1],
                          [0., 1., 0.],
                          [0., 0., 1.]])
            gComposedM = M@gComposedM

        elif key == glfw.KEY_A:
            M = np.array([[np.cos(np.pi/18), -np.sin(np.pi/18), 0.],
                               [np.sin(np.pi/18),  np.cos(np.pi/18),0.],
                          [0., 0., 1.]])
            gComposedM = gComposedM@M

        elif key == glfw.KEY_D:
            M = np.array([[np.cos(-np.pi / 18), -np.sin(-np.pi / 18), 0.],
                          [np.sin(-np.pi / 18), np.cos(-np.pi / 18), 0.],
                          [0., 0., 1.]])
            gComposedM = gComposedM@M

       
        elif key == glfw.KEY_1:
            gComposedM = np.identity(3)





def main():
    global gComposedM
    if not glfw.init():
        return
    window = glfw.create_window(640,640,"2014004120",
    None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render(gComposedM)
        glfw.swap_buffers(window)
    glfw.terminate()
if __name__ == "__main__":
    main()