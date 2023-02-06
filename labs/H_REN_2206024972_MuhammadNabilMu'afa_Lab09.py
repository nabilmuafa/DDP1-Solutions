# Lab 09 DDP 1 - H
#
# Dikerjakan oleh Muhammad Nabil Mu'afa - 2206024972

from random import *

class Entity:
    def __init__(self, name, hp, atk):
        self.__name = name
        self.__hp = hp
        self.__atk = atk

    def set_hp(self, hp):
        self.__hp = hp

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_atk(self):
        return self.__atk

    def attack(self, other):
        other.take_damage(self.get_atk())

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)

    def is_alive(self):
        return self.get_hp() > 0

class Player(Entity):
    def __init__(self, name, hp, atk, defense):
        super().__init__(name, hp, atk)
        self.__defense = defense

    def get_defense(self):
        return self.__defense

    def take_damage(self, damage):
        dmg_taken = damage - self.get_defense()
        if dmg_taken > 0:
            self.set_hp(self.get_hp() - dmg_taken)

class Boss(Entity):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

    def attack(self, other):
        other.take_damage(self.get_atk() + other.get_defense())

def print_enemy(depram, enemy):
    """Fungsi yang mencetak status battle"""
    print(f"{enemy.get_name()} muncul!\n")
    print("---Status---")
    print(f"{enemy.get_name():20}HP: {enemy.get_hp()}")
    print(f"{depram.get_name():20}HP: {depram.get_hp()}")
    print("------------")

def battle(depram, enemy):
    """Fungsi yang menjalankan battle"""
    running = True
    # Giliran pertama adalah Depram
    turn = "Depram"
    # Menjalankan battle selama running == True
    while running:
        if turn == "Depram":
            # Jika giliran Depram, maka Depram menyerang dan giliran berubah ke enemy
            depram.attack(enemy)
            print(f"Depram menyerang {enemy.get_name()} dengan {depram.get_atk()} ATK!")
            turn = "enemy"
        else:
            # Jika giliran enemy, maka enemy menyerang dan giliran berubah ke Depram
            depram_hp = depram.get_hp()
            enemy.attack(depram)
            print(f"{enemy.get_name()} menyerang Depram dengan {depram_hp - depram.get_hp()} ATK!")
            turn = "Depram"
        if not depram.is_alive() or not enemy.is_alive():
            # Akan mengubah running jadi False jika HP salah satu ada yang <= 0
            running = False
    return turn

def main():
    # Meminta input
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))
    depram = Player("Depram", 100, atk, defense)

    # Mengenerate musuh secara random
    enemy_list = [Entity(f"Enemy {i}", randint(20, 100), randint(10, 30))
                    for i in range(randint(0,1))]
    enemy_list.append(Boss("Final Boss", randint(20, 100), randint(10, 30)))

    print(f"Terdapat {len(enemy_list)} musuh yang melawan Depram!")
    print("------------")
    # Iterasi setiap musuh
    for enemies in enemy_list:
        # Mencetak pesan status battle
        print_enemy(depram, enemies)
        # Melakukan battle melalui fungsi battle()
        hasil = battle(depram, enemies)
        # Jika turn terakhir adalah enemy, artinya enemy kalah
        if hasil == "enemy":
            print(f"{enemies.get_name()} telah kalah!")
            print("------------\n")
        # Jika turn terakhir adalah Depram, maka Depram kalah dan program exit
        else:
            print("------------\n")
            print("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            exit()
    # Jika for loop mencapai akhir maka semua musuh Depram sudah kalah
    print("Selamat! Semua musuh Depram telah kalah!")    
    
if __name__ == "__main__":
    main()