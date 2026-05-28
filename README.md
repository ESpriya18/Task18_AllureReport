# BDD Selenium Allure Automation Framework

## Project Overview

This project is a Behavior Driven Development (BDD) automation testing framework developed using:

- Python
- Selenium WebDriver
- Behave (BDD)
- Allure Reporting
- Page Object Model (POM)

The framework is designed for scalable, maintainable, and reusable web automation testing.

---

# Technologies Used

- Python
- Selenium
- Behave
- Allure Reports
- WebDriver Manager
- Pytest
- Git & GitHub

---

# Framework Features

- BDD Feature Files using Gherkin syntax
- Page Object Model Design Pattern
- Explicit Wait Implementation
- Screenshot Capture on Failure
- Allure HTML Reporting
- Reusable Utility Functions
- Cross Browser Ready Structure
- Git Integrated Project

---

# Project Structure

```text
BDD_Allure_project/
│
├── features/
│   ├── login.feature
│   ├── logout.feature
│   └── steps/
│
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
│
├── screenshots/
├── reports/
├── allure-report/
├── environment.py
├── requirements.txt
└── README.md
```

---

# Test Scenarios Covered

## Login Module
- Valid Login
- Invalid Login
- Username Validation
- Password Validation
- Login Button Validation

## Logout Module
- Successful Logout Functionality

---

# Reporting

Allure Reports are integrated for detailed execution reporting.

Features include:
- Step-wise execution logs
- Failure screenshots
- Execution history
- Test status visualization

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Tests

```bash
behave
```

---

# Generate Allure Report

```bash
allure generate reports -o allure-report --clean
```

---

# Open Allure Report

```bash
allure open allure-report
```

---

# Author

Developed by Shunmugapriya E
