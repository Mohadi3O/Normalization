
from  PyQt5.QtWidgets  import *
from PyQt5 import QtCore, uic

from PyQt5.QtGui import QFont
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import pandas as pd
from PyQt5.QtWidgets import QWidget
from binarytree import Node


# ===========================================================================================
# ===========================================================================================
# ===========================================================================================

import tkinter as tk

class TrueFalseDialog:
    def __init__(self, var,width=300, height=150, background_color="white", text_color="black"):
        self.root = tk.Tk()
        self.root.title("True/False Dialog")
        self.root.configure(bg=background_color)  # Set the background color of the root window
        self.result = None

        # Set the window size
        self.root.geometry(f"{width}x{height}")

        self.label = tk.Label(self.root,text=f"\tChoose the vlaue of \" {var} \":", bg=background_color, fg=text_color)  # Set text and background color of the label
        self.label.pack(pady=10)

    def choose_true(self):
        self.result = True
        self.root.destroy()

    def choose_false(self):
        self.result = False
        self.root.destroy()

    def get_user_choice(self):
        true_button = tk.Button(self.root, text="True", command=self.choose_true, bg="lightgreen", fg="black")  # Set text and background color of the button
        true_button.pack(padx=10, pady=5)

        false_button = tk.Button(self.root, text="False", command=self.choose_false, bg="lightcoral", fg="black")  # Set text and background color of the button
        false_button.pack(padx=10, pady=5)

        self.root.mainloop()
        return self.result


# ===========================================================================================
# ===========================================================================================
# ===========================================================================================
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn_list=[]
        self.CNF=[]
        uic.loadUi('UI.ui',self)
        self.Validate=self.findChild(QPushButton,'Validate')
        self.Validate.clicked.connect(lambda:self.val())
        self.input_screen=self.findChild(QLineEdit,'seq')
        self.comp=self.findChild(QPushButton,'compile')
        self.comp.clicked.connect(lambda:self.F_N_C()) # type: ignore
        self.clear=self.findChild(QPushButton,'clear')
        self.simpl=self.findChild(QTextEdit,'simplify')
        self.cnf=self.findChild(QTextEdit,'cnf')
        self.clear=self.findChild(QPushButton,f"clear")
        self.clear.clicked.connect(lambda:self.cl()) # type: ignore
        self.show()
    def cl(self):
        self.input_screen.setText("" ) # type: ignore
        self.cnf.setText("" ) # type: ignore
        self.simpl.setText("" ) # type: ignore
    def add_to_CNF_screen(self,word):
        self.cnf.setText(self.cnf.toPlainText()+"\n\n\n"+ word)
    def add_to_simplify_screen(self,word):
        self.simpl.setText(self.simpl.toPlainText()+"\n\n\n"+ word)
        
    def distribute_possible(self,root):
        copy_root = copy_tree(root)
        while distribute_disjunction(copy_root):
            self.add_to_CNF_screen("="*100 + "\n")
            self.add_to_CNF_screen("distribute_disjunction loop")
            self.add_to_CNF_screen(show_tree(copy_root))



        return copy_root    
    def F_N_C(self):
        self.cnf.setText("" ) # type: ignore
        self.simpl.setText("" ) # type: ignore
        postfix_formula=infix_To_postfix(self.input_screen.text())
        
        root = create_tree(postfix_formula)
        self.add_to_CNF_screen("My Tree is")
        
        self.add_to_CNF_screen(show_tree(root))
        self.add_to_CNF_screen("eliminate_equivalence_and_implication")
        root_CNF = eliminate_equivalence_and_implication(root)
        self.add_to_CNF_screen(show_tree(root_CNF))
        
        root_CNF = reduce_negation(root_CNF)
        self.add_to_CNF_screen("reduce_negation :")
        self.add_to_CNF_screen(show_tree(root_CNF))
        self.add_to_CNF_screen("distribute_possible :")
        root_CNF = self.distribute_possible(root_CNF)
        self.add_to_CNF_screen("conjunctive_normal_form :")
        FNC = conjunctive_normal_form(root_CNF)
        
        self.add_to_CNF_screen("Final CNF  : \n\n\n"+ str(display_formula(FNC)))
        

        FNC_p = simplify_repeated_propositions(FNC)
        self.add_to_simplify_screen("My formula after (simplify_repeated_propositions) :\n\n\n"+str( display_formula(FNC_p)))

        
        FNC_t, I_can_eliminate = A_and_not_A_simplification(FNC_p)
        while I_can_eliminate:
            FNC_t, I_can_eliminate = A_and_not_A_simplification(FNC_t)
            
        self.add_to_simplify_screen("My formula after (A_and_not_A_simplification)\n now we test if A and ~A in same clause :\n\n\n"+ str(display_formula(FNC_t)))
        self.add_to_simplify_screen("="*50)
        
        fnc_clauses, I_can_eliminate = simplify_repeated_clauses(FNC_t)
        while I_can_eliminate:
            fnc_clauses, I_can_eliminate = simplify_repeated_clauses(fnc_clauses)
            
        self.add_to_simplify_screen("My formula after (simplify_repeated_clauses) :\n\n\n"+ str(display_formula(fnc_clauses)))
        self.add_to_simplify_screen("="*50)
        fnc_final = eliminate_repeated_clauses(fnc_clauses)
        
        self.add_to_simplify_screen("Final simplify :\n\n\n"+ str(display_formula(fnc_final)))
        self.add_to_simplify_screen("="*50)
        self.postfix=infix_To_postfix(str(display_formula(fnc_final)).replace(" ",""))
        
        
    def val(self):
        variables = list(char for char in self.postfix if char.isalpha())
        num_variables = len(variables)
        rows = list(set(variables))
        # dialog = TrueFalseDialog(width=400, height=200, background_color="lightblue", text_color="black")
        values={}
        for i in range(len(rows)):
            dialog = TrueFalseDialog(width=400, height=200, background_color="lightblue", text_color="black",var=variables[i])
            
            user_choice=dialog.get_user_choice() 
            values[rows[i]] =  user_choice

        return self.evaluate_postfix_expression_for_my_teacher( values)




    def evaluate_postfix_expression_for_my_teacher(self, values):
        stack = []
        # self.Truth_table.setText("")# type: ignore
        
        self.add_to_simplify_screen("\t\t\t The results : ")
        postfix_expression=list(self.postfix)
        
        def process_operator(operator, left, right):
            if operator == '~':
                result = not left
            elif operator == '#':
                result = left == right
            elif operator == '&':
                result = left and right
            elif operator == '|':
                result = left or right
            elif operator == '>':
                result = not left or right
            else:
                raise ValueError("Invalid operator: {}".format(operator))
            return result
#  he<span class="form">ll</span><span class="result">o</span>
        for char in postfix_expression:
            if char.isalpha():
                value = values.get(char, "Key not found in dictionary")
                self.add_to_simplify_screen(f'\nThe value of [ {char} ] is :\t{value}')
                stack.append(value)
            else:
            
                if char == '~':
                    operand = stack.pop()
                    result = not operand
                    self.add_to_simplify_screen(f'\nThe value of [ not {operand} ]  is :\t{result} ')
                else:
                    right = stack.pop()
                    left = stack.pop()
                    result = process_operator(char, left, right)
                    self.add_to_simplify_screen(f'\n\tThe value of [ {left} {char} {right} ] is :\t{result} ')
                stack.append(result)

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        self.add_to_simplify_screen(f"\n======> the result is :\t{stack.pop()} <======\n")






# Importing necessary ANSI escape codes for colored output


from binarytree import build

def postfix_to_logic_tree(postfix):
    stack = []
    chars={"|":'OR',"&":"AND","#":"equals",">":'implication'}
    for char in postfix:
        if char.isalpha():
            stack.append(Node(char))
        else:
            right = stack.pop()
            if char == '~':
                node = Node("NOT", right=right)
            else:
                left = stack.pop()
                
                node = Node(chars[char], left=left, right=right)
            stack.append(node)

    tree = stack.pop()
    return tree

# Example usage:






def print_logic_tree(postfix:str):
    
    
    stack = []
    
    for char in postfix:
        if char.isalpha():
            stack.append(Node(char))
        else:
            right = stack.pop()
            if char == '¬':
                node = Node("NOT", right=right)
            else:
                left = stack.pop()
                node = Node(char, left=left, right=right)
            stack.append(node)

    tree = stack.pop()
    return tree
# Creating a string of stars with red color for formatting


# List of logical operators
operators = "~>#&|"

# Definition of the LogicTree class representing a node in the logical tree
class LogicTree:
    def __init__(self, value,right = None,left = None):  # Constructor for initializing a node
        self.value = value
        self.right = right
        self.left = left
    def tree_to_postfix(self,root):
        """
        Convert a logical tree to its postfix representation.

        :param root: The root of the logical tree.
        :return: A string representing the postfix notation of the logical tree.
        """
        postfix_list = []

        def traverse(node):
            if node:
                traverse(node.right)
                traverse(node.left)
                postfix_list.append(node.value)

        traverse(root)
        return ''.join(postfix_list)
    @staticmethod
    def tree_to_list(root, node_list: list):  # Static method to convert a tree to a list
        if root.right:  # Non-null right child
            LogicTree.tree_to_list(root.right, node_list)  # Recursive call
        node_list.append(root.value)  # Add the value of the root to the list
        if root.left:  # Non-null left child
            LogicTree.tree_to_list(root.left, node_list)  # Recursive call

# Function to convert an infix logical formula to postfix
def infix_To_postfix(infix_formula: str):
    postfix_formula = ""
    stack = []
    operators = "|&~>#()"
    priority_of_operators = {"~": 1, "&": 2, "|": 2, ">": 3, "#": 3}

    for char in infix_formula:
        if char in operators:
            if char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix_formula += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != "(" and priority_of_operators[char] >= priority_of_operators[stack[-1]]:
                    postfix_formula += stack.pop()
                stack.append(char)
        else:
            postfix_formula += char

    while stack:
        postfix_formula += stack.pop()

    return postfix_formula

# Function to create a logical tree from a postfix expression
def create_tree(postfix):
    stack = []
    for char in postfix:
        if char in operators:
            root = LogicTree(char)
            if char == '~':
                root.left = stack.pop(0)
            else:
                root.left = stack.pop(0)
                root.right = stack.pop(0)
            stack.insert(0, root)
        else:
            stack.insert(0, LogicTree(char))

    return stack.pop()

# Function to copy a logical tree
def copy_tree(node):
    new_node = LogicTree(node.value)
    if node.right:
        new_node.right = copy_tree(node.right)
    if node.left:
        new_node.left = copy_tree(node.left)
    return new_node

#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
####################################################################################################

# Function to eliminate equivalence and implication in a logical tree
def eliminate_equivalence_and_implication(node): #   implication : >    equivalence  : #
    if node.value == '#':
        child_1 = LogicTree('>',right = copy_tree(node.right),left = copy_tree(node.left))
        child_2 = LogicTree('>',right = copy_tree(node.left),left = copy_tree(node.right))
        new_node = LogicTree('&',right = child_1,left = child_2)

    elif node.value == '>':
        negation = LogicTree('~',left = copy_tree(node.right))

        new_node = LogicTree('|',right = negation,left = copy_tree(node.left))

    else:
        new_node = copy_tree(node)
        
    if new_node.right:
        new_node.right = eliminate_equivalence_and_implication(new_node.right)
    if new_node.left:
        new_node.left = eliminate_equivalence_and_implication(new_node.left)
    return new_node



#################################################################################################### 
#################################################################################################### 


# Function to reduce negation in a logical tree
def reduce_negation(node):
    new_node = LogicTree(None)
    if node.value == '~' and node.left.value == '~':  #  for case of '~~'
        new_node = node.left.left
    elif node.value == '~' and ((node.left.value == '&') or (node.left.value == '|')):
        if node.left.value == '&':
            node.left.value = '|'
        else:
            node.left.value = '&'
        right_negation = LogicTree('~',left = node.left.right)

        node.left.right = right_negation
        left_negation = LogicTree('~',left = node.left.left)
        node.left.left = left_negation
        new_node = node.left
    else:
        new_node = copy_tree(node)

    if new_node.right:
        new_node.right = reduce_negation(new_node.right)
    if new_node.left:
        new_node.left = reduce_negation(new_node.left)
    return new_node



#################################################################################################### 
#################################################################################################### 

# Function to distribute disjunction in a logical tree
def distribute_disjunction(node):
    repeat_1 = False
    repeat_2 = False
    repeat_3 = False
    if node.value == '|':
        if node.left.value == '&':

            Right = LogicTree('|',right = copy_tree(node.right), left = copy_tree(node.left.right))
            Left = LogicTree('|' ,right = copy_tree(node.right) , left = copy_tree(node.left.left))

            node.value = '&'
            node.right = Right
            node.left = Left
            repeat_1 = True
            
        if node.right.value == '&':
            
            Right = LogicTree('|',right = copy_tree(node.right.right),left = copy_tree(node.left))
            Left = LogicTree('|',right = copy_tree(node.right.left),left = copy_tree(node.left))

            node.value = '&'
            node.right = Right
            node.left = Left
            repeat_1 = True
    if node.right:
        repeat_2 = distribute_disjunction(node.right)
    if node.left:
        repeat_3 = distribute_disjunction(node.left)
    return (repeat_1 or repeat_2 or repeat_3)


#################################################################################################### 
#################################################################################################### 

# Print the tree 
def show_tree(root:LogicTree):
        copy_root=copy_tree(root)
        pos=copy_root.tree_to_postfix(copy_root)
        return  "\n Postfix : " + str(pos)+"\n"+str(postfix_to_logic_tree(pos))
        


#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 


# Function to convert a logical tree to conjunctive normal form (FNC)
def conjunctive_normal_form(root):
    nodes_list = []
    LogicTree.tree_to_list(root, nodes_list)
    clauses_list = []
    i = 0
    clause = []
    while i < len(nodes_list):
        if nodes_list[i] == '~':
            clause.append(nodes_list[i] + nodes_list[i + 1])
            i += 1
        elif nodes_list[i] == '&':
            clauses_list.append(clause)
            clause = []
        else:
            clause.append(nodes_list[i])
        i += 1
    clauses_list.append(clause)
    return clauses_list

#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 


# Function to display the formula from a list of clauses
def display_formula(clauses):
    FNC = ['(']
    i = 0
    while i < len(clauses):
        FNC += clauses[i]
        FNC.append(') & (')
        i += 1
    FNC.pop()
    FNC.append(')')
    return ''.join(FNC)

#################################################################################################### 
####################################################################################################

# Function to simplify repeated propositions within the same clause
# now we test if A and ~A in same clause
def A_and_not_A_simplification(clauses: list):
    elimination = False
    for i in range(len(clauses)):
        j = 0
        while i < len(clauses) and j < len(clauses[i]):
            if clauses[i][j] == '|':
                j += 1
            else:
                if clauses[i][j].isalpha():
                    negation_proposition = '~' + clauses[i][j]
                    if ((clauses[i][j] in clauses[i]) and (negation_proposition in clauses[i])):
                        clauses.remove(clauses[i]) # becouse we have 1 
                        elimination = True
                    j += 1
                j += 1
    return clauses, elimination

#################################################################################################### 
#################################################################################################### 


# Function to simplify repeated propositions within each clause
# for letters
def simplify_repeated_propositions(clauses: list):
    for i in range(len(clauses)):
        j = 0
        while j < len(clauses[i]):
            if clauses[i][j] == '|':
                j += 1
            else:
                while clauses[i].count(clauses[i][j]) > 1:
                    clauses[i].pop(j) # for latter or ~latter
                    clauses[i].pop(j) # for its oparetor
                j += 1
    return clauses

    
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
####################################################################################################

# Function to simplify repeated clauses within the formula
# test if A in B
def simplify_repeated_clauses(clauses: list):
    for i in range(len(clauses)):
        elimination = False
        j = 0
        while j < len(clauses):
            if i < len(clauses) and j < len(clauses) and i != j and len(clauses[i]) < len(clauses[j]):
                exist = True
                for k in range(len(clauses[i])):
                    if clauses[j].count(clauses[i][k]) == 0:
                        exist = False
                        j += 1
                        break
                if exist == True:
                    clauses.pop(j)
                    elimination = True
            else:
                j += 1
    return clauses, elimination

#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
####################################################################################################

# Function to eliminate repeated clauses within the formula
# for clauses 
def eliminate_repeated_clauses(clauses: list):
    i = 0
    while i < len(clauses):
        while clauses.count(clauses[i]) > 1:
            clauses.remove(clauses[i])
        i += 1
    return clauses

#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
#################################################################################################### 
####################################################################################################

if __name__=='__main__':
    app=QApplication(sys.argv)
    jj=Main()
    app.exec_()
