import numpy as np
import matplotlib.pyplot as plt

r_values = np.linspace(5, 25, 1000)

exponents = np.load('lyapunov_exponent_r.npy')
plt.figure(figsize=(20,8))
plt.plot(r_values, exponents, color="red")
plt.vlines(5.0, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(6.7, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(8.3, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(9.0, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(11.65, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(12.5, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(14.0, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(15.0, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(17.62, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(21.0, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(23.9, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(24.5, np.min(exponents)-np.mean(exponents)*0.1,np.max(exponents)+np.mean(exponents)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.xlabel('R', fontsize=26, fontweight='bold', fontstyle='oblique', labelpad=20)
plt.ylabel('Największy wykładnik Lapunowa', fontsize=26, fontweight='bold', fontstyle='oblique', labelpad=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig('pictures/rosenstein_exponents.jpg')
plt.show()

exponents = np.load('lyapunov_exponent_e.npy')
max_exponents_chaos = np.max(exponents, axis=1)
plt.figure(figsize=(20,8))
plt.plot(r_values, max_exponents_chaos, color="green")
plt.vlines(5.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(6.7, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(8.3, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(9.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(11.65, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(12.5, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(14.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(15.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(17.62, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(21.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(23.9, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(24.5, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

# plt.title('title name')
plt.xlabel('R', fontsize=26, fontweight='bold', fontstyle='oblique', labelpad=20)
plt.ylabel('Największy wykładnik Lapunowa', fontsize=26, fontweight='bold', fontstyle='oblique', labelpad=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig('pictures/eckmann_exponents.jpg')
plt.show()

r_list = ["5.0", "6.7", "8.3", "9.0", "11.65", "12.5", "14.0", "15.0", "17.62", "21.0", "23.9", "24.5"]
exponents = np.load('parker_chua_dt_001009_sims_1000_error_1e3_steps_100_burn_1000.npy')
max_exponents_chaos = np.max(exponents, axis=1)
plt.figure(figsize=(20,8))
plt.plot(r_values, max_exponents_chaos, color="brown")
plt.vlines(5.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(6.7, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(8.3, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(9.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(11.65, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(12.5, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(14.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(15.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(17.62, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(21.0, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

plt.vlines(23.9, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])
plt.vlines(24.5, np.min(max_exponents_chaos)-np.mean(max_exponents_chaos)*0.1,np.max(max_exponents_chaos)+np.mean(max_exponents_chaos)*0.1, color="black", linestyles=[(0,(9,3,4,4))])

# plt.title('001006 100')
plt.xlabel('R', fontsize=26, fontweight='bold', fontstyle='oblique', labelpad=20)
plt.ylabel('Największy wykładnik Lapunowa', fontsize=26, fontweight='bold', fontstyle='oblique', labelpad=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig('pictures/parker_exponents.jpg')
plt.show()
