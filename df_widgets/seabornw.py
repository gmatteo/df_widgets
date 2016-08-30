# coding: utf-8
"""Widgets for Pandas Dataframes based on seaborn API."""
from __future__ import print_function, division, unicode_literals, absolute_import

import sys
import ipywidgets as ipw
import seaborn as sns
import df_widgets.utils as ut

from functools import wraps
from collections import OrderedDict
from IPython.display import display, clear_output

__all__ = [
    "api_selector",
    "countplot",
    "swarmplot",
    "pairplot",
    "lmplot",
    "factorplot",
    "stripplot",
    "swarmplot",
]


def api_selector(df, funcname="countplot"):
    """
    A widgets with ToogleButtons that allow the user to select and display
    the widget associated to the different seaborn functions.
    """
    this_module = sys.modules[__name__]
    name2wfunc = OrderedDict()
    for a in __all__:
        if a == "api_selector": continue
        func = this_module.__dict__.get(a)
        if not callable(func): continue
        name2wfunc[func.__name__] = func

    w1 = ipw.ToggleButtons(description='seaborn API', options=list(name2wfunc.keys()))
    w1.value = funcname
    w2 = name2wfunc[funcname](df)
    box = ipw.VBox(children=[w1, w2])

    def on_value_change(change):
        #print(change)
        box.close()
        clear_output()
        api_selector(df, funcname=change["new"])
    w1.observe(on_value_change, names='value')

    return display(box)

"""
Regression plots
lmplot(x, y, data[, hue, col, row, palette, ...])	Plot data and regression model fits across a FacetGrid.
regplot(x, y[, data, x_estimator, x_bins, ...])	Plot data and a linear regression model fit.
residplot(x, y[, data, lowess, x_partial, ...])	Plot the residuals of a linear regression.
interactplot(x1, x2, y[, data, filled, ...])	Visualize a continuous two-way interaction with a contour plot.
coefplot(formula, data[, groupby, ...])	Plot the coefficients from a linear model.

Categorical plots
factorplot([x, y, hue, data, row, col, ...])	Draw a categorical plot onto a FacetGrid.
boxplot([x, y, hue, data, order, hue_order, ...])	Draw a box plot to show distributions with respect to categories.
violinplot([x, y, hue, data, order, ...])	Draw a combination of boxplot and kernel density estimate.
stripplot([x, y, hue, data, order, ...])	Draw a scatterplot where one variable is categorical.
swarmplot([x, y, hue, data, order, ...])	Draw a categorical scatterplot with non-overlapping points.
pointplot([x, y, hue, data, order, ...])	Show point estimates and confidence intervals using scatter plot glyphs.
barplot([x, y, hue, data, order, hue_order, ...])	Show point estimates and confidence intervals as rectangular bars.
countplot([x, y, hue, data, order, ...])	Show the counts of observations in each categorical bin using bars.

Matrix plots
heatmap(data[, vmin, vmax, cmap, center, ...])	Plot rectangular data as a color-encoded matrix.
clustermap(data[, pivot_kws, method, ...])	Plot a hierarchically clustered heatmap of a pandas DataFrame

Timeseries plots
tsplot(data[, time, unit, condition, value, ...])	Plot one or more timeseries with flexible representation of uncertainty.

Miscellaneous plots
palplot(pal[, size])	Plot the values in a color palette as a horizontal array.

Axis grids
FacetGrid(data[, row, col, hue, col_wrap, ...])	Subplot grid for plotting conditional relationships.
PairGrid(data[, hue, hue_order, palette, ...])	Subplot grid for plotting pairwise relationships in a dataset.
JointGrid(x, y[, data, size, ratio, space, ...])	Grid for drawing a bivariate plot with marginal univariate plots.
"""


@wraps(sns.countplot)
def countplot(df, **kwargs):

    def countplot(x, y, hue, color, saturation):
        x, y, hue, color = ut.widget2py(x, y, hue, color)
        ax, fig, _ = ut.get_ax_fig_plt()
        sns.countplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None, orient=None,
                      color=color, palette=None, saturation=saturation, ax=ax, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                countplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                color=ut.colors_dropdow(),
                saturation=ut.saturation_slider(),
                __manual=True,
            )


@wraps(sns.jointplot)
def joinplot(df, joint_kws=None, marginal_kws=None, annot_kws=None, **kwargs):

    def joinplot(x, y, kind, color):
        x, y, color = ut.widget2py(x, y, color)
        # TODO: stat_func
        sns.jointplot(x, y, data=df, kind=kind, # stat_func=<function pearsonr>,
                      color=color, size=6, ratio=5, space=0.2, dropna=True, xlim=None, ylim=None,
                      joint_kws=joint_kws, marginal_kws=marginal_kws, annot_kws=annot_kws, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                joinplot,
                x=allcols,
                y=allcols,
                kind=["scatter", "reg", "resid", "kde", "hex"],
                color=ut.colors_dropdow(),
                __manual=True,
            )


@wraps(sns.swarmplot)
def swarmplot(df, **kwargs):

    def swarmplot(x, y, hue, split, orient, color, size, linewidth):
        x, y, hue, orient, color = ut.widget2py(x, y, hue, orient, color)
        ax, fig, _ = ut.get_ax_fig_plt()
        sns.swarmplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None,
                      split=split, orient=orient, color=color, palette=None, size=size,
                      edgecolor='gray', linewidth=linewidth, ax=ax, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                swarmplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                split=False,
                orient=["None", "v", "h"],
                color=ut.colors_dropdow(),
                size=ut.size_slider(default=5),
                linewidth=ut.linewidth_slider(default=0),
                __manual=True,
            )


@wraps(sns.pairplot)
def pairplot(df, plot_kws=None, diag_kws=None, grid_kws=None):
    # TODO: Write widget with multiple checkboxes to implement lists.

    def pairplot(x_vars, y_vars, hue, kind, diag_kind):
        x_vars, y_vars, hue = ut.widget2py(x_vars, y_vars, hue)
        sns.pairplot(df, hue=hue, hue_order=None, palette=None, vars=None, x_vars=x_vars, y_vars=y_vars,
                     kind=kind, diag_kind=diag_kind, markers=None, size=2.5, aspect=1, dropna=True,
                     plot_kws=plot_kws, diag_kws=diag_kws, grid_kws=grid_kws)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                pairplot,
                x_vars=allcols,
                y_vars=allcols,
                hue=allcols,
                kind=["scatter", "ref"],
                diag_kind=["hist", "kde"],
                __manual=True,
            )


@wraps(sns.lmplot)
def lmplot(df, scatter_kws=None, line_kws=None):

    def lmplot(x, y, hue, col, row, legend, size):
        x, y, hue, col, row = ut.widget2py(x, y, hue, col, row)
        sns.lmplot(x, y, df, hue=hue, col=col, row=row, palette=None, col_wrap=None,
                   size=size, aspect=1, markers='o', sharex=True, sharey=True, hue_order=None,
                   col_order=None, row_order=None, legend=legend, legend_out=True,
                   x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True,
                   ci=95, n_boot=1000, units=None, order=1, logistic=False, lowess=False, robust=False,
                   logx=False, x_partial=None, y_partial=None, truncate=False, x_jitter=None, y_jitter=None,
                   scatter_kws=scatter_kws, line_kws=line_kws)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                lmplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                col=allcols,
                row=allcols,
                legend=True,
                size=ut.size_slider(default=5),
                __manual=True,
            )


@wraps(sns.factorplot)
def factorplot(df, facet_kws=None, **kwargs):

    def factorplot(x, y, hue, color, kind, size, legend):
        x, y, hue, color = ut.widget2py(x, y, hue, color)
        sns.factorplot(x=x, y=y, hue=hue, data=df, row=None, col=None, col_wrap=None, # estimator=<function mean>,
                       ci=95, n_boot=1000, units=None, order=None, hue_order=None, row_order=None, col_order=None,
                       kind=kind, size=size, aspect=1, orient=None, color=color, palette=None,
                       legend=legend, legend_out=True, sharex=True, sharey=True, margin_titles=False,
                       facet_kws=facet_kws, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                factorplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                color=ut.colors_dropdow(),
                kind=["point", "bar", "count", "box", "violin", "strip"],
                size=ut.size_slider(default=4),
                legend=True,
                __manual=True,
            )


@wraps(sns.boxplot)
def boxplot(df, **kwargs):

    def boxplot(x, y, hue, orient, color, notch):
        x, y, hue, orient, color = ut.widget2py(x, y, hue, orient, color)
        ax, fig, _ = ut.get_ax_fig_plt()
        sns.boxplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None, orient=orient,
                    color=color, palette=None, saturation=0.75, width=0.8, fliersize=5, linewidth=None,
                    whis=1.5, notch=notch, ax=ax, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                boxplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                orient=["None", "v", "h"],
                color=ut.colors_dropdow(),
                notch=False,
                __manual=True,
            )


@wraps(sns.violinplot)
def violinplot(df, **kwargs):

    def violinplot(x, y, hue, bw, scale, inner, split, orient, color, saturation):
        x, y, hue, inner, orient, color = ut.widget2py(x, y, hue, inner, orient, color)
        ax, fig, _ = ut.get_ax_fig_plt()

        sns.violinplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None,
                       bw=bw, cut=2, scale=scale, scale_hue=True,
                       gridsize=100, width=0.8, inner=inner, split=split, orient=orient,
                       linewidth=None, color=color, palette=None, saturation=saturation, ax=ax, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                violinplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                bw=["scott", "silverman", "float"],
                scale=["area", "count", "width"],
                inner=["box", "quartile", "point", "stick", "None"],
                split=False,
                orient=["None", "v", "h"],
                color=ut.colors_dropdow(),
                saturation=ut.saturation_slider(),
                __manual=True,
            )


@wraps(sns.stripplot)
def stripplot(df, **kwargs):

    def stripplot(x, y, hue, split, orient, color, size, linewidth):
        x, y, hue, orient, color = ut.widget2py(x, y, hue, orient, color)
        ax, fig, _ = ut.get_ax_fig_plt()

        sns.stripplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None, jitter=False,
                      split=split, orient=orient, color=color, palette=None, size=size, edgecolor='gray',
                      linewidth=linewidth, ax=ax, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                stripplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                split=False,
                orient=["None", "v", "h"],
                color=ut.colors_dropdow(),
                size=ut.size_slider(default=5),
                linewidth=ut.linewidth_slider(default=0),
                __manual=True,
            )


@wraps(sns.swarmplot)
def swarmplot(df, **kwargs):

    def swarmplot(x, y, hue, split, orient, color, size, linewidth):
        x, y, hue, orient, color = ut.widget2py(x, y, hue, orient, color)
        ax, fig, _ = ut.get_ax_fig_plt()

        sns.swarmplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None,
                     split=split, orient=orient, color=color, palette=None, size=size, edgecolor='gray',
                     linewidth=linewidth, ax=ax, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                swarmplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                split=False,
                orient=["None", "v", "h"],
                color=ut.colors_dropdow(),
                size=ut.size_slider(default=5),
                linewidth=ut.linewidth_slider(default=0),
                __manual=True,
            )


@wraps(sns.pointplot)
def pointplot(df, **kwargs):

    def pointplot(x, y, hue, split, join, orient, color, linewidth):
        x, y, hue, orient, color = ut.widget2py(x, y, hue, orient, color)
        ax, fig, _ = ut.get_ax_fig_plt()

        sns.pointplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None, # estimator=<function mean>,
                      ci=95, n_boot=1000, units=None, markers='o', linestyles='-', dodge=False, join=join, scale=1,
                      orient=orient, color=color, palette=None, ax=ax, errwidth=None, capsize=None, **kwargs)

    allcols = ["None"] + list(df.keys())
    return ipw.interactive(
                pointplot,
                x=allcols,
                y=allcols,
                hue=allcols,
                split=False,
                join=True,
                orient=["None", "v", "h"],
                color=ut.colors_dropdow(),
                linewidth=ut.linewidth_slider(default=0),
                __manual=True,
            )
