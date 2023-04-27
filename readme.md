My algorithm first processes input by storing the count and maximum capacity
of the list of items, and then stores each item as a dictionary.

This processes information is then passed to generate_value_table, where a table
is created. This table has rows that represent each item in the list of items, 
and columns that represent capacities from 0 to the maximum capacity. So if 
there were 5 items and the maximum capacity was 15, there would be 5 rows and
16 columns.

The table is filled based on the weight and value of the current item. 

- If the current item's weight exceeds the current column's capacity, the 
current cell is filled by the value of the cell above it.

- If the current item's weight fits in the current column's capacity, the 
current cell is filled based on the maximum of the two below values:
    - value of the cell directly above the current cell.
    - value of the current item + value of the next cell where the current 
    item's weight can fit.

The items are then selected from the table by comparing the cell values to the
item values, and determining which items are the best choice.

This program's algorithmic runtime is O(nW) where n is the number of items in the
list and W is the maximum capacity. The reason it's O(nW) is because the table
being used to calculate the best combination of items has n rows and W + 1 columns,
and each cell in the table is only ever visited once. The algorithm does not have
to go back over the cells to make more calculations.