# avid_draw
A tool for looking at the path of an organism in Avida.

Open avid draw and click run.  The program will prompt you for the location of the single_runs file location that you want to look at.  Avida draw will then find the environment file, as well as the .trace file, which avida draw assumes is in the /data/archive file of the you input.

Avida draw will then prompt you for the size of the grid.  A 25 by 25 grid is input as just a size of 25.

Avida draw will then open a python turtle window on your computer, which will display the grid from the environment file.  The program will then show the path the organism took on the grid.

Two pictures will be saved in the single_runs file you selected.  One of the grid, alone by itself labeled grid.eps.  The other one will be of the grid and the path the organism took, labeled path.eps. 
