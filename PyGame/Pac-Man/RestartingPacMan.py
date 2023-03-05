# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:40:02 2022

@author: mrbar
"""

import pygame
import time
import random
import pickle
import os

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pac-Man")

# Sets the size of the screen via (WIDTH, HEIGHT)
SCREEN_WIDTH = 478
SCREEN_HEIGHT = 608
# Speed of Characters
SPEED = 1
# Frames per second, how fast the game runs
FPS = 50
# Colors (RED, GREEN, BLUE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PEACH = (255, 218, 185)

# Sets the WIDTH and HEIGHT of the window
WINDOW = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Displays the screen
SCREEN = pygame.display.set_mode(WINDOW)
CLOCK = pygame.time.Clock()

BackgroundSurface = pygame.image.load(
                    os.path.join("Background", "Background.png")).convert()

pygame.mixer.music.load(os.path.join("Sound Effects", "power_pellet.wav"))

Font = pygame.font.Font("emulogic.ttf", 15)

class Maze():
    def __init__(self):
        self.Pellets = []
        self.Walls = []
        self.Energizer = []
        self.Ghosts = []
        self.BlockWidth = 25
        self.BlockHeight = 25
        self.MazeOffsetX = 0
        self.MazeOffsetY = 50
        # 0 - Pellets
        # 1 - Walls
        # 2 - Empty Spaces
        # 3 - Energizers
        # 4 - Ghosts
        self.Matrix = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], \
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], \
                      [1,3,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,3,1], \
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], \
                      [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1], \
                      [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1], \
                      [1,1,1,1,0,1,1,1,2,1,2,1,1,1,0,1,1,1,1], \
                      [2,2,2,1,0,1,2,2,2,4,2,2,2,1,0,1,2,2,2], \
                      [1,1,1,1,0,1,2,1,1,1,1,1,2,1,0,1,1,1,1], \
                      [2,2,2,2,0,2,2,1,4,4,4,1,2,2,0,2,2,2,2], \
                      [1,1,1,1,0,1,2,1,1,1,1,1,2,1,0,1,1,1,1], \
                      [2,2,2,1,0,1,2,2,2,2,2,2,2,1,0,1,2,2,2], \
                      [1,1,1,1,0,1,2,1,1,1,1,1,2,1,0,1,1,1,1], \
                      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], \
                      [1,3,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,3,1], \
                      [1,0,0,1,0,0,0,0,0,2,0,0,0,0,0,1,0,0,1], \
                      [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1], \
                      [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1], \
                      [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1], \
                      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], \
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                   
        # BackgroundImage(X, Y, WIDTH, HEIGHT)
        self.MazeX = self.BlockWidth * (len(self.Matrix[0]) 
                      + self.MazeOffsetX)
        self.MazeY = self.BlockHeight * (len(self.Matrix)
                      + self.MazeOffsetY)
        self.MazeWidth = self.BlockWidth * len(self.Matrix[0])
        self.MazeHeight = self.BlockHeight * len(self.Matrix) 

    def DrawMaze(self, MazeSurface):
        for Row in range(len(self.Matrix)):
            for Column in range(len(self.Matrix[0])):
                # Saves the position of each pellet
                if self.Matrix[Row][Column] == 0:
                    self.Pellets.append([(Row, Column), 
                                         (self.BlockWidth * Column,
                                          self.BlockHeight * Row, 4, 4)])
                    if self.Matrix[Row][Column - 1] != 1 and \
                       self.Matrix[Row][Column - 1] != 2:
                        self.Pellets.append([(Row, Column), 
                                             (((self.BlockWidth * Column) - 13),
                                                self.BlockHeight * Row , 4, 4)])
                    if Column + 1 == None and Row - 1 == None:
                        if self.Matrix[Row][Column + 1] != 1 and \
                           self.Matrix[Row][Column + 1] != 2:
                            self.Pellets.append([(Row, Column), 
                                                 (((self.BlockWidth * Column) + 13),
                                                    self.BlockHeight * Row, 4, 4)])
                        if self.Matrix[Row - 1][Column] != 1 and \
                           self.Matrix[Row - 1][Column] != 2:
                            self.Pellets.append([(Row, Column), 
                                                 (self.BlockWidth * Column,
                                                 ((self.BlockHeight * Row) - 13),
                                                 4, 4)])
                    if self.Matrix[Row + 1][Column] != 1 and \
                       self.Matrix[Row + 1][Column] != 2:
                        self.Pellets.append([(Row, Column), 
                                             (self.BlockWidth * Column,
                                             ((self.BlockHeight * Row) + 13), 
                                               4, 4)])
                # Saves the position of each wall
                if self.Matrix[Row][Column] == 1:
                    self.Walls.append(pygame.draw.rect(MazeSurface, WHITE,
                                     [((self.BlockWidth) * Column),
                                      ((self.BlockHeight) * Row), 
                                        self.BlockWidth, self.BlockHeight]))
                # Saves the position of each Energizer
                if self.Matrix[Row][Column] == 3:
                    self.Energizer.append([(Row, Column), 
                                           ((self.BlockWidth * Column),
                                            (self.BlockHeight * Row), 14, 14)])
                # Saves the position of each Ghost
                if self.Matrix[Row][Column] == 4:
                    self.Ghosts.append([(self.BlockWidth * Column), 
                                        (self.BlockHeight * Row), 23, 23])

class ShortestPath(Maze):
    """
    This algorithm is used to locate the original position of a ghost
    that has been ate. It grabs the current position and checks its
    surrounding neighbors to find the shortest neighbor and adds it to
    the dictionary.
    """
    def __init__(self):
        Maze.__init__(self)
        self.D = {}
        self.Queue = []
        self.Target = set()
        self.Path = []
        
    def FindShortestPath(self):
        while len(self.Queue) > 0:
            # Taking out the first coordinate in Queue
            i, j = self.Queue.pop(0)
            Previous = (i, j)
            ShortestDistance = self.D[(i, j)]["Shortest Distance"]
            # Searching neighbors - UP, DOWN, LEFT, RIGHT
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                # (ni, nj) are the new coordinate 
                ni, nj = i + dx, j + dy
                # Ignore (ni, nj) if it's out of bounds
                if ni < 0 or nj < 0:
                    continue
                # Ignore (ni, nj) if it's out of bounds
                if ni >= len(self.Matrix) or nj >= len(self.Matrix[0]):
                    continue
                # Ignore (ni, nj) if it's a Wall
                if self.Matrix[ni][nj] == 1:
                    continue
                # If (ni, nj) is not inside self.D, add it to self.D
                # then add (ni,nj) back to Queue so we can search it later
                if (ni, nj) not in self.D:
                    self.D[(ni, nj)] = {
                                         "Shortest Distance": ShortestDistance + 1, 
                                         "Previous": Previous
                                       }
                    self.Queue.append((ni, nj))
                # If (ni,nj) is already inside self.D, 
                # check if the new "Shortest Distance" is shorter than the orignal
                # and update the original only if the new shorter distance 
                # is in fact shorter
                else:
                    OriginalShortestDistance = self.D[(ni, nj)]["Shortest Distance"]
                    if ShortestDistance + 1 < OriginalShortestDistance:
                        self.D[(ni, nj)] = {
                                            "Shortest Distance": ShortestDistance + 1, 
                                            "Previous": Previous
                                           }
                # If coordinate is equal to target coordinate
                # we add it to target
                if self.Matrix[ni][nj] == 4:
                    self.Target.add((ni, nj))
        # At this point, Queue is empty and we have searched all possible 
        # points inside self.Matrix
        Out = {}
        # Constructing shortest paths based on self.D
        for Target in self.Target:
            Path = []
            Current = Target
            while Current != None:
                Path.append(Current)
                Current = self.D[Current]["Previous"]
            Out[Target] = Path[::-1]
        NestedList = list(Out.values())
        ListOfCoordinates = [Coordinate for Sublist in NestedList for Coordinate in Sublist]
        self.GetPath = False
        return ListOfCoordinates
        
class PacMan(ShortestPath):
    def __init__(self):
        ShortestPath.__init__(self)
        self.PacManStartSurface = pygame.transform.scale(
                                  pygame.image.load(
                                  os.path.join("Pac Man", "PacManStart.png"))
                                  .convert_alpha(), (25, 25))
        self.PacManStartRect = pygame.Rect((225, 375, 23, 23))
        self.PacManSurface = pygame.transform.scale(
                             pygame.image.load(
                             os.path.join("Pac Man", "PacManRight1.png"))
                             .convert_alpha(), (25, 25))
        self.PacManRect = pygame.Rect((225, 375, 23, 23))
        self.PacManSurface1 = pygame.transform.scale(
                              pygame.image.load(
                              os.path.join("Pac Man", "PacManRight2.png"))
                              .convert_alpha(), (25, 25))
        self.PacManRect1 = pygame.Rect((225, 375, 23, 23))
        self.CurrentSurface = self.PacManStartSurface
        self.CurrentRect = self.PacManStartRect
        self.Move = False
        self.Switch = False
        self.Stop = False
        self.Continue = True
        self.PacManDirection = ""
        self.LastDirection = self.PacManDirection
        self.PacManDecision = []
        self.LastBiteTime = time.time()
        self.TimeBetweenBites = 0.1
        self.Lives = 3
        self.Image = 0
        
    def PacManPosToMazePos(self):
        # Ex: self.CurrentRect.x = 225
        #     self.CurrentRect.y = 176
        #     MazeX = 225 // 25 = 9
        #     MazeY = 176 // 25 = 15
        MazeX = self.CurrentRect.x // self.BlockWidth
        MazeY = self.CurrentRect.y // self.BlockHeight
        return (MazeX, MazeY)
                
    def PacManMovement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.PacManDirection = "LEFT"
        if key[pygame.K_RIGHT]:
            self.PacManDirection = "RIGHT"
        if key[pygame.K_UP]:
            self.PacManDirection = "UP"
        if key[pygame.K_DOWN]:
            self.PacManDirection = "DOWN"
            
    def PacManTeleport(self):
        if self.CurrentRect.x < -30 and self.PacManDirection == "LEFT":
            self.CurrentRect.x = 500
        if self.CurrentRect.x > 485 and self.PacManDirection == "RIGHT":
            self.CurrentRect.x = -30
            
    def GetAvailablePacManMoves(self):
        MazeX, MazeY = self.PacManPosToMazePos()
        if MazeX == 18 or MazeX == 19:
            MazeX -= 2
        if self.Matrix[MazeY][MazeX - 1] != 1:
            self.PacManDecision.append("LEFT")
        if self.Matrix[MazeY][MazeX + 1] != 1:
            self.PacManDecision.append("RIGHT")
        if self.Matrix[MazeY - 1][MazeX] != 1:
            self.PacManDecision.append("UP")
        if self.Matrix[MazeY + 1][MazeX] != 1:
            self.PacManDecision.append("DOWN")
        return self.PacManDecision
    
    def Intersection(self, PacManDecision):
        PacMan.PacManTeleport(self)
        if self.PacManDirection == "LEFT":
            self.CurrentRect.move(-SPEED, 0)
            self.PacManWallDetection(-1, 0)
        if self.PacManDirection == "RIGHT":
            self.CurrentRect.move(SPEED, 0)
            self.PacManWallDetection(1, 0)
        if self.PacManDirection == "UP":
            self.CurrentRect.move(0, -SPEED)
            self.PacManWallDetection(0, -1)
        if self.PacManDirection == "DOWN":
            self.CurrentRect.move(0, SPEED)
            self.PacManWallDetection(0, 1)
    
    def StopPacManMovement(self, PacManDecision):
        if len(self.PacManDecision) > 2:
            self.PacManDirection = "STOP"
        PacMan.PacManMovement(self)

    def ContinuePacManMovement(self):
        if self.PacManDirection in ['LEFT', 'RIGHT'] and self.CurrentRect.x % 25 == 0:
            self.Continue = True
            if self.Continue == True:
                self.PacManDecision = self.GetAvailablePacManMoves()
                PacMan.StopPacManMovement(self, self.PacManDecision)
                if self.PacManDirection in self.PacManDecision:
                    PacMan.Intersection(self, self.PacManDecision)
        if self.PacManDirection in ['UP', 'DOWN'] and self.CurrentRect.y % 25 == 0:
            self.Continue = True
            if self.Continue == True:
                self.PacManDecision = self.GetAvailablePacManMoves()
                PacMan.StopPacManMovement(self, self.PacManDecision)
                if self.PacManDirection in self.PacManDecision:
                    PacMan.Intersection(self, self.PacManDecision)
        self.PacManDecision.clear()
        if self.CurrentRect.x % 25 != 0 or self.CurrentRect.y % 25 != 0:
            self.Continue = False
        if self.Continue == False:
            PacMan.Intersection(self, self.PacManDecision)
            
    def PacManWallDetection(self, x, y):
        if y == 0:
            self.CurrentRect.right += x
            for Wall in self.Walls:
                Collide = self.CurrentRect.colliderect(Wall)
                if Collide:
                    if x < 0: 
                        self.CurrentRect.left = Wall.right
                    if x > 0:
                        self.CurrentRect.right = Wall.left
                    break
            
        if x == 0:
            self.CurrentRect.top += y
            for Wall in self.Walls:
                Collide = self.CurrentRect.colliderect(Wall)
                if Collide:
                    if y < 0:
                        self.CurrentRect.top = Wall.bottom
                    if y > 0:
                        self.CurrentRect.bottom = Wall.top
                    break
            
    def EatPellets(self):
        for Pellet in self.Pellets:
            if Pellet[1][0] < self.CurrentRect.x + Pellet[1][2] and \
               Pellet[1][0] + self.CurrentRect.width > self.CurrentRect.x and \
               Pellet[1][1] < self.CurrentRect.y + Pellet[1][3] and \
               self.CurrentRect.height + Pellet[1][1] > self.CurrentRect.y:
                Chomp = self.CurrentRect.colliderect(Pellet[1])
                if Chomp:
                    Main.PlaySound(0)
                    self.Pellets.remove(Pellet)
                    self.Matrix[Pellet[0][0]][Pellet[0][1]] = 2
                    self.Score += 10
        if self.Score > self.HighScore:
            self.HighScore = self.Score
        return str(self.Score), str(self.HighScore)
    
    def EatEnergizer(self):
        for Energizer in self.Energizer:
            EnergizerPoint = pygame.Rect(Energizer[1])
            Chomp = self.CurrentRect.collidepoint(EnergizerPoint.center)
            if Chomp:
                self.Energizer.remove(Energizer)
                PinkGhost.FrightenedMode(self)
                self.Score += 50
                Main.PlaySound(1)
        if self.Score > self.HighScore:
            self.HighScore = self.Score
        return str(self.Score), str(self.HighScore)
    
    def EatGhosts(self):
        if self.CurrentRect.collidepoint(self.CurrentGhostRect.center): 
            print("PacMan center", self.CurrentRect.center)
            print("Ghost center", self.CurrentRect.center)
            Y = self.CurrentGhostRect.y // 25
            X = self.CurrentGhostRect.x // 25
            self.CheckStartPosition = ((Y, X))
            self.PinkGhostState = "DEAD"
            print("Initial Ghost death position", self.CurrentGhostRect.x,
                                                  self.CurrentGhostRect.y)
            self.GetPath = True
            MazeX, MazeY = PinkGhost.GhostPosToMazePos(self)
            self.D[(MazeY, MazeX)] = { 
                                      "Shortest Distance": 0,
                                      "Previous": None 
                                     }
            self.Queue.append((MazeY, MazeX))
            Path = ShortestPath.FindShortestPath(self)
            for Coordinate in Path:
                self.Path.append(Coordinate)
            print("Path", Path)
            
    def PacManAnimation(self):
        LastSurface = self.CurrentSurface
        if time.time() - self.LastBiteTime >= self.TimeBetweenBites:
            if self.Image == 0:
                self.CurrentSurface = self.PacManStartSurface
                self.Switch = True
            if self.Image == 1:
                self.CurrentSurface = self.PacManSurface
            if self.Image == 2:
                self.CurrentSurface = self.PacManSurface1
                self.Switch = False
            if self.PacManDirection == "LEFT":
                self.CurrentSurface = pygame.transform.rotate(
                                      self.CurrentSurface, 180)
            if self.PacManDirection == "RIGHT":
                self.CurrentSurface = self.CurrentSurface
            if self.PacManDirection == "UP":
                self.CurrentSurface = pygame.transform.rotate(
                                      self.CurrentSurface, 90)
            if self.PacManDirection == "DOWN":
                self.CurrentSurface = pygame.transform.rotate(
                                      self.CurrentSurface, 270)
            if self.PacManDirection == "STOP":
                self.CurrentRect.move(0, 0)
                self.CurrentSurface = LastSurface
            if self.Switch == True:
                self.Image += 1
            else:
                self.Image -= 1
                
    def DrawPacMan(self):
        MazeSurface.blit(self.CurrentSurface, self.CurrentRect)
            
class ScaredGhost():
    def __init__(self):
        self.ScaredGhostSurface1 = pygame.transform.scale(
                                   pygame.image.load(
                                   os.path.join("Scared Ghost",
                                                "ScaredGhost1.png"))
                                   .convert_alpha(), (25, 25))
        self.ScaredGhostRect1 = pygame.Rect((225, 175, 23, 23))
        self.ScaredGhostSurface2 = pygame.transform.scale(
                                   pygame.image.load(
                                   os.path.join("Scared Ghost",
                                                "ScaredGhost2.png"))
                                   .convert_alpha(), (25, 25))
        self.ScaredGhostRect2 = pygame.Rect((225, 175, 23, 23))
        self.ScaredGhostToNormalGhostSurface1 = pygame.transform.scale(
                                                pygame.image.load(
                                                os.path.join("Scared Ghost",
                                                "ScaredGhostToNormalGhost1.png"))
                                                .convert_alpha(), (25, 25))
        self.ScaredGhostToNormalGhostRect1 = pygame.Rect((225, 175, 23, 23))
        self.ScaredGhostToNormalGhostSurface2 = pygame.transform.scale(
                                                pygame.image.load(
                                                os.path.join("Scared Ghost",
                                                "ScaredGhostToNormalGhost2.png"))
                                                .convert_alpha(), (25, 25))
        self.ScaredGhostToNormalGhostRect2 = pygame.Rect((225, 175, 23, 23))
        self.EyesUpSurface = pygame.transform.scale(pygame.image.load(
                                                    os.path.join("Scared Ghost",
                                                    "EyesUp.png"))
                                                    .convert_alpha(), (25, 25))
        self.EyesUpRect = pygame.Rect((225, 175, 23, 23))
        self.EyesDownSurface = pygame.transform.scale(pygame.image.load(
                                                      os.path.join("Scared Ghost",
                                                      "EyesDown.png"))
                                                      .convert_alpha(), (25, 25))
        self.EyesDownRect = pygame.Rect((225, 175, 23, 23))
        self.EyesLeftSurface = pygame.transform.scale(pygame.image.load(
                                                      os.path.join("Scared Ghost",
                                                      "EyesLeft.png"))
                                                      .convert_alpha(), (25, 25))
        self.EyesLeftRect = pygame.Rect((225, 175, 23, 23))
        self.EyesRightSurface = pygame.transform.scale(pygame.image.load(
                                                       os.path.join("Scared Ghost",
                                                       "EyesRight.png"))
                                                       .convert_alpha(), (25, 25))
        self.EyesRightRect = pygame.Rect((225, 175, 23, 23))
        self.ScaredGhostImage = 0   
        
class PinkGhost(PacMan, ScaredGhost):
    def __init__(self):
        PacMan.__init__(self)
        ScaredGhost.__init__(self)
        # Use convert_alpha() for transparent surfaces
        self.PinkGhostSurfaceLeft1 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Pink Ghost", 
                                                  "PinkGhostLeft1.png"))
                                     .convert_alpha(), (25, 25))
        self.PinkGhostRectLeft1 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceLeft2 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Pink Ghost", 
                                                  "PinkGhostLeft2.png"))
                                     .convert_alpha(), (25, 25))
        self.PinkGhostRectLeft2 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceRight1 = pygame.transform.scale(
                                      pygame.image.load(
                                      os.path.join("Pink Ghost", 
                                                   "PinkGhostRight1.png"))
                                      .convert_alpha(), (25, 25))
        self.PinkGhostRectRight1 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceRight2 = pygame.transform.scale(
                                      pygame.image.load(
                                      os.path.join("Pink Ghost", 
                                                   "PinkGhostRight2.png"))
                                      .convert_alpha(), (25, 25))
        self.PinkGhostRectRight2 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceUp1 = pygame.transform.scale(
                                   pygame.image.load(
                                   os.path.join("Pink Ghost", 
                                                "PinkGhostUp1.png"))
                                   .convert_alpha(), (25, 25))
        self.PinkGhostRectUp1 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceUp2 = pygame.transform.scale(
                                   pygame.image.load(
                                   os.path.join("Pink Ghost", 
                                                "PinkGhostUp2.png"))
                                   .convert_alpha(), (25, 25))
        self.PinkGhostRectUp2 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceDown1 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Pink Ghost", 
                                                  "PinkGhostDown1.png"))
                                     .convert_alpha(), (25, 25))
        self.PinkGhostRectDown1 = pygame.Rect((225, 175, 23, 23))
        self.PinkGhostSurfaceDown2 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Pink Ghost", 
                                                  "PinkGhostDown2.png"))
                                     .convert_alpha(), (25, 25))
        self.PinkGhostRectDown2 = pygame.Rect((225, 175, 23, 23))
        self.CurrentGhostSurface = self.PinkGhostSurfaceLeft1
        self.CurrentGhostRect = self.PinkGhostRectLeft1
        self.Flag = True
        self.Float = False
        self.ScaredFloat = True
        self.Change = True
        self.Switch = True
        self.GhostFlag = True
        self.GetPath = False
        self.LastFloatTime = time.time()
        self.LastFrightenedTime = time.time()
        self.CheckStartPosition = ()
        self.GhostDecision = []
        self.Current = 0
        self.ChangeImage = 0
        self.TimeBetweenScared = 0.1
        self.TimeBetweenFloat = 0.1
        self.TimeUntilNormal = 0
        self.TimeBetweenFrightened = 0.1
        self.ChangeBackToNormal = 260
        self.PinkGhostState = "NORMAL"
        self.OppositeDirection = ""
        self.LastDirection = ""
        self.PinkGhostDirection = ""
        self.DeadGhostDirection = ""
        
    def MoveGhost(self):
        if self.PinkGhostDirection == "LEFT":
            self.CurrentGhostRect.x -= SPEED
        if self.PinkGhostDirection == "RIGHT":
            self.CurrentGhostRect.x += SPEED
        if self.PinkGhostDirection == "UP":
            self.CurrentGhostRect.y -= SPEED
        if self.PinkGhostDirection == "DOWN":
            self.CurrentGhostRect.y += SPEED
        self.LastDirection = self.PinkGhostDirection
        if self.PinkGhostDirection in ("LEFT", "RIGHT"):
            if self.CurrentGhostRect.x % 25 == 0:
                self.Flag = True
            else:
                self.Flag = False
        if self.PinkGhostDirection in ("UP", "DOWN"):
            if self.CurrentGhostRect.y % 25 == 0:
                self.Flag = True
            else:
                self.Flag = False
        self.GhostDecision.clear()
            
    def ContinuePinkGhostMovement(self):
        if self.PinkGhostState in ["NORMAL", "FRIGHTENED", "FRIGHTENED_TO_NORMAL"]: 
            self.PinkGhostTeleport()
            if self.CurrentGhostRect.x >= 450 or self.CurrentGhostRect.x <= 0:
                self.PinkGhostDirection = self.LastDirection
                self.Flag = False
            if self.Flag == True:
                self.PinkGhostDirection = self.GetAvailableGhostMoves()
            PinkGhost.MoveGhost(self)
        if self.PinkGhostState == "DEAD":
            if self.GhostFlag == False:
                self.Current += 1
            print("Current", self.Current)
            CurrentX, CurrentY = self.Path[self.Current]
            print("X:", CurrentX)
            print("Y:", CurrentY)
            NextCoordinateX, NextCoordinateY = self.Path[self.Current + 1]
            print("X + 1:", NextCoordinateX)
            print("Y + 1:", NextCoordinateY)
            if self.Current == len(self.Path) - 1:
                self.Path.clear()
                self.D = {}
                self.Target = set()
                self.PinkGhostState = "NORMAL"
                self.PinkGhostDirection = random.choice(["LEFT", "RIGHT"])
                self.Current = 0
                self.CheckStartPositon = ()
                return
            if CurrentY - 1 == NextCoordinateY:
                self.DeadGhostDirection = "LEFT"
            if CurrentY + 1 == NextCoordinateY:
                self.DeadGhostDirection = "RIGHT"
            if CurrentX - 1 == NextCoordinateX:
                self.DeadGhostDirection = "UP"
            if CurrentX + 1 == NextCoordinateX:
                self.DeadGhostDirection = "DOWN"
            print("Direction", self.DeadGhostDirection)
            print("before moving once", self.CurrentGhostRect.x, 
                                        self.CurrentGhostRect.y)
            if self.DeadGhostDirection == "LEFT":
                self.CurrentGhostRect.x -= SPEED
                self.CurrentGhostSurface = self.EyesLeftSurface 
                print("moving to left")
            if self.DeadGhostDirection == "RIGHT":
                self.CurrentGhostRect.x += SPEED
                self.CurrentGhostSurface = self.EyesRightSurface 
                print("moving to right")
            if self.DeadGhostDirection == "UP":
                self.CurrentGhostRect.y -= SPEED
                self.CurrentGhostSurface = self.EyesUpSurface 
                print("moving to up")
            if self.DeadGhostDirection == "DOWN":
                self.CurrentGhostRect.y += SPEED
                self.CurrentGhostSurface = self.EyesDownSurface 
                print("moving to down")
            print("after moving once", self.CurrentGhostRect.x, 
                                       self.CurrentGhostRect.y)
            if self.DeadGhostDirection in ("LEFT", "RIGHT"):
                print(self.CurrentGhostRect.x)
                print(CurrentY * 25)
                if self.CurrentGhostRect.x % 25 == 0:
                    self.GhostFlag = False
                else:
                    self.GhostFlag = True
            if self.DeadGhostDirection in ("UP", "DOWN"):
                print(self.CurrentGhostRect.y)
                print(CurrentX * 25)
                if self.CurrentGhostRect.y % 25 == 0:
                    self.GhostFlag = False
                else:
                    self.GhostFlag = True
            print()
        self.DeadGhostDirection = ""

    def GetAvailableGhostMoves(self):
        if self.PinkGhostState != "DEAD":
            MazeX, MazeY = self.GhostPosToMazePos()
            if self.Matrix[MazeY][MazeX - 1] != 1:
                self.GhostDecision.append("LEFT")
            if self.Matrix[MazeY][MazeX + 1] != 1:
                self.GhostDecision.append("RIGHT")
            if self.Matrix[MazeY - 1][MazeX] != 1:
                self.GhostDecision.append("UP")
            if self.Matrix[MazeY + 1][MazeX] != 1:
                self.GhostDecision.append("DOWN")
            self.LastDirection = self.GetOppositeDirection(self.PinkGhostDirection)
            if self.LastDirection in self.GhostDecision:
                self.GhostDecision.remove(self.LastDirection)
            self.PinkGhostDirection = random.choice(self.GhostDecision)
            return self.PinkGhostDirection
    
    def PinkGhostTeleport(self):
        if self.CurrentGhostRect.x < -30 and self.PinkGhostDirection == "LEFT":
            self.CurrentGhostRect.x = 508
        if self.CurrentGhostRect.x > 485 and self.PinkGhostDirection == "RIGHT":
            self.CurrentGhostRect.x = -30
            
    def GetOppositeDirection(self, LastDirection):
        OppositeDirection = {"LEFT": "RIGHT",
                             "RIGHT": "LEFT",
                             "UP": "DOWN",
                             "DOWN": "UP"}
        if self.LastDirection == "":
            return None
        return OppositeDirection[LastDirection]
    
    def MazePosToGhostPos(self, X, Y):
        X = X * self.BlockWidth
        Y = Y * self.BlockHeight
        return (X, Y)
    
    def GhostPosToMazePos(self):
        MazeX = self.CurrentGhostRect.x // self.BlockWidth
        MazeY = self.CurrentGhostRect.y // self.BlockHeight
        return (MazeX, MazeY)

    def ChangeImages(self, Surface1, Surface2):
        if time.time() - self.LastFloatTime >= self.TimeBetweenFloat:
            self.LastFloatTime = time.time()
            if self.Float:
                self.CurrentGhostSurface = Surface1
            if not self.Float:
                self.CurrentGhostSurface = Surface2
            self.Float = not self.Float
        if self.TimeUntilNormal >= 35:
            self.PinkGhostState = "FRIGHTENED_TO_NORMAL"
        
    def PinkGhostAnimation(self):
        if self.PinkGhostState == "NORMAL":
            if self.PinkGhostDirection == "LEFT":
                PinkGhost.ChangeImages(self, self.PinkGhostSurfaceLeft1, 
                                             self.PinkGhostSurfaceLeft2)
            if self.PinkGhostDirection == "RIGHT":
                PinkGhost.ChangeImages(self, self.PinkGhostSurfaceRight1,
                                             self.PinkGhostSurfaceRight2)
            if self.PinkGhostDirection == "UP":
                PinkGhost.ChangeImages(self, self.PinkGhostSurfaceUp1,
                                             self.PinkGhostSurfaceUp2)
            if self.PinkGhostDirection == "DOWN":
                PinkGhost.ChangeImages(self, self.PinkGhostSurfaceDown1,
                                             self.PinkGhostSurfaceDown2)
        if self.PinkGhostState == "FRIGHTENED":
            self.TimeUntilNormal += time.time() - self.LastFloatTime
            PinkGhost.ChangeImages(self, self.ScaredGhostSurface1,
                                         self.ScaredGhostSurface2)
            PacMan.EatGhosts(self)
        if self.PinkGhostState == "FRIGHTENED_TO_NORMAL":
            self.TimeUntilNormal += time.time() - self.LastFloatTime
            PinkGhost.FrightenedToNormal(self)
            PacMan.EatGhosts(self)
        
    def FrightenedMode(self):
        self.PinkGhostDirection = self.GetOppositeDirection(self.PinkGhostDirection)
        self.PinkGhostState = "FRIGHTENED"
        self.TimeUntilNormal = 0
        
    def FrightenedToNormal(self):
        if time.time() - self.LastFrightenedTime >= self.TimeBetweenFrightened:
            self.LastFrightenedTime = time.time()
            if self.ChangeImage == 0:
                self.CurrentGhostSurface = self.ScaredGhostToNormalGhostSurface1
                self.Switch = True
            if self.ChangeImage == 1:
                self.CurrentGhostSurface = self.ScaredGhostToNormalGhostSurface2
            if self.ChangeImage == 2:
                self.CurrentGhostSurface = self.ScaredGhostSurface2
            if self.ChangeImage == 3:
                self.CurrentGhostSurface = self.ScaredGhostSurface1
                self.Switch = False
            if self.Switch == True:
                self.ChangeImage += 1
            else:
                self.ChangeImage -= 1
        if self.TimeUntilNormal >= self.ChangeBackToNormal:
            self.PinkGhostState = "NORMAL"
            self.TimeUntilNormal = 0
        
    def KillPacMan(self):
        if self.CurrentGhostRect.collidepoint(self.CurrentRect.center) and \
            self.PinkGhostState == "NORMAL":
            self.Lives -= 1
            time.sleep(2)
            Main.TakeAwayLife()
            PinkGhost.ResetPosition(self)
            
    def ResetPosition(self):
        self.CurrentRect.topleft = (225, 375)
        self.CurrentGhostRect.topleft = (225, 175)
        self.PacManDirection = ""
        self.PinkGhostDirection = random.choice(["LEFT", "RIGHT"])
            
    def DrawPinkGhost(self):    
        MazeSurface.blit(self.CurrentGhostSurface, self.CurrentGhostRect)
    
class YellowGhost(PinkGhost):
    def __init__(self):
        self.YellowGhostSurfaceLeft1 = pygame.transform.scale(
                                       pygame.image.load(
                                       os.path.join("Yellow Ghost", 
                                                    "YellowGhostLeft1.png"))
                                       .convert_alpha(), (25, 25))
        self.YellowGhostRectLeft1 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceLeft2 = pygame.transform.scale(
                                       pygame.image.load(
                                       os.path.join("Yellow Ghost", 
                                                    "YellowGhostLeft2.png"))
                                       .convert_alpha(), (25, 25))
        self.YellowGhostRectLeft2 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceRight1 = pygame.transform.scale(
                                        pygame.image.load(
                                        os.path.join("Yellow Ghost", 
                                                     "YellowGhostRight1.png"))
                                        .convert_alpha(), (25, 25))
        self.YellowGhostRectRight1 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceRight2 = pygame.transform.scale(
                                        pygame.image.load(
                                        os.path.join("Yellow Ghost", 
                                                     "YellowGhostRight2.png"))
                                        .convert_alpha(), (25, 25))
        self.YellowGhostRectRight2 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceUp1 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Yellow Ghost", 
                                                  "YellowGhostUp1.png"))
                                     .convert_alpha(), (25, 25))
        self.YellowGhostRectUp1 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceUp2 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Yellow Ghost", 
                                                  "YellowGhostUp2.png"))
                                     .convert_alpha(), (25, 25))
        self.YellowGhostRectUp2 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceDown1 = pygame.transform.scale(
                                       pygame.image.load(
                                       os.path.join("Yellow Ghost", 
                                                    "YellowGhostDown1.png"))
                                       .convert_alpha(), (25, 25))
        self.YellowGhostRectDown1 = pygame.Rect((225, 175, 23, 23))
        self.YellowGhostSurfaceDown2 = pygame.transform.scale(
                                       pygame.image.load(
                                       os.path.join("Yellow Ghost", 
                                                    "YellowGhostDown2.png"))
                                       .convert_alpha(), (25, 25))
        self.YellowGhostRectDown2 = pygame.Rect((225, 175, 23, 23))
        #self.CurrentGhostSurface = self.YellowGhostSurfaceLeft1
        #self.CurrentGhostRect = self.YellowGhostRectLeft1
    
class BlueGhost(YellowGhost):
    def __init__(self):
        self.BlueGhostSurfaceLeft1 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Blue Ghost", 
                                                  "BlueGhostLeft1.png"))
                                     .convert_alpha(), (25, 25))
        self.BlueGhostRectLeft1 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceLeft2 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Blue Ghost", 
                                                  "BlueGhostLeft2.png"))
                                     .convert_alpha(), (25, 25))
        self.BlueGhostRectLeft2 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceRight1 = pygame.transform.scale(
                                      pygame.image.load(
                                      os.path.join("Blue Ghost", 
                                                   "BlueGhostRight1.png"))
                                      .convert_alpha(), (25, 25))
        self.BlueGhostRectRight1 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceRight2 = pygame.transform.scale(
                                      pygame.image.load(
                                      os.path.join("Blue Ghost", 
                                                   "BlueGhostRight2.png"))
                                      .convert_alpha(), (25, 25))
        self.BlueGhostRectRight2 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceUp1 = pygame.transform.scale(
                                   pygame.image.load(
                                   os.path.join("Blue Ghost", 
                                                "BlueGhostUp1.png"))
                                   .convert_alpha(), (25, 25))
        self.BlueGhostRectUp1 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceUp2 = pygame.transform.scale(
                                   pygame.image.load(
                                   os.path.join("Blue Ghost", 
                                                "BlueGhostUp2.png"))
                                   .convert_alpha(), (25, 25))
        self.BlueGhostRectUp2 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceDown1 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Blue Ghost", 
                                                  "BlueGhostDown1.png"))
                                     .convert_alpha(), (25, 25))
        self.BlueGhostRectDown1 = pygame.Rect((225, 175, 23, 23))
        self.BlueGhostSurfaceDown2 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Blue Ghost", 
                                                  "BlueGhostDown2.png"))
                                     .convert_alpha(), (25, 25))
        self.BlueGhostRectDown2 = pygame.Rect((225, 175, 23, 23))
        #self.CurrentGhostSurface = self.BlueGhostSurfaceLeft1
        #self.CurrentGhostRect = self.BlueGhostRectLeft1
    
class RedGhost(BlueGhost):
    def __init__(self):
        self.RedGhostSurfaceLeft1 = pygame.transform.scale(
                                    pygame.image.load(
                                    os.path.join("Red Ghost", 
                                                 "RedGhostLeft1.png"))
                                    .convert_alpha(), (25, 25))
        self.RedGhostRectLeft1 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceLeft2 = pygame.transform.scale(
                                    pygame.image.load(
                                    os.path.join("Red Ghost", 
                                                 "RedGhostLeft2.png"))
                                    .convert_alpha(), (25, 25))
        self.RedGhostRectLeft2 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceRight1 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Red Ghost", 
                                                  "RedGhostRight1.png"))
                                     .convert_alpha(), (25, 25))
        self.RedGhostRectRight1 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceRight2 = pygame.transform.scale(
                                     pygame.image.load(
                                     os.path.join("Red Ghost", 
                                                  "RedGhostRight2.png"))
                                     .convert_alpha(), (25, 25))
        self.RedGhostRectRight2 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceUp1 = pygame.transform.scale(
                                  pygame.image.load(
                                  os.path.join("Red Ghost", 
                                               "RedGhostUp1.png"))
                                  .convert_alpha(), (25, 25))
        self.RedGhostRectUp1 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceUp2 = pygame.transform.scale(
                                  pygame.image.load(
                                  os.path.join("Red Ghost", 
                                               "RedGhostUp2.png"))
                                  .convert_alpha(), (25, 25))
        self.RedGhostRectUp2 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceDown1 = pygame.transform.scale(
                                    pygame.image.load(
                                    os.path.join("Red Ghost", 
                                                 "RedGhostDown1.png"))
                                    .convert_alpha(), (25, 25))
        self.RedGhostRectDown1 = pygame.Rect((225, 175, 23, 23))
        self.RedGhostSurfaceDown2 = pygame.transform.scale(
                                    pygame.image.load(
                                    os.path.join("Red Ghost", 
                                                 "RedGhostDown2.png"))
                                    .convert_alpha(), (25, 25))
        self.RedGhostRectDown2 = pygame.Rect((225, 175, 23, 23))
        #self.CurrentGhostSurface = self.RedGhostSurfaceLeft1
        #self.CurrentGhostRect = self.RedGhostRectLeft1
            
class Main(RedGhost):
    def __init__(self):
        # Inherits Maze class
        Maze.__init__(self)
        PacMan.__init__(self)
        PinkGhost.__init__(self)
        YellowGhost.__init__(self)
        BlueGhost.__init__(self)
        RedGhost.__init__(self)
        self.Score = 0
        self.HighScore = 0
        self.LastFlashTime = time.time()
        self.TimeBetweenFlash = 0.2
        self.PacManLives = []
        self.PacManLife1Surface = self.PacManSurface
        self.PacManLife2Surface = self.PacManSurface
        self.PacManLife3Surface = self.PacManSurface
        self.PacManLife1Surface = pygame.transform.rotate(self.PacManLife1Surface, 
                                                          180)
        self.PacManLife2Surface = pygame.transform.rotate(self.PacManLife2Surface, 
                                                          180)
        self.PacManLife3Surface = pygame.transform.rotate(self.PacManLife3Surface, 
                                                          180)
        self.PacManLife1 = self.PacManLife1Surface \
                           .get_rect(center = ((SCREEN_WIDTH - 370) // 2, 
                                                SCREEN_HEIGHT - 17))
        self.PacManLife2 = self.PacManLife2Surface \
                           .get_rect(center = ((SCREEN_WIDTH - 310) // 2, 
                                                SCREEN_HEIGHT - 17))
        self.PacManLife3 = self.PacManLife3Surface \
                           .get_rect(center = ((SCREEN_WIDTH - 250) // 2,
                                                SCREEN_HEIGHT - 17))
        
    def AddLives(self):
        self.PacManLives.append(self.PacManLife1Surface)
        self.PacManLives.append(self.PacManLife2Surface)
        self.PacManLives.append(self.PacManLife3Surface)
        
    def TakeAwayLife(self):
        self.PacManLives[-1].fill(BLACK)
        self.PacManLives.pop(-1)
        print("PacMan WAS KILLED")
        print()
        
    def DrawLives(self):
        SCREEN.blit(self.PacManLife1Surface, self.PacManLife1)
        SCREEN.blit(self.PacManLife2Surface, self.PacManLife2)
        SCREEN.blit(self.PacManLife3Surface, self.PacManLife3)
        
    def DrawPellets(self):
        for Position in self.Pellets:
            X = Position[1][0] + 13
            Y = Position[1][1] + 13
            Width = Position[1][2] // 2
            Height = Position[1][3] // 2
            pygame.draw.circle(MazeSurface, PEACH, (X, Y), Width, Height)
        
    def DrawEnergizers(self):
        if time.time() - self.LastFlashTime >= self.TimeBetweenFlash:
            self.LastFlashTime = time.time()
            for Position in self.Energizer:
                X = Position[1][0] + 13
                Y = Position[1][1] + 20
                Width = Position[1][2] // 2
                Height = Position[1][3] // 2
                pygame.draw.circle(MazeSurface, PEACH, (X, Y), Width, Height)
        else:
            for Position in self.Energizer:
                X = Position[1][0] + 13
                Y = Position[1][1] + 20
                Width = Position[1][2] // 2
                Height = Position[1][3] // 2
                pygame.draw.circle(MazeSurface, BLACK, (X, Y), Width, Height)
        
    def DrawBackground(self):
        MazeSurface.blit(BackgroundSurface, BackgroundRect) 
        
    def PlaySound(self, Track):
        if Track == 0:
            Eat = pygame.mixer.Sound(
                  os.path.join("Sound Effects", "pacman_chomp.wav"))
            Eat.play()
            pygame.mixer.fadeout(400)
        if Track == 1:
            EatPellet = pygame.mixer.Sound(
                        os.path.join("Sound Effects", "pacman_eatghost.wav"))
            EatPellet.play()
            pygame.mixer.music.play(7)
            pygame.mixer.fadeout(400)
            
    def GameOver(self):
        if self.Lives == 0:
            pygame.time.wait(1000)
            pygame.quit()
                
    def ShowScore(self):
        global Font
        OneUpText = Font.render("1UP", True, WHITE)
        OneUpTextRect = OneUpText.get_rect(center = (70, 10))
        # Displays current score
        OneUpScoreText = Font.render(str(self.Score), True, WHITE)
        OneUpScoreRect = OneUpScoreText.get_rect(center =
                                                ((SCREEN_WIDTH - 290) 
                                                // 2, 26))
        HighScoreText = Font.render("High Score", True, WHITE)
        HighScoreTextRect = HighScoreText.get_rect(center = 
                                                  (SCREEN_WIDTH // 2, 10))
        # Displays High Score
        HighScoreNumber = Font.render(str(self.HighScore), True, WHITE)
        HighScoreNumberRect = HighScoreNumber.get_rect(center = 
                                                      ((SCREEN_WIDTH + 90) 
                                                      // 2, 26))
        SCREEN.blit(OneUpText, OneUpTextRect)
        SCREEN.blit(OneUpScoreText, OneUpScoreRect)
        SCREEN.blit(HighScoreText, HighScoreTextRect)
        SCREEN.blit(HighScoreNumber, HighScoreNumberRect)
    
    def Update(self):
        # Update PacMan
        Main.ContinuePacManMovement()
        Main.PacManAnimation()
        # Update PinkGhost
        Main.PinkGhostTeleport()
        Main.ContinuePinkGhostMovement()
        Main.PinkGhostAnimation()
        Main.KillPacMan()
        # Update Main
        Main.DrawBackground()
        Main.DrawPellets()
        Main.DrawEnergizers()
        Main.DrawPinkGhost()
        Main.DrawPacMan()
        Main.DrawLives()
        Main.GameOver()
        Main.EatPellets()
        Main.EatEnergizer()
        SCREEN.blit(MazeSurface, MazeRect)
        Main.ShowScore()
     
Main = Main()

BackgroundSurface = pygame.transform.scale(BackgroundSurface, 
                                          (Main.MazeWidth, 
                                           Main.MazeHeight))
BackgroundRect = BackgroundSurface.get_rect()

MazeSurface = pygame.Surface((Main.MazeWidth, Main.MazeHeight))
MazeRect = MazeSurface.get_rect(topleft = (Main.MazeOffsetX, 
                                           Main.MazeOffsetY))
Main.DrawMaze(MazeSurface)
Main.AddLives()

'''
Before the game starts ...
pregame = True
while pregame:
    if key button pressed:
        pregame = False
        run = True
'''

run = True
while run:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            Main.PacManMovement()
        
    Main.Update()
    CLOCK.tick(FPS)
    pygame.display.update()
    
pygame.quit()