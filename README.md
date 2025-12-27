# K-MEANS IMAGE COMPRESSION (RGB vs Lab, MiniBatch, Sampling, Spatial Features)

This project demonstrates image compression via color quantization using K-means clustering.
Each pixel is treated as a data point in color space, and the image is reconstructed using a palette of K representative colors.

Beyond a baseline implementation, the project explores several practical extensions relevant to real-world data science and machine learning workflows:

- RGB vs Lab color space comparisons (perceptual analysis)
- KMeans vs MiniBatchKMeans scalability tradeoffs
- Pixel sampling strategies for faster training
- Spatially-aware clustering using RGB + (x, y) features
- Quantitative evaluation using MSE, PSNR, and runtime profiling

The goal is to study compression–quality–runtime tradeoffs while demonstrating unsupervised learning techniques applied to high-dimensional visual data.

## PROJECT GOALS
1. Compress images by reducing the number of unique colors to K using K-means centroids as a color palette.
2. Evaluate reconstruction quality using quantitative metrics and visual inspection.
3. Compare algorithmic variants that improve either perceptual quality or computational efficiency.
4. Present results in a reproducible, GitHub-ready data science project.

## METHODS

### BASELINE: RGB K-MEANS COLOR QUANTIZATION
- Load an RGB image of shape (H, W, 3)
- Reshape into a matrix of pixels with shape (H*W, 3)
- Run K-means clustering to find K color centroids
- Replace each pixel with its nearest centroid
- Reshape the result back to (H, W, 3)

### RGB VS LAB COLOR SPACE COMPARISON
- Convert RGB images to Lab color space
- Perform K-means clustering in Lab space
- Reconstruct the image in Lab, then convert back to RGB for visualization
- Compare visual quality and reconstruction error at equal K

### KMEANS VS MINIBATCHKMEANS
- Compare standard KMeans and MiniBatchKMeans
- Measure runtime, memory behavior, and reconstruction quality
- Evaluate scalability on high-resolution images

### PIXEL SAMPLING STRATEGIES
- Randomly sample a fraction of pixels (e.g., 1%, 5%, 10%)
- Fit K-means only on the sampled pixels
- Assign all pixels to the nearest learned centroid
- Compare runtime reduction and quality loss

### SPATIALLY-AWARE CLUSTERING (RGB + X,Y)
- Augment each pixel feature vector with normalized spatial coordinates
- Encourage smooth regions and reduce isolated color artifacts

## REPO STRUCTURE
kmeans-image-compression/
  README.md
  .gitignore
  requirements.txt
  environment.yml
  src/
  notebooks/
  data/
  outputs/
  reports/

EXPECTED RESULTS
- Lab color space yields better perceptual quality than RGB
- MiniBatchKMeans significantly improves runtime
- Sampling preserves quality while reducing computation
- Spatial features improve region coherence