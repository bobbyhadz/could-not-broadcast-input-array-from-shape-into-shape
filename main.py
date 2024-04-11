# Could not broadcast input array from shape into shape

# ✅ Works
import numpy as np

a_list = [
    np.zeros((1, 2, 3)),
    np.zeros((1, 2, 3)),
    np.zeros((1, 2, 3))
]

arr = np.array(a_list)

print(arr)

print(arr.shape)  # 👉️ (3, 1, 2, 3)