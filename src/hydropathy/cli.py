import argparse
import importlib.metadata
from .hydropathy import WaterAngles


def build_cli():
    des = ("The script takes frames of a molecular dynamics of a solvent-solute system "
           "(e.g.: protein + water, ligand + water, rna + water, ...) in pdb format "
           "and calculates all the angles that water molecules (modeled with spc, "
           "tip3p, tip4p or tip5p) form with each heavy atom of the structure at a "
           "distance less than 6A. It returns in the output folder one file for each " 
           "residue or nucleotide of the analyzed structure. "
           "Each file contains seven column: distance, theta1, theta2, theta3, theta4, theta_d. "
           "For further information you can see https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7954116/")
    parser = argparse.ArgumentParser(description=des, add_help=False)
    req_grp = parser.add_argument_group(title="positional arguments")
    req_grp.add_argument("-i", "--input",
                         required=True,
                         help="input path; folder with pdb files",
                         metavar="")
    req_grp.add_argument("-o", "--output",
                         required=True,
                         help="output path; destination folder of output files",
                         metavar="")
    req_grp.add_argument("-w", "--water",
                         required=True,
                         help="water model; spc, tip3p, tip4p, tip5p",
                         metavar="")
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-v", "--version",
                          action="version",
                          version=importlib.metadata.version('hydropathy'))
    optional.add_argument("-h", "--help",
                          action="help",
                          help="show this help message and exit")
    return parser.parse_args()

def main():
    args = build_cli()
    wa = WaterAngles(args.input, args.output, args.water)
    process_time = wa.get_angles()
    print('Execution time = %.6f seconds' % (process_time))


if __name__ == "__main__":
    main()
