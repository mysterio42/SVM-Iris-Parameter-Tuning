import re

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import colors

FIGURES_DIR = 'figures/'

plt.rcParams['figure.figsize'] = (13.66, 6.79)
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 100


def plot_boundary(model, data, param):
    x_min, x_max = data['features'][:, 0].min(), data['features'][:, 0].max()
    y_min, y_max = data['features'][:, 1].min(), data['features'][:, 1].max()

    h = (x_max / x_min) / 100
    x_min -= h
    y_min -= h
    x_max += h
    y_max += h

    h = h / 4

    x_dots = np.arange(x_min, x_max, h)
    y_dots = np.arange(y_min, y_max, h)
    x_torow, y_tocol = np.meshgrid(x_dots, y_dots)
    x_flatten_rep = x_torow.ravel()
    y_flatten_rep = y_tocol.ravel()
    x_y = np.c_[x_flatten_rep, y_flatten_rep]
    preds = model.predict(x_y)
    preds = preds.reshape(x_torow.shape)

    cmap = colors.ListedColormap(['deeppink', 'green', 'blue', ])

    plt.subplot(1, 1, 1)
    plt.contourf(x_torow, y_tocol, preds, cmap=cmap, alpha=0.8)
    plt.scatter(data['features'][:, 0], data['features'][:, 1], c=data['labels'], cmap=cmap)
    plt.xlabel('SepalLength')
    plt.ylabel('SepalWidth')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    title = re.sub("[{}' ,()]", '', str(param))
    plt.title(f'svm {title}')
    plt.savefig(FIGURES_DIR + f'Figure_preds_{title}' + '.png')
    plt.show()


def plot_cm(cm, param):
    sns.heatmap(cm / np.sum(cm), annot=True, fmt='.2%', cmap='Blues')
    title = re.sub("[{}' ,()]", '', str(param))
    plt.title(title)
    plt.savefig(FIGURES_DIR + f'Figure_cm_{title}' + '.png')
    plt.show()
