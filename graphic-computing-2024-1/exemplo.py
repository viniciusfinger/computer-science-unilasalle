import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

P0x = 0
P0y = 0
P1x = 0
P1y = 0
P2x = 0
P2y = 0
P3x = 0
P3y = 0
xDesloc=0.5
yDesloc=-0.5
vRot=0.0
xScale=0.5
yScale=0.5

def iniciaObjeto():
    global P0x,P0y,P1x, P1y, P2x, P2y, P3x, P3y
    P0x = 0.0
    P0y = 0.0    
    P1x = -0.3    # P1 = (0,0.3)
    P1y = 0.0
    P2x = -0.3    # P2 = (-0.2,0)
    P2y = 0.1
    P3x = 0.0     # P3 = (0.2,0)
    P3y = 0.1
      

def iniciaExibicao ():
    glClearColor(1.0, 1.0, 1.0, 1.0) #cor branca de fundo da janela


def desenhaRetangulo ():
    glScalef(1.0,0.5,1.0)
    glBegin (GL_QUADS)
    glVertex2f (P0x,P0y)
    glVertex2f (P1x,P1y)
    glVertex2f (P2x,P2y)
    glVertex2f (P3x,P3y)
    glVertex2f (P0x,P0y)
    glEnd()


def desenhaEixos():
    glBegin(GL_LINES)
    glVertex2f (0.0, -1.0)
    glVertex2f (0.0, 1.0)
    glVertex2f (-1.0, 0.0)
    glVertex2f (1.0, 0.0)
    glEnd()


def desenha():
    global vRot, P1x
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0.0, 0.0, 0.0)
    desenhaEixos()
    glColor3f(1.0, 0.0, 0.0)
    
    glPushMatrix()  #PAREDE DA ESQUERDA
    glTranslatef(-0.4,0.0,0.0)
    desenhaRetangulo()
    glPopMatrix()
    
    glPushMatrix() #PAREDE DA DIREITA
    glTranslatef(0.7,0.0,0.0)
    desenhaRetangulo()
    glPopMatrix()
    glColor3f(0.0, 0.0, 1.0)
    
    glPushMatrix() #PORTA DA DIREITA
    glTranslatef (0.3, 0.1,0.0)   #translacao  em X
    glRotatef (-vRot,0.0, 0.0, 1.0)
    glTranslatef (-0.3, -0.1,0.0) #translacao  em X
    glTranslatef(0.3,0.1,0.0)
    desenhaRetangulo()
    glPopMatrix()

    glPushMatrix() #PORTA DA ESQUERDA*/
    glTranslatef (P1x, 0.1,0.0) #translacao  em X
    glRotatef (vRot,0.0, 0.0, 1.0)
    glTranslatef (-P1x, -0.1,0.0) #translacao  em X
    glTranslatef(0.0,0.1,0.0)
    desenhaRetangulo()
    glPopMatrix()
    glutSwapBuffers()


def teclado (tecla, x, y):
    global vRot
    if tecla == b'R':  #ABRE
        vRot += 1.0
    if tecla == b'r':  #FECHA
        vRot = 0
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Exemplo Transf Geometricas!")
    glutKeyboardFunc(teclado)
    #glutSpecialFunc(teclasEspeciais)
    glutDisplayFunc(desenha)
    iniciaExibicao()
    iniciaObjeto()
    glutMainLoop()


main()