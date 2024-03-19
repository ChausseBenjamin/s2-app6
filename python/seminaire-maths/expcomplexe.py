import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2.5, 250)
f = 4  # Hz
decay = 0  # seconds
env = np.exp(decay*t)
y = np.exp(2*np.pi*f*1j*t)*env

xproj = np.real(y)
yproj = np.imag(y)

fig = plt.figure(figsize=(6, 6))
fig.suptitle(f'Exponentielle tournante de fréquence {f} Hz et amortissement de {np.abs(decay)} s')
ax = plt.axes(projection='3d')
ax.plot3D(t, xproj, yproj, linewidth=2)
ax.plot3D(t, xproj, np.ones_like(t)*-1.5)
ax.plot3D(t, np.ones_like(t)*2, yproj)
ax.plot3D(t, np.zeros_like(t), env)
ax.plot3D(t, np.ones_like(t)*2, env)
ax.plot3D(t, -env, np.zeros_like(t))
ax.plot3D(t, -env, np.ones_like(t)*-1.5)
ax.grid(visible=None, which='both', axis='both', linewidth=0.5)
ax.set_xlim(-.1, 3)
ax.set_ylim(-2, 2)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Real Axis')
ax.set_zlabel('Imag Axis')

plt.show()