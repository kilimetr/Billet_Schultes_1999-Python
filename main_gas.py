


import scipy.optimize as sp
import numpy as np
import os

os.chdir("/Users/kilimetr/Desktop/python/Billet&Schultes")

# from packings_library import packingsss
from calc_gas_Fl      import calc_gas_flooding
from calc_gas_Ld      import calc_gas_loading

# PHASES CHARACTERISTICS
etaL = 0.001021      # liq dynam viscos [Pas]
rhoL = 998.773       # liq density      [kg/m3]
uL   = 0.043056      # gas velocity     [m/s]
etaV = 1.8*10**(-5)  # gas dynam viscos [Pas]
rhoV = 1.23595       # gas density      [kg/m3]
g    = 9.81          # grav accelerat   [m/s2]

# PACKING CHARACTERISTICS
epsilon = 0.945           # void fraction         [-]     RALU PAK YC-250
a       = 250             # specific surface area [m2/m3]
CFltab  = 2.558           # packings constant     [-]
CStab   = 3.178           # packings constant     [-]
Cp0     = 0.191           # packings constant     [-]
CL      = 1.334           # packings constant     [-]
CV      = 0.385           # packings constant     [-]
dp      = 6*(1-epsilon)/a # particle diameter     [m]

# COLUMN CHARACTERISTICS
dkol = 1               # column diameter [m]
Skol = np.pi * (dkol**2) / 4 # column surface  [m2]

L = rhoL*uL*Skol*3600 # gas mass flow rate [kg/s]

# CALCULATIONS - Flooding Point
uVFl  = 1
hLmin = epsilon/3
hLmax = epsilon
hLFl  = (hLmin + hLmax)/2
psi   = 14  # IF podmínka na hLFl jinak nekonverguje & CONDITION FOR PSI nástřel

pars = [uL, g, epsilon, a, rhoL, rhoV, L, CFltab, Skol, etaL, etaV]

result = sp.fsolve(lambda y: calc_gas_flooding(pars,y), [uVFl, hLFl, psi])

uVFl   = result[0]
hLFl   = result[1]
psiFl  = result[2]

print("uVFl: "   + str(uVFl))
print("hLFl: "   + str(hLFl))
print("psi:Fl "  + str(psiFl))


# CALCULATIONS - Loading Point
parss = [uL, g, epsilon, a, rhoL, rhoV, L, CStab, Skol, etaL, etaV]

uVS  = uVFl*0.75
psiS = psiFl*2   # CONDITION FOR PSI nástřel

result2 = sp.fsolve(lambda y: calc_gas_loading(parss,y), [uVS, psiS])

uVS  = result2[0]
psiS = result2[1]

print("uVS: "  + str(uVS))
print("psiS: " + str(psiS))

# uL = uLFl
# hLS  = pow(12 * 1/g * etaL/rhoL * uL * pow(a, 2), 1/3)

# # DRY PRESSURE DROP
# uV   = 1.5
# ds   = dkol
# K    = 1 / (1 + 2/3 * 1/(1-epsilon) * dp/ds)
# ReV  = uV*dp / ((1-epsilon)*etaV) * rhoV*K
# psi0 = Cp0 * (64/ReV + 1.8/pow(ReV, 0.08))
# FV   = uV * pow(rhoV, 0.5)                        # gas load factor
# dp0H = psi0 * a/pow(epsilon, 3) * pow(FV, 2) /2 * 1/K # [Pa/m]

# # WET PRESSURE DROP
# uVFl = uV
# hL   = hLS + (hLFl - hLS)*pow(uV/uVFl, 13) # uVS<uV<uVFl
# C1   = 13300 / pow(a, 3/2)
# FrL  = pow(uL, 2) * a/g
# psiL = Cp0 * (64/ReV + 1.8/pow(ReV, 0.08)) * pow((epsilon-hL)/epsilon, 1.5) * pow(hL/hLS, 0.3) * np.exp(C1*pow(FrL, 0.5))
# dpH  = psiL * a/pow(epsilon-hL, 3) * pow(FV, 2)/2 * 1/K # [Pa/m]