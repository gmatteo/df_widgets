# coding: utf-8
"""Widgets for Pandas Dataframes."""
from __future__ import print_function, division, unicode_literals, absolute_import

import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as ipw
import df_widgets.utils as ut

from functools import wraps


@wraps(pd.DataFrame.plot)
def dfw_plot(df, **kwargs):

    def plot_dataframe(x, y, kind, subplots, grid, legend):
        x, y = ut.widget2py(x, y)
        df.plot(x=x, y=y, kind=kind, subplots=subplots, sharex=None, sharey=False,
                layout=None, figsize=None, use_index=True, title=None, grid=grid, legend=legend, style=None,
                logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None,
                rot=None, fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False,
                sort_columns=False, **kwargs)
        plt.show()

    allcols = list(df.keys())
    return ipw.interactive(
                plot_dataframe,
                x=["None"] + allcols,
                y=["None"] + allcols,
                kind=["line", "bar", "barh", "hist", "box", "kde", "density", "area", "pie", "scatter", "hexbin"],
                subplots=False,
                grid=True,
                legend=True,
                __manual=True,
            )
