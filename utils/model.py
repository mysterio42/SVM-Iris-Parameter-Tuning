from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score

from utils.plot import plot_cm


def train_model(data, args,param):
    model = svm.SVC(C=args.C if args.__contains__('C') else 1.0,
                    kernel=args.kernel if args.__contains__('kernel') else 'rbf',
                    degree=args.degree if args.__contains__('degree') else 3,
                    gamma=args.gamma if args.__contains__('gamma') else 'scale',
                    )

    model.fit(data['train']['features'], data['train']['labels'])

    preds = model.predict(data['test']['features'])

    score = accuracy_score(data['test']['labels'], preds)


    param['C']= model.C,
    param['kernel']= model.kernel,
    param['degree']= model.degree,
    param['gamma']= model.gamma,
    param['accuracy']= f'{score:.2f}'

    cm = confusion_matrix(data['test']['labels'], preds)
    plot_cm(cm, param)

    return model, param
