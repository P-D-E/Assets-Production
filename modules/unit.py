import VS
def isLandable (un):
    unit_fgid = un.getFlightgroupName()
    retval = (((un.isPlanet ()) and (not un.isJumppoint())) or unit_fgid=="Base")
    return retval
  
def isBase (un):
    unit_fgid = un.getFlightgroupName()
    retval = unit_fgid=="Base"
    return retval

   
def isAsteroid (un):
    unit_fgid = un.getFlightgroupName()
    retval = unit_fgid=="Asteroid"
    return retval

   

def getSignificant (whichsignificant, landable_only, capship_only):
	un=VS.Unit()
	which=0
	signum=0
	while (signum<=whichsignificant):
		un=VS.getUnit(which)
		if (un.isNull()):
		  which=0
		  if (signum==0):
		    signum=whichsignificant+1
		else:
		  if ((landable_only) or (capship_only)):
		    if(capship_only):
		      if (isBase (un)):
			signum=signum+1
		    else:
		      if (isLandable (un)):
			signum=signum+1
		  else:
		    if (un.isSignificant()):
		      signum=signum+1
		  which=which+1			
	return un
  
  #this one terminates if fewer than so many planets exist with null
def getPlanet (whichsignificant, sig):
	un=VS.Unit()
	which=0
	signum=0
	while (signum<=whichsignificant):
		un=VS.getUnit(which)
		if (un):
		  if(sig):
		    if (un.isSignificant ()):
		      signum=signum+1
		  else:
		    if (un.isPlanet ()):
		      signum=signum+1
		  which=which+1			
		else:
		  if (signum<=whichsignificant):
		    signum=whichsignificant+1
	return un
  
def getJumpPoint(whichsignificant):
	un=VS.Unit()
	which=0
	signum=0
	while (signum<whichsignificant):
		un=VS.getUnit(which)
		if (un):
			if (_unit.isJumppoint(un)):
				signum=signum+1
			which=which+1							
		else:
			which=0
			if (signum==0):
				un.setNull()
				signum=whichsignificant
	return un
  
def obsolete_getNearestEnemy(my_unit,range):
    ship_nr=0
    min_dist=9999999.0
    min_enemy=VS.Unit()
    un=VS.getUnit(ship_nr)
    while(unit):
      unit_pos=un.getPosition()
      dist=my_unit.getMinDis(unit_pos)
      relation=_unit.getRelation(my_unit,unit)
      if(relation<0.0):
	if((my_unit==unit) and (dist<range) and (dist<min_dist)):
	  min_dist=dist
	  min_enemy=unit
      ship_nr=ship_nr+1
      unit=VS.getUnit(ship_nr)
    if(min_enemy):
      other_fgid=_unit.getFgID(min_enemy)
    return min_enemy
  

def obsolete_getThreatOrEnemyInRange(un,range):
    threat=_unit.getThreat(un)
    if(threat.isNull()):
      threat=obsolete_getNearestEnemy(un,range)
    return threat
    
def setPreciseTargetShip (which_fgid, target_unit):
    ship_nr=0
    un=VS.getUnit(ship_nr)
    if (target_unit):
      while(un.isNull()):
        unit_fgid=un.getFgID()
        if(unit_fgid[:len(which_fgid)]==which_fgid):
	  un.setTarget(target_unit)
        ship_nr=ship_nr+1
        un=VS.getUnit(ship_nr)
    
  
  
def getUnitByFgIDFromNumber(fgid, ship_nr):
    unit=VS.getUnit(ship_nr)
    found_unit=VS.Unit()
    while(unit and found_unit.isNull()):
      unit_fgid=unit.getFgID()
      if(unit_fgid==fgid):
	found_unit=unit
      ship_nr=ship_nr+1
      unit=VS.getUnit(ship_nr)
    return found_unit
  
def getUnitByFgID(fgid):
    return getUnitByFgIDFromNumber(fgid,0)

def setTargetShip(which_fgid,target_fgid):
    target_unit=getUnitByFgID(target_fgid)
    setPreciseTargetShip(which_fgid,target_unit)
  
def removeFg(which_fgid):
    ship_nr=0
    un=VS.getUnit(ship_nr)
    while(un):
      unit_fgid=un.getFgID()
      if(unit_fgid[:len(which_fgid)]==which_fgid):
	un.Kill()
      else:
	ship_nr=ship_nr+1
      un=VS.getUnit(ship_nr)

