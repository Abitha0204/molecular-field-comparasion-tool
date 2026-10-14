import numpy as np


def field_similarity(field1, field2):
    values1 = np.array(field1, dtype=float)
    values2 = np.array(field2, dtype=float)

    features1 = np.array([
        np.mean(values1),
        np.std(values1),
        np.min(values1),
        np.max(values1)
    ])

    features2 = np.array([
        np.mean(values2),
        np.std(values2),
        np.min(values2),
        np.max(values2)
    ])

    difference = np.linalg.norm(features1 - features2)
    scale = np.linalg.norm(features1) + np.linalg.norm(features2) + 1e-6

    similarity = 1 - (difference / scale)

    similarity = max(0, min(1, similarity))

    return similarity * 100