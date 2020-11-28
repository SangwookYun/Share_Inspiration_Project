import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import imageio

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
# print(predictions)
# print(tf.nn.softmax(predictions).numpy())

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)
prob_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

predictions = prob_model(x_train[:1])
print(predictions);
print(np.argmax(predictions[0]))
print(y_train[0])


def read_image(path):
    return imageio.imread(path) / 255.0


def predict_digit(img):
    img = (np.expand_dims(img, 0))
    print(img.shape)
    prob = prob_model(img)
    print(prob)
    detected_digit = np.argmax(prob.numpy())
    print(f"It looks like : {detected_digit}")


def display_images(image_names: list, images: list):
    for i in range(10):
        plt.subplot(1, 10, i + 1)
        plt.xticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(image_names[i])
    plt.show()


def get_images(image_files: list):
    images = []
    for file in image_files:
        images.append(read_image(file))
    return images


image_files = ['digit-black_0.png', 'digit-black_1.png', 'digit-black_2.png', 'digit-black_3.png', 'digit-black_4.png',
               'digit-black_5.png', 'digit-black_6.png', 'digit-black_7.png', 'digit-black_8.png', 'digit-black_9.png']
images = get_images(image_files)
display_images(image_files, images)

for i, name in enumerate(image_files):
    print(f"Test image: {name}")
    predict_digit(images[i])
    print()
