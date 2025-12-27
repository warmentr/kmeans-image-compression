from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
import numpy as np
from sklearn.cluster import KMeans

@dataclass(frozen=True)
class CompressionResult:
    reconstructed: np.ndarray       # (H, W, 3) float32 in [0,1]
    centers: np.ndarray             # (K, 3) float32 in [0,1]
    labels: np.ndarray              # (H * W,) int
    runtime_sec: float              # fit + predict time

def flatten_pixels(img01: np.ndarray) -> tuple[np.ndarray, tuple[int, int]]:
    '''
    
    (H, W, 3) -> (H*W, 3)
    returns flattened pixels and (H, W).
    '''
    if img01.ndim != 3 or img01.shape[2] != 3:
        raise ValueError("Expected RGB image with shape (H, W, 3).")
    h, w, _ = img01.shape
    x = img01.reshape(-1,3).astype(np.float32)
    return x, (h, w)

def reconstruct_from_labels(labels: np.ndarray, centers: np.ndarray, hw: tuple[int, int]) -> np.ndarray:
    '''
    
    labels: (N,) ints, centers: (K, 3), hw: (H, W, 3)
    '''
    h, w = hw
    rgb = centers[labels] # (N, 3)
    return rgb.reshape(h, w, 3).astype(np.float32)

def kmeans_compress_rgb(
        img01: np.ndarray,
        k: int,
        random_state: int = 42,
        n_init: int = 10,
        max_iter: int = 300,
) -> CompressionResult:
    '''
    
    Baseline RGB KMeans compression:
    - Fit KMeans on all pixels
    - Reconstruct using cluster centers
    '''

    x, hw = flatten_pixels(img01)

    kmeans = KMeans(
        n_clusters=k,
        random_state=random_state,
        n_init=n_init,
        max_iter=max_iter,
        verbose=0
    )

    t0 = perf_counter()
    labels = kmeans.fit_predict(x)
    t1 = perf_counter()

    centers = kmeans.cluster_centers_.astype(np.float32)
    reconstructed = reconstruct_from_labels(labels, centers, hw)

    return CompressionResult(
        reconstructed= reconstructed,
        centers= centers,
        labels= labels,
        runtime_sec=float(t1 - t0),
    )
