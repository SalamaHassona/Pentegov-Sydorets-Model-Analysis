import time
import numpy as np


def arc(state, jacobian_state, R, C, L):
    x, y, z = state[:, 0], state[:, 1], state[:, 2]
    dx_dt = 1 / L * (y - x * np.power(z, -2 / 3.0))
    dy_dt = (R + 1 - y - R * x) / (R * C)
    dz_dt = x * x - z
    arc_system = np.stack([dx_dt, dy_dt, dz_dt], axis=1)
    jacobian = np.stack([
        np.stack([-1/L*np.power(z, -2 / 3.0), - np.ones_like(x) / L, 2/(3.0*L)*x* np.power(z, -5 / 3.0)], axis=1),
        np.stack([-1.0/C, -1.0/(R * C), np.zeros_like(x)], axis=1),
        np.stack([2*x, np.zeros_like(x), -np.ones_like(x)], axis=1)
    ], axis=1)
    evolution = np.matmul(jacobian_state, jacobian)
    return arc_system, evolution


def runge_kutta_step(func, state, jacobian_state, steps, dt, *args):
    for step in range(steps):
        k1_s, k1_j = func(state, jacobian_state, *args)
        k1_s = dt * k1_s
        k1_j = dt * k1_j
        k2_s, k2_j = func(state + 0.5 * k1_s, jacobian_state + 0.5 * k1_j, *args)
        k2_s = dt * k2_s
        k2_j = dt * k2_j
        k3_s, k3_j = func(state + 0.5 * k2_s, jacobian_state + 0.5 * k2_j, *args)
        k3_s = dt * k3_s
        k3_j = dt * k3_j
        k4_s, k4_j = func(state + k3_s, jacobian_state + k3_j, *args)
        k4_s = dt * k4_s
        k4_j = dt * k4_j
        state = state + (k1_s + 2 * k2_s + 2 * k3_s + k4_s) / 6
        jacobian_state = jacobian_state + (k1_j + 2 * k2_j + 2 * k3_j + k4_j) / 6
    return state, jacobian_state


def lyapunov_exponents_parker_chua(initial_state, cr_point_list, sim_time, steps, sims, burn_ins=1000, dt=0.001,
                                       rel_error=1e-3, abs_error=1e-3):
    n = initial_state.shape[0]
    num_pairs = cr_point_list.shape[0]

    exponents = np.zeros((num_pairs, n), dtype=np.longdouble)
    sum = np.zeros((num_pairs, n), dtype=np.longdouble)
    state = np.repeat(initial_state.copy()[np.newaxis, :], num_pairs, axis=0)
    jacobian_state = np.repeat(np.eye(n, dtype=np.longdouble)[np.newaxis, :, :], num_pairs, axis=0)

    R = cr_point_list[:, 0]
    C = cr_point_list[:, 1]
    L = 1

    converged = np.zeros(num_pairs, dtype=np.bool_)
    sim_n_number = np.zeros(num_pairs, dtype=np.longdouble)
    PREV_LYAPUNOV_EXPONENTS = np.zeros(n, dtype=np.longdouble)

    # Burn-in phase
    for _ in range(burn_ins):
        state, jacobian_state = runge_kutta_step(arc, state, jacobian_state, steps, dt, R, C, L)

        v = jacobian_state.copy()
        for k in range(n):
            v[:, k, :] = v[:, k, :] / np.linalg.norm(v[:, k, :], axis=-1, keepdims=True)
            for j in range(k+1,n):
                v[:, j, :] -= np.sum(v[:, k, :] * v[:, j, :], axis=-1, keepdims=True) * v[:, k, :]
            jacobian_state[:, k, :] = v[:, k, :]

    for sim_n in range(sims):
        if np.all(converged).item():
            return exponents, sim_n_number
        else:
            indices = converged == False
            sim_n_number[indices] += 1

            PREV_LYAPUNOV_EXPONENTS = exponents[indices, :].copy()
            state[indices, :], jacobian_state[indices, :] = runge_kutta_step(arc, state[indices, :],
                                                                             jacobian_state[indices, :],
                                                                             sim_time, steps, dt,
                                                                             R[indices], C[indices], L)
            v = jacobian_state.copy()
            for k in range(n):
                sum[indices, k] += np.log(np.linalg.norm(v[indices, k, :], axis=-1))
                v[indices, k, :] = v[indices, k, :] / np.linalg.norm(v[indices, k, :], axis=-1, keepdims=True)
                for j in range(k + 1, n):
                    v[indices, j, :] -= np.sum(v[indices, k, :] * v[indices, j, :], axis=-1, keepdims=True) * v[indices, k, :]
                jacobian_state[indices, k, :] = v[indices, k, :]
                exponents[indices, k] = sum[indices, k] / ((sim_n + 1) * sim_time)

            diff = np.linalg.norm(PREV_LYAPUNOV_EXPONENTS - exponents[indices, :], axis=-1)
            threshold = rel_error * np.linalg.norm(exponents[indices, :], axis=-1) + abs_error
            converged[indices] = diff < threshold

    return exponents, sim_n_number


r_values = np.linspace(5, 25, 1000)

cr_point_list = np.array([[item, 3.14] for item in r_values], dtype=np.longdouble)

initial_state = np.array([0.50, 4.00, 1.00], dtype=np.longdouble)


sim_time = 0.35

steps = 100
sims = 1000
burn_ins = 1000
dt = 0.001006
start = time.time()
# Calculate the Lyapunov exponents
exponents, sim_number = lyapunov_exponents_parker_chua(initial_state, cr_point_list, sim_time, steps, sims, burn_ins, dt)
end = time.time()
print(str(end - start))
np.save(exponents, "parker_chua_dt_001009_sims_1000_error_1e3_steps_100_burn_1000.npy")
np.save(sim_number, "sim_number_parker_chua_dt_001009_sims_1000_error_1e3_steps_100_burn_1000.npy")
print("Lyapunov exponents for each sigma and rho value combination:\n", exponents)
print("# simulations:\n", sim_number)
