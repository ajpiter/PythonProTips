#While True loops continue to run.
#Any code after a While True loop will not be executed 

#The hero repeatedly moves, and then attacks the same person whoose name is "Enemy"
While True: 
  hero.moveRight()
  hero.attack("Enemy")
  
#The hero repetedly moves, and then attacks the nearest enemy
While True: 
  hero.moveRight()
  Enemy = hero.findNearestEnemy()
  hero.attack("Enemy")
