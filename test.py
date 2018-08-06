import random
MATRIX_SIZE = 3


def is_cell_alive_dead_or_hibernating(cellValue):
    if cellValue >= 0.7:
        return "ALIVE"
    elif cellValue >= 0.4:  
        return "HIBERNATING"
    else:
        return "DEAD"


def build3dMatrixOfCells():
    array = []
    third_counter = 0
    while third_counter < MATRIX_SIZE: 
        outer_counter = 0
        outer_array = []
        array.append(outer_array)
        
        outer_counter = 0
        while outer_counter < MATRIX_SIZE:
            inner_counter = 0
            inner_array = []
            outer_array.append(inner_array)
            
            while inner_counter < MATRIX_SIZE:
                random_value = random.random()
                cell_state = is_cell_alive_dead_or_hibernating(random_value)
                
                inner_array.append(cell_state)
                
                inner_counter += 1
            outer_counter +=1
        third_counter = third_counter + 1
    return array



def cellstatecounter(cells):
    counter1 = 0
    numberDead = 0
    numberAlibve = 0
    numberHibernate = 0
    while counter1 < len(cells):
        xAxisListElement = cells[counter1]
        counter2 = 0 
        while counter2 < len(xAxisListElement):
            yAxisListElement = xAxisListElement[counter2]
            counter3 = 0
            while counter3 < len(yAxisListElement):
                cellValue = yAxisListElement[counter3]
                if cellValue ==  "ALIVE":
                    numberAlibve += 1
                elif cellValue == "HIBERNATING":  
                    numberHibernate += 1 
                else:
                    numberDead += 1
                counter3 += 1   
            counter2 += 1
        counter1 += 1
    return {
        "ALIVE":numberAlibve, "HIBERNATE":numberHibernate, "DEAD":numberDead, "WHATISMOST":mostAliveDeadOrHibernatin(numberAlibve, numberDead, numberHibernate)
    }
   

 
def mostAliveDeadOrHibernatin(numberAlibve, numberDead, numberHibernate):
    if  (numberAlibve > numberDead) and (numberAlibve > numberHibernate):
        return  "ALIVE"
    elif (numberHibernate > numberDead) and (numberHibernate > numberAlibve):
        return "HIBERNATING"
    else:
        return "DEAD"


#inner_array[inner_counter]

cells = build3dMatrixOfCells()
whatIsMost = cellstatecounter(cells)
print ("2")
