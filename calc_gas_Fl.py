# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr


import numpy as np

def calc_gas_flooding(pars,yvec):

	uL      = pars[0]
	g       = pars[1]
	epsilon = pars[2]
	a       = pars[3]
	rhoL    = pars[4]
	rhoV    = pars[5]
	L       = pars[6]
	CFltab  = pars[7]
	Skol    = pars[8]
	etaL    = pars[9]
	etaV    = pars[10]

	uVFl = yvec[0]
	hLFl = yvec[1]
	psi  = yvec[2]

	VFl = uVFl*rhoV*Skol*3600; # [kg/h]

	if L/VFl*pow(rhoV/rhoL, 0.5) < 0.4:
		nFl = -0.194
		CFl = CFltab
	else:
		nFl = -0.708
		CFl = 0.6244*CFltab*pow((etaL/etaV), 0.1028)

	res = np.empty(3)

	res[0] = uVFl - (pow(2, 0.5) * pow(g/psi, 0.5) * pow(epsilon-hLFl, 3/2) / (pow(epsilon, 0.5)) * pow(hLFl/a, 0.5) * pow(rhoL/rhoV, 0.5))
	res[1] = psi - (g/pow(CFl, 2) * pow(L/VFl * pow(rhoV/rhoL, 0.5) * pow(etaL/etaV, 0.2), -2*nFl))
	res[2] = pow(hLFl, 3) * (3*hLFl-epsilon) - (6/g * pow(a, 2) * epsilon * (etaL/rhoL) * (L/VFl) * (rhoV/rhoL) * uVFl)

	return res

