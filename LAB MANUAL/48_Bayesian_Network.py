# 38. Bayesian Network
# Simple conditional probability example
P_rain=0.3
P_wet_given_rain=0.9
P_wet_given_no_rain=0.1
P_wet=P_rain*P_wet_given_rain+(1-P_rain)*P_wet_given_no_rain
print('P(WetGrass)=',round(P_wet,2))
# Output: P(WetGrass)= 0.34