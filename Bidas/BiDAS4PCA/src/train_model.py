from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer
from sklearn.metrics import f1_score, matthews_corrcoef, average_precision_score
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import connect as c
import warnings
import time
warnings.filterwarnings('ignore')
model = MLPClassifier(max_iter=1000)
data = None
X = None
y = None

def fetch_data():
    return load_breast_cancer()
    '''url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
    data = pd.read_csv(url, names=[i for i in range(61)])
    data[60] = data[60].apply(numeric_class)
    print(data.shape)
    print(data)
    return data'''

def numeric_class(y):
    if y == 'M':
        return 0
    else:
        return 1

def train_model(X, y):
    global model, data
    #data = fetch_data()
    #X = data.iloc[:, :59]
    #y = data.iloc[:, 60]
    model.fit(X, y)

def obtain_metrics(X, y):
    metrics = []
    print("###########################################################")
    score = model.score(X, y)
    metrics.append(score)
    print("# Accuracy:\t", score)
    f1 = f1_score(y, model.predict(X), average='macro')
    metrics.append(f1)
    print("# f-score:\t", f1)
    auc = average_precision_score(y, model.predict(X))
    metrics.append(auc)
    print("# AUC:\t", auc)
    matthews = matthews_corrcoef(y, model.predict(X))
    metrics.append(matthews)
    print("# Matthew's:\t", matthews)
    print("###########################################################")
    return metrics

def establish_connection():
    return c.connect()

def get_dataset_metrics(conn, X_train, y_train):
    return c.get_metrics(conn, X_train, y_train)

def obtain_cv_metrics(k=3):
    global model#, data, X, y
    data = fetch_data()
    #print(data)
    X = data["data"] #data.iloc[:, :59]
    y = data["target"] #data.iloc[:, 60]
    k_fold = KFold(k)
    fold = 0
    table = []
    for train_index, test_index in k_fold.split(X):#X.values):
        fold += 1
        print("###########################################################")
        print("# Fold: ", fold)
        print("###########################################################")
        '''X_train, X_test = X.values[train_index], X.values[test_index]
        y_train, y_test = y.values[train_index], y.values[test_index]'''
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        #print(X_train)
        #print(y_train)
        model.fit(X_train, y_train)
        #print(X_test)
        #print(y_test)
        metrics = [k, len(X_train)]
        metrics.extend(obtain_metrics(X_test, y_test))
        X_train = np.c_[X_train]
        y_train = np.c_[y_train]
        conn = establish_connection()
        dataset_metrics = get_dataset_metrics(conn, X_train, y_train)
        conn.close()
        metrics.extend(dataset_metrics)
        table.append(metrics)
    #print(np.mean(table, axis=0))
    return table

def iterative_cv(lower_limit=2, upper_limit=15):
    metrics = []
    for k in range(lower_limit, upper_limit+1):
        for i in range(15):
            print("\n\n>> Number of folds: ", k)
            metrics.extend(obtain_cv_metrics(k))
    df = pd.DataFrame(metrics, columns=['k', 'samples', 'accuracy', 'f-score', 'auc', 'matthews',
                                      'balance_c1', 'balance_c2', 'correlation_c1',
                                      'correlation_c2', 'correlation_c3',
                                      'correlation_c4', 'dimensionality_t2',
                                      'dimensionality_t3', 'dimensionality_t4',
                                      'l1', 'l2', 'l3', 'n1', 'n2', 'n3', 'n4',
                                      't1', 'lsc', 'density', 'clscoef', 'hub',
                                      'f1' ,'f1v', 'f2', 'f3', 'f4', 's1', 's2',
                                      's3', 's4'])
    df.to_csv('results/'+str(time.time())+'.csv', header=True, mode='w+')
    plot_values(df)

def plot_values(df):
    return
    df = df.sort_values('balance_c1')
    df.plot(kind='line', x='balance_c1', y='f-score', color='blue')
    #plt.show()
    df = df.sort_values('balance_c2')
    df.plot(kind='line', x='balance_c2', y='f-score', color='red')
    #plt.show()
    df = df.sort_values('correlation_c1')
    df.plot(kind='line', x='correlation_c1', y='f-score', color='green')
    #plt.show()
    df = df.sort_values('dimensionality_t2')
    df.plot(kind='line', x='dimensionality_t2', y='f-score', color='orange')
    plt.show()

if __name__ == "__main__":
    iterative_cv(lower_limit=3, upper_limit=10)
    #obtain_cv_metrics()
    '''train_model()
    obtain_metrics()'''
    #data = np.c_[data['data'], data['target']]
    #print(type(data))
    '''X = np.c_[X]
    y = np.c_[y]
    get_dataset_metrics(establish_connection())'''
