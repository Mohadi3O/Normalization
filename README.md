# ***Normalization of propositional logic formulas theory***
The objective of this practical work is to create a program which performs the syntactic analysis of formulas of the logic of ´
propositions, evaluates them, and simplifies them after having put them in normal form. `
1. Starting from the syntax seen in the course, write a program that transforms the formulas (we ´
assume they are well trained). Represent the connectors respectively by: ´ ∼, &,|,> and
#.
For example: p∨ ¬q ⇒ r will be written ´ p |∼ q > r
2. The program must also generate a tree representation of the formula. The main connector
cipal will position itself at the root of the tree. The wires of each connector (only one wire in the case `
of negation) are the subformulas representing the operands of this connector. ´
3. Knowing the truth value of each propositional variable, evaluate the formula (give its value
of truth). ´
4. Transform the formula into conjunctive normal form (CNF), that is to say, a conjunct
tion of clauses. A clause being a disjunction of literals. ´
5. Carry out the simplification of the standardized formula.
6. now i used python for programming it and i used pyqt5/6 and pyside6 for create a GUI for Easily to use
7. and i use binarytree lib for represent the tree in the output 
