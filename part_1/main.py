from GameManager import GameManager

print("Hi")
game = GameManager()
game.Init()

def Main():
  try:
    print("Hi")
    game = GameManager()
    game.Init()
    
    print("Not in the game anymore!")
  except SyntaxError:
    print("your syntax is BAD")
  except Exception:
    print("ERROR!")
    print(Exception)

Main()