import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

np.random.seed(3)
n = 500
y_true = np.random.binomial(1, 0.5, n)
scores = np.where(
    y_true == 1,
    np.random.beta(6, 2.2, n),
    np.random.beta(2.2, 6, n),
)
fpr, tpr, _ = roc_curve(y_true, scores)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(5.5, 4.6))
plt.plot(fpr, tpr, color="#1D9E75", lw=2.5, label=f"Model (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], "k--", lw=1.2, label="Random guessing (AUC = 0.50)")
plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("ROC curve")
plt.legend(loc="lower right", fontsize=9)
plt.tight_layout()
plt.savefig("episodes/fig/roc-curve-example.png", dpi=150)
