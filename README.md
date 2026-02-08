# Selenium UI Automation Framework (Mini SDET Project)

A structured UI automation framework built using Python and Selenium WebDriver, following Page Object Model (POM) principles and incorporating logging for execution traceability.

This project demonstrates clean automation design, test structuring, and debugging practices aligned with Quality Engineering fundamentals.

---

## 🔹 Project Structure

selenium-ui-automation-basics/
│
├── tests/
│   └── test_login.py
│
├── pages/
│   └── login_page.py
│
├── utils/
│   ├── driver_factory.py
│   └── logger.py
│
├── config/
│   └── config.py
│
├── logs/
├── requirements.txt
└── README.md

---

## 🔹 Concepts Implemented

- Page Object Model (POM) for separation of concerns
- Driver factory abstraction for scalability
- Config-based environment setup
- Explicit waits for synchronization handling
- Positive, negative, and boundary test scenarios
- Structured logging (console + file logging)
- Clean modular project architecture

---

## 🔹 Test Scenarios Automated

1. Valid login (Happy path)
2. Invalid credentials
3. Empty input validation (Boundary case)

---

## 🔹 Logging Implementation

- Logs are written to:
  logs/test_execution.log
- Includes timestamps, log levels, and execution steps
- Helps with debugging in CI/CD or headless environments

---

## 🔹 Tools & Technologies

- Python
- Selenium WebDriver
- ChromeDriver
- Logging module (Python standard library)

---

## 🔹 How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the test from project root:
   python -m tests.test_login

---

## 🔹 Key Learning Outcomes

- Designing maintainable automation frameworks
- Handling synchronization to reduce flakiness
- Structuring reusable test components
- Implementing logging for better debuggability
- Applying test case design strategies (positive, negative, boundary)

---

## 🔹 Future Improvements (Planned)

- Cross-browser support
- Integration with pytest
- CI/CD pipeline integration
- Screenshot capture on failure
- Log rotation handling

