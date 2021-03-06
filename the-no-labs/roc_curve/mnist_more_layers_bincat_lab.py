
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Flatten

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score


def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()


data = tf.keras.datasets.mnist.load_data()

train_data = data[0][0]
train_labels = data[0][1]

test_data = data[1][0]
test_labels = data[1][1]

print(train_data.shape)
print(train_labels.shape)


item_data = train_data[530]
item_label = train_labels[530]
print(item_data.shape)

plt.imshow(item_data)
plt.title('LABEL: ' + str(item_label))
plt.show()


# train data
X = train_data
Y = (train_labels == 5).astype(int)

print(X.shape)
print(Y.shape)

# model

model = Sequential()
model.add(
    Input(shape=(28, 28, ))
)
model.add(
    Flatten()
)
model.add(
    Dense(5, activation='relu')
)
model.add(
    Dense(1, activation='sigmoid')
)
model.summary()


# train model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=3, batch_size=32, verbose=1)


# img_file = './model_arch.png'
# tf.keras.utils.plot_model(model, to_file=img_file, show_shapes=True, show_layer_names=True)


# train data
prediction_train = model.predict(X)
auc = roc_auc_score(Y, prediction_train)
print('Train AUC: %.2f' % auc)

fpr, tpr, thresholds = roc_curve(Y, prediction_train)
plot_roc_curve(fpr, tpr)


# test data
X_test = test_data
Y_test = (test_labels == 5).astype(int)

prediction_test = model.predict(X_test)
auc = roc_auc_score(Y_test, prediction_test)
print('Test AUC: %.2f' % auc)

fpr, tpr, thresholds = roc_curve(Y_test, prediction_test)
plot_roc_curve(fpr, tpr)


# validation data





