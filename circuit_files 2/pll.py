import math


dt_sample=100.0e-6
nom_omega = 370.0


pll_kp = 0.2
pll_ki = 4.5


if t_clock>=t1:

    volt_alpha = math.sqrt(2.0/3.0)*(volt_a - 0.5*volt_b - 0.5*volt_c)
    volt_beta = math.sqrt(2.0/3.0)*math.sqrt(3)*(volt_b - volt_c)/2.0

    volt_d = volt_alpha*math.cos(ph_angle) + volt_beta*math.sin(ph_angle)
    volt_q = -volt_alpha*math.sin(ph_angle) + volt_beta*math.cos(ph_angle)

    pll_d = volt_d
    pll_q = volt_q

    pll_err = volt_q

    pll_int += pll_err*dt_sample

    if (pll_ki*pll_int > 30.0):
        pll_int = 30.0/pll_ki

    if (pll_ki*pll_int < -30.0):
        pll_int = -30.0/pll_ki

    if (pll_ki*pll_int > 30.0):
        pll_int = 30.0/pll_ki

    if (pll_ki*pll_int < -30.0):
        pll_int = -30.0/pll_ki

    omega = nom_omega + pll_kp*pll_err + pll_ki*pll_int

    ph_angle += omega*dt_sample

    if (ph_angle > 2*math.pi):
        ph_angle = ph_angle - 2*math.pi

    t1=t1+dt_sample



pll_phase_angle = ph_angle
pll_omega = omega
pll_volt_d = volt_d
pll_volt_q = volt_q
pll_cont_int = pll_int

