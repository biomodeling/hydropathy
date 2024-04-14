# hydropathy
[![Version](figures/version.svg)](https://github.com/biomodeling/hydropathy)
[![License: GPL v3](figures/license.svg)](https://github.com/biomodeling/hydropathy/blob/master/LICENSE.md)

`hydropathy` is a script written in `python` that calculates the orientation of water modecules around a solute. 

## Theoretical foundations
Given a water molecule, it is possible to construct a tetrahedron having the oxygen atom as its center and the two real (**H1**, **H2**) and two _virtual_ (**LP1**, **LP2**) hydrogens as vertices.

Considering each water molecule and the nearest solute atom, a vector is defined that connects the solute atom with the oxygen atom of the water particle (**R**). 

We also define the vectors joining the center of the tetrahedron with the four vertices (**H1**, **H2**, **LP1**, **LP2**) and the dipole vector obtained as **d** = **H1** + **H2**. 

By measuring the angles formed by **R** with **H1**, **H2**, **LP1**, **LP2** and **d**, the hydropathy of the solute can be characterized.

More information on theory can be found <a href="https://www.frontiersin.org/articles/10.3389/fmolb.2021.626837/full" target="_blank">here</a>


## Installation
`hydropathy` is not released on PyPi. You can install it from the GitHub repo as follows
```
pip install git+https://github.com/biomodeling/hydropathy.git
```


## Usage
The script takes as parameters:
- an input path that contains a set of files in pdb format of the solute + solvent system
- an output path where the results will be written
- the water model used (`tip3p`, `tip4p`, `tip5p`, `spc`)

From your shell for example you can directly launch
```
hyrdopathy -i /your/input/path/ -o /yout/output/path -w tip3p
```


## Output
The output consists of a series of files of the type `<resno>_<resname>.csv`, one for each solute residue. Each file contains 6 columns: `distance, theta1, theta2, theta3, theta4, theta_d`, where:

- `distance`: is the distance (expressed in Å) between the oxygen atom of a water molecule (center of the tetrahedron) and the nearest solute atom (excluding hydrogens), if the latter is at a distance less than 6Å (**R**)
- `theta1, ..., theta4`: are the angles formed between **R** and the vectors joining the center and vertices of the tetrahedron (**H1**, **H2**, **LP1**, **LP2**); all angles are expressed in degrees (°)
- `theta_d`: is the dipole angle, formed between **R** and the dipole vector **d** = **H1** + **H2** 
