import math

dt_sample=100.0e-6

curr_kp = 0.0001
curr_ki = 20.0


if t_clock>=t1:
    
    curr_ref_d = inv2ref_curr_d
    curr_ref_q = inv2ref_curr_q

    # Control code removed
    
    
    t1=t1+dt_sample

    

if t_clock<0.4:
    Disconnect1a = 0.0
    Disconnect2a = 0.0
    Disconnect1b = 0.0
    Disconnect2b = 0.0
    Disconnect1c = 0.0
    Disconnect2c = 0.0
    curr_d_int = 0.9/curr_ki
    curr_q_int = 0.05/curr_ki
else:
    Disconnect1a = 1.0
    Disconnect2a = 1.0
    Disconnect1b = 1.0
    Disconnect2b = 1.0
    Disconnect1c = 1.0
    Disconnect2c = 1.0



currconinv2_curr_d = curr_d
currconinv2_curr_q = curr_q
currconinv2_curr_d_int = curr_d_int
currconinv2_curr_q_int = curr_q_int
currconinv2_md = mod_d
currconinv2_mq = mod_q
currconinv2_ma = modsignal_a
currconinv2_mb = modsignal_b
currconinv2_mc = modsignal_c


