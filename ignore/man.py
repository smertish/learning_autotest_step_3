from base_person import Person, Warrior

man = Person("Алекс", 30, 180)
man.description_person()

warrior = Warrior("Конан", 30, 200)
print("Нового человека зовут: " + warrior.description_person())
