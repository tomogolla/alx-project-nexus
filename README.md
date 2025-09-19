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





# API endpoints

## 🔐 **Authentication Endpoints**
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login (JWT tokens)
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/refresh/` - Refresh JWT token
- `GET /api/auth/me/` - Get current user profile
- `PUT /api/auth/me/` - Update current user profile

## 👥 **User Management Endpoints** (Admin only)
- `GET /api/users/` - List all users
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user (admin)
- `DELETE /api/users/{id}/` - Delete user (admin)

## 📋 **Categories Endpoints**
- `GET /api/categories/` - List all categories
- `GET /api/categories/{id}/` - Get category details
- `POST /api/categories/` - Create category (admin only)
- `PUT /api/categories/{id}/` - Update category (admin only)
- `DELETE /api/categories/{id}/` - Delete category (admin only)

## 💼 **Jobs Endpoints**
- `GET /api/jobs/` - List all jobs (with filtering)
- `GET /api/jobs/{id}/` - Get job details
- `POST /api/jobs/` - Create job (employers & admin)
- `PUT /api/jobs/{id}/` - Update job (owner or admin)
- `DELETE /api/jobs/{id}/` - Delete job (owner or admin)
- `GET /api/jobs/my-jobs/` - Get jobs posted by current user
- `PATCH /api/jobs/{id}/toggle-active/` - Toggle job active status

## 🔍 **Job Search & Filtering Endpoints**
- `GET /api/jobs/search/` - Search jobs by keyword
- `GET /api/jobs/filter/` - Filter jobs by:
  - Category
  - Location
  - Job type
  - Salary range
  - Company
  - Date posted

## 📨 **Applications Endpoints**
- `GET /api/applications/` - List applications (employer sees their jobs' apps, job seeker sees their apps)
- `GET /api/applications/{id}/` - Get application details
- `POST /api/jobs/{job_id}/apply/` - Apply for a job
- `PUT /api/applications/{id}/status/` - Update application status (employer/admin)
- `GET /api/applications/job/{job_id}/` - Get applications for specific job (employer)
- `GET /api/applications/my-applications/` - Get current user's applications

## 📊 **Dashboard & Analytics Endpoints** (Admin/Employers)
- `GET /api/dashboard/stats/` - Get platform statistics
- `GET /api/dashboard/employer-stats/` - Get employer-specific stats
- `GET /api/dashboard/recent-activity/` - Get recent activity

## 📁 **File Upload Endpoints**
- `POST /api/upload/resume/` - Upload resume file
- `POST /api/upload/profile-picture/` - Upload profile picture

## 🔔 **Notification Endpoints** (Optional)
- `GET /api/notifications/` - Get user notifications
- `POST /api/notifications/mark-read/` - Mark notifications as read
- `POST /api/notifications/subscribe/` - Subscribe to job alerts

## 🌐 **Public Endpoints** (No authentication required)
- `GET /api/public/jobs/` - List active jobs (for landing page)
- `GET /api/public/categories/` - List categories
- `GET /api/public/stats/` - Get public platform statistics



## 📌**location filtering api** 
-- `GET /api/location/jobs` - list jobs in each country

## 📋 **Endpoint Features Summary**

**Authentication Required**: Most endpoints
**Role-Based Access**: Different permissions for admin, employer, job seeker
**Filtering & Search**: Extensive query parameters for jobs
**Pagination**: All list endpoints
**File Handling**: Resume and image uploads
**Statistics**: Dashboard and analytics data




### My Django Apps
1. **Users**
   - **Purpose**: Manages user authentication, registration, and role-based access control.
   - **Functionality**:
     - User model (with roles: admin, user).
     - JWT-based authentication (login, logout, token refresh).
     - User profile management (e.g., name, email).
     - Role-based permissions (e.g., admins manage jobs, users apply for jobs).
   - **Key Models**: User

2. **Jobs**
   - **Purpose**: Handles job postings and related operations.
   - **Functionality**:
     - Create, update, delete, and retrieve job postings.
     - Categorize jobs by industry, location, and type.
     - APIs for job listing and details.
   - **Key Models**: JobPosting, Category, Location

3. **Applications**
   - **Purpose**: Manages job applications submitted by users.
   - **Functionality**:
     - Create and track job applications.
     - Allow users to view their application history.
     - Allow admins to review and update application statuses.
     - APIs for application submission and management.
   - **Key Models**: JobApplication

4. **Search**
   - **Purpose**: Handles optimized job search and filtering functionality.
   - **Functionality**:
     - Implement search APIs with filters (e.g., by category, location, job type).
     - Optimize queries using indexing for performance.
     - Support advanced filtering (e.g., keyword search, location-based search).
   - **Key Models**: (Relies on JobPosting, Category, Location from the Jobs app; no new models needed unless adding specific search-related data like search history)

5. **API**
   - **Purpose**: Centralizes API configurations and documentation.
   - **Functionality**:
     - Define REST API endpoints using Django REST Framework.
     - Integrate Swagger for API documentation (hosted at `/api/docs`).
     - Consolidate API views, serializers, and routes for all apps.
   - **Key Models**: None (focuses on API logic, not database models)
