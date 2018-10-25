import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 9.6526e-10)
mat.add_nuclide('Pu239', 2.3402e-05)
mat.add_nuclide('Pu240', 6.0327e-07)
mat.add_nuclide('Pu241', 1.7873e-08)
mat.add_nuclide('Pu242', 3.3224e-09)
mat.add_nuclide('N14', 7.6951e-04)
mat.add_nuclide('H1', 6.5031e-02)
mat.add_nuclide('O16', 3.4493e-02)
mat.add_element('Al', 2.1110e-06)
mat.add_element('B', 7.3750e-09)
mat.add_element('Cd', 3.5470e-10)
mat.add_element('Cl', 3.2120e-08)
mat.add_element('Ca', 4.2630e-08)
mat.add_element('Cr', 1.6430e-07)
mat.add_element('Gd', 3.6220e-10)
mat.add_element('Ga', 4.0850e-07)
mat.add_element('Fe', 7.1380e-07)
mat.add_element('F', 2.9980e-07)
mat.add_element('Mg', 4.6850e-08)
mat.add_element('Mn', 1.5550e-08)
mat.add_element('Ni', 9.7040e-08)
mat.add_element('P', 1.8390e-07)
mat.add_element('K', 1.4570e-08)
mat.add_element('S', 1.7760e-07)
mat.add_element('Si', 1.0140e-07)
mat.add_element('Na', 7.4310e-08)
mat.add_nuclide('U235', 7.2690e-09)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9881e-02)
mat.add_element('Si', 3.7770e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mats.export_to_xml()