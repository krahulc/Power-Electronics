import math

dt_sample=100.0e-6

if t_clock>=t1:

    curr_alpha = math.sqrt(2.0/3.0)*(curr_a - 0.5*curr_b - 0.5*curr_c)
    curr_beta = math.sqrt(2.0/3.0)*math.sqrt(3)*(curr_b - curr_c)/2.0

    curr_d = curr_alpha*math.cos(pll_phase_angle) + curr_beta*math.sin(pll_phase_angle)
    curr_q = -curr_alpha*math.sin(pll_phase_angle) + curr_beta*math.cos(pll_phase_angle)

    t1=t1+dt_sample


inv2ref_curr_d = -curr_d
inv2ref_curr_q = -curr_q
