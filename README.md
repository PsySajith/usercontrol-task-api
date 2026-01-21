# 🚀 UserControl Task API

## 📌 Description
UserControl Task API is a role-based task management REST API built using Django and Django REST Framework.  

This project focuses on secure user management and controlled access to task operations.

In this system:
- 👨‍💼 Admin can allow or restrict users
- 👤 Authorized users can perform full CRUD operations on tasks
- 🔐 Token Authentication is implemented to secure all API endpoints

This project demonstrates real-world backend concepts like authentication, permissions, and role-based access control.

---

## ✨ Features
- 🔑 Token-based authentication  
- 👨‍💼 Admin can:
  - Allow users  
  - Restrict users  
- 👤 Users can:
  - Add tasks  
  - View tasks  
  - Update tasks  
  - Delete tasks  
- 🛡 Secure API endpoints  
- 🧩 Role-based permission system  

---

## 🛠 Tech Stack
- 🐍 Python  
- 🌐 Django  
- ⚙ Django REST Framework  
- 🔐 Token Authentication  
- 🗄 SQLite / MySQL  

---

## 👥 User Roles

### 👨‍💼 Admin
- Manage user access  
- Allow or restrict users  

### 👤 User
- Create tasks  
- Read tasks  
- Update tasks  
- Delete tasks  

---

## 🔗 API Endpoints
- POST /login  
- GET /task *(AllowAny – public access)*  
- GET /tasks  
- POST /tasks  
- PUT /tasks/{id}  
- DELETE /tasks/{id}  

---

## 🏃 How to Run Project
1. Clone the repository  
2. Create virtual environment  
3. Install dependencies  
4. Run migrations  
5. Start server  

---

## 👨‍💻 Author
**Sajith Sabu**  


