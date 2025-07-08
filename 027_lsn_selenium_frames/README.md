# Selenium Frames Verification Test

This project automates iframe interaction and alert verification using Python + Selenium + Pytest.

## 📁 Project Structure

027_lsn_selenium_frames/
├── html/
│ ├── dz.html
│ ├── dz_frame1.html
│ └── dz_frame2.html
├── page_objects/
│ ├── frame1_page.py
│ └── frame2_page.py
├── tests/
│ ├── conftest.py
│ ├── test_driver_check.py
│ └── test_verify_frames.py
├── requirements.txt
└── README.md

## 🚀 How to Run

1. Install requirements:

   pip install -r requirements.txt

2. Run the tests:

   pytest tests/test_verify_frames.py

## 🔍 What It Tests

- Opens the main page with two iframes.
- Switches into each iframe.
- Enters the secret phrase (`Frame1_Secret` / `Frame2_Secret`).
- Clicks the verify button.
- Checks the alert message.
- Accepts the alert.

## 🧪 Technologies

- Python 3.12+
- Selenium
- Pytest

## 💡 Notes

- Uses Page Object pattern (`page_objects/`) for clean code separation.
- `conftest.py` provides reusable driver fixture.
- Alert handling is wrapped into `get_alert_text_and_accept()`.
