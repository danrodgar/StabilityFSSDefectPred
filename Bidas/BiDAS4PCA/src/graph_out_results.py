import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error as mse
import seaborn as sns
import numpy as np

file = 'results/1572452875.9526474.csv'
df = pd.read_csv(file)
#print(df[df.k==5])
blacklist = ['Unnamed: 0','k', 'samples',
        'accuracy', 'f-score', 'auc', 'matthews']
#print(df.shape)

for k in range(2, np.max(df['k'].values + 1)):
    df_filtered = df[df.k==k].drop(blacklist, axis=1)
    print(df_filtered.corr())
    pca = PCA(n_components=(min(df_filtered.shape)))
    pca.fit(df_filtered)
    #print(pca.explained_variance_ratio_)
    df_pca = pca.transform(df_filtered)
    df_recons = pca.inverse_transform(df_pca)
    #print(mse(df_filtered, df_recons))
    ex_variance = np.var(df_pca, axis=0)
    ex_variance_ratio = ex_variance/np.sum(ex_variance)
    plt.plot(np.cumsum(pca.explained_variance_ratio_), label=str(k)+' folders')
    #sns.lineplot(data=np.cumsum(pca.explained_variance_ratio_), hue=k)

plt.legend()
#plt.xscale("log")
plt.yscale("log")
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
'''df_filtered = df.drop(blacklist, axis=1)
pca = PCA(n_components=(min(df_filtered.shape)))
pca = pca.fit(df_filtered)
df_pca = pd.DataFrame(pca.transform(df_filtered))
df_pca.columns = [['pc'+str(i) for i in range(0, len(pca.explained_variance_))]]
df_pca.head()
print(df_pca)
#sns.lmplot('pc1', 'pc2', data=df_pca, fit_reg = False, size = 15, scatter_kws={"s": 100})
g = sns.jointplot("n1", "f-score", data=df, kind="hex")
g = sns.jointplot("density", "f-score", data=df, kind="hex")'''
'''xvector = pca.components_[0]
yvector = pca.components_[1]
xs = pca.transform(df_filtered)[:,0]
ys = pca.transform(df_filtered)[:,1]
for i in range(len(xvector)):
    # arrows project features (ie columns from csv) as vectors onto PC axes
    # we can adjust length and the size of the arrow
    plt.arrow(0, 0, xvector[i]*max(xs), yvector[i]*max(ys),
              color='r', width=0.005, head_width=0.05)
    plt.text(xvector[i]*max(xs)*1.1, yvector[i]*max(ys)*1.1,
             list(df.columns.values)[i], color='r')
 
for i in range(len(xs)):
    plt.text(xs[i]*1.08, ys[i]*1.08, list(X.index)[i], color='b') # index number of each observations
plt.title('PCA Plot of first PCs')'''
plt.show()
'''print(ex_variance_ratio)
print(pca.explained_variance_)'''
#ax = sns.violinplot("f-score", "balance_c1", data=df, split=False)
#ax = sns.pairplot(df , vars=["f-score", "balance_c1", "dimensionality_t2", "density"])
'''ax.set(xlim=(df['f-score'].min(),df['f-score'].max()))
ax.xaxis.set_major_locator(
    ticker.MultipleLocator(
        (df['f-score'].max() - df['f-score'].min())/5))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())'''
#sns.relplot(x="balance_c1", y="f-score", hue="k", data=df)
#plt.show()


