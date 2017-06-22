import math

carr_freq = 5000.0
dt_carr = 5.0e-7


if t_clock>=tcarr:
    modsignal_a = inv1control_ma
    modsignal_b = inv1control_mb
    modsignal_c = inv1control_mc
    
    if (x_tri>=1.0):
        x_tri_sign=-1.0
    
    if (x_tri<=-1.0):
        x_tri_sign=1.0
    
    x_tri+=x_tri_sign*(4.0*carr_freq)*dt_carr
    
    if (x_tri>modsignal_a):
        s1logic=0.0
        s2logic=1.0
    else:
        s1logic=1.0
        s2logic=0.0

    if (x_tri>modsignal_b):
        s3logic=0.0
        s4logic=1.0
    else:
        s3logic=1.0
        s4logic=0.0

    if (x_tri>modsignal_c):
        s5logic=0.0
        s6logic=1.0
    else:
        s5logic=1.0
        s6logic=0.0
    
    tcarr=tcarr+dt_carr


s1gate = s1logic
s2gate = s2logic
s3gate = s3logic
s4gate = s4logic
s5gate = s5logic
s6gate = s6logic

