#%%
import ktrain
from ktrain import text
import pandas as pd
import re
# %%
MODEL_NAME = '../models/bert-model-1M'

# %%
t = text.Transformer(MODEL_NAME, maxlen=500, classes=['NOT','OFF'])

# %%
df = pd.read_csv('off_tr.tsv',names=['idx','tw','label'],header=0, sep='\t')


# %%
tweets=[]
for tw in df['tw']:
    tweets+=[' '.join(re.sub("(@[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",tw).split())]


# %%
df['tw'] = tweets

# %%
train = df[:24000]
test = df[24000:]
trainx=list(train['tw'])
trainy=list(train['label'])
testx=list(test['tw'])
testy=list(test['label'])


# %%
trn = t.preprocess_train(trainx, trainy)
val = t.preprocess_test(testx, testy)

# %%
model = t.get_classifier()

# %%
learner = ktrain.get_learner(model, train_data=trn, val_data=val, batch_size=6)

#%%
learner.fit_onecycle(5e-1, 1)


# %%


# %%
