import random
from superheros import batman, ironman, superman, captain, thor


while True:
  def get_user_name():
    name = input('What is your name?\n')
    print('Hi, %s.' % name)
    return name
  def select_hero(name):
    vowels = ['A', 'E', 'I', 'O', 'U']
    if name[0].upper() in vowels:
      superheroes = [ "Thor","Batman", "Iron Man", "Superman", "Captain America"]
    else:
      superheroes = ["Superman", "Iron Man", "Captain America", "Batman", "Thor"]
    return random.choice(superheroes)
  def main():
    name = get_user_name()
    random_hero = select_hero(name)
    print("You have to design " + random_hero)
    if random_hero == "Captain America":
      captain.draw()
    if random_hero == "Batman":
      batman.draw()
    if random_hero == "Superman":
      superman.draw()
    if random_hero == "Iron Man":
      ironman.draw()
    if random_hero == "Thor":
      thor.draw()
  if __name__ == "__main__":
    main()