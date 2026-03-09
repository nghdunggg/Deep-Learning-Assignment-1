import os

def create_structure():
    # Định nghĩa cấu trúc thư mục
    folders = [
        ".github/workflows",
        "data",
        "models",
        "notebooks",
        "src",
        "docs/assignment1",
        "assets"
    ]

    # Tạo thư mục
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Nội dung README.md tổng quát
    readme_content = """# HCMUT - Deep Learning and Its Applications (CO3133)
**Instructor:** Le Thanh Sach
**Academic Year:** 2025-2026, Semester 2

## Project Overview
This repository contains all assignments for the Deep Learning course.

### Assignments Checklist
- [ ] **Assignment 1:** Classification on Image, Text, and Multimodal data.
- [ ] **Assignment 2:** (To be updated)
"""

    # Nội dung Landing Page (index.html) theo yêu cầu [cite: 86]
    index_html = """<!DOCTYPE html>
<html>
<head><title>Deep Learning Project - HCMUT</title></head>
<body>
    <h1>Group Name: [Your Group Name]</h1>
    <h3>Members:</h3>
    <ul>
        <li>Member 1 - Student ID</li>
        <li>Member 2 - Student ID</li>
    </ul>
    <p><strong>Instructor:</strong> Le Thanh Sach</p>
    <hr>
    <h2>Assignments</h2>
    <ul>
        <li><a href="assignment1/report.html">Assignment 1: Classification Comparison</a></li>
    </ul>
</body>
</html>
"""

    # Nội dung Report Assignment 1 (report.md) [cite: 92, 100-104]
    report_md = """# Assignment 1: Deep Learning Classification

## 1. Problem & EDA
- Dataset Image: [Name]
- Dataset Text: [Name]
- Dataset Multimodal: [Name]

## 2. Methodology
- **Image:** CNN vs ViT
- **Text:** RNN vs Transformer
- **Multimodal:** Zero-shot vs Few-shot

## 3. Results & Discussion
| Model | Accuracy | F1-Score |
|---|---|---|
| CNN | | |
| ViT | | |

## 4. Extensions
- [Link to extension report or explanation]
"""

    # Tạo các file mặc định
    files = {
        "README.md": readme_content,
        "requirements.txt": "torch\\ntransformers\\npandas\\nmatplotlib\\ngradio\\n",
        "docs/index.html": index_html,
        "docs/assignment1/report.md": report_md,
        "notebooks/image_classification.ipynb": "",
        "notebooks/text_classification.ipynb": "",
        "notebooks/multimodal_classification.ipynb": "",
        "src/train.py": "# Training logic here",
        "src/evaluate.py": "# Evaluation logic here",
        "src/utils.py": "# Utility functions here"
    }

    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_structure()
    print("\\n--- Setup Complete! ---")