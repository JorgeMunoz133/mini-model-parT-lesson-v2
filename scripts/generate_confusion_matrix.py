import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

np.random.seed(42)
class_names = ["Hbb", "Hcc", "QCD"]
n_per_class = 400
y_true = np.repeat([0, 1, 2], n_per_class)
scores = np.zeros((len(y_true), 3))
for i, label in enumerate(y_true):
    base = np.random.dirichlet(alpha=[1, 1, 1])
    boost = np.zeros(3)
    if label == 2:
        boost[2] = 3.5
    else:
        boost[label] = 2.0
        boost[1 - label] = 0.8
    logits = base + boost + np.random.normal(0, 0.3, 3)
    scores[i] = np.exp(logits) / np.exp(logits).sum()
y_pred = scores.argmax(axis=1)
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(5, 4.2))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=class_names, yticklabels=class_names, cbar=False)
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Confusion matrix")
plt.tight_layout()
plt.savefig("episodes/fig/confusion-matrix-example.png", dpi=150)
