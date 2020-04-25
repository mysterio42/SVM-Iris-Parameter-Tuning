import argparse

import numpy as np

from utils.config import params
from utils.data import load_data
from utils.model import train_model
from utils.plot import plot_boundary


def parse_args():
    parser = argparse.ArgumentParser()

    subp = parser.add_subparsers(help='which kernel we choose', dest='kernel')

    parser_lin = subp.add_parser('linear', help='linear kernel')
    parser_lin.add_argument('--C', choices=params['C'], type=float, help='C params')

    parser_rbf = subp.add_parser('rbf', help='rbf kernel')
    parser_rbf.add_argument('--gamma', choices=params['gamma'], type=float, help='Gamma params')
    parser_rbf.add_argument('--C', choices=params['C'], type=float, help='C params')

    parser_poly = subp.add_parser('poly', help='kernel poly')
    parser_poly.add_argument('--gamma', choices=params['gamma'], type=float, help='Gamma params')
    parser_poly.add_argument('--C', choices=params['C'], type=float, help='C params')
    parser_poly.add_argument('--degree', choices=params['degree'], type=int, help='degree params')

    parser.print_help()

    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()

    np.random.seed(2)

    features = (('PetalLength', 'PetalWidth'), ('SepalLength', 'SepalWidth'))

    for feature in features:

        param = {}
        data = load_data('data/iris_data.csv', 'Class', feature)
        param['feature'] = ''.join(feature)

        model, param = train_model(data, args,param)


        param['mode'] = 'train'
        plot_boundary(model, data['train'], param)

        param['mode'] = 'test'
        plot_boundary(model, data['test'], param)
