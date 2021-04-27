from matplotlib import pyplot as pl
import pandas as pd

df = pd.read_csv('visc_cu50zr50_set_1-run_1_1100K.csv')

x = df['v_time'].values
y = df['v_visc'].values

indx_start = x < 8
indx_end = x >= 8

fig, ax = pl.subplots()

ax.plot(x[indx_end], y[indx_end], label='Settled')
ax.plot(x[indx_start], y[indx_start])

ax.legend()
ax.set_xlabel(r'$t_{s}$ [ns]')
ax.set_ylabel(r'Viscosity [$Pa \cdot s$]')
fig.tight_layout()
fig.savefig('visc_cu50zr50_set_1-run_1_1100K')

pl.show()
