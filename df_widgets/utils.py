# coding: utf-8
"""Widgets for Pandas Dataframes."""
from __future__ import print_function, division, unicode_literals, absolute_import

from collections import OrderedDict
from ipywidgets import widgets


def add_docstrings(*tuples):
    """
    This decorator adds to the docstring the documentation for functions.
    When writing high-level API, it's quite common to call thirdy-party functions
    with a restricted set of arguments while optional keyword arguments are
    collected in an optional dictionary.

    The first item of the tuple contains the function (python object) wrapped by the code.
    The second item is list of strings with the name of the actual arguments passed to function.
    """
    from functools import wraps
    def wrapper(func):
	@wraps(func)
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)

        # Add docstrings for the functions that will be called by func.
	lines = []
	app = lines.append
	for t in tuples:
	    fname = t[0].__name__
	    # List of strings or string.
	    if isinstance(t[1], (list, tuple)):
		fargs = ",".join("`%s`" % a for a in t[1])
	    else:
		fargs = "`%s`" % t[1]
	    app("\n%s are passed to function :func:`%s` in module :mod:`%s`" % (fargs, fname, t[0].__module__))
	    app("Docstring of `%s`:" % fname)
	    app(t[0].__doc__)
	s = "\n".join(lines)

        if wrapped_func.__doc__ is not None:
            # Add s at the end of the docstring.
            wrapped_func.__doc__ += "\n" + s
        else:
            # Use s
            wrapped_func.__doc__ = s
        return wrapped_func
    return wrapper


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
        description='marker',
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
        description='color',
    )


def linewidth_slider(default=1, orientation="horizontal"):
    return widgets.FloatSlider(
        value=default,
        min=0,
        max=10,
        step=0.5,
        description='linewidth',
        orientation=orientation,
        readout_format='.1f'
    )


def size_slider(default=5, orientation="horizontal"):
    return widgets.FloatSlider(
        value=default,
        min=0,
        max=20,
        step=0.5,
        description='size',
        orientation=orientation,
        readout_format='.1f'
    )

def saturation_slider(default=0.75, orientation="horizontal"):
    return widgets.FloatSlider(
        value=default,
        min=0,
        max=1,
        step=0.05,
        description='saturation',
        orientation=orientation,
        readout_format='.1f'
    )
