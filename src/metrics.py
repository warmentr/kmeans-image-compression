from __future__ import annotations

import numpy as np

def mse(img_a: np.ndarray, img_b: np.ndarray) -> float:
    '''
    
    Mean Squared Error between two images in the same scale/shape
    '''

    if img_a.shape != img_b.shape:
        raise ValueError(f"Shape mismatch: {img_a.shape} vs {img_b.shape}")
    diff = img_a.astype(np.float32) - img_b.astype(np.float32)
    return float(np.mean(diff * diff))

def psnr(img_true: np.ndarray, img_pred:np.ndarray, data_range: float = 1.0) -> float:
    '''
    
    Peak Signal-to-Noise Ratio in dB.
    Assumes images are in [0, data_range]. For baseline: [0,1] => data_range=1.
    '''

    m = mse(img_true, img_pred)

    if m == 0:
        return float("inf")
    return float(20.0 * np.log10(data_range) - 10.0 * np.log10(m))
