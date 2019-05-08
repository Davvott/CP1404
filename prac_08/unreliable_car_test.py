"""Test UnreliableCar class functionality"""

from prac_08.unreliable_car import UnreliableCar

old_bomb = UnreliableCar("Old Bomb", 100, reliability=75)

print(old_bomb)
old_bomb.drive(40)
print(old_bomb)

another_bomb = UnreliableCar("Test 2", 95)
print(another_bomb)
another_bomb.drive(34)
print(another_bomb)

test_3 = UnreliableCar("Test 3", 100)
print(test_3)
test_3.drive(45)
print(test_3)
