# K-MEANS IMAGE COMPRESSION

This project explores image compression through **K-means color quantization**.  
The main objective is to measure how changing the number of clusters (**k**) affects:

- **Compression factor**
- **Run time**
- **Mean Squared Error (MSE)**
- **Peak Signal-to-Noise Ratio (PSNR)**

Instead of treating this as a broad experiment with multiple clustering variants, this version of the project focuses entirely on analyzing the tradeoff between **compression efficiency**, **image quality**, and **computational cost** across a range of k values.

---

## PROJECT OVERVIEW

Digital images often contain many more unique colors than are necessary for a visually recognizable reconstruction.  
K-means compression reduces the image to a limited palette of **k representative colors** by clustering similar pixels together.

Each pixel is treated as a 3-dimensional data point in RGB space:

- Red
- Green
- Blue

After clustering:

1. The algorithm learns **k centroids**
2. Each pixel is assigned to its nearest centroid
3. The image is reconstructed using only those centroid colors

This reduces color diversity and can significantly decrease storage requirements while preserving much of the original visual structure.

---

## PROJECT GOALS

The goals of this project are to:

1. Implement image compression using **K-means clustering**
2. Compare results across a **variety of k values**
3. Measure the tradeoff between:
   - stronger compression
   - reconstruction quality
   - algorithm run time
4. Evaluate compression performance using:
   - **Compression factor**
   - **Run time**
   - **MSE**
   - **PSNR**
5. Visualize how image quality changes as k increases

---

## METHOD

### 1. Load the image
The input image is read as an RGB image with shape:

(H, W, 3)

where:
- **H** = image height
- **W** = image width
- **3** = RGB color channels

### 2. Reshape pixels into feature vectors
The image is flattened into a 2D matrix of shape:

(H × W, 3)

Each row represents one pixel in RGB space.

### 3. Apply K-means clustering
K-means is run on the pixel matrix for a chosen value of **k**.

- Each centroid represents a color in the compressed palette
- Larger **k** gives more available colors
- Smaller **k** increases compression but may reduce image quality

### 4. Reconstruct the image
Each original pixel is replaced by its nearest centroid color, then reshaped back into the original image dimensions.

### 5. Evaluate the compressed result
For each tested k value, the compressed image is evaluated using:

- **Compression factor**
- **Run time**
- **MSE**
- **PSNR**

---

## EVALUATION METRICS

### Compression Factor
Compression factor measures how much the image representation is reduced relative to the original.

In this project, compression is based on replacing the full original color set with a palette of **k colors** plus pixel-to-cluster assignments.

A higher compression factor means stronger compression.

### Run Time
Run time measures how long the K-means compression process takes for a given k.

This helps show the computational cost of using more clusters.

### Mean Squared Error (MSE)
MSE measures the average squared difference between the original and compressed image pixels.

Lower MSE indicates that the compressed image is closer to the original.

\[
MSE = \frac{1}{N} \sum_{i=1}^{N}(I_i - \hat{I}_i)^2
\]

where:
- \(I_i\) is the original pixel value
- \(\hat{I}_i\) is the reconstructed pixel value
- \(N\) is the total number of pixel values

### Peak Signal-to-Noise Ratio (PSNR)
PSNR is a quality metric derived from MSE and is commonly used in image compression.

Higher PSNR indicates better reconstruction quality.

\[
PSNR = 10 \log_{10}\left(\frac{MAX^2}{MSE}\right)
\]

For standard 8-bit images, **MAX = 255**.

---

## EXPERIMENT DESIGN

The central experiment in this project is to run image compression over a range of k values, such as:

- k = 2
- k = 4
- k = 8
- k = 16
- k = 32
- k = 64

For each k value, the project records:

- compressed image output
- compression factor
- run time
- MSE
- PSNR

This allows direct comparison of how increasing the number of clusters affects both quality and efficiency.

---

## EXPECTED TRADEOFFS

The project is designed to highlight several expected trends:

- **Low k**
  - stronger compression
  - faster or simpler representation
  - higher error
  - lower PSNR
  - more visible color banding

- **High k**
  - weaker compression
  - better visual reconstruction
  - lower MSE
  - higher PSNR
  - increased computational cost

The main takeaway is that **k controls the balance between compression strength and image fidelity**.

---

## RESULTS TO REPORT

A complete results section should compare k values using tables, plots, and reconstructed images.

Suggested outputs include:

### Quantitative table
| k | Compression Factor | Run Time (s) | MSE | PSNR |
|---|--------------------|--------------|-----|------|
| 2 | ...                | ...          | ... | ...  |
| 4 | ...                | ...          | ... | ...  |
| 8 | ...                | ...          | ... | ...  |
| 16| ...                | ...          | ... | ...  |
| 32| ...                | ...          | ... | ...  |
| 64| ...                | ...          | ... | ...  |

### Visual comparisons
Include reconstructed images for several k values to show how compression changes appearance.

### Metric plots
Recommended plots:
- **k vs Compression Factor**
- **k vs Run Time**
- **k vs MSE**
- **k vs PSNR**
