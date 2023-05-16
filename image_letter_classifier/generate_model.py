import numpy as np
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
        tf.keras.layers.Conv2D(25, (5, 5)),
        tf.keras.layers.MaxPooling2D((4, 4)),
        
        tf.keras.layers.Conv2D(100, (3, 3)),
        tf.keras.layers.MaxPooling2D((4, 4)),
        
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
    generate_model()