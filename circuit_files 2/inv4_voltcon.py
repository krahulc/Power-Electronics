import math

dt_sample=100.0e-6
omega_nominal = 2*3.141*60.0
vmag_nominal = 208.0

#volt_kp = 0.05
#volt_kp = 0.075
#volt_ki = 10.0

volt_kp = 0.05
#volt_kp = 0.075
volt_ki = 5.0

curr_kp = 0.0002
curr_ki = 10.0


if t_clock>=t1:
    # Control code removed


    t1=t1+dt_sample

if t_clock>0.1:
    Disconnect1inv4a = 1.0
    Disconnect2inv4a = 1.0
    Disconnect1inv4b = 1.0
    Disconnect2inv4b = 1.0
    Disconnect1inv4c = 1.0
    Disconnect2inv4c = 1.0
else:
    Disconnect1inv4a = 0.0
    Disconnect2inv4a = 0.0
    Disconnect1inv4b = 0.0
    Disconnect2inv4b = 0.0
    Disconnect1inv4c = 0.0
    Disconnect2inv4c = 0.0


inv4control_curr_d = volt_d
inv4control_curr_q = volt_q
inv4control_curr_d_int = curr_d
inv4control_curr_q_int = curr_q
inv4control_md = curr_ref_d
inv4control_mq = curr_ref_q
inv4control_ma = modsignal_a
inv4control_mb = modsignal_b
inv4control_mc = modsignal_c


