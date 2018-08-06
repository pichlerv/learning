'''
a live cell will continue with min. 2 max. 3 live neighbours.
a dead cell will become live with 3 live neighbours.
a live cell will become dead with > 7 dead neighbours
a live cell will become dead with < 4 dead neighbours


initialize
build a grid of 100 x 100
randomly assign alive or dead to each cell

generation
    iterate through each cell
        check cell suroundings
        count number of live cells
        produce new state FOR CELL
    each generation is isloated
    PRINT NEW GENERATION TO SCREEN

'''


'''

     0 1 2 3 4
0    x 0 0 0 x
1    x 0 0 0 x
2    x 0 0 x x


(0,0) => (0,1);(1,0);(1,1)
(1,2) => (0,1);(0,2); ()
(x,y) => 
where x > 0 and y > 0 and  x < (len(xaxis) -1) and y < (len(yaxis)-1)
 (x -1, y -1); (x , y -1); (x+1, y-1) ; (x -1, y ); ; (x+1, y) ; (x -1, y +1); (x , y +1); (x+1, y+1) ;
need to consider edges


'''