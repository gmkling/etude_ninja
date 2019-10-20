'''
range_select_view.py

Functions using the range select model in bokeh to adjust event markers
in a sound file.

'''

import argparse
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from bokeh.io import show
from bokeh.events import ButtonClick
from bokeh.layouts import column
from bokeh.models import CustomJS, Button, ColumnDataSource, RangeTool
from bokeh.plotting import figure


def load_wav(filename):
    '''
    load_wav
    :param filename: full path to wav file, functions in this file assume mono
    :return: ColumnDataSource, sRate (sampleRate)
    '''
    sRate, data = wavfile.read(filename)
    audioSource = ColumnDataSource({'y': data, 'x': np.arange(0, len(data), 1)})
    return audioSource, sRate

def play_selection(audioSlice, inPoint, outPoint):
    return CustomJS(args=dict(source=audioSlice, inPt=inPoint, outPt=outPoint), code="""
    var data = source.data;
    var f = cb_obj.value
    console.log(`JS:Click to play from ${inPt} to ${outPt}`)
""")

def plot_wav_range(audioSource):
    p = figure(plot_height=300, plot_width=800, tools="xpan", toolbar_location=None,
               x_axis_type="linear", x_axis_location="above",
               background_fill_color="#efefef", x_range=(2000, 12500))

    p.line('x', 'y', source=audioSource)
    p.yaxis.axis_label = 'Audio'

    select = figure(title="Drag the middle and edges of the selection box to change the range above",
                    plot_height=130, plot_width=800, y_range=p.y_range,
                    x_axis_type="datetime", y_axis_type=None,
                    tools="", toolbar_location=None, background_fill_color="#efefef")

    range_tool = RangeTool(x_range=p.x_range)
    range_tool.overlay.fill_color = "navy"
    range_tool.overlay.fill_alpha = 0.2
    play_button = Button(label="Play Selection")
    play_button.js_on_event(ButtonClick, play_selection(audioSource, range_tool.x_range.start, range_tool.x_range.end))

    select.line('x', 'y', source=audioSource)
    select.ygrid.grid_line_color = None
    select.add_tools(range_tool)
    select.toolbar.active_multi = range_tool

    show(column(p, select, play_button))

def main():
    ''''
        This script will be run with an audio filename and some sort of list of events
        User will use web UI to adjust the in and out points visually, with the assistance
        of audio playback of segments. 
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fname', metavar='Filename', type=str, nargs=1,
                        help='Name of the audio file to input.')
    args = parser.parse_args()
    filepath = args.fname

    if filepath:
        #filename = str(args.fname)
        print(Path(str(filepath)))
        audio, fs = load_wav(filepath[0])
        plot_wav_range(audio)

if __name__ == '__main__':
    main()