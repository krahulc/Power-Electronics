import math

dt_sample=100.0e-6
omega_nominal = 2*3.141*60.0
vmag_nominal = 208.0

volt_kp = 0.05
volt_ki = 5.0

curr_kp = 0.0002
curr_ki = 10.0


if t_clock>=t1:
    # Control code removed


    t1=t1+dt_sample


inv1control_curr_d = volt_d
inv1control_curr_q = volt_q
inv1control_curr_d_int = curr_d
inv1control_curr_q_int = curr_q
inv1control_md = curr_ref_d
inv1control_mq = curr_ref_q
inv1control_ma = modsignal_a
inv1control_mb = modsignal_b
inv1control_mc = modsignal_c


