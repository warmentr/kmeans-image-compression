from __future__ import annotations

from pathlib import Path
import numpy as np
from PIL import Image


def load_image_rgb(path: str | Path) -> np.ndarray:
    '''

    Load an image as RGB float32 in [0, 1].
    Returns: (H, W, 3) float32.
    '''
    path = Path(path)
    img = Image.open(path).convert("RGB")
    arr = np.array(img, dtype=np.float32) / 255.0
    return arr

def save_image_rgb(img01: np.ndarray, path: str | Path) -> None:
    '''

    Save an RGB image assumed float in [0,1] as PNG/JPG.
    '''
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    img01 = np.clip(img01, 0.0, 1.0)
    img255 = (img01 * 255.0).round().astype(np.uint8)
    Image.fromarray(img255, mode="RGB").save(path)