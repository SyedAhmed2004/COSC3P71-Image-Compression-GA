import numpy as np
from skimage.metrics import structural_similarity as ssim

def mse(original, reconstructed):
    return np.mean((original - reconstructed) ** 2)

def psnr(original, reconstructed):
    mse_val = mse(original, reconstructed)
    if mse_val == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse_val))

def ssim_metric(original, reconstructed):
    return ssim(original, reconstructed, channel_axis=2)
