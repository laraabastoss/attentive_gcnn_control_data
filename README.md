# 🧠 Fundamental Research in Machine and Deep Learning: Controlled Dataset

This repository provides a **controlled synthetic dataset** designed to evaluate whether neural networks—specifically **Attentive Group Equivariant CNNs (AGE-CNNs)**—can learn **task-specific equivariance**, i.e., to focus on transformations that matter for the task while ignoring those that do not.

---

## 📌 Problem Statement

Convolutional Neural Networks (CNNs) are widely used for image recognition tasks due to their ability to detect local patterns regardless of their position in the image. This property is known as **translation equivariance**.

To generalize equivariance beyond translations, **Group Convolutional Neural Networks (Group CNNs)** were introduced by *Cohen and Welling*, which incorporate transformations such as **rotations and flips** directly into convolutional layers. These models aim to achieve equivariance to a broader set of transformations, improving generalization for tasks where such transformations are semantically meaningful.

However, **standard Group CNNs treat all transformations equally**, regardless of their relevance to the task. **Romero et al.** proposed extending Group CNNs with an **attention mechanism** over the transformation group to **weight transformations by importance**.

This controlled dataset is designed to **verify equivariance** in this context. Specifically, models should learn to:
- Respond differently to transformations that **affect the class label** (e.g., rotation turning a 6 into a 9),
- While **ignoring** transformations that do not (e.g., rotation of an 8).

---

## 🗂️ Dataset Description

- **Digits:** {6, 7, 8, 9}
- **Rotations:** {0°, 90°, 180°, 270°}
- **Total samples:** 16 (each digit in 4 orientations)
- **Labels:** Reflect the digit identity **after rotation**:
  - Rotated 6 → 9 and vice versa
  - Rotated 7 or 8 → same label
- **Image Format:** Grayscale, 128×128 px, white background

### Example
- `6_rot180_label9.png` → Image of a 6 rotated 180°, labeled as 9
- `8_rot90_label8.png` → Image of an 8 rotated 90°, label unchanged

---

## 🛠️ How to Generate the Dataset

### 🧾 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
