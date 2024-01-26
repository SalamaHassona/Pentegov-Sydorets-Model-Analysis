import numpy as np
import time
import pickle

kd = 400001
dt = 0.01
x0 = 0.50
y0 = 4.00
z0 = 1.00
L = 1
C = 3.14


def runge_kutta_4(R, data_range):
    _xp = np.ones((data_range, kd))
    _xp[:, 0] = _xp[:, 0] * x0
    _yp = np.ones((data_range, kd))
    _yp[:, 0] = _yp[:, 0] * y0
    _zp = np.ones((data_range, kd))
    _zp[:, 0] = _zp[:, 0] * z0
    for k in range(1, kd):
        xx = _xp[:, k-1]
        yy = _yp[:, k-1]
        zz = _zp[:, k-1]
        kx1 = (yy - xx * pow(zz, -2 / 3)) / L
        ky1 = (R + 1 - yy - R * xx) / (R * C)
        kz1 = xx * xx - zz
        x1 = xx + (dt * kx1) / 2
        y1 = yy + (dt * ky1) / 2
        z1 = zz + (dt * kz1) / 2
        kx2 = (y1 - x1 * pow(z1, -2 / 3)) / L
        ky2 = (R + 1 - y1 - R * x1) / (R * C)
        kz2 = x1 * x1 - z1
        del x1, y1, z1
        x2 = xx + (dt * kx2) / 2
        y2 = yy + (dt * ky2) / 2
        z2 = zz + (dt * kz2) / 2
        kx3 = (y2 - x2 * pow(z2, -2 / 3)) / L
        ky3 = (R + 1 - y2 - R * x2) / (R * C)
        kz3 = x2 * x2 - z2
        del x2, y2, z2
        x3 = xx + (dt * kx3)
        y3 = yy + (dt * ky3)
        z3 = zz + (dt * kz3)
        kx4 = (y3 - x3 * pow(z3, -2 / 3)) / L
        ky4 = (R + 1 - y3 - R * x3) / (R * C)
        kz4 = x3 * x3 - z3
        del x3, y3, z3
        _xp[:, k] = xx + ((kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6) * dt
        _yp[:, k] = yy + ((ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6) * dt
        _zp[:, k] = zz + ((kz1 + 2 * kz2 + 2 * kz3 + kz4) / 6) * dt
        del kx1, kx2, kx3, ky1, ky2, ky3, kz1, kz2, kz3
    end = time.time()
    print(str(end - start))
    return _xp, _yp, _zp


start = time.time()
R = np.array([5.0, 6.7, 8.3, 9.0, 11.65, 12.5, 14.0, 15.0, 17.62, 21.0, 23.9, 24.5])
# R = np.linspace(5.0, 25.0, num=1000)

try:
    time_series = runge_kutta_4(R, 12)
    # time_series = runge_kutta_4(R, 1000)
    # with open('time_series_xyz_x_0_51_y_4_01_z_1_01_t_400001_1000_param.pickle', 'wb') as time_series_xyz:
    with open('time_series_xyz_x_0_5_y_4_z_1_t_400001_12_param.pickle', 'wb') as time_series_xyz:
        pickle.dump(time_series, time_series_xyz, protocol=pickle.HIGHEST_PROTOCOL)
except Exception as ex:
    print("exception: "+str(ex))
end = time.time()
print(str(end-start))