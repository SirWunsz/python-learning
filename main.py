MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_manegment(resources, ask_machine):
  milk = resources["milk"]
  water = resources["water"]
  coffee = resources["coffee"]

  if ask_machine in MENU:
    milk_coffe = MENU[ask_machine]["ingredients"]["milk"]
    water_coffe = MENU[ask_machine]["ingredients"]["water"]
    coffee_coffee = MENU[ask_machine]["ingredients"]["coffee"]

    if (milk > milk_coffe and
        water > water_coffe and
        coffee > coffee_coffee):
        resources["milk"] -= milk_coffe
        resources["water"] -= water_coffe
        resources["coffee"] -= coffee_coffee
        do_coffe = "yes"
        return do_coffe
    else:
      do_coffe = "no"
      print("Za mało zasobów na produkcję kawy")
      return do_coffe


def got_coins(ask_machine):
    coffe_price = MENU[ask_machine]["cost"]
    got_money = float(input("Wsadź 1 groszówki: "))/100
    got_money += float(input("Wsadź 2 groszówki: "))/100 * 2
    got_money += float(input("Wsadź 5 groszówki: "))/100 * 5
    got_money += float(input("Wsadź 10 groszówki: "))/100 * 10
    got_money += float(input("Wsadź 50 groszówki: "))/100 * 50
    got_money += float(input("Wsadź 1 złotówki: "))

    if coffe_price <= got_money:
      change = got_money - coffe_price
      print(f"Proszę oto twoja reszta {change} zł")
      print("Oto wtoja kawa, smacznego")
    else:
      print(f"Dałeś {got_money} kawa kosztuje {coffe_price}\
              transakcja odrzucona o to twoje pieniądze")


ask_machine = input("Witam na jaką kawę masz ochotę espresso, latte, cappuccino: ")


while ask_machine != "off":

  if ask_machine == "help":
      print("Lista dostępnych komend: On, off, espresso, latte,\
              cappuccino, raport, help")
  elif ask_machine == "raport":
      print(f"Pozostało: \n{resources['milk']}ml mleka, \
      \n{resources['water']}ml wody \n{resources['coffee']}g kawy")
  elif ask_machine in MENU:
      do_coffe = resources_manegment(resources, ask_machine)
      if do_coffe == "yes":
        got_coins(ask_machine)


  ask_machine = input("Witam na jaką kawę masz ochotę espresso,\
                        latte, cappuccino: ")
if ask_machine == "off":
  print("Wyłaczony modół w celu naprawy")
