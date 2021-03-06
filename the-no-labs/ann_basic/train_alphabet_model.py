
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

from ann_basic.data.data import *

# load data


# pre pros data

a_image_array = np.array(a_image)
a1_image_array = np.array(a1_image)
a2_image_array = np.array(a2_image)
a3_image_array = np.array(a3_image)
b_image_array = np.array(b_image)
c_image_array = np.array(c_image)
d_image_array = np.array(d_image)
e_image_array = np.array(e_image)
e1_image_array = np.array(e1_image)
e2_image_array = np.array(e2_image)
f_image_array = np.array(f_image)
g_image_array = np.array(g_image)
h_image_array = np.array(h_image)
i_image_array = np.array(i_image)
j_image_array = np.array(j_image)
k_image_array = np.array(k_image)
l_image_array = np.array(l_image)
m_image_array = np.array(m_image)
n_image_array = np.array(n_image)
o_image_array = np.array(o_image)
p_image_array = np.array(p_image)
q_image_array = np.array(q_image)
r_image_array = np.array(r_image)
s_image_array = np.array(s_image)
t_image_array = np.array(t_image)
u_image_array = np.array(u_image)
v_image_array = np.array(v_image)
w_image_array = np.array(w_image)
x_image_array = np.array(x_image)
y_image_array = np.array(y_image)
z_image_array = np.array(z_image)


plt.imshow(a_image_array)
plt.show()


# create data set
data_set = [
    a_image_array.flatten(),
    a1_image_array.flatten(),
    a2_image_array.flatten(),
    a3_image_array.flatten(),
    b_image_array.flatten(),
    c_image_array.flatten(),
    d_image_array.flatten(),
    e_image_array.flatten(),
    e1_image_array.flatten(),
    e2_image_array.flatten(),
    f_image_array.flatten(),
    g_image_array.flatten(),
    h_image_array.flatten(),
    i_image_array.flatten(),
    j_image_array.flatten(),
    k_image_array.flatten(),
    l_image_array.flatten(),
    m_image_array.flatten(),
    n_image_array.flatten(),
    o_image_array.flatten(),
    p_image_array.flatten(),
    q_image_array.flatten(),
    r_image_array.flatten(),
    s_image_array.flatten(),
    t_image_array.flatten(),
    u_image_array.flatten(),
    v_image_array.flatten(),
    w_image_array.flatten(),
    x_image_array.flatten(),
    y_image_array.flatten(),
    z_image_array.flatten(),
]

data_set_array = np.array(data_set)

# label data
labels = np.array([1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
print(data_set_array.shape)

# create model
input_dim = 10*11
X = data_set_array
Y = labels

model = Sequential()
model.add(Dense(50, input_dim=input_dim, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.summary()

# train model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=20, batch_size=1, verbose=1)

# test
model.predict(data_set_array)

prediction_first = model.predict(data_set_array)


# test with other data

other_image_a = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

other_image_e = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

other_image_a_array = np.array(other_image_a)
other_image_e_array = np.array(other_image_e)

new_data_set = [
    other_image_a_array.flatten(),
    other_image_e_array.flatten()
]

new_data_set_array = np.array(new_data_set)

model.predict(new_data_set_array)
