#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'notebooks'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Data Analysis and Interpretation

#%% [markdown]
# # Show all files
import os

path = '../Scenario 3 - all change/data_base/Scenario-03/'
dirs = os.listdir(path)
dirs


#%%
import numpy as np
import pandas as pd

data = {}
data['tipo'] = []
data['percentual'] = []
data['F1'] = []
data['Pearson_Correlation'] = []
data['RMSE'] = []
data['pesos'] = []
data['kernel_names'] = []

for dir in dirs:
    # print('DIR', dir)
    mean_f1 = []
    mean_pearsonCorrelation = []
    mean_RMSE = []
    weights = []
    for iter in os.listdir(path+dir):
        # print('ITER', iter)
        f1_file = path+dir+'/'+iter+'/F1_score.txt'
        f1 = np.loadtxt(f1_file)
        mean_f1.append(f1.mean())

        pearsonCorrelation_file = path+dir+'/'+iter+'/Pearson_correlation.txt'
        pearsonCorrelation = np.loadtxt(pearsonCorrelation_file)
        mean_pearsonCorrelation.append(pearsonCorrelation.mean())

        RMSE_file = path+dir+'/'+iter+'/RMSE.txt'
        RMSE = np.loadtxt(RMSE_file)
        mean_RMSE.append(RMSE.mean())

        pesos        = np.loadtxt(path+dir+'/'+iter+'/pairwise_kernel_weights.txt').mean(axis=0)
        weights.append(pesos)
        kernel_names = open(path+dir+'/'+iter+'/pairwise_kernel_names.txt','r').read().split('\t')
        partes = dir.split('_')

    data['tipo'].append(partes[1])
    data['percentual'].append(int(partes[2]))
    data['F1'].append(np.mean(mean_f1))
    data['Pearson_Correlation'].append(np.mean(mean_pearsonCorrelation))
    data['RMSE'].append(np.mean(mean_RMSE))
    data['pesos'].append(np.mean(weights, axis=0))
    data['kernel_names'].append(kernel_names)


df = pd.DataFrame(data=data)
df


#%% [markdown]
# Analysis grouped by percent: 10%
df[df['percentual'] == 10]

#%% [markdown]
# Analysis grouped by percent: 30%
df[df['percentual'] == 30]

#%% [markdown]
# Analysis grouped by percent: 50%
df[df['percentual'] == 50]

#%% [markdown]
# Analysis grouped by percent: 70%
df[df['percentual'] == 70]



#%% [markdown]
# Evaluation of the performance of the techniques in comparison with the F1 score
import seaborn as sns
sns.barplot(x='tipo', y='F1', data=df, hue='percentual')

#%% [markdown]
# Evaluation of the performance of the techniques in comparison with the Pearson Correlation
sns.barplot(x='tipo', y='Pearson_Correlation', data=df, hue='percentual')

#%% [markdown]
# Evaluation of the performance of the techniques in comparison with the RMSE
sns.barplot(x='tipo', y='RMSE', data=df, hue='percentual')



#%%
def plot_heatmap(dataframe, percentual=10, tipo='zero'):

    # testando com 50% e tipo=zero
    pesos = dataframe[(dataframe['percentual'] == percentual)                     & (dataframe['tipo'] == tipo)]['pesos'].values[0]
    kernel_names = dataframe[(dataframe['percentual'] == percentual)                            & (dataframe['tipo'] == tipo)]['kernel_names'].values[0]
    # assumindo que kernel_names nao muda em cada execucao
    kds = [kn.split('.txt')[0] for kn in kernel_names[:-1]]
    kcs = [kn.split('.txt')[1] for kn in kernel_names[:-1]]
    pesos = dataframe[(dataframe['percentual'] == 50)                     & (dataframe['tipo'] == 'zero')]['pesos'].values[0]

    df2 = pd.DataFrame(data={
        'kd': kds,
        'kc': kcs,
        'peso': pesos} )

    matrix = df2.groupby(['kd','kc'])['peso'].mean().unstack()

    sns.heatmap(matrix)


#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: zero; percentage: 10.
plot_heatmap(df, percentual=10, tipo='zero')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: zero; percentage: 30.
plot_heatmap(df, percentual=30, tipo='zero')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: zero; percentage: 50.
plot_heatmap(df, percentual=50, tipo='zero')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: zero; percentage: 70.
plot_heatmap(df, percentual=70, tipo='zero')



#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: average; percentage: 10.
plot_heatmap(df, percentual=10, tipo='average')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: average; percentage: 30.
plot_heatmap(df, percentual=30, tipo='average')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: average; percentage: 50.
plot_heatmap(df, percentual=50, tipo='average')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: average; percentage: 70.
plot_heatmap(df, percentual=70, tipo='average')



#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: median; percentage: 10.
plot_heatmap(df, percentual=10, tipo='median')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: median; percentage: 30.
plot_heatmap(df, percentual=30, tipo='median')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: median; percentage: 50.
plot_heatmap(df, percentual=50, tipo='median')

#%% [markdown]
# Analysis of weights according to the combination of drug and protein files.
# Evaluated with: technique: median; percentage: 70.
plot_heatmap(df, percentual=70, tipo='median')


#%%



#%%



#%%



#%%




