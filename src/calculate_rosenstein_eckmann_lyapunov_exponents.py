import numpy as np
import nolds
import time


def rk4_step(func, y, t, dt, *args):
    k1 = dt * func(t, y, *args)
    k2 = dt * func(t + 0.5 * dt, y + 0.5 * k1, *args)
    k3 = dt * func(t + 0.5 * dt, y + 0.5 * k2, *args)
    k4 = dt * func(t + dt, y + k3, *args)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6


def arc_system(t, state, R, C, L):
    x, y, z = state[:, 0], state[:, 1], state[:, 2]
    dx_dt = 1 / L * (y - x * np.power(z, -2 / 3.0))
    dy_dt = (R + 1 - y - R * x) / (R * C)
    dz_dt = x * x - z
    return np.stack([dx_dt, dy_dt, dz_dt], axis=1)


def generate_arc_data(initial_state, t_span, dt, *args):
    steps = int((t_span[1] - t_span[0]) / dt)
    t = np.linspace(t_span[0], t_span[1], steps)
    state = np.array(initial_state, dtype=np.double)
    trajectory = [state]

    for i in range(1, len(t)):
        state = rk4_step(arc_system, state, t[i - 1], dt, *args)
        trajectory.append(state)

    return np.stack(trajectory)


r_values = np.linspace(5, 25, 1000)
cr_point_list = np.array([[item, 3.14] for item in r_values], dtype=np.double)
initial_state = np.array([0.50, 4.00, 1.00], dtype=np.double)

num_pairs = cr_point_list.shape[0]
state = np.repeat(initial_state.copy()[np.newaxis, :], num_pairs, axis=0)

start = time.time()
# Generate data
t_span = [0, 2000]
dt = 0.01
R = cr_point_list[:, 0]
C = cr_point_list[:, 1]
L = 1
states = generate_arc_data(state, t_span, dt, R, C, L)[100000 - 1:-1, :, :][::8, :, :]
print(str(time.time() - start))

# Apply Rosenstein & Eckmann methods
lyapunov_exponent_r = []
lyapunov_exponent_e = []
for i in range(states.shape[1]):
    lyapunov_exponent_r.append(nolds.lyap_r(states[:, i, 0], emb_dim=3))
    lyapunov_exponent_e.append(nolds.lyap_e(states[:, i, 0], emb_dim=3, matrix_dim=3))

lyapunov_exponent_r = np.stack(lyapunov_exponent_r)
lyapunov_exponent_e = np.stack(lyapunov_exponent_e)
np.save('lyapunov_exponent_r.npy', lyapunov_exponent_r)
np.save('lyapunov_exponent_e.npy', lyapunov_exponent_e)
print(str(time.time() - start))
