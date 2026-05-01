# 🔐 Secure Data Encryption System (Python + MySQL)

## 📌 Overview

This project is a secure data encryption system built using Python that protects sensitive information using **Fernet symmetric encryption**. It integrates with a MySQL database to securely store encrypted data and ensures that only authorized access with the correct key is possible.

---

## 🚀 Key Features

* 🔑 **Fernet-based Encryption/Decryption** for strong data security
* 🗄️ **MySQL Database Integration** for storing encrypted records
* 🔐 **Automatic Key Generation** (`master.key`) for encryption
* 🧾 **Hashing Support** using `hashlib` (for additional security use cases)
* ⚡ Simple CLI-based execution

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** cryptography (Fernet), hashlib
* **Database:** MySQL (mysql-connector-python)

---

## ⚙️ How It Works

1. On first run, the system generates a **secure encryption key** (`master.key`)
2. User data is encrypted using Fernet before storing
3. Encrypted data is saved into MySQL database
4. Data can only be decrypted using the same key

---

## 📂 Project Structure

```
project/
│── crypto.py        # Main application logic
│── master.key       # Encryption key (auto-generated, not uploaded)
│── .gitignore       # Ignore sensitive files
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/secure-data-encryption-python.git
cd secure-data-encryption-python
```

### 2. Install Dependencies

```bash
pip install cryptography mysql-connector-python
```

### 3. Setup MySQL Database

* Create a database (example: `secure_db`)
* Update your MySQL credentials inside `crypto.py`

### 4. Run the Project

```bash
python crypto.py
```

---

## 🔐 Security Notice

⚠️ `master.key` is **excluded from this repository** to prevent unauthorized access.
A new key will be generated automatically when running the program.

---

## 📊 Example Use Cases

* Secure password storage
* Confidential data protection
* Basic encryption system for applications

---

## 🚧 Future Enhancements

* GUI interface (Tkinter / Web app)
* User authentication system
* Role-based access control
* Cloud database integration

---

## 👤 Author

**Yash Ramje**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

