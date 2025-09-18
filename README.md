# 💼 Job Board Backend – ProDev BE

## 📌 Overview
This project implements the backend for a **Job Board Platform**.  
It provides APIs for managing job postings, categories, and applications, while enforcing **role-based access control** and ensuring **efficient job search** via optimized database queries.

The backend is built using **Django** and **PostgreSQL**, with **JWT authentication** for secure access and **Swagger** for API documentation.

---

## 🎯 Project Goals
- **API Development**: Expose endpoints for jobs, categories, and applications.  
- **Access Control**: Implement secure role-based access for admins and users.  
- **Database Efficiency**: Optimize job search using indexes and query optimization.  
- **Documentation**: Provide detailed API docs with Swagger.

---

## 🛠 Technologies Used
| Technology | Purpose |
|------------|---------|
| **Django** | High-level Python framework for backend development |
| **PostgreSQL** | Database for storing job board data |
| **JWT** | Role-based authentication & authorization |
| **Swagger (drf-yasg)** | API endpoint documentation |

---

## 🔑 Key Features
### 📝 Job Posting Management
- CRUD APIs for job postings.  
- Categorization by **industry, location, and type**.

### 🔐 Role-Based Authentication
- **Admins**: Manage jobs and categories.  
- **Users**: Apply for jobs and manage applications.  

### ⚡ Optimized Job Search
- Efficient query filtering with **indexes**.  
- Search by **location** and **category**.  

### 📖 API Documentation
- Swagger UI hosted at `/api/docs`.  
- Interactive API testing for frontend integration.  

---

## 🚀 Implementation Process
### 🔹 Git Commit Workflow
- **Initial Setup**  
  - `feat: set up Django project with PostgreSQL`  
- **Feature Development**  
  - `feat: implement job posting and filtering APIs`  
  - `feat: add role-based authentication for admins and users`  
- **Optimization**  
  - `perf: optimize job search queries with indexing`  
- **Documentation**  
  - `feat: integrate Swagger for API documentation`  
  - `docs: update README with usage details`  

---

## 📂 Submission Details
- **Deployment**: API and Swagger docs must be hosted and accessible.  
- **Evaluation Criteria**:
  - ✅ **Functionality**: CRUD works, RBAC is enforced.  
  - ✅ **Code Quality**: Modular, Django best practices, normalized DB schema.  
  - ✅ **Performance**: Indexed queries make job search fast.  
  - ✅ **Documentation**: Swagger is complete; README provides setup and usage instructions.  

---

## ⚙️ Setup Instructions
1. Clone repo:  
   ```bash
   git clone https://github.com/tomogolla/job-board-backend.git
   cd job-board-backend
