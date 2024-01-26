import time

import matplotlib
import numpy as np

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pickle


def rungeplot_time_series(time_series, i, r, sr):
    plt.tight_layout(pad=0)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim([-2, 6])
    ax.set_ylim([-2, 4])
    ax.set_zlim([0, 30])
    ax.plot(time_series[0][i][100000:1600001:10].ravel(),
            time_series[1][i][100000:1600001:10].ravel(),
            time_series[2][i][100000:1600001:10].ravel())
    ax.set_xlabel(r'$x$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$y$', fontsize=14, labelpad=10)
    ax.set_zlabel(r'$z$', fontsize=14, labelpad=5)
    ax.view_init(elev=22., azim=111.)
    ax.scatter(1, 1, 1, c='r', marker='o', label=r'$(1, 1, 1)$')
    plt.title(f'R={r}   t=[1000, 16000]', fontsize=18, pad=10)
    plt.savefig(f'pictures/1600001/R_{sr}.jpg', bbox_inches='tight')


start = time.time()
try:
    r_list = ["5.0", "6.7", "8.3", "9.0", "11.65", "12.5", "14.0", "15.0", "17.62", "21.0", "23.9", "24.5"]
    pr_list = ["5_0", "6_7", "8_3", "9_0", "11_65", "12_5", "14_0", "15_0", "17_62", "21_0", "23_9", "24_5"]
    t = np.array([0.01 * i for i in range(0, 1600001)])
    with open('time_series_xyz_x_0_5_y_4_z_1_t_400001_12_param.pickle', 'rb') as time_series_xyz:
        time_series = pickle.load(time_series_xyz)
    for i in range(0, 12):
        rungeplot_time_series(time_series, i, r_list[i], pr_list[i])
except Exception as ex:
    print("exception: " + str(ex))
end = time.time()
print(str(end - start))
