import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data(path, label, *features):
    df = pd.read_csv(path)

    features, labels = df[list(*features)].to_numpy(), df[label].to_numpy()
    labels = LabelEncoder().fit_transform(labels)

    data = train_test_split(features, labels, test_size=0.3, random_state=42)
    data = {
        'train': {
            'features': data[0],
            'labels': data[2],
        },
        'test': {
            'features': data[1],
            'labels': data[3]
        }
    }

    return data
