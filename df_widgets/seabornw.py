# coding: utf-8
"""Widgets for Pandas Dataframes based on seaborn API."""
from __future__ import print_function, division, unicode_literals, absolute_import

import ipywidgets as ipw
import seaborn as sns
import df_widgets.utils as ut

from functools import wraps


@wraps(sns.countplot)
def countplot(df, **kwargs):

    def countplot(x, y, hue, color, saturation):
        x, y, hue = ut.widget2py(x, y, hue, color)
        ax, fig, _ = ut.get_ax_fig_plt()
        sns.countplot(x=x, y=y, hue=hue, data=df, order=None, hue_order=None, orient=None,
                      color=color, palette=None, saturation=saturation, ax=ax, **kwargs)

    allcols = list(df.keys())
    return ipw.interactive(
                countplot,
                x=["None"] + allcols,
                y=["None"] + allcols,
                hue=["None"] + allcols,
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

    allcols = list(df.keys())
    return ipw.interactive(
                joinplot,
                x=["None"] + allcols,
                y=["None"] + allcols,
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

    allcols = list(df.keys())
    return ipw.interactive(
                swarmplot,
                x=["None"] + allcols,
                y=["None"] + allcols,
                hue=["None"] + allcols,
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

    allcols = list(df.keys())
    return ipw.interactive(
                pairplot,
                x_vars=["None"] + allcols,
                y_vars=["None"] + allcols,
                hue=["None"] + allcols,
                kind=["scatter", "ref"],
                diag_kind=["hist", "kde"],
                __manual=True,
            )
