# DynaMol
DynaMol is a molecular mechanics program written form scratch in python. It can be used to calculate the interactions, bonds, energies, movements and optimally stable configurations of simple carbohydrate molecules. For an in Detail description of the theory beinding the method see https://github.com/leorobinson11/DynaMol/blob/main/The_Role_of_Molecular_Dynamics_in_Simulating_the_Shapes_of_Organic_Compounds.pdf. 


## Installation

Download by cloning Git repository:
```
git inshttps://github.com/leorobinson11/DynaMol.git
cd DynaMol
pip install -r equirements.txt
```

## Usage
```
             ____     __   __ 
            |  _ \    |  \/  |
            | | | |   | \  / |
            | | | |   | |\/| |
            | |_| |   | |  | |
            |____/    |_|  |_|
                  
            DynaMol @Leo Robinson 2023
    
----------------------------------------------------------------------

usage: main.py [-h] [-dt DELTATIME] [-rn REPETITIONNUMBER] [-t THRESHHOLD] [-c CUTOFF] [-e] [-b] [-s] Molecule

DynaMol is a tool for performing molecular dynamic simulations and energy calculations on carbohydrate molecules

positional arguments:
  Molecule              Molecule filename, Saved in the Molecules directory (without the .xyz)

optional arguments:
  -h, --help            show this help message and exit
  -dt DELTATIME, --DeltaTime DELTATIME
                        Delta time, The change in time for each repetition (stepsize) - default=5e-5
  -rn REPETITIONNUMBER, --RepetitionNumber REPETITIONNUMBER
                        Repitition number, Number of steps in the simulation - default=1e4
  -t THRESHHOLD, --Threshhold THRESHHOLD
                        Constant to determine what atoms are bonded to oneanother - default=0.3
  -c CUTOFF, --Cutoff CUTOFF
                        Interactions of atoms beiong the cutoff distance are ignored - default=10
  -e, --Energy          Calculate the different types of energy of the system
  -b, --Bonds           Graph the bonded and non bonded interactions
  -s, --Simulate        Simulate the movements of the system and calculate the energies
```

1. Place the .xyz file of the molecule in the Molecules folder
2.  Adjust the optional thresh-hold paramater and check if the correct bonding behavour is being simulated. This can be done with the bond (-b) fland
3. Calculate energy or simulate the movement with the corresponding flags


