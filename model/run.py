from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

from matplotlib import pyplot as pl
from scipy.stats import sem

import pandas as pd
import numpy as np
import jsonlines
import pickle
import random
import shap
import sys
import os

label = {}
label['tstar'] = r'$T^{*}$'
label['tl'] = r'$T_{l}$'
label['tstarextrap'] = r'$T_{g}^{*}$'
label['ta'] = r'$T_{A}^{*}$'
label['tprime'] = r"$T^{'}$"
label['taprime'] = r"$T_{A}^{'}$"
label['tprimeextrap'] = r"$T_{g}^{'}$"
label['tg'] = r'$T_{gm}$'


def parallel(func, x, *args, **kwargs):
    '''
    Run some function in parallel.
    '''

    pool = Pool(os.cpu_count())
    part_func = partial(func, *args, **kwargs)

    data = list(tqdm(pool.imap(part_func, x), total=len(x), file=sys.stdout))
    pool.close()
    pool.join()

    return data


def main():
    df = 'features_gfa_cts.csv'
    save = './'
    seed = 22478
    model = 'xgboost_model.pickle'

    os.makedirs(save, exist_ok=True)

    with open(model, 'rb') as f:
        model = pickle.load(f)

    # Setting seed for reproducibility
    np.random.seed(seed)
    np.random.RandomState(seed)
    model.random_state = seed

    df = pd.read_csv(df)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    y = df['gfa'].values
    y = [1 if i == 'good' else 0 for i in y]

    feats = df.drop(['comp', 'gfa'], axis=1)
    X = feats.values

    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    feat_names = np.array(feats.columns)

    names = [label[i] for i in list(feats.columns)]

    model.fit(X, y)
    pickle.dump(model, open(save+'/xgboost_model.pickle', 'wb'))
    explainer = shap.Explainer(model, X, feature_names=names)

    ranks = explainer(X)

    with open(save+'/shap.pickle', 'wb') as f:
        pickle.dump(ranks, f)

    shap.summary_plot(ranks, X, class_names=['Poor GFA', 'Good GFA'], show=False)
    pl.savefig(save+'/shap')
    pl.close('all')


if __name__ == '__main__':
    main()
