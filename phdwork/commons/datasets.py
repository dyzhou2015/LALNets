from keras.datasets import mnist
import numpy as np
import scipy.io as sio

def load_mnist(order='th'):

    # input image dimensions
    img_rows, img_cols, img_channels,  = 28, 28, 1

    if order == 'tf':
        input_shape=(img_rows, img_cols, img_channels)
    elif order == 'th':
        input_shape=(img_channels, img_rows, img_cols)

    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    X_train = X_train.reshape(len(X_train), input_shape[0], input_shape[1], input_shape[2])
    X_test = X_test.reshape(len(X_test), input_shape[0], input_shape[1], input_shape[2])

    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255

    return (X_train, y_train), (X_test, y_test), input_shape

def load_svhn(order='th'):

    # input image dimensions
    img_rows, img_cols, img_channels,  = 32, 32, 3
    nb_classes = 10

    if order == 'tf':
        input_shape=(img_rows, img_cols, img_channels)
    elif order == 'th':
        input_shape=(img_channels, img_rows, img_cols)

    train_data = sio.loadmat('/home/ozsel/Jupyter/datasets/svhn/train_32x32.mat')

    # access to the dict
    X_train = train_data['X']
    X_train = X_train.reshape(nb_channels*img_rows*img_cols, X_train.shape[-1]).T
    X_train = X_train.reshape(len(X_train), input_shape[0], input_shape[1], input_shape[2])
    X_train = X_train.astype('float32')
    X_train /= 255

    y_train = train_data['y']
    y_train = y_train.reshape(len(y_train))
    y_train = y_train%nb_classes

    del train_data

    test_data = sio.loadmat('/home/ozsel/Jupyter/datasets/svhn/test_32x32.mat')

    # access to the dict
    X_test = test_data['X']
    X_test = X_test.reshape(nb_channels*img_rows*img_cols, X_test.shape[-1]).T
    X_test = X_test.reshape(len(X_test), input_shape[0], input_shape[1], input_shape[2])
    X_test = X_test.astype('float32')
    X_test /= 255

    y_test= test_data['y']
    y_test = y_test.reshape(y_test.shape[0])
    y_test = y_test%nb_classes

    del test_data

    return (X_train, y_train), (X_test, y_test), input_shape
