from bokeh.embed import components
from collections import namedtuple
from flask import render_template


PlotHtml = namedtuple('PlotHtml', ('id', 'grid_div', 'grid_script', 'closeup_div', 'closeup_script'))

plot_id = 1

def plot_grid(columns, *plots):
    # create html content
    html = []
    for plot in plots:
        current_sizing_mode = plot.sizing_mode
        try:
            current_toolbar_location = plot.toolbar_location
            plot.sizing_mode = 'scale_width'
            try:
                plot.toolbar_location = None
                grid_html = components(plot)
            finally:
                plot.toolbar_location = current_toolbar_location
            closeup_html = components(plot)
        finally:
            plot.sizing_mode = current_sizing_mode

        global plot_id
        html.append(PlotHtml(id=plot_id,
                             grid_div=grid_html[1],
                             grid_script=grid_html[0],
                             closeup_div=grid_html[1],
                             closeup_script=closeup_html[0]))
        plot_id += 1

    return render_template('plot_grid.html', columns=columns, plot_html=html)
