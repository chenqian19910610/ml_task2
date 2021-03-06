# import pandas as pd
# import numpy as np
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import make_scorer
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.svm import NuSVC
#
# def accu_score(y_true,y_pred):
#     acc=accuracy_score(y_true,y_pred)
#     return acc
#
# rawDataTrain = pd.read_hdf('train.h5','train').values
# X_train = rawDataTrain[:, 1:]   # the features
# y_train = rawDataTrain[:, 0]   # the target value
# print(X_train.shape)
# print(np.unique(y_train))
#
#
# rawDataTest = pd.read_hdf('test.h5','test').values
# X_test = rawDataTest[:, :]
# y_test = np.zeros([X_test.shape[0], 2])   # [id, y]
# y_test[:, 0] = pd.read_csv('./sample.csv', index_col=False).values[:,0]
# # clf = RandomForestClassifier(n_estimators=300, criterion='entropy', max_features=None,
# #                                    bootstrap=True, min_samples_leaf=1, max_leaf_nodes=None, class_weight='balanced_subsample')
#
# # clf=AdaBoostClassifier(learning_rate=0.5)
#
# clf=NuSVC()
#
# clf.fit(X_train,y_train)
# cvscore=cross_val_score(clf,X_train,y_train,scoring=make_scorer(accu_score),verbose=0,cv=10)
# print('cvscore',np.mean(cvscore))
#
# y_test[:,1]= clf.predict(X_test)
# print(y_test.shape)
# pd.DataFrame(data=y_test).to_csv('./NN-keras.csv', header=['Id', 'y'], sep=',', index=False)

"""
multilayer perceptron for multi-class softmax
"""
# from keras.models import Sequential
# from keras.layers import Dense,Dropout,Activation
# from keras.optimizers import SGD
# import numpy as np
# import pandas as pd
#
# X_train=pd.read_hdf('train.h5','train').values[:,1:]
# print(X_train.shape)
# y_train=pd.read_hdf('train.h5','train').values[:,0]
# print(y_train.shape)
# from keras.utils.np_utils import to_categorical
# y_train=to_categorical(y_train)
# X_test=pd.read_hdf('test.h5','test').values[:,:]
# print(X_test.shape)
# y_test=np.zeros([X_test.shape[0],2])
# y_test[:,0]=pd.read_csv('sample.csv', index_col=False).values[:,0]
#
#
# model=Sequential()
# model.add(Dense(256,activation='relu',input_dim=100))
# model.add(Dropout(0.5))
# model.add(Dense(128,activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64,activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(5,activation='softmax'))
#
#
# sgd=SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
# model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['categorical_accuracy'])
#
# model.fit(X_train,y_train,epochs=1000,batch_size=128)
# score=model.evaluate(X_train,y_train,batch_size=128)
# print(score)
#
# y_test[:,1]=model.predict_classes(X_test)
# df=pd.DataFrame(data=y_test)
# df.to_csv('MLP.csv', header=['Id', 'y'], sep=',', index=False, float_format='%.0f')

"""
MLP change the optimizer--ada sgd see more: http://sebastianruder.com/optimizing-gradient-descent/
https://keras.io/optimizers/
"""
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
from keras.optimizers import SGD
from keras import regularizers
import numpy as np
import pandas as pd

X_train=pd.read_hdf('train.h5','train').values[:,1:]
print(X_train.shape)
y_train=pd.read_hdf('train.h5','train').values[:,0]
print(y_train.shape)
from keras.utils.np_utils import to_categorical
y_train=to_categorical(y_train)
X_test=pd.read_hdf('test.h5','test').values[:,:]
print(X_test.shape)
y_test=np.zeros([X_test.shape[0],2])
y_test[:,0]=pd.read_csv('sample.csv', index_col=False).values[:,0]


model=Sequential()
model.add(Dense(256,activation='relu',input_dim=100))
model.add(Dropout(0.5))
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(5,activation='softmax'))


# sgd=SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['categorical_accuracy'])
# model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['categorical_accuracy'])
# model.compile(loss='categorical_crossentropy',optimizer='adamax',metrics=['categorical_accuracy'])

model.fit(X_train,y_train,epochs=500,batch_size=128)
score=model.evaluate(X_train,y_train,batch_size=128)
print(score)

y_test[:,1]=model.predict_classes(X_test)
df=pd.DataFrame(data=y_test)
df.to_csv('MLP.csv', header=['Id', 'y'], sep=',', index=False, float_format='%.0f')

# from keras.utils import plot_model
# plot_model(model,to_file='MLP_model.png')

"""
encoding to categorical--------sooooooo slow????????
The model is not configured to compute accuracy. ["accuracy"]`to the `model.compile()` method
The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
why train is ok, predict is wrong???????
"""
# import numpy as np
# import pandas as pd
# from keras.models import Sequential
# from keras.layers import Dense,Dropout,Activation
# from keras.utils import np_utils
# from sklearn.preprocessing import LabelEncoder
#
# X_train=pd.read_hdf('train.h5','train').values[:,1:]
# y_train=pd.read_hdf('train.h5','train').values[:,0]
# X_test=pd.read_hdf('test.h5','test').values[:,:]
# y_test=np.zeros([X_test.shape[0],2])
# y_test[:,0]=pd.read_csv('sample.csv', index_col=False).values[:,0]
#
# encoder=LabelEncoder()
# encoder.fit(y_train)
# encoded_y=encoder.transform(y_train)
# dummy_y=np_utils.to_categorical(encoded_y)
# print(dummy_y)
#
# def baseline_model():
#     model=Sequential()
#     model.add(Dense(256,activation='relu',input_dim=100))
#     model.add(Dropout(0.5))
#     model.add(Dense(128,activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(64,activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(5,activation='softmax'))
#     model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['categorical_accuracy'])
#     return model
#
# baseline_model().fit(X_train,dummy_y,epochs=500,batch_size=128)
# score=baseline_model().evaluate(X_train,dummy_y,batch_size=128)
# print(score)
#
# y_test[:,1]=baseline_model().predict_classes(X_test)
#
# df=pd.DataFrame(data=y_test)
# df.to_csv('encoder_mlp.csv', header=['Id', 'y'], sep=',', index=False, float_format='%.0f')

"""
MLPClassifier sklearn--reach maximum iterations, but cannot converge the optimization
"""
# import numpy as np
# import pandas as pd
# from sklearn.neural_network import MLPClassifier
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import make_scorer,accuracy_score
#
# def accu_score(y_true,y_pred):
#     acc=accuracy_score(y_true,y_pred)
#     return acc
#
# X_train=pd.read_hdf('train.h5','train').values[:,1:]
# y_train=pd.read_hdf('train.h5','train').values[:,0]
# X_test=pd.read_hdf('test.h5','test').values[:,:]
# y_test=np.zeros([X_test.shape[0],2])
# y_test[:,0]=pd.read_csv('sample.csv', index_col=False).values[:,0]
#
# clf=MLPClassifier(solver='adam',alpha=1e-5,activation='relu',random_state=1)
# clf.fit(X_train,y_train)
#
# cvscore=cross_val_score(clf,X_train,y_train, scoring=make_scorer(accu_score),verbose=0,cv=10)
# y_test[:,1]=clf.predict(X_test)
#
# df=pd.DataFrame(data=y_test)
# df.to_csv('MLPclassifier.csv', header=['Id', 'y'], sep=',', index=False, float_format='%.0f')
