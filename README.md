# Sudoku solver CBC

## Instructions 
- Install python 3.8
- Copy `cbcCInterfaceDll.dll` to the same directory as your python executable, e.g. `C:\Users\<Username>\AppData\Local\Programs\Python\Python38`
- Run `pip install mip`
- To run the solver: `python sudoku.py <inputfile>`

I have also implemented some constraints for common sudoku variants. Currently, these include
- anti-consecutive sudoku (-ac, --anticonsecutive)
- anti-king sudoku (-ak, --antiking)
- anti-knight sudoku (-an, --antiknight)
- diagonal sudoku (-d, --diagonal)
- killer sudoku (-k, --killer)

You can indicate that you want the solver to take these variant rules into account by using the corresponding flag after the filename. 
For example, if you wanted to solve Mitchell Lee's 'miracle sudoku' as shown [here](https://youtu.be/yKf9aUIxdb4), then this can be done by running `python sudoku.py examples\sudoku_miracle.txt -ac -ak -an` or `python sudoku.py examples\sudoku_miracle.txt --anticonsecutive --antiking --antiknight`

If you want to solve a killer sudoku, then as before, you need to provide the .txt file with any starting numbers, however you also need to follow this with information about the regions in the grid. A region is described by writing the row, col coordinates (0-8) of all the cells in that region, followed by what they sum to. If there is no given sum, then this should be 0. Do this for all regions and separate each of them with a comma to get it into the required format for the solver to solve. I have taken some care in trying to make it so that any line breaks or spaces don't break it, so don't worry about doing it over multiple lines if it begins to get messy.

Then, as before, it is solved by running `python sudoku.py examples\killer_antiknight.txt -k -an`
You can see the sources of the killer sudoku examples at the following links to ensure that you understand how the notation works.

[killer anticonsecutive](https://app.crackingthecryptic.com/sudoku/j3m76TrmfD)  
[killer antiknight](https://i2.wp.com/www.djape.net/wp-content/uploads/2010/05/S001-M-AN.png)  
[killer easy](https://www.dailykillersudoku.com/puzzle/684)  
[killer hard](https://www.dailykillersudoku.com/puzzle/21332)  