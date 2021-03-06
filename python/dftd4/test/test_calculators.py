# This file is part of dftd4.
#
# Copyright (C) 2019 Sebastian Ehlert
#
# dftd4 is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dftd4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with dftd4.  If not, see <https://www.gnu.org/licenses/>.

"""Tests for the ASE interface to dftd4."""

def test_d4_molecular():
    """Short test for DFT-D4 on a subset of the G2."""
    from pytest import approx
    from ase.collections import g2
    from dftd4.calculators import D4_model
    thr = 1.0e-7
    subset = {'C4H4NH': (-0.17255494625289736, 0.0016477006410405726),
              'CH3SCH3': (-0.1184068121240227, 0.0013815131754339742),
              'SiH2_s3B1d': (-0.018605808311545353, 0.00015467635458531962),
              'CH3SH': (-0.057225664710572166, 0.0005448583198760675),
              'CH3CO': (-0.05123854136602616, 0.0007740283810664048),
              'C3H4_D2d': (-0.07030109649113268, 0.0009592270677273752),
              'ClF3': (-0.04213171440293672, 0.0007278443442761045),
              'H2CO': (-0.019942382858774994, 0.000214878508039154),
              'CH3COOH': (-0.08745799871811986, 0.0011439136440678434),
              'HCF3': (-0.038875458546899694, 0.0002913185062774874),
              'CH3S': (-0.04507412915084048, 0.00037777210121433776),
              'C3H6_D3h': (-0.09236020188511877, 0.0006334098964455702),
              'CS2': (-0.06616927201561966, 0.0018260660788891434),
              'SiH2_s1A1d': (-0.018788347860837842, 0.00038250905286212267),
              'C4H4S': (-0.1993641839842852, 0.0018407544464185575)}

    calc = D4_model(s6=1.0, s8=1.26829475, a1=0.39907098, a2=5.03951304,
                    s9=1.0, alp=16)  # PBE-D4 parameters
    # table = {}
    for name, data in subset.items():
        atoms = g2[name]
        energy, gnorm = data
        atoms.set_calculator(calc)
        # energy = atoms.get_potential_energy()
        # gnorm = abs(atoms.get_forces().flatten()).mean()
        # table[name] = (energy, gnorm)
        assert atoms.get_potential_energy() == approx(energy, thr)
        assert abs(atoms.get_forces().flatten()).mean() == approx(gnorm, thr)
    # print(table)
    # assert 0


def test_d3_molecular():
    """Short test for DFT-D4 on a subset of the G2."""
    from pytest import approx
    from ase.collections import g2
    from dftd4.calculators import D3_model
    thr = 1.0e-7
    subset = {'cyclobutene': (-0.14587622430572988, 0.0038656482276170404),
              'CH3ONO': (-0.0747841729798892, 0.0013910783512913769),
              'SiH3': (-0.032866030506839346, 0.0005981896646390799),
              'C3H6_D3h': (-0.09951649333326623, 0.0013357628341227497),
              'CO2': (-0.021752309773642422, 0.00019733017890112477),
              'ClF3': (-0.03591759204325222, 0.0005044197142909924),
              'C3H4_D2d': (-0.07806623987941828, 0.001347275326803856),
              'COF2': (-0.02991964741255898, 0.00027298278394812854),
              '2-butyne': (-0.12278065983118544, 0.0019017285760430556),
              'C2H5': (-0.058322182037988494, 0.0008120132484610599),
              'BF3': (-0.025533905226208957, 0.0002610462043875494),
              'SiH2_s3B1d': (-0.0210666014260993, 0.00033626052109999774),
              'N2O': (-0.022067882590594678, 0.0002285471242781216)}

    calc = D3_model(s6=1.0, s8=1.44956635, a1=0.32704579, a2=5.36988013,
                    s9=1.0, alp=16)  # refitted PBE-D3 parameters
    # table = {}
    for name, data in subset.items():
        atoms = g2[name]
        energy, gnorm = data
        atoms.set_calculator(calc)
        # energy = atoms.get_potential_energy()
        # gnorm = abs(atoms.get_forces().flatten()).mean()
        # table[name] = (energy, gnorm)
        assert atoms.get_potential_energy() == approx(energy, thr)
        assert abs(atoms.get_forces().flatten()).mean() == approx(gnorm, thr)
    # print(table)
    # assert 0
