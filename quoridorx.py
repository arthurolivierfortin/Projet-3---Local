from quoridor import Quoridor
import turtle
import copy 



class QuoridorX(Quoridor):
    import turtle
    
    def __init__(self, état):
        self.fen = turtle.Screen()
        self.fen.title("Quoridor phase 3")
        self.fen.setup(width=800, height=600)
        self.J1 = turtle.Turtle()
        self.J2 = turtle.Turtle()
        self.M1 = turtle.Turtle()
        self.M1.shape("square")
        self.M1.penup()
        self.M2 = turtle.Turtle()
        self.M2.penup()
        self.état = état
        self.effaceur_J1 = turtle.Turtle()
        self.effaceur_J2 = turtle.Turtle()
        
        
    def graphique():
        #fen = turtle.Screen()
        #fen.title("Quorido phase 3")
        #fen.setup(width=800, height=600)
        alex = turtle.Turtle()
        #création de l'arrière plan noir
        alex.penup()
        alex.speed("fast")
        alex.fillcolor("black")
        alex.begin_fill()
        alex.forward(400)
        alex.left(90)
        alex.forward(300)
        alex.left(90)
        alex.forward(800)
        alex.left(90)
        alex.forward(600)
        alex.left(90)
        alex.forward(800)
        alex.left(90)
        alex.forward(300)
        alex.end_fill()

        #périmètre du jeu
        clair = turtle.Turtle()
        clair.speed("fast")
        clair.shape("circle")
        clair.pencolor("white")
        clair.penup()
        clair.forward(200)
        clair.left(90)
        clair.pendown()
        clair.forward(200)
        clair.left(90)
        clair.forward(400)
        clair.left(90)
        clair.forward(400)
        clair.left(90)
        clair.forward(400)
        clair.left(90)
        clair.forward(200)
        clair.left(90)
        clair.penup()
        clair.forward(200)
        clair.right(90)
        clair.shapesize(0.1)
        

        #point dans le jeu
        clair.stamp()
        nombre_stamp = 1
        while nombre_stamp < 9:
            for i in range(nombre_stamp):
                clair.forward(40)
                clair.stamp()
            clair.right(90)
            for i in range(nombre_stamp):
                clair.forward(40)
                clair.stamp()
            clair.right(90)
           
            nombre_stamp +=1
        for i in range(8):
                clair.forward(40)
                clair.stamp()

        #chiffre de la grille
        #positionnement de Charles
        charles = turtle.Turtle()
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(200)
        charles.right(90)
        charles.forward(220)
        charles.right(90)
        charles.forward(30)
        #chiffre
        #1 
        charles.speed("fastest")       
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.color("black")
        charles.penup()
        charles.forward(20)
        #2
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.forward(1)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.forward(40)
        #3
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.forward(1)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.forward(1)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.left(90)
        charles.forward(20)
        #4
        
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(104)
        charles.penup()
        charles.color("black")
        charles.forward(10)
        charles.right(90)
        charles.pendown()
        charles.color("white")
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.left(90)       
        charles.forward(20)
        
        #5
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(166)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.left(90)
        charles.forward(40)
        charles.left(90)
        charles.forward(5)
        charles.right(90)
        #6
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.right(90)
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(76)
        charles.penup()
        charles.color("black")
        charles.forward(10)
        charles.left(90)
        charles.forward(40)
        #7
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.right(90)
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(76)
        charles.penup()
        charles.color("black")
        charles.forward(15)
        charles.left(90)
        charles.forward(40)
        #8
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.right(90)
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(76)
        charles.penup()
        charles.color("black")
        charles.forward(20)
        charles.left(90)
        charles.forward(40)
        #9
        charles.right(90)
        charles.forward(4.96)
        charles.left(116.47)
        charles.color("white")
        charles.pendown()
        charles.forward(22.34)
        charles.left(180)
        charles.forward(22.34)
        charles.penup()
        charles.color("black")
        charles.right(116.47)
        charles.forward(9.92)
        charles.right(116.47)
        charles.color("white")
        charles.pendown()
        charles.forward(22.34)
        charles.left(180)
        charles.forward(22.34)
        charles.penup()
        charles.color("black")
        charles.right(63.53)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.forward(60)

        
        
        
        
        
        #horizontal
        charles.right(90)
        charles.forward(66)
        charles.left(90)
        #chiffre
        #1 
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(37)
        charles.left(90)
        #2
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(33)
        charles.left(90)
        #3
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.left(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(38)
        charles.left(90)
        #4
        
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(104)
        charles.penup()
        charles.color("black")
        charles.forward(10)
        charles.right(90)
        charles.pendown()
        charles.color("white")
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.left(90)
        charles.penup()
        charles.color("black")
        charles.forward(10)      
        charles.forward(37)
        charles.left(90)
        
        #5
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(166)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(45)
        charles.left(90)
        #6
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.right(90)
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(76)
        charles.penup()
        charles.color("black")
        charles.forward(10)
        charles.forward(45)
        charles.left(90)
        #7
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.right(90)
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(76)
        charles.penup()
        charles.color("black")
        charles.forward(15)
        charles.forward(42)
        charles.left(90)
        #8
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.right(90)
        charles.forward(10)
        charles.right(90)
        charles.right(14)
        charles.color("white")
        charles.pendown()
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.right(152)
        charles.forward(20.5)
        charles.right(180)
        charles.forward(20.5)
        charles.left(76)
        charles.penup()
        charles.color("black")
        charles.forward(20)
        charles.forward(30)
        charles.left(90)
        #9
        charles.right(90)
        charles.forward(4.96)
        charles.left(116.47)
        charles.color("white")
        charles.pendown()
        charles.forward(22.34)
        charles.left(180)
        charles.forward(22.34)
        charles.penup()
        charles.color("black")
        charles.right(116.47)
        charles.forward(9.92)
        charles.right(116.47)
        charles.color("white")
        charles.pendown()
        charles.forward(22.34)
        charles.left(180)
        charles.forward(22.34)
        charles.penup()
        charles.color("black")
        charles.right(63.53)
        charles.forward(5)
        charles.right(90)
        charles.color("white")
        charles.pendown()
        charles.forward(20)
        charles.right(180)
        charles.forward(20)
        charles.penup()
        charles.color("black")
        charles.left(90)
        charles.forward(5)
        charles.forward(50)
    
    def légende_murs_départ():
        Joe = turtle.Turtle()
        Joe.penup()
        Joe.shape('circle')
        Joe.shapesize(0.1)
        Joe.color('black')
        Joe.speed('fastest')
        Joe.pensize(1)


        #positionnement joueur1
        Joe.right(90)
        Joe.forward(250)
        Joe.right(90)
        Joe.forward(300)
        Joe.right(90)

        #Mur
        #M
        Joe.pendown()
        Joe.color('blue')
        Joe.forward(20)
        Joe.right(135)
        Joe.forward(7)
        Joe.left(90)
        Joe.forward(7)
        Joe.right(135)
        Joe.forward(21)
        Joe.penup()
        Joe.color('black')
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        Joe.forward(10)
        Joe.right(180)
        #u
        Joe.pendown()
        Joe.color('blue')
        Joe.forward(9)
        Joe.left(90)
        Joe.forward(7)
        Joe.left(90)
        Joe.forward(9)
        Joe.right(180)
        Joe.forward(10)
        Joe.penup()
        Joe.color('black')
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        #r
        Joe.pendown()
        Joe.color('blue')
        Joe.forward(10)
        Joe.right(90)
        Joe.forward(7)
        Joe.penup()
        Joe.color('black')
        Joe.right(90)
        Joe.forward(10)
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        Joe.forward(2.5)
        Joe.color('blue')
        Joe.stamp()
        Joe.forward(5)
        Joe.stamp()
        Joe.color('black')
        Joe.right(180)
        Joe.forward(7.5)
        Joe.left(90)
        Joe.forward(10)
        Joe.left(90)
        
        #Murs
        for i in range(10):
            Joe.pendown()
            Joe.color('blue')
            Joe.forward(20)
            Joe.right(180)
            Joe.forward(20)
            Joe.penup
            Joe.color('black')
            Joe.left(90)
            Joe.forward(10)
            Joe.left(90)

        #positionnement joueur2
        Joe.left(90)
        Joe.forward(149.071)
        Joe.left(90)
        Joe.forward(25)
        Joe.left(180)

 #Mur
        #M
        Joe.pendown()
        Joe.color('red')
        Joe.forward(20)
        Joe.right(135)
        Joe.forward(7)
        Joe.left(90)
        Joe.forward(7)
        Joe.right(135)
        Joe.forward(21)
        Joe.penup()
        Joe.color('black')
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        Joe.forward(10)
        Joe.right(180)
        #u
        Joe.pendown()
        Joe.color('red')
        Joe.forward(9)
        Joe.left(90)
        Joe.forward(7)
        Joe.left(90)
        Joe.forward(9)
        Joe.right(180)
        Joe.forward(10)
        Joe.penup()
        Joe.color('black')
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        #r
        Joe.pendown()
        Joe.color('red')
        Joe.forward(10)
        Joe.right(90)
        Joe.forward(7)
        Joe.penup()
        Joe.color('black')
        Joe.right(90)
        Joe.forward(10)
        Joe.left(90)
        Joe.forward(5)
        Joe.left(90)
        Joe.forward(2.5)
        Joe.color('red')
        Joe.stamp()
        Joe.forward(5)
        Joe.stamp()
        Joe.color('black')
        Joe.right(180)
        Joe.forward(7.5)
        Joe.left(90)
        Joe.forward(10)
        Joe.left(90)
        
        #Murs
        for i in range(10):
            Joe.pendown()
            Joe.color('red')
            Joe.forward(20)
            Joe.right(180)
            Joe.forward(20)
            Joe.penup
            Joe.color('black')
            Joe.left(90)
            Joe.forward(10)
            Joe.left(90)

   

    def positionnement_joueur(self):
        
        #positionnement effaceurs
        effaceur_J1 = turtle.Turtle()
        effaceur_J2 = turtle.Turtle()
        self.effaceur_J1 = effaceur_J1
        self.effaceur_J2 = effaceur_J2
        self.effaceur_J1.penup()
        self.effaceur_J2.penup()
        self.effaceur_J1.color('black')
        self.effaceur_J2.color('black')
        self.effaceur_J1.shapesize(0.5)
        self.effaceur_J2.shapesize(0.5)
        self.effaceur_J1.pensize(1)
        self.effaceur_J2.pensize(1)
        self.effaceur_J1.goto((-151, -250))
        self.effaceur_J2.goto((-151, -276))
        self.effaceur_J1.left(90)
        self.effaceur_J2.left(90)
        #positionnement m1 et m2
        M1 = turtle.Turtle()
        self.M1 = M1
        M2 = turtle.Turtle()
        self.M2 = M2
        self.M1.penup()
        self.M2.penup()
        self.M1.forward(250)
        self.M1.right(180)
        self.M2.forward(250)
        self.M2.right(180)
        #joueur
        J1 = turtle.Turtle()
        self.J1 = J1
        self.J1.penup()
        self.J1.shape('turtle')
        self.J1.color("blue")
        J2 = turtle.Turtle()
        self.J2 = J2
        self.J2.penup()
        self.J2.shape('turtle')
        self.J2.color("red")
        #positionnement initial
        
        self.J1.right(90)
        self.J1.forward(170)
        self.J1.left(180)
        
        self.J2.left(90)
        self.J2.forward(170)
        self.J2.right(180)
        
    def déplacement_joueur(self, position, état):
        
        delta_x = état["joueurs"][0]["pos"][0] - position[0]
        delta_y = état["joueurs"][0]["pos"][1] - position[1]

        if delta_y != 0:
            if delta_y == -1:
                self.J1.forward(40)
            if delta_y == 1:
                self.J1.right(180)
                self.J1.forward(40)
                self.J1.right(180)

        if delta_x != 0:
            if delta_x == -1:
                self.J1.right(90)
                self.J1.forward(40)
                self.J1.left(90)
                
            if delta_x == 1:
                self.J1.left(90)
                self.J1.forward(40)
                self.J1.right(90)
        
        état = copy.deepcopy(état)
        self.état = état

    def placement_mur(self, position, orientation, état, joueur):
        print(état)
        print("état ligne 846")
        
        if orientation == 'MV':
            self.M1.penup()
            print('???')
            self.M1.forward(250)
            if joueur == 1:
                self.M1.color('blue')
            if joueur == 2:
                self.M1.color('red')
            self.M1.speed('normal')
            
            if position[0] == 5 and position[1] == 5:
                self.M1.forward(20)
                self.M1.left(90)
                self.M1.forward(20)
                self.M1.left(180)

            ### ne pas toucher
            if 1 <= position[0] <= 5:
                print("****")
                déplacement = (5 - int(position[0]))*40
                self.M1.forward(déplacement+20)
                self.M1.right(90)
            
                
            ### ne pas toucher 
            if 9 >= position[0] > 5:
                print("mmmm")
                déplacement = (5 - int(position[0]))*-40
                self.M1.right(180)
                self.M1.forward(déplacement-20)
                self.M1.left(90)

            ### ne pas toucher 
            if 1 <= position[1] <= 5:
                print("&&&&")
                self.M1.right(180)
                déplacement = (5 - int(position[1]))*40
                self.M1.forward(déplacement+20)
                self.M1.left(180)
            ### ne pas toucher
            if 9 >= position[1] > 5:
                print("jjjjj")
                déplacement = (5 - int(position[1]))*-40
                self.M1.forward(déplacement-20)

            
            self.M1.pendown()
            self.M1.forward(80)
            self.M1.penup()
            self.M1.goto((250,0))
            self.M1.color('white')
            self.M1.left(90)
            if joueur == 1:
                état['murs']['verticaux'] += [position]
            
            if joueur == 1:
                self.effaceur_J1.left(90)
                self.effaceur_J1.forward(10)
                self.effaceur_J1.right(90)
                self.effaceur_J1.pendown()
                self.effaceur_J1.forward(20)
                self.effaceur_J1.right(180)
                self.effaceur_J1.forward(20)
                self.effaceur_J1.right(180)
                self.effaceur_J1.penup()
            
            if joueur == 2:
                self.effaceur_J2.left(90)
                self.effaceur_J2.forward(10)
                self.effaceur_J2.right(90)
                self.effaceur_J2.pendown()
                self.effaceur_J2.forward(20)
                self.effaceur_J2.right(180)
                self.effaceur_J2.forward(20)
                self.effaceur_J2.right(180)
                self.effaceur_J2.penup()
        
      



        if orientation == 'MH':
            
            self.M1.penup()
            self.M1.forward(250)
            if joueur == 1:
                self.M1.color('blue')
            if joueur == 2:
                self.M1.color('red')
            self.M1.speed('normal')

            if position[0] == 5 and position[1] == 5:
                self.M1.forward(20)
                self.M1.left(90)
                self.M1.forward(20)
                self.M1.left(180)
            
            ### ne pas toucher
            if 1 <= position[0] <= 5:
                print('****')
                déplacement = (5 - int(position[0]))*40
                self.M1.forward(déplacement+20)
                self.M1.right(90)
              
                
            if 9 >= position[0] > 5:
                print("mmmm")
                déplacement = (5 - int(position[0]))*-40
                self.M1.right(180)
                self.M1.forward(déplacement-20)
                self.M1.left(90)
            
            #### ne pas toucher
            if 1 <= position[1] <= 5:
                print('????')
                self.M1.right(180)
                déplacement = (5 - int(position[1]))*40
                self.M1.forward(déplacement+20)
                self.M1.right(180)
            

            if 9 >= position[1] > 5:
                print("jjjjj")
                déplacement = (5 - int(position[1]))*-40
                self.M1.forward(déplacement-20)
            
            
            self.M1.right(90)
            self.M1.pendown()
            self.M1.forward(80)
            self.M1.penup()
            self.M1.goto((250,0))
            self.M1.color('white')
            self.M1.left(180)
            if joueur == 1:
                état['murs']['horizontaux'] += [position]
            
            if joueur == 1:
                self.effaceur_J1.left(90)
                self.effaceur_J1.forward(10)
                self.effaceur_J1.right(90)
                self.effaceur_J1.pendown()
                self.effaceur_J1.forward(20)
                self.effaceur_J1.right(180)
                self.effaceur_J1.forward(20)
                self.effaceur_J1.right(180)
                self.effaceur_J1.penup()
            
            if joueur == 2:
                self.effaceur_J2.left(90)
                self.effaceur_J2.forward(10)
                self.effaceur_J2.right(90)
                self.effaceur_J2.pendown()
                self.effaceur_J2.forward(20)
                self.effaceur_J2.right(180)
                self.effaceur_J2.forward(20)
                self.effaceur_J2.right(180)
                self.effaceur_J2.penup()
        
        print(état)
        print("état ligne 947")
        état = copy.deepcopy(état)
        self.état = état
    
    def analyser_mouv_bot(self, état):
        print(self.état)
        print('ligne(951)')
        print(état)
        print('ligne(953)')

        if self.état["joueurs"][1]["pos"] != état["joueurs"][1]["pos"]:
            position_J2 = état["joueurs"][1]["pos"]
            QuoridorX.déplacement_joueur2(QuoridorX, position_J2, self.état)

        if self.état["murs"]["verticaux"] != état["murs"]["verticaux"]:
            position_MV = état["murs"]["verticaux"][len(état["murs"]["verticaux"])-1]
            QuoridorX.placement_mur(QuoridorX, position_MV, "MV", état, 2)

        if self.état["murs"]["horizontaux"] != état["murs"]["horizontaux"]:
            position_MH = état["murs"]["horizontaux"][len(état["murs"]["horizontaux"])-1]
            QuoridorX.placement_mur(QuoridorX, position_MH, "MH", état, 2)

    def déplacement_joueur2(self, position, état):
        delta_x = état["joueurs"][1]["pos"][0] - position[0]
        delta_y = état["joueurs"][1]["pos"][1] - position[1]

        if delta_y != 0:
            if delta_y == 1:
                self.J2.forward(40)
            if delta_y == -1:
                self.J2.right(180)
                self.J2.forward(40)
                self.J2.right(180)

        if delta_x != 0:
            if delta_x == 1:
                self.J2.right(90)
                self.J2.forward(40)
                self.J2.left(90)
                
            if delta_x == -1:
                self.J2.left(90)
                self.J2.forward(40)
                self.J2.right(90)

   