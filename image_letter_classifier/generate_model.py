import numpy as np, numba as nb
import tensorflow as tf

def load_numpy_file(filename) :
    return np.load(filename)['arr_0']

def load_test() :
    return (
        load_numpy_file('data/k49-test-imgs.npz'),
        load_numpy_file('data/k49-test-labels.npz'),
    )

def load_train() :
    return (
        load_numpy_file('data/k49-train-imgs.npz'),
        load_numpy_file('data/k49-train-labels.npz'),
    )
def load_all() :
    '''
    load all training and test data
    '''
    (x_train, y_train) , (x_test, y_test) = load_train(), load_test()

    x_train = x_train / 255.0
    x_test = x_test / 255.0

    return (x_train, y_train) , (x_test, y_test)

def generate_model(save_file='model.h5'):
    (x_train, y_train) , (x_test, y_test) = load_all()

    model = tf.keras.Sequential([
        tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.1),
        
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Dropout(0.1),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(49)
    ])

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(
        optimizer = 'adam',
        loss = loss_fn,
        metrics=['accuracy'],
    )

    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

    model.save(save_file)

def double_size(matrix) :
    new_matrix = np.zeros((matrix.shape[0] * 2, matrix.shape[1] * 2))
    numba_double_size (matrix, new_matrix)
    return new_matrix

@nb.njit()
def numba_double_size (matrix, new_matrix) :
    for i in range(matrix.shape[0]) :
        for j in range(matrix.shape[1]) :
            new_matrix[2 * i : 2 * ( i + 1), 2 * j : 2 * ( j + 1)] = matrix[i, j]

def generate_model_dense(save_file='model_densenet.h5'):
    (x_train_small, y_train) , (x_test_small, y_test) = load_all()
    
    x_train = np.zeros((x_train_small.shape[0], 56, 56))
    x_test = np.zeros((x_test_small.shape[0], 56, 56))
    for i in range(x_train.shape[0]) :
        x_train[i] = double_size(x_train_small[i])
    for i in range(x_test.shape[0]) :
        x_test[i] = double_size(x_test_small[i])
    del x_train_small, x_test_small

    x_train = x_train[:, :, :, np.newaxis]
    x_test = x_test[:, :, :, np.newaxis]

    model = tf.keras.Sequential([
        tf.keras.applications.densenet.DenseNet121(weights=None, include_top=False, input_shape=(56, 56, 1)),
        tf.keras.layers.Dropout(0.1),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(49)
    ])

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(
        optimizer = 'adam',
        loss = loss_fn,
        metrics=['accuracy'],
    )

    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

    model.save(save_file)

    

if __name__ == '__main__' :
    #generate_model()
    generate_model_dense()