class player:
  
  def play(self):
    print("The player is playing cricket ")


class Batsman:

  def play(self):
    print("The Batsman is batting ")


class Bowler:

  def play(self):
    print("The Bowler is bowling ")

player = player()
batsman = Batsman()
bowler = Bowler()

player.play()
batsman.play()
bowler.play()
