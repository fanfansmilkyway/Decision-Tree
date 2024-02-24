branches = []
fruits = []

class Tree:
    """Create a decision tree"""
    def __init__(self, name:str):
        self.name = name
        self.open = True

    def show():
        pass

    def add_branch(self, father, condition:tuple, name:str=''):
        """Create a decision branch"""
        if father.__class__ != Branch and father.__class__ != Tree:
            raise TypeError("Incorrect 'father' augument for Branch. It should be Tree or Branch.")
        new_branch = Branch(father=father, condition=condition, name=name)
        branches.append(new_branch)
        return new_branch # Return a object

class Branch(): # !: User cannot use this class, only create branch by Tree.add_branch
    def __init__(self, father, condition:tuple, name:str=''):
        self.father = father  # Branch or Tree
        self.open = False # Branch is open or close. False for close, True for open.
        if self.father.__class__ != Branch and self.father.__class__ != Tree:
            raise TypeError("Incorrect 'father' augument for Branch. It should be Tree or Branch.")
        
        # Give default name to the branch if user doesn't set
        if name == '':
            self.name = "Branch Without Name"
        else:
            self.name = name

        self.condition = condition
        print(self.condition)
        self.detect_target = self.condition[0]
        self.operator = self.condition[1]
        self.expected_value = self.condition[2]
        number_types = [int, float, complex, list, tuple, bool]
        
        # Because of different inputs types, so we need different ways to process them.
        # Divide inputs to two types: number(bool) or string
        if type(self.detect_target) in number_types:
            if type(self.expected_value) in number_types:
                self.condition_statement = f"{self.detect_target} {self.operator} {self.expected_value}"
            else:
                self.condition_statement = f"{self.detect_target} {self.operator} '{self.expected_value}'"
        else:
            if type(self.expected_value) in number_types:
                self.condition_statement = f"'{self.detect_target}' {self.operator} {self.expected_value}"
            else:
                self.condition_statement = f"'{self.detect_target}' {self.operator} '{self.expected_value}'"

        print(self.condition_statement)
        if eval(self.condition_statement):
            if self.father.open == True:
                self.open = True

class Fruit: # Fruit represents result
    def __init__(self, father, value):
        self.father = father  # Branch
        if self.father.__class__ != Branch and self.father.__class__ != Tree:
            raise TypeError("Incorrect 'father' augument for Fruit. It should be Tree or Branch.")
        self.value = value
        fruits.append(self)


a = "hello"
tree = Tree(name="Tree")
fruit = Fruit(father=tree, value=10)
b1 = tree.add_branch(father=tree, condition=(10,"==",10))
b2 = tree.add_branch(father=tree, condition=(9,">=",10))
b3 = tree.add_branch(father=b1, condition=(0,"==",1))
b4 = tree.add_branch(father=b1, condition=([10,10],"==", [10,10]))
b5 = tree.add_branch(father=b2, condition=(a, '==', 'hello'))
b6 = tree.add_branch(father=b2, condition=(a, '==', 'Hello'))

for branch in branches:
    print(branch.name + " :", branch.open, branch.father.name)
print(branches, fruits)
