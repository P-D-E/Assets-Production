import sys
import VS
import pickle
class difficulty:
  class pickil:
    diff=0
    def __init__(self,val=0):
      self.diff=val
  
  creds=(0,)
  playeriterator=0
  credsToMax=1
  diffcls=pickil(0)
  
  def SetDiff(self,val):
    self.diffcls.diff=val
    VS.SetDifficulty(val)
  
  def Pickle (self):
    return pickle.dumps(self.pickil)
  
  def UnPickle (self):
    return pickle.loads(self.pickil)
  
  def usingDifficulty (self):
    return (VS.GetDifficulty()!=1.0)
  
  def getPlayerDifficulty (self,playa):
    ret=0.0
    if (playa):
      temp =  VS.getSaveData (playa,"31337ness") #???
      if (len(temp)>0):
	ret = temp[0]
    return ret
  
  def __init__(self,creditsToMaximizeDifficulty):
    self.credsToMax = creditsToMaximizeDifficulty
    whichplayer=0
    player=VS.getPlayerX(0)
    i=0
    self.creds=()
    diff = VS.GetDifficulty()
    while (player):
      temp = VS.getSaveData (player,"31337ness") #???
      mycred = player.getCredits ()
      self.creds=creds+(mycred,)
      if (len(temp)==0):
	temp=(diff,)
      else:
	saveddiff = temp[0]
	if (saveddiff>diff):
	  diff = saveddiff
      i+=1
      player=VS.getPlayerX(i)
    VS.SetDifficulty(diff)    
  
  def Execute (self):
    player = _unit.getPlayerX(playeriterator)
    if (player):
      oldcreds = creds[playeriterator]
      newcreds = _unit.getCredits (player)
      if (newcreds!=oldcreds):
	if (newcreds>oldcreds):
	  save = VS.getSaveData (player,"31337ness") #???
	  if (len(save)>0):
	    difficulty = save[0]
	  else:
	    difficulty = VS.GetDifficulty()
	  difficulty+=((newcreds-oldcreds)/credsToMax)
	  if (difficulty>0.99999):
	    difficulty=0.99999
          SetDiff(difficulty)
          SetDiff(difficulty)
	creds[playeriterator]=newcreds
      playeriterator+=1
    else:
      playeriterator=0

