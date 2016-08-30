# coding: utf-8
"""Widgets for Pandas Dataframes."""
from __future__ import print_function, division, unicode_literals, absolute_import

from collections import OrderedDict
from ipywidgets import widgets


def widget2py(*args):
    return [None if a == "None" else a for a in args]


def get_ax_fig_plt(ax=None):
    """
    Helper function used in plot functions supporting an optional Axes argument.
    If ax is None, we build the `matplotlib` figure and create the Axes else
    we return the current active figure.

    Returns:
        ax: :class:`Axes` object
        figure: matplotlib figure
        plt: matplotlib pyplot module.
    """
    import matplotlib.pyplot as plt
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
    else:
        fig = plt.gcf()

    return ax, fig, plt


# Taken from matplotlib.markers.MarkerStyle (replaced dict with OrderedDict).
_mpl_markers = OrderedDict([
    ('.', 'point'),
    (',', 'pixel'),
    ('o', 'circle'),
    ('v', 'triangle_down'),
    ('^', 'triangle_up'),
    ('<', 'triangle_left'),
    ('>', 'triangle_right'),
    ('1', 'tri_down'),
    ('2', 'tri_up'),
    ('3', 'tri_left'),
    ('4', 'tri_right'),
    ('8', 'octagon'),
    ('s', 'square'),
    ('p', 'pentagon'),
    ('*', 'star'),
    ('h', 'hexagon1'),
    ('H', 'hexagon2'),
    ('+', 'plus'),
    ('x', 'x'),
    ('D', 'diamond'),
    ('d', 'thin_diamond'),
    ('|', 'vline'),
    ('_', 'hline'),
    #(TICKLEFT: 'tickleft',
    #(TICKRIGHT: 'tickright',
    #(TICKUP: 'tickup',
    #(TICKDOWN: 'tickdown',
    #(CARETLEFT: 'caretleft',
    #(CARETRIGHT: 'caretright',
    #(CARETUP: 'caretup',
    #(CARETDOWN: 'caretdown',
    ("None", 'nothing'),
    (None, 'nothing'),
    (' ', 'nothing'),
    ('', 'nothing'),
])


def markers_dropdown(default="o"):
    return widgets.Dropdown(
        options={name: key for key, name in _mpl_markers.items()},
        value=default,
        description='Marker:',
    )


_mpl_colors = OrderedDict([
    ("None", "None"),
    ("blue", "b"),
    ("green", "g"),
    ("red", "r"),
    ("cyan", "c"),
    ("magenta", "m"),
    ("yellow", "y"),
    ("black", "k"),
    ("white", "w"),
])


def colors_dropdow(default="None"):
    return widgets.Dropdown(
        options=_mpl_colors,
        value=default,
        description='Color:',
    )


def linewidth_slider(default=1, orientation="horizontal"):
    return widgets.FloatSlider(
        value=default,
        min=0,
        max=10,
        step=0.5,
        description='Linewidth:',
        orientation=orientation,
        readout_format='.1f'
    )


def size_slider(default=5, orientation="horizontal"):
    return widgets.FloatSlider(
        value=default,
        min=0,
        max=20,
        step=0.5,
        description='Size:',
        orientation=orientation,
        readout_format='.1f'
    )

def saturation_slider(default=0.75, orientation="horizontal"):
    return widgets.FloatSlider(
        value=default,
        min=0,
        max=1,
        step=0.05,
        description='Saturation:',
        orientation=orientation,
        readout_format='.1f'
    )
