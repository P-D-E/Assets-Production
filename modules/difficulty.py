import sys
import VS
import Director
def usingDifficulty ():
  return (VS.GetDifficulty()!=1.0)

def SetDiff(diff):
  if (diff>VS.GetDifficulty()):
    VS.SetDifficulty(diff)

_key="31337ness"
class difficulty:
  diff=[]
  creds=[]
  credsToMax=1
  i=0 #comment this if you want to check all in 1 frame
  
  def SetDiff(self,diff):
    if (diff>VS.GetDifficulty()):
      VS.SetDifficulty(diff)

  def __init__(self,credsMax):
    self.credsToMax=credsMax
    un=VS.getPlayerX(0)
    self.i=0
    while (un):
      newdiff=0
      if (Director.getSaveDataLength(self.i,_key)):
        newdiff=Director.getSaveData(self.i,_key,0)
        self.diff+=[newdiff]
      else:
        newdiff=VS.GetDifficulty()
        self.diff+=[newdiff]
        Director.pushSaveData(self.i,_key,newdiff)
      SetDiff(newdiff)
      self.creds+=[un.getCredits()]
      self.i+=1
      un=VS.getPlayerX(self.i)
      
  def usingDifficulty (self):
    return (VS.GetDifficulty()!=1.0)
  
  def getPlayerDifficulty (self,playa):
    return self.diff[playa]
  
  def Execute(self):
#    for i in range(len(self.creds)): #uncomment this if you want to check all in 1 frame
      if (len(self.creds)<=0):
        if (self.i!=-1):
          self.i=-1
          raise IndexError("Empty creds and diff arrays in difficulty module\nUnable to find any players...")
        return
      if (self.i>=len(self.creds)):
        self.i=0
      un=VS.getPlayerX(self.i)
      newcreds=un.getCredits()
      if (self.creds[self.i]!=newcreds):
        if (self.creds[self.i]>newcreds):
          newdiff=((newcreds-self.creds[self.i])/self.credsToMax)
          Director.putSaveData(self.i,_key,0,newdiff)
          SetDiff(newdiff)
        self.creds[self.i]=newcreds
      self.i+=1 #comment this also if you want to check all in 1 frame
  
