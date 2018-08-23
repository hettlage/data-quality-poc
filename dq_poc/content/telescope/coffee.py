import numpy as np
from bokeh.plotting import figure
from dq_poc.util import plot_grid

def plot(f):
    x = np.linspace(0, 2 * 3.14159)

    p = figure(plot_height=1500, plot_width=2000)
    p.line(x, f(x))

    return p

title = 'Coffee Machine Uptime'

content = plot_grid(2, plot(np.sin), plot(np.cos), plot(np.tan), plot(np.sin))

description = 'Availability of the coffee machine. The availability of the machine itself as well as the supply of coffee beans are measured.'
