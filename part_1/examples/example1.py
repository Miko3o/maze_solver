class Guy:

  def __init__(self, name, pointer_to_guy=None):
    self.name = name
    self.pointer_to_guy = pointer_to_guy
  
  def badFunction(self):
    self = Guy("Bad guy")

  def weirdFunction(self):
    self = self.pointer_to_guy

  def printName(self):
    print(self.name)

guy = Guy("Good guy")
guy.badFunction()
guy.printName()

m_guy = Guy("Mysterious Guy")
guy = Guy("Good Guy", m_guy)

guy.weirdFunction()
guy.printName()
m_guy.printName()