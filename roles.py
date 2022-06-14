#Jeu de rôles'
import random

print("\n================================ Bienvenue sur le Jeu '007' ================================\n")

while True:
  player_health = 50
  ia_health = 50
  shield = 3

  while ia_health > 0 and player_health > 0:

    ia_damage = random.randint(5,15)
    player_damage = random.randint(5,10)
    player_shield = random.randint(15,50)

    player_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion de soins (2) ?\nVotre saisie: ")
    while player_choice.isdigit() == False or int(player_choice) <= 0 or int(player_choice) > 2:
      player_choice = input("\nValeur non valide !\nVotre saisie: ")

    if int(player_choice) == 1:
      player_health -= ia_damage
      ia_health -= player_damage
      print(f"Vous avez infligé {player_damage} points de dégats 🗡️.")
      print(f"L'ennemi vous a infligé {ia_damage} points de dégats 🩸.\n\n")

      if player_health > 0 and ia_health > 0:
        print(f"Il vous reste {player_health} points de vie.")
        print(f"Il reste {ia_health} points de vie à l'ennemi.")

      elif player_health > 0 and ia_health <= 0:
        print(f"Il vous reste {player_health} points de vie.")
        print(f"Il reste 0 points de vie à l'ennemi.")

      elif player_health <= 0 and ia_health > 0:
        print(f"Il vous reste 0 points de vie.")
        print(f"Il reste {ia_health} points de vie à l'ennemi.")

      print("\n================================================================\n")

    elif int(player_choice) == 2:
      shield -= 1

      if shield >= 0:

        player_health -= ia_damage
        player_health += player_shield
        print(f"Vous avez récupérez {player_shield} points de vie 💉 (il vous reste {shield}🧪 restantes).")
        print(f"L'ennemi vous a infligé {ia_damage} points de dégats 🩸.\n\n")

        if player_health > 50:
          player_health = 50
          print("Vous avez atteint la limite de points de vie\n")
          print(f"Il vous reste {player_health} points de vie.")
          print(f"Il reste {ia_health} points de vie à l'ennemi.")

        else:
          print(f"Il vous reste {player_health} points de vie.")
          print(f"Il reste {ia_health} points de vie à l'ennemi.")

      else:
        print("\nVous avez utilisé toutes vos potions de soins.")

      print("\n================================================================\n")

  else:
    print("Fin de la partie.")

  if player_health > ia_health:
    print("Vous avez gagné !")
  elif player_health < ia_health:
    print("Vous avez perdu")
  else:
    print("Aucun vainqueur...")

  repeat = input("\nVoulez vous rejouer ?\nOui: 0\nNon: 1\nVotre saisie: ")
  while repeat.isdigit() == False or int(repeat) != 0 and int(repeat) != 1:
    print("\nValeur non valide.")
    repeat = input("Voulez vous rejouer ?\nOui: 0\nNon: 1\nVotre saisie: ")

  if int(repeat) == 0:
    continue
  else:
    print(exit())
