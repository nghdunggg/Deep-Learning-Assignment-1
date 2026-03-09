---

Deep Learning and Its Applications (CO3133) - 2025-2026 

**Instructor:** Le Thanh Sach 

**Group:** [Your Group Name] 

---

Assignment 1: Classification on Images, Text, and Multimodal Data 

1. Objectives and Tasks 

* 
**Image Data:** Compare models from two families: CNN (Convolutional Neural Networks) and ViT (Vision Transformer).


* 
**Text Data:** Compare models from two families: RNN (Recurrent Neural Networks, e.g., LSTM) and Transformer.

* 
**Multimodal Data:** Compare two approaches: Zero-shot classification and Few-shot classification.

2. Dataset Constraints 

* 
**Number of Classes:** There must be at least 5 classes per dataset for image, text, and multimodal data.

* 
**Size:** The training set must contain at least 5,000 samples for both image and text datasets.

* 
**Difficulty:** Datasets should have moderate or higher class separability; for images, avoid MNIST and consider CIFAR-10/100 or Fashion-MNIST.

* 
**Multimodal Integrity:** The multimodal dataset must feature genuine image-text pairs describing the same entity or event.

* 
**Examples:** Recommended multimodal datasets include COCO captions or Flickr30k.

3. Deadlines 

* 
**Report 1:** Due at 23:59 on 26 March 2026 (accounts for 50% of the presentation grade).

* 
**Final Report:** Due at 23:59 on 06 April 2026 (accounts for 100% of the presentation grade).

* 
**Late Submission:** Each week late incurs a 20% deduction on the presentation grade for that round.

### 4. Project Checklist

* [ ] **Data Selection & EDA:** Choose datasets and state why they satisfy the project constraints.

* [ ] **Data Pipeline:** Prepare Dataset, DataLoader, and apply appropriate augmentation.

* [ ] **Model Implementation:** Apply pretrained models (CNN, ViT, RNN, Transformer, and multimodal models).

* [ ] **Evaluation:** Report at least Accuracy and F1-score (for imbalanced data) using consistent metrics across models.

* [ ] **Extensions (Aiming for 40% of the grade):** 

* [ ] **Interpretability:** Visualize attention regions using techniques like Grad-CAM or saliency maps.

* [ ] **Error Analysis:** Categorize errors and illustrate misclassified cases with explanations.

* [ ] **Demo Application:** Build a simple interface using Gradio, Streamlit, or Flask.

* [ ] **GitHub Pages:** Create a dedicated landing page and assignment page with required video links and documentation.