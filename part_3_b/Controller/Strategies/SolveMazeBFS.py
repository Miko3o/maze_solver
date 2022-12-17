from Controller.Strategies.AbstractStrategy import AbstractStrategy
from View.GameStateENUM import GridObjects as go
import pygame
from View.UISquare.SquareData import square

class SolveMazeBFS(AbstractStrategy):

  def __init__(self, *args):
    super().__init__(*args)

  def Solve(self, currentGrid, currentPastGrids, currentPastGridsIndex):
  
    visited = []
    origin = []
    queue = []

    #get starting node location
    startingNodeLocation = list(self.GetSolverLocation(currentGrid))

    visited.append(startingNodeLocation)
    queue.append(startingNodeLocation)

    clock = pygame.time.Clock()

    while queue:
      self.viewManager.uiGrid.Draw(currentGrid, currentPastGrids, 0, 0, go.NOTHING, currentPastGridsIndex)
      poppedNode = queue.pop(0)

      #neighbors
      left = [poppedNode[0] - 1, poppedNode[1]]
      up = [poppedNode[0], poppedNode[1] + 1]
      right = [poppedNode[0] + 1, poppedNode[1]]
      down = [poppedNode[0], poppedNode[1] - 1]

      neighboringNodes = [left, up, right, down]

      
      print("popped node:", poppedNode)
      for neighbor in neighboringNodes:
        if neighbor[0] < len(currentGrid) and neighbor[1] < len(currentGrid) and neighbor[0] > -1 and neighbor[1] > -1:
          if neighbor not in visited and currentGrid[neighbor[1]][neighbor[0]] == go.NOTHING:
            print("neighbor:", neighbor)
            visited.append(neighbor)
            origin.append(poppedNode)
            queue.append(neighbor)
            currentGrid[neighbor[1]][neighbor[0]] = go.FINDER
            self.viewManager.modelManager.gridMetaData.ChangeGridData(currentGrid, False, False, False)
            
            
            self.DrawFinderSquaresHandler(currentGrid, self.gameWindow, neighbor)

          if currentGrid[neighbor[1]][neighbor[0]] == go.GOAL:
            print("visited:", visited)
            print("origin: ", origin)
            self.BackTrack(currentGrid, poppedNode, neighbor, visited, origin, self.gameWindow)
            return

      for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      pygame.display.update()
      clock.tick(20)
          


      print("queue:", queue)








    super().Solve()


  def GetSolverLocation(self, currentGrid):
    for gridRow in range(len(currentGrid)):
      for gridSquare in range(len(currentGrid[gridRow])):
        if currentGrid[gridRow][gridSquare] == go.SOLVER:
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
    self.DrawPathBackSquaresHandler(currentGrid, gameWindow, currentNode)
    #clock
    clock = pygame.time.Clock()
    #continue with rest of nodes
    while True:
      #coorelates current node with the node it came from
      currentIndex = visited.index(currentNode) - 1
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
