"""
Created on Wed Oct 07 23:48:09 2015
Waste Heat Recovery Systems
@author: Dimitris Lourandos 
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt




# Saturated steam for the ship's services
m_s_heating_services = 1400 # kg/h
L_tg_rated = 800   # Turbogenerator rated electric load (kW)  - max 2000

# Fuel Composition 
c = 0.86           # carbon mass fraction kg C/kg fuel 
h = 0.11           # hudrogen mass fraction kg H/kg fuel
s = 0.03           # sulfur mass fraction kg S/kg fuel
LHV = 40500        # fuel lower heating value (kJ/kg), typical for HFO with s=3#

lamda = np.linspace(4. ,2.8, 19) # A/F ratio or use mass of gas from engine output

#-------------------------- Assumptions------------------------#

eff_b = 0.98;      # boiler efficiency (from boiler manufacturer)
DT_g = 3;          # temperature drop in the exhaust pipe (connecting the engine t/c turbine and the boiler (usually <= 5 deg C)
DT_sh = 3;         # temperature drop in the steam pipe (connecting the engine the boiler and the steam turbine (usually <= 5 deg C)
DT_b_OUT = 15;     # temperature difference at exhaust gas exit side of the boiler (must be 10-25 deg C)/(at least 10 deg C according to SNAME T&R3-49 p.39)
DT_b_IN = 30;      # boiler maximum temperature difference (at boiler exhaust gas inlet) is >=30deg C
DT_pp = 15;        # Pinch point temperature difference (10-25 celsius)
eff_p = 0.6;       # Pump efficiency

#--------------------------------------------------------------#

Tg_in = Tg_exhaust - DT_g # temperature of gas entering the boiler
# required temperature (deg C) of water entering into the boiler economizer 
# as function of fuel sulfur weight fraction s(-)
T_sulfur_dewpoint = 0.1239e6*s**3 - 1.3644e4*s**2 + 6.5509e2*s + 124.97 

m_hs = m_s_hs*np.ones(np.size(Load))/3600.  # saturated steam (kg/s)
#m_g = Mass_flow_of_gas/3600.          # gas flow rate (kg/s)

#---------- 1: Available pressures (User Input) ----------------#
p_d = 7.0           # water/steam drum pressure
p_fw = 1            # feed water tank pressure
p_c = 0.075         # pressure of condenser in bar (recommended values 0.05-0.08 bar) 

#---------- 2: Pressure drops (User Input) ---------------------#
Dp_ec = 0.03*p_d;     # pressure drop in the economizer section (bar)
Dp_sh = 0.05*p_d;     # steam pressure drop in boiler superheater piping (2.5# SNAME 3-49, 5# Dzida 2009, 7# Ioannides 1984)
Dp_ev = 0.15*p_d;     # pressure drop in the evaporator section 15-20% of drum pressure (bar)
Dp_cond = p_fw - p_c  # pressure increase in condensate water pump in bar

#---------- 3: Calculated pressures ----------------------------#
p_sh = p_d - Dp_sh;   # pressure of superheated steam exiting the boiler and entering into the steam turbine (bar)



# dashfaksf'hasf




















