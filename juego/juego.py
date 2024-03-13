class AttackBehavior:
    def attack(self):
        pass


class SoldierAttack(AttackBehavior):
    def attack(self):
        print("El soldado ataca ")


class ArcherAttack(AttackBehavior):
    def attack(self):
        print("El arquero dispara ")


class KnightAttack(AttackBehavior):
    def attack(self):
        print("El caballero lanza")


class MovementBehavior:
    def move(self):
        pass


class SoldierMovement(MovementBehavior):
    def move(self):
        print("El soldado camina")


class ArcherMovement(MovementBehavior):
    def move(self):
        print("El arquero camina silenciosamente")


class KnightMovement(MovementBehavior):
    def move(self):
        print("El caballero corre.")


class MilitaryUnit:
    def __init__(self, attack_behavior, movement_behavior):
        self.attack_behavior = attack_behavior()
        self.movement_behavior = movement_behavior()

    def perform_attack(self):
        self.attack_behavior.attack()

    def perform_movement(self):
        self.movement_behavior.move()


soldier = MilitaryUnit(SoldierAttack, SoldierMovement)
archer = MilitaryUnit(ArcherAttack, ArcherMovement)
knight = MilitaryUnit(KnightAttack, KnightMovement)


soldier.perform_attack()
soldier.perform_movement()

archer.perform_attack()
archer.perform_movement()

knight.perform_attack()
knight.perform_movement()