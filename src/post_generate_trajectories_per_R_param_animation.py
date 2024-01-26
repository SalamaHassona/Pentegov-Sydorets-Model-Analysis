import numpy as np
import time
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pickle
import matplotlib.animation as animation

start = time.time()

try:
    r_list = np.linspace(5.0, 25.0, num=1000)
    with open('time_series_xyz_x_0_5_y_4_z_1_t_400001_1000_param.pickle', 'rb') as time_series_xyz:
        time_series = pickle.load(time_series_xyz)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca(projection='3d')
    plt.tight_layout(pad=3)
    def rungeplot_time_series(i):
        ax.clear()
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
        plt.title(fr'$R = {r_list[i]:.2f}$', fontsize=18, pad=0)

    rungeplot_time_series(0)

    ani = animation.FuncAnimation(fig=fig, func=rungeplot_time_series, frames=1000, interval=30)
    ani.save(filename="animation_200001_30_r.mp4", writer="ffmpeg")

except Exception as ex:
    print("exception: " + str(ex))
end = time.time()
print(str(end - start))
