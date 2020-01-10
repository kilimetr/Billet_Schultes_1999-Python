# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr
# Description: Calculation liquid flow at LOADING point

import numpy as np

def calc_liq_loading(pars,yvec):

	uLS     = pars[0]
	g       = pars[1]
	epsilon = pars[2]
	a       = pars[3]
	rhoL    = pars[4]
	rhoV    = pars[5]
	LS      = pars[6]
	CStab   = pars[7]
	Skol    = pars[8]
	etaL    = pars[9]
	etaV    = pars[10]

	uVS  = yvec[0]
	psiS = yvec[1]

	VS = uVS*rhoV*Skol*3600

	if LS/VS*pow(rhoV/rhoL, 0.5) < 0.4:
		nS = -0.326
		CS = CStab
	else:
		nS = -0.723
		CS = 0.695*CStab*pow(etaL/etaV, 0.1588)
	
	res = np.empty(2)
	
	res[0] = uVS - (pow(g/psiS, 0.5) * (epsilon/pow(a, 1/6) - pow(a, 0.5) * pow(12 * 1/g * etaL/rhoL * uLS, 1/3)) * 
		     pow(12 * 1/g * etaL/rhoL * uLS, 1/6) * pow(rhoL/rhoV, 0.5))
	res[1] = psiS - (g/pow(CS, 2) * pow(LS/VS * pow(rhoV/rhoL, 0.5) * pow(etaL/etaV, 0.4), -2*nS))

	return res

