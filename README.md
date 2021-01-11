# Sudoku solver CBC

## Instructions 
- Install python 3.8
- Copy `cbcCInterfaceDll.dll` to the same directory as you python executable, e.g. `C:\Users\<Username>\AppData\Local\Programs\Python\Python38`
- Run in command prompt: `pip install mip`
- To run the solver: `python sudoku.py <inputfile> (optional_flags)`

I have also implemented some constraints for common sudoku variants. Currently, these include
- anti-consecutive sudoku (-ac, --anticonsecutive)
- anti-king sudoku (-ak, --antiking)
- anti-knight sudoku (-an, --antiknight)
- diagonal sudoku (-d, --diagonal)

You can indicate that you want the solver to take these variant rules into account by using the corresponding flag after the filename. 
For example, if you wanted to solve Mitchell Lee's 'miracle sudoku' as shown [here](https://youtu.be/yKf9aUIxdb4), then this can be done by running `python sudoku.py sudoku_miracle.txt -ac -ak -an` or `python sudoku.py sudoku_miracle.txt --anticonsecutive --antiking --antiknight`