from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from View.UISquare.SquareData import square
from math import sqrt, floor
import copy

class SolveMazeAstar(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)
    
  def Solve(self, currentGrid, currentPastGrids, currentPastGridsIndex):
    
    
    open = []
    visited = []
    close = []
    origin = []


    startingNodeLocation = list(self.GetSolverLocation(currentGrid))
    print("startingNode:", startingNodeLocation)
    
    goalNodeLocation = list(self.GetGoalLocation(currentGrid))
    print("goalNode:", goalNodeLocation)
    open.append(startingNodeLocation)

    clock = pygame.time.Clock()

    while open:
      poppedNode = open.pop(0)

      #neighbors
      left = [poppedNode[0] - 1, poppedNode[1]]
      up = [poppedNode[0], poppedNode[1] - 1]
      right = [poppedNode[0] + 1, poppedNode[1]]
      down = [poppedNode[0], poppedNode[1] + 1]

      neighboringNodes = [left, up, right, down]

      #g score of neighbors
      gLeft = sqrt((((startingNodeLocation[0]) - (left[0]))**2) + (((startingNodeLocation[1]) - (left[1]))**2))
      gUp = sqrt((((startingNodeLocation[0]) - (up[0]))**2) + (((startingNodeLocation[1]) - (up[1]))**2))
      gRight = sqrt((((startingNodeLocation[0]) - (right[0]))**2) + (((startingNodeLocation[1]) - (right[1]))**2))
      gDown = sqrt((((startingNodeLocation[0]) - (down[0]))**2) + (((startingNodeLocation[1]) - (down[1]))**2))

      gScores = [gLeft, gUp, gRight, gDown]

      #h score of neighbors
      hLeft = sqrt((((goalNodeLocation[0]) - (left[0]))**2) + (((goalNodeLocation[1]) - (left[1]))**2))
      hUp = sqrt((((goalNodeLocation[0]) - (up[0]))**2) + (((goalNodeLocation[1]) - (up[1]))**2))
      hRight = sqrt((((goalNodeLocation[0]) - (right[0]))**2) + (((goalNodeLocation[1]) - (right[1]))**2))
      hDown = sqrt((((goalNodeLocation[0]) - (down[0]))**2) + (((goalNodeLocation[1]) - (down[1]))**2))

      hScores = [hLeft, hUp, hRight, hDown]

      #f score of neighbors
      fLeft = gLeft + hLeft
      fUp = gUp + hUp
      fRight = gRight + hRight
      fDown = gDown +hDown

      fScores = [floor(fLeft), floor(fUp), floor(fRight), floor(fDown)]

      lowestFScore = self.GetLowestFScore(fScores)
      print("gScores:", gScores)
      print("hScores:", hScores)
      print("fScores:", fScores)
      print("popped node:", poppedNode)
      for neighbor, neighborFScore in zip(neighboringNodes, fScores):
        if neighbor[0] < len(currentGrid) and neighbor[1] < len(currentGrid) and neighbor[0] > -1 and neighbor[1] > -1:
          print(currentGrid[neighbor[1]][neighbor[0]])
          if neighbor not in visited and currentGrid[neighbor[1]][neighbor[0]] == go.NOTHING:
            print("neighbor:", neighbor)
            visited.append(neighbor)
            origin.append(poppedNode)
            if neighborFScore == lowestFScore:
              open.insert(0, neighbor)
            else:
              open.append(neighbor)
            currentGrid[neighbor[1]][neighbor[0]] = go.FINDER
            self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
            print("hi")
            
            
            self.DrawFinderSquaresHandler(currentGrid, self.gameWindow, neighbor)

          if currentGrid[neighbor[1]][neighbor[0]] == go.GOAL:
            print("visited:", visited)
            print("origin: ", origin)
            self.BackTrack(currentGrid, poppedNode, neighbor, visited, origin, self.gameWindow)
            return
        print("nieghborFScore:", neighborFScore)
        print("lowestFScore:", lowestFScore)
      for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      pygame.display.update()
      clock.tick(20)

      print("open:", open)


      


  def GetLowestFScore(self, fScores):
    fScoresCopy = copy.deepcopy(fScores)
    fScoresCopy.sort()
    return fScoresCopy[0]

  def GetSolverLocation(self, currentGrid):
    for gridRow in range(len(currentGrid)):
      for gridSquare in range(len(currentGrid[gridRow])):
        if currentGrid[gridRow][gridSquare] == go.SOLVER:
          return gridSquare, gridRow

  def GetGoalLocation(self, currentGrid):
    for gridRow in range(len(currentGrid)):
      for gridSquare in range(len(currentGrid[gridRow])):
        if currentGrid[gridRow][gridSquare] == go.GOAL:
          return gridSquare, gridRow


  def DrawFinderSquaresHandler(self, currentGrid, gameWindow, neighbor):

    positions = [160 + (neighbor[0]*(280/len(currentGrid))), 60 + (neighbor[1]*(280/len(currentGrid))), 280/len(currentGrid), 280/len(currentGrid)]
    pygame.draw.rect(gameWindow, square["finder"]["color"], positions)

  def DrawPathBackSquaresHandler(self, currentGrid, gameWindow, currentNode):

    positions = [160 + (currentNode[0]*(280/len(currentGrid))), 60 + (currentNode[1]*(280/len(currentGrid))), 280/len(currentGrid), 280/len(currentGrid)]
    pygame.draw.rect(gameWindow, square["path"]["color"], positions)


  def BackTrack(self, currentGrid, poppedNode, neighbor, visited, origin, gameWindow):
    #first node
    currentGrid[poppedNode[1]][poppedNode[0]] = go.PATH
    currentNode = [poppedNode[0], poppedNode[1]]
    print("initialCurrentNode:", currentNode)
    self.DrawPathBackSquaresHandler(currentGrid, gameWindow, currentNode)
    #clock
    clock = pygame.time.Clock()
    #continue with rest of nodes
    while True:
      #coorelates current node with the node it came from
      print("realIndex:", visited.index(currentNode))
      currentIndex = visited.index(currentNode)
      print("currentIndex:", currentIndex)
      currentNode = origin[currentIndex]

      self.DrawPathBackSquaresHandler(currentGrid, gameWindow, currentNode)

      if currentGrid[currentNode[1]][currentNode[0]] == go.SOLVER:
        return
      else:
        currentGrid[currentNode[1]][currentNode[0]] = go.PATH

      for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      pygame.display.update()
      clock.tick(20)