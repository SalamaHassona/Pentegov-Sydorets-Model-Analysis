import time
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pickle


def rungeplot_time_series(time_series, i, div, sdiv):
    plt.tight_layout(pad=0)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim([-2, 6])
    ax.set_ylim([-2, 4])
    ax.set_zlim([0, 30])
    ax.plot(time_series[0][i][100000:200001:10].ravel(),
            time_series[1][i][100000:200001:10].ravel(),
            time_series[2][i][100000:200001:10].ravel())
    ax.set_xlabel(r'$x$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$y$', fontsize=14, labelpad=10)
    ax.set_zlabel(r'$z$', fontsize=14, labelpad=5)
    ax.view_init(elev=22., azim=111.)
    ax.scatter(1, 1, 1, c='r', marker='o', label=r'$(1, 1, 1)$')
    plt.title(fr'R=17.62  $\Delta x_0={div}$  t=[1000, 2000]', fontsize=18, pad=10)
    plt.savefig(f'pictures/200001_div/R_17_62_x0_{sdiv}.jpg', bbox_inches='tight')


start = time.time()
try:
    div_list = ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
    pdiv_list = ["0_0", "0_1", "0_2", "0_3", "0_4", "0_5", "0_6", "0_7", "0_8", "0_9", "1_0"]
    with open('time_series_xyz_x_0_5_y_4_z_1_R_17_62_C_3_14_L_1_t_400001_11_ic.pickle', 'rb') as time_series_xyz:
        time_series = pickle.load(time_series_xyz)
    for i in range(0, 11):
        rungeplot_time_series(time_series, i, div_list[i], pdiv_list[i])
except Exception as ex:
    print("exception: " + str(ex))
end = time.time()
print(str(end - start))
