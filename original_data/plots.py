#### Plots

#plotting the harmonic potential as before
plt.plot(_x, _harmpot(_x), color='red', label="Harmonic potential")
plt.title('Harmonic Potential and $\psi$ vs. $x$')
plt.xlabel("$x$")
plt.ylabel("$V_{harmonic}$ and $\psi$")
plt.show
#plotting the wave functions over the harmonic potential plot, on their respective energies
for i in range(0,7):
    _psi=sp.lambdify([x], psi[i])
    _x = np.linspace(-5.,5.,250)
    _psi
    plt.plot(_x, _psi(_x)+evs(i), color=colors[i], label=labels[i])
    plt.legend()
    plt.show