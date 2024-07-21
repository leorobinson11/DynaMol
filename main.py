from ForceFields.system import System
from ForceFields.energy import Energy
from Simulations.dynamics import DynamicSymulation
import os
import time
import argparse

def Test_BondSetup(atomname:str)->None:
    syst = System()
    syst.readXYZFile(os.path.join('Molecules',atomname+'.xyz'))
    syst.Build_basic_Graph(thresh, cutoff)
    check = syst.check_bonded_Graph()
    print(
    f"""
    [-] There are {len(check)} atoms with too many bonds: {[I.symbol for I in check]}

    [+] Bond Graph:
    {'-'*60}
    """)
    syst.DrawGraph(syst.bonded_graph)
    print(
    f"""
    [+] Non Bonded Graph:
    {'-'*60}
    """)
    syst.DrawGraph(syst.non_bonded_graph)
    print()

def Test_EnergyCalculations(atomname:str)->None:
    syst = System()
    syst.readXYZFile(os.path.join('Molecules',atomname+'.xyz'))
    syst.Build_basic_Graph(thresh, cutoff)
    ener = Energy(syst)
    ener.GETenergyPairs()
    print(
    f"""
    [+] Energies of the current configuration:
    {'-'*60}
    {len(ener.System.bonddistance_graph)} Bonds: 
    {ener.SumGraph(ener.System.bonddistance_graph,ener.GETbondPotential)}

    {len(ener.System.angle_graph)} Angles:
    {ener.SumGraph(ener.System.angle_graph,ener.GETanglePotential)}

    {len(ener.System.torsion_graph)} Torsions:
    {ener.SumGraph(ener.System.torsion_graph,ener.GETtorsionPotential)}

    {len(ener.System.non_bonddistance_graph)} Van der Wals:
    {ener.SumGraph(ener.System.non_bonddistance_graph,ener.GETvanderwallPotential)}
    """)
    print()

def Test_simulation(atomname:str, stepsize:float, stepnumber:int)->None:
    try:
        os.remove(os.path.join('Results','Trajectories',f'{atomname}_traj.xyz'))
        os.remove(os.path.join('Results','Optimized',f'{atomname}_opt.xyz'))
    except:
        pass
    finally:
        # rewrite this so that the filepath is in the dynamics module
        sim = DynamicSymulation(atomname, stepsize, rec_numb, thresh, cutoff, find_energy=True)
        sim.simulate(stepnumber)
        print('[+] Simulation compleate')


if __name__ == "__main__":
    print("""
             ____     __   __ 
            |  _ \    |  \/  |
            | | | |   | \  / |
            | | | |   | |\/| |
            | |_| |   | |  | |
            |____/    |_|  |_|
                  
            DynaMol @Leo Robinson 2023
    """)
    print("-"*70 + "\n")

    parser = argparse.ArgumentParser(description="DynaMol is a tool for performing molecular dynamic simulations and energy calculations on carbohydrate molecules")
    parser.add_argument("-dt", "--DeltaTime", help="Delta time, The change in time for each repetition (stepsize) - default=5e-5", default=5e-5)
    parser.add_argument("-rn", "--RepetitionNumber", help="Repitition number, Number of steps in the simulation - default=1e4", default=int(1e4))
    parser.add_argument("-t", "--Threshhold", help="Constant to determine what atoms are bonded to oneanother - default=0.3", default=0.3)
    parser.add_argument("-c", "--Cutoff", help="Interactions of atoms beiong the cutoff distance are ignored - default=10", default=10)

    parser.add_argument("-e", "--Energy", action='store_true', help="Calculate the different types of energy of the system")
    parser.add_argument("-b", "--Bonds", action='store_true', help="Graph the bonded and non bonded interactions")
    parser.add_argument("-s", "--Simulate", action='store_true', help="Simulate the movements of the system and calculate the energies")
    
    parser.add_argument("Molecule", help="Molecule filename, Saved in the Molecules directory (without the .xyz)")

    args = parser.parse_args()


    start_time = time.time()
    stepsize = args.DeltaTime#5e-5 #6
    stepnumber = args.RepetitionNumber #4
    thresh, cutoff = float(args.Threshhold), args.Cutoff
    rec_numb = stepnumber/100

    
    NAME = args.Molecule


    if args.Bonds:
        Test_BondSetup(NAME)
    if args.Energy:
        Test_EnergyCalculations(NAME)
    if args.Simulate:
        Test_simulation(NAME, stepsize, stepnumber)
    print('\n Time taken: ' + str(time.time() - start_time)+ 's')