# Inventory_Management_and_Tracking_system
The Inventory Management and Tracking System (ITS) for supermarket to manage inventory, orders, and user roles through a robust and scalable backend developed with Django. The project will focus on implementing backend APIs, database management, authentication, and role-based access control, while ensuring security, performance, and scalability.

Requirements Specification Document
Project Title: Inventory Management and Tracking System for Abadir
Author: Nebiyu Esaiyas Mamo
Date: January 28, 2025


1. Introduction
    The Inventory Management and Tracking System (ITS) for Abadir aims to manage inventory, orders, and user roles through a robust and scalable backend developed with Django. The project will focus on implementing backend APIs, database management, authentication, and role-based access control, while ensuring security, performance, and scalability.

      1.1 Purpose
      This document outlines the backend requirements for the ITS, specifying API endpoints, database models, authentication methods, and backend logic. It will guide the development process, ensuring alignment with the project's objectives and requirements.

      1.2 Scope
      The backend will:
        Provide RESTful APIs for frontend integration
        Manage product inventory, stock movements, and orders securely
        Implement authentication and authorization
        Enable role-based access (Stock Clerks, Retail Stores, Managers, Owners)
        Support manual stock decreases through an API instead of automatic purchases
        Allow Managers to place and track orders from Retail Stores


2. Functional Requirements
    2.1 User Management
      Registration & Authentication: Implement user registration, login, and password management using Django authentication or JWT.
      Role Management: Define roles and assign permissions accordingly:
        Stock Clerk – Manages inventory, manually updates stock levels, and receives stock alerts.
        Retail Store – Supplies stock and receives orders from Managers.
        Manager – Can perform CRUD operations on products, place orders from retail stores, view sales reports, and manage stock movements.
        Owner – Has read-only access to view sales, stock levels, and reports.
    2.2 Product & Inventory Management
      CRUD Operations: Implement APIs to create, read, update, and delete products.
      Manual Stock Management: Stock levels will only be updated manually (no automatic stock reduction from purchases).
      Decrease Stock API: Allow authorized users (Stock Clerks, Managers) to manually decrease stock to simulate customer purchases.
      Low Stock Alerts: Provide an endpoint to notify managers of low inventory.
    2.3 Orders Management (For Managers)
      Place Orders from Retail Stores
      Track Order Status: Order Statuses: Ordered → Pending → Approved → Shipped → Delivered
      Managers can place orders.
      Retail Stores can approve and process orders.
    2.4 Stock Movement Tracking
      Record Stock Changes: Track every stock reduction or increase.
      Functionality: Deducts the given quantity from the product’s stock level.
      Role Access: Only Stock Clerks and Managers can decrease stock.
    2.5 Reporting (For Owner & Manager)
      Sales Reports: Generate API endpoints to retrieve sales data.
      Inventory Reports: Provide insights into stock levels and product performance.


3. Non-Functional Requirements
    Performance: API response times under 500ms.
    Scalability: Design with future feature integration in mind.
    Security: Use authentication, authorization, and input validation.
    Reliability: Ensure accurate data persistence and transaction safety.


4. Database Models
    User Model: Includes roles and authentication fields.
    Product Model: Details of products including stock levels.
    Stock Movement Model: Logs stock decreases and restocking activities.
    Sales Model: Includes sales amount, timestamps, and associations with stock movements.
    Orders Model: Stores order details for Managers ordering from Retail Stores.


5. Sprint Schedule
    Sprint	Feature/Functionality	Git Commit Message
    Sprint 1	Project Setup & Database Models	init: setup Django project and database models
    Sprint 2	User Authentication (JWT)	feat: add JWT authentication
    Sprint 3	Role-Based Access Control	feat: implement RBAC with roles
    Sprint 4	CRUD Operations for Products	feat: add product CRUD APIs
    Sprint 5	Decrease Stock API	feat: implement stock decrease API
    Sprint 6	Orders API (Placing & Tracking Orders)	feat: add orders API for retail store orders
    Sprint 7	Stock Movement Tracking	feat: log stock movements in database
    Sprint 8	Reporting APIs (Sales & Inventory)	feat: implement sales and inventory reports
    Sprint 9	Final Testing & Documentation	chore: finalize testing and update documentation

7. Conclusion
The backend development of the ITS for Abadir will lay the groundwork for a robust and maintainable system, enabling smooth integration with a frontend in the future while delivering key functionalities through secure and well-defined APIs.