# printdat
PrintDat is a python program that generates a data file (.dat) based off the value of select pixels in the image and then can be executed by PrintDat.bas (GW-BASIC program) and is designed to be used by an FX-80 dot-matrix printer.

WARNING: Some GW-BASIC printer drivers change the output going to the printer and may cause unexpected results. I am currently dealing with this on a Tandy 1400 FD. (will likely re-write program to print in smaller group sizes. This will likely change the printdat.bas program.

Use of the program looks like:

<img width="969" height="83" alt="Screenshot 2025-07-28 002508" src="https://github.com/user-attachments/assets/da993c6b-a104-4575-8c58-be2c0a5ea3e1" />


This will output a preview of the image that is not an exact representation but should give a general idea before it is printed, due to ASCII output being less "square" it is adjusted to correct for some distortion via the calibration variable outputArrCali. It should also be noted that the matrix is generated with its own calibration variable based off of the printer to correct for distortion (or if you use doubble-density or other that changes the ratio) this variable is "calibration".


The bottom of the file output will produce:

<img width="660" height="45" alt="image" src="https://github.com/user-attachments/assets/827b7f83-e49d-4046-ac29-04e1d9c5f66b" />

This is fine, this is saying that the image was did not exactly generate a matrix that was divisible by 7 in the y direction.

After the .dat file is generated, the .dat file and the PrintDat.bas file can be transfered to the computer capable of LPRINT (with printer connected) via GW-BASIC for printing the .dat file.
To be clear: The PrintDat.bas file does not need to be replaced everytime the .dat file is changed as it prints based off ot the .dat file.
Furthermore: you can do "ECHO BASIC PRINTDAT.BAS > PRINTDAT.BAT" so that the program can be ran by simply entering PRINTDAT at the command prompt.
