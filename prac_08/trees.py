"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random

TREE_LEAVES_PER_ROW = 3


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """ represent an even tree, one that only grows leaves in full rows """

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):
    """Represent an upside-down tree; like a normal tree, but upside-down."""

    def __str__(self):
        """Return a string representation of the full tree,
        upside-down compared to a normal tree."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree, e.g.
 #####
 ######
 ######
   ||
   ||  """

    def __init__(self):
        """Initialise WideTree with trunk 2 wide"""
        super().__init__()
        self._leaves *= 2

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += "  || \n"
        return result

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * (TREE_LEAVES_PER_ROW * 2)
            result += "\n"
        return result


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow a faster tree based on sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water*2)
        self._leaves += random.randint(0, sunlight*2)


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves, e.g.
.
...
##
###
###
 |
 |  """
    def __init__(self):
        """Initialise FruitTree with fruit"""
        super().__init__()
        self._fruit = 1

    def __str__(self):
        """Return string of FruitTree"""
        return self.get_ascii_fruit() + super().__str__()

    def grow(self, sunlight, water):
        """Grow fruit on a fruit Tree"""
        super().grow(sunlight, water)

        chance_to_add_fruit = 0.5
        if random.randint(1, 2)/2 < chance_to_add_fruit:
            self._fruit += 1
        chance_to_lose_fruit = 0.2
        if random.randint(1, 5)/5 < chance_to_lose_fruit:
            self._fruit -= 1

    def get_ascii_fruit(self):
        """Print number of fruit on FruitTree"""
        result = ""
        result += "." * self._fruit
        result += "\n"

        return result


class PineTree(Tree):
    """Represent a pine tree, e.g.
   *
  ***
 *****
*******
   |
   |    """
    def __init__(self):
        super().__init__()
        self._rows = 0

    def grow(self, sunlight, water):
        """Grow a PineTree starting from 1+3, _rows++"""

    def get_ascii_leaves(self):
        """Dynamically position pineleaves from height"""
        j = self._rows * 2 - 1  # Previous space value

        self._rows += 1

        i = self._rows * 2 - 1  # = 1, 3, 5, 7 ...
        k = self._rows * 2 + 1
        result = "{}*\n".format(" " * i)
        result += "{}***\n".format(" " * (i -1))

        # Starts from rows=2
        for n in range(1, self._rows):
            result += "{}{}\n".format(" " * (j), "*" * k)

        return result

    def get_ascii_trunk(self):
        """Dynamically position trunk according to height"""
        centre = 1
        centre += self._rows

        return "{}|".format(" " * centre)
