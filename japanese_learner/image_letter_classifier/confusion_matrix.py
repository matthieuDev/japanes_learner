

import numpy as np, json

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from model_handler import load_categories, load_model
from generate_model import load_test

(x_test, y_test) =  load_test()
model = load_model()

y_pred = model.predict(x_test[:, :, :, np.newaxis]).argmax(axis=1)

confusion_mat = np.zeros((49, 49), dtype=int)
for i, j in zip(y_test, y_pred) :
    confusion_mat[i, j] += 1



categories = load_categories()
with open('../command_prompt_learner/hiragana2letter.json', encoding='utf8') as f:
    hiragana2letter = json.load(f)
categories = np.array([hiragana2letter.get(x) for x in categories] )

plt.figure(figsize=(20, 20))
plt.imshow(confusion_mat, cmap='hot', interpolation='nearest')

plt.xticks(list(range(49)), categories, fontsize=14)
plt.yticks(list(range(49)), categories, fontsize=14)

plt.xlabel('prediction')
plt.ylabel('test')

plt.savefig('data/confusion_matrix.jpg')
