# visionkart

# 🏪 Virtual Lens Frame Try-On and Smart Billing System

## 📌 Overview
The **Virtual Lens Frame Try-On and Smart Billing System** is designed to enhance the eyewear shopping experience by enabling customers to try lens frames virtually and streamline the billing process. The system integrates **augmented reality (AR)** for virtual frame try-on and a **smart billing system** for seamless transactions.

---

## 🎯 Purpose & Use Cases
This system is ideal for:
- **Optical Stores & E-Commerce Platforms** → Provides a virtual try-on feature for customers.
- **Self-Checkout Kiosks** → Reduces in-store congestion and simplifies the checkout process.
- **Personal Styling Applications** → Helps users choose the perfect lens frames with AR.
- **Automated Billing Systems** → Enables efficient, error-free invoice generation.

---

## 🛠️ Features
### ✅ Virtual Frame Try-On
- Uses **augmented reality** (AR) for real-time frame overlay.
- Works with a **live webcam feed** for a seamless experience.
- Provides an intuitive UI for selecting different frames.

### ✅ Facial Feature Detection
- Uses **advanced AI algorithms** for accurate facial recognition.
- Ensures proper placement and realistic alignment of frames.

### ✅ Frame Recognition
- Identifies selected frames using a **pre-registered database**.
- Retrieves **frame details, price, and availability** dynamically.

### ✅ Smart Billing System
- Generates **automated invoices** for selected frames.
- Calculates the **total cost** and displays it for confirmation.
- Supports **digital payment integration** (Razorpay, PayPal, UPI, etc.).

### ✅ User-Friendly Interface
- Provides a **clean and interactive GUI**.
- Ensures smooth navigation for frame selection and billing.

### ✅ Database Integration
- Stores **product details, pricing, and specifications** in a central database.
- Facilitates quick retrieval for **frame recognition and billing**.

### ✅ Customizable Framework
- Allows retailers to **update frames, prices, and specifications**.
- Supports **scalability** for various retail environments.

### ✅ Error Handling & Robustness
- Ensures accurate **frame alignment and recognition**.
- Displays **user-friendly error messages** in case of mismatches.

---

## 📂 Project Structure
```
📁 Virtual-Lens-TryOn
│── 📄 virtual_tryon.py        # Handles virtual frame overlay
│── 📄 frame_recognition.py    # Identifies frames and fetches details
│── 📄 billing_system.py       # Computes total cost and generates invoices
│── 📄 database.json           # Stores frame details and pricing
│── 📄 README.md               # Project documentation
│── 📁 assets                  # Stores UI elements & frame images
│── 📄 requirements.txt        # List of dependencies
```

---

## 🖥️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Virtual-Lens-TryOn.git
cd Virtual-Lens-TryOn
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.9+** installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
#### ➤ Start Virtual Try-On
```bash
python virtual_tryon.py
```
#### ➤ Run Frame Recognition
```bash
python frame_recognition.py
```
#### ➤ Execute Smart Billing System
```bash
python billing_system.py
```

---

## 🏗️ Technologies Used
- **Python** 🐍
- **OpenCV** → Handles live webcam feed processing.
- **MediaPipe** → Implements facial detection & feature alignment.
- **Tkinter** → Develops an interactive GUI.
- **JSON & SQLite** → Stores frame details and user transactions.
- **NumPy & Pandas** → Data handling and processing.

---

## 🚀 Future Enhancements
- Implement **3D frame modeling** for an enhanced try-on experience.
- Add **AI-powered recommendations** for personalized frame selection.
- Enable **online shopping integration** for direct purchase.
- Introduce **voice-assisted navigation** for hands-free operation.

---
![Screenshot 2024-11-23 142643](https://github.com/user-attachments/assets/fb630e46-5ad9-4873-a67d-70dc9e87920f)
![Screenshot 2024-11-23 142241](https://github.com/user-attachments/assets/4d76e91a-5cd4-4c96-b5d6-5c3f2a2aba48)
![Screenshot 2024-11-23 140729](https://github.com/user-attachments/assets/2dfdaeff-5130-4b29-9a7a-cfaa07403e77)
![Screenshot 2024-11-22 231720](https://github.com/user-attachments/assets/4e1c7111-bcaa-4e71-8a74-9bdaaa1c0e26)



## 🤝 Contributing
Contributions are welcome! Feel free to **open an issue** or **submit a pull request** on GitHub.

---

## 📜 License
This project is **open-source** and licensed under the MIT License.

---

## 🌟 Show Your Support
If you find this project useful, consider giving it a ⭐ on GitHub!

---

**Developed with ❤️ by [Rishi]**

