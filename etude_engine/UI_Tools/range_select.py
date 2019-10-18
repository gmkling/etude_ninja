
import numpy as np

from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.plotting import figure

from scipy.io import wavfile
fs, data = wavfile.read('/home/garrykling/Projects/electroform/audio/Kopprasch_3_excerpt2.wav')

source = ColumnDataSource({'y': data, 'x': np.arange(0, len(data), 1)})

p = figure(plot_height=300, plot_width=800, tools="xpan", toolbar_location=None,
           x_axis_type="linear", x_axis_location="above",
           background_fill_color="#efefef", x_range=(2000, 12500))

p.line('x', 'y', source=source)
p.yaxis.axis_label = 'Audio'

select = figure(title="Drag the middle and edges of the selection box to change the range above",
                plot_height=130, plot_width=800, y_range=p.y_range,
                x_axis_type="datetime", y_axis_type=None,
                tools="", toolbar_location=None, background_fill_color="#efefef")

range_tool = RangeTool(x_range=p.x_range)
range_tool.overlay.fill_color = "navy"
range_tool.overlay.fill_alpha = 0.2

select.line('x', 'y', source=source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool

show(column(p, select))