# %%
import sys
import os
import numpy as np
import pytest
import warnings

if __package__:
    from ..petrophysics.porosity import porosity
else:
    sys.path.append(os.path.dirname(__file__) + '/..')
    from petrophysics.porosity import porosity

# ---------------------------------------------------------- #
# function

def sorted_values (configuration, size = 15, seed = 99):

    np.random.seed(seed)

    # transform ["a","b","c"] into "a,b,c"
    list_names = list(configuration.keys())
    values_names = ','.join(list_names)

    property_values = []
    for k in configuration:
        property = np.random.uniform(low = configuration[k][0], high = configuration[k][1], size = size)
        property_values.append(property)

    property_values = np.array(property_values).T

    return property_values,values_names

# ---------------------------------------------------------- #
# where all modifications will be applied

config_1 = {
    "rhob":(0.0,1.0),
    "rhom":(0.0,1.0),
    "rhof":(0.0,1.0),
}

density_values = sorted_values(config_1)

@pytest.mark.parametrize(density_values[1], density_values[0])
def test_density(rhob, rhom, rhof):
    p = porosity(rhob = rhob, rhom = rhom, rhof = rhof,
                        method = "density")
    assert p >= 0 and p <= 1


config_2 = {
    "nphi":(0.0,1.0),
    "vsh":(0.0,1.0),
    "nphi_sh":(0.0,1.0),
}

neutron_values = sorted_values(config_2)

@pytest.mark.parametrize(neutron_values[1], neutron_values[0])
def test_neutron(nphi, vsh, nphi_sh):
    p = porosity(nphi = nphi, vsh = vsh, nphi_sh = nphi_sh,
                        method = "neutron")
    assert p >= 0 and p <= 1

# ---------------------------------------------------------- #


not_squared_neutron_density_values = []
for i in range(15):
    phid = np.random.uniform(low=0.0, high=1.0, size=None)
    phin = np.random.uniform(low=0.0, high=1.0, size=None)
    not_squared_neutron_density_values.append((phid, phin))

@pytest.mark.parametrize("phid, phin", not_squared_neutron_density_values)
def test_neutron_density(phid, phin):
    p = porosity(phid = phid, phin = phin, squared = False,
                        method = "neutron-density")
    assert p >= 0 and p <= 1


squared_neutron_density_values = []
for i in range(15):
    phid = np.random.uniform(low=0.0, high=1.0, size=None)
    phin = np.random.uniform(low=0.0, high=1.0, size=None)
    squared_neutron_density_values.append((phid, phin))

@pytest.mark.parametrize("phid, phin", squared_neutron_density_values)
def test_neutron_density_squared(phid, phin):
    p = porosity(phid = phid, phin = phin, squared = True,
                        method = "neutron-density")
    assert p >= 0 and p <= 1


sonic_values = []
for i in range(15):
    dt = np.random.uniform(low=50.0, high=100.0, size=None)
    dtma = np.random.uniform(low=10.0, high=100.0, size=None)
    dtf = np.random.uniform(low=150.0, high=300.0, size=None)
    sonic_values.append((dt, dtma, dtf))

@pytest.mark.parametrize("dt, dtma, dtf", sonic_values)
def test_sonic(dt, dtma, dtf):
    p = porosity(dt = dt, dtma = dtma, dtf = dtf,
                        method = "sonic")
    assert p >= 0 and p <= 1


gaymard_values = []
for i in range(15):
    phid = np.random.uniform(low=0.0, high=1.0, size=None)
    phin = np.random.uniform(low=0.0, high=1.0, size=None)
    gaymard_values.append((phid, phin))

@pytest.mark.parametrize("phid, phin", gaymard_values)
def test_gaymard(phid, phin):
    p = porosity(phid = phid, phin = phin,
                        method = "gaymard")
    assert p >= 0 and p <= 1


unique_density_value = []
rhob = 2.60
rhom = 1.10
rhof = 1.10
unique_density_value.append((rhob, rhom, rhof))

@pytest.mark.parametrize("rhob, rhom, rhof", unique_density_value)
def test_unique_density(rhob, rhom, rhof):
    p = porosity(rhob = 2.60, rhom = 1.10, rhof = 1.10,
                        method = "density")
    assert p >= 0 and p <= 1


unique_sonic_value = []
dt = 75.0
dtma = 100.0
dtf = 100.0
unique_sonic_value.append((dt, dtma, dtf))

@pytest.mark.parametrize("dt, dtma, dtf", unique_sonic_value)
def test_unique_sonic(dt, dtma, dtf):
    p = porosity(dt = 75.0, dtma = 100.0, dtf = 100.0,
                        method = "sonic")
    assert p >= 0 and p <= 1    

#TODO: pytest for the rest of porosity
