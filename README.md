# 🎬 AI Movie Recommender

Hệ thống gợi ý phim thông minh sử dụng Machine Learning, xây dựng bằng Python và giao diện đồ họa CustomTkinter.

![Python](https://img.shields.io/badge/Python-3.13-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## ✨ Tính năng

- Gợi ý phim dựa trên **thể loại**, **năm phát hành**, **thời lượng** và **quốc gia sản xuất**
- So sánh hiệu suất 3 mô hình ML: **Linear Regression**, **Random Forest**, **Gradient Boosting**
- Dự báo điểm đánh giá phim (thang 10)
- Giao diện desktop hiện đại (Dark mode) với CustomTkinter
- Dữ liệu từ bộ dataset TMDB với hơn **5.000 phim**

---

## 🛠️ Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ | Python 3.13 |
| Machine Learning | scikit-learn (LinearRegression, RandomForest, GradientBoosting) |
| Giao diện | CustomTkinter |
| Xử lý dữ liệu | Pandas, NumPy |
| Dataset | TMDB Movie Dataset v11 |

---

## 📁 Cấu trúc project

```
ai-movie-recommender/
├── main.py                  # Entry point
├── movie_recommender/
│   ├── __init__.py
│   ├── config.py            # Cấu hình tham số
│   ├── data.py              # Tải và xử lý dữ liệu
│   ├── model.py             # Xây dựng & đánh giá mô hình
│   └── gui.py               # Giao diện người dùng
├── .gitignore
└── README.md
```

---

## 🚀 Hướng dẫn cài đặt

### 1. Clone repo

```bash
git clone https://github.com/nha253158-hub/ai-movie-recommender.git
cd ai-movie-recommender
```

### 2. Tạo môi trường ảo và cài thư viện

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install numpy pandas scikit-learn customtkinter
```

### 3. Tải dataset

Tải file `TMDB_movie_dataset_v11.csv` từ [Kaggle](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) và đặt vào thư mục gốc của project.

### 4. Chạy ứng dụng

```bash
python main.py
```

---

## 📊 Kết quả mô hình

| Mô hình | R² | MAE | RMSE |
|---|---|---|---|
| Linear Regression | 0.507 | 0.421 | 0.563 |
| Random Forest | 0.577 | 0.399 | 0.521 |
| **Gradient Boosting** | **0.618** | **0.376** | **0.495** |

> Gradient Boosting cho kết quả tốt nhất với R² = 0.618 và MAE = 0.376 trên tập test (thang điểm 0–10).
---


