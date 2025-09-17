# Online Flower Shop 🌸

This project is a **web application for an online flower shop**, developed using **Django** and **Python**, and deployed on **PythonAnywhere**. The live site is available at [https://ecaterina.pythonanywhere.com](https://ecaterina.pythonanywhere.com).

---

## Overview

The application provides a complete **user experience**, including:

- **User authentication and account management:** Users can register, log in, and manage their account data.  
- **Administration panel:** Administrators can manage the site content using Django's built-in admin interface.  
- **Flower catalog:** A list of flowers with descriptions and available quantities.  
- **Favorites management:** Users can add or remove flowers from their favorites list.  
- **Shopping cart and orders:** Users can add products to a cart and place orders directly from it.  
- **Search functionality:** Users can quickly find flowers in the catalog.

All user interactions, including login, favorites, and orders, are securely handled, with data stored and managed through Django.

---

## Why Django?

Django was chosen for this project because it provides:

- **Rapid development:** Built-in authentication, admin panel, and database management allow quick setup of key features.  
- **Security:** Django handles common security issues like SQL injection, cross-site scripting, and CSRF protection automatically.  
- **Scalability:** The framework supports complex projects and can grow with additional features.  
- **File and URL management:** Django allows organizing the project into reusable apps, managing static files (CSS, JavaScript), templates (HTML), and linking URLs between views and templates efficiently.  
- **Integrated ORM and templating:** Makes it easy to work with databases and render dynamic HTML pages efficiently.  

These features made Django ideal for implementing authentication, catalog management, favorites, shopping cart functionality, and secure deployment.

---

## Development Process

The project was initially developed **locally**, which provided several advantages:

- **Clear development workflow:** Developing locally allowed testing of features without affecting the live site.  
- **Terminal management:** Using the terminal on PythonAnywhere, the project was managed easily with commands such as `git pull` to update files, and commands to start or stop the site as administrator.  
- **GitHub integration:** Source code was version-controlled and synchronized with GitHub, ensuring proper backup and collaborative potential.  
- **Organized project structure:** Static files (CSS, JS) and templates (HTML) were separated from backend logic, making the code maintainable and readable.  

---

## Frontend and Backend Technologies

- **Backend:** Django (Python) for handling authentication, database management, business logic, and server-side rendering.  
- **Frontend:** HTML and CSS for structure and styling, JavaScript for dynamic behavior, integrated with Django templates.  
- **Database:** SQLite for local development and small-scale deployment.  
- **Hosting:** PythonAnywhere for live deployment and public access.

---

## Deployment

- Deployment on **PythonAnywhere** enabled online access at [https://ecaterina.pythonanywhere.com](https://ecaterina.pythonanywhere.com).  
- Static and media files are managed using Django's `STATICFILES` and `MEDIA_ROOT` settings.  
- Terminal commands on PythonAnywhere simplified project updates, restarts, and maintenance.  

---

## Access

The live application is available at: [https://ecaterina.pythonanywhere.com](https://ecaterina.pythonanywhere.com)

---

This project demonstrates the use of **Django** to build dynamic web applications, handle user authentication, manage interactive content like favorites and shopping carts, and deploy efficiently on a cloud platform. The development process highlights best practices for **project organization, terminal management, and deployment workflow**.
