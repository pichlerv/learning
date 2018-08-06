import random
import numpy as np
import time
MATRIX_SIZE = 3


def is_cell_alive_dead_or_hibernating(cellValue):
    if cellValue >= 0.7:
        return "-"
    elif cellValue >= 0.4:  
        return "0"
    else:
        return "X"


def build3dMatrixOfCells():
    array = []
    outer_counter = 0

    while outer_counter < MATRIX_SIZE:
        inner_counter = 0
        inner_array = []
        array.append(inner_array)
        
        while inner_counter < MATRIX_SIZE:
            random_value = random.random()
            cell_state = is_cell_alive_dead_or_hibernating(random_value)
            
            inner_array.append(cell_state)
            
            inner_counter += 1
        outer_counter +=1

    return array


 
def mostAliveDeadOrHibernatin(numberAlibve, numberDead, numberHibernate):
    if  (numberAlibve > numberDead) and (numberAlibve > numberHibernate):
        return  "ALIVE"
    elif (numberHibernate > numberDead) and (numberHibernate > numberAlibve):
        return "HIBERNATING"
    else:
        return "DEAD"


#inner_array[inner_counter]
appLoop = 0
while appLoop < 40:
    cells = build3dMatrixOfCells()
    print(np.matrix(cells))
    time.sleep(0.5)
    appLoop += 1