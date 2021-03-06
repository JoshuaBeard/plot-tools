import plottingtools as pt
import numpy as np


length = 25
y = np.arange(length) - np.random.randint(length, size=length)

kwargs = dict(plot_type='lines',
              y=y,
              title='Witty Title',
              )

if __name__ == "__main__":
    plot = pt.plot.Lines(**kwargs)
