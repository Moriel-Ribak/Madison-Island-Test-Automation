[README.md](https://github.com/user-attachments/files/33251150/README.md)
# Madison Island — Automation Testing Project

**Languages:** [English](#english) · [עברית](#עברית)

---

<a id="english"></a>

## English — Web Test Automation

[עברית](#עברית) · [STD test document](./Madison_Island_STD_Bilingual_Severity_Colors.xlsx)

## About the project

This project tests the [Madison Island](https://madison-island.com/) online store using **Python, Playwright, Pytest, and Allure**. It uses the **Page Object Model (POM)** to keep test steps separate from website actions.

The repository contains **44 test cases across 15 test files**, including tests that run with different data using `pytest.mark.parametrize`.

## Tools

- **Python** — test code
- **Playwright** — browser actions and checks
- **Pytest** — test runs, fixtures, and test data
- **POM** — reusable page objects
- **Allure** — test reports and optional screenshots
- **Excel STD** — documented test cases and expected results

## Project structure

```text
project/
├── components/        # Shared components, such as the header
├── pages/             # Page objects and BasePage
├── tests/             # Test files grouped by feature
├── util/              # Configuration and test data
├── conftest.py        # Browser setup and pytest fixtures
├── pytest.ini         # Pytest settings
└── README.md          # Project documentation
```

## Test coverage

| Area | What is tested |
| --- | --- |
| Home | Main content, collections, and slideshow |
| Header | Navigation to different pages |
| Catalog | Products, pages, and price sorting |
| Product | Title, price, size, color, and cart details |
| Cart | Empty cart, shopping link, products, and quantity |
| Search | Existing and missing products |
| Login | Valid and invalid sign-in data; reset password pages |
| Registration | Valid, invalid, and missing form data |
| E2E | Shopping flows from product selection to the cart |

## STD — Software Test Description

The project includes an **STD Excel file in English and Hebrew**. It documents the **44 test cases** with test IDs, steps, test data, expected results, severity, and fields for actual results and status.

The STD is a description of planned checks. It does **not** mean that every test has passed.

To make the link above work, place `Madison_Island_STD_Bilingual_Severity_Colors.xlsx` in the same folder as `README.md` (or update the link to its real location).

## Important: CAPTCHA limitation

Madison Island uses **CAPTCHA / anti-bot protection** on authentication forms. Because of this, **login and registration submissions may be blocked during automated runs**, even when the test code works as written.

This can affect valid login, invalid login, account registration, and the E2E test that signs in. Tests that only open the Login or Reset Password pages may still run normally. CAPTCHA is not bypassed in this project.

**A failed authentication test does not by itself prove there is a website bug.** Check whether CAPTCHA caused the failure before reporting a defect.

## Running the tests

### 1. Install the Python packages

```bash
python -m pip install pytest playwright allure-pytest
python -m playwright install chromium
```

The current `conftest.py` opens **Google Chrome** with `channel="chrome"`, so Chrome must also be installed on your computer.

### 2. Configure test discovery

The project's test files use names such as `cart_001.py` instead of Pytest's default `test_*.py` pattern. Make sure your root `pytest.ini` contains:

```ini
[pytest]
testpaths = tests
python_files = *_001.py *_002.py *_003.py *_004.py
python_classes = Test*
python_functions = test_*
addopts = --alluredir=allure-results
```

### 3. Run all tests

```bash
python -m pytest tests/ -v
```

Run one file:

```bash
python -m pytest tests/cart_page_tests/cart_001.py -v
```

Check how many tests Pytest finds:

```bash
python -m pytest --collect-only -q
```

### 4. View the Allure report

```bash
allure serve allure-results
```

This requires **Allure Commandline** to be installed separately. Screenshots appear in reports when the screenshot attachment hook is enabled in `conftest.py`.

## Framework overview

- `BasePage` provides common actions such as click, fill, and read text.
- Page objects contain actions for each website page.
- `BaseTest` exposes page objects to the tests.
- `conftest.py` sets up and closes browsers using fixtures.
- Tests contain steps and assertions that check expected results.

## Purpose

This is a learning and portfolio project showing hands-on experience with **web automation, functional testing, E2E testing, data-driven testing, test documentation, and reporting**.


---

<a id="עברית"></a>

## עברית — פרויקט אוטומציה לבדיקות Web

[English](#english) · [מסמך STD](./Madison_Island_STD_Bilingual_Severity_Colors.xlsx)

## על הפרויקט

פרויקט בדיקות אוטומטיות לאתר המסחר [Madison Island](https://madison-island.com/), באמצעות **Python, Playwright, Pytest ו-Allure**. הפרויקט משתמש בתבנית **Page Object Model (POM)** כדי להפריד בין שלבי הבדיקה לבין הפעולות באתר.

הפרויקט כולל **44 מקרי בדיקה ב־15 קובצי בדיקות**, ובהם בדיקות עם כמה מערכי נתונים באמצעות `pytest.mark.parametrize`.

## כלים וטכנולוגיות

- **Python** – כתיבת קוד הבדיקות
- **Playwright** – פעולות ובדיקות בדפדפן
- **Pytest** – הרצת בדיקות, Fixtures ונתוני בדיקה
- **POM** – מחלקות נפרדות לפעולות בכל עמוד
- **Allure** – דוחות בדיקה וצילומי מסך, אם הוגדרו
- **Excel STD** – תיעוד מקרי הבדיקה והתוצאות הצפויות

## מבנה הפרויקט

```text
project/
├── components/        # רכיבים משותפים, כמו Header
├── pages/             # Page Objects ו-BasePage
├── tests/             # קובצי בדיקות לפי תחום
├── util/              # הגדרות ונתוני בדיקה
├── conftest.py        # הגדרת דפדפן ו-Fixtures
├── pytest.ini         # הגדרות Pytest
└── README.md          # תיעוד הפרויקט
```

## כיסוי הבדיקות

| אזור | מה נבדק |
| --- | --- |
| Home | תוכן דף הבית, קולקציות ומצגת תמונות |
| Header | ניווט בין עמודי האתר |
| Catalog | הצגת מוצרים, מעבר עמודים ומיון לפי מחיר |
| Product | שם ומחיר מוצר, מידה, צבע ופרטים בעגלה |
| Cart | עגלה ריקה, המשך קנייה, מוצרים וכמות |
| Search | חיפוש מוצר קיים ומוצר שלא קיים |
| Login | התחברות עם נתונים תקינים ושגויים, ודפי איפוס סיסמה |
| Registration | הרשמה עם נתונים תקינים, שגויים או חסרים |
| E2E | תהליכי קנייה מבחירת מוצר ועד לעגלה |

## מסמך STD – Software Test Description

לפרויקט מצורף **קובץ Excel בעברית ובאנגלית** הכולל תיעוד של **44 מקרי בדיקה**: מזהה בדיקה, שלבים, נתוני קלט, תוצאה צפויה, רמת חומרה ועמודות למילוי תוצאה בפועל וסטטוס.

ה־STD מתאר מה הבדיקה אמורה לאמת; הוא **לא אומר שכל הבדיקות עברו בהצלחה**.

כדי שהקישור בראש המסמך יעבוד, יש לשים את הקובץ `Madison_Island_STD_Bilingual_Severity_Colors.xlsx` באותה תיקייה של `README.md`, או לעדכן את הקישור למיקום האמיתי שלו.

## מגבלה חשובה: CAPTCHA

באתר Madison Island קיימת **הגנת CAPTCHA / Anti-Bot** בטפסים הקשורים להתחברות ולהרשמה. לכן, **בדיקות אוטומטיות ששולחות טופסי Login או Registration עלולות להיחסם**, גם כאשר קוד הבדיקה תקין.

המגבלה יכולה להשפיע על התחברות תקינה או שגויה, הרשמה ועל בדיקת E2E שמבצעת התחברות. בדיקות שרק פותחות את מסכי ההתחברות או איפוס הסיסמה עדיין עשויות לפעול כרגיל. הפרויקט אינו עוקף CAPTCHA.

**כישלון בבדיקת התחברות אינו מוכיח לבדו שיש באג באתר.** לפני פתיחת תקלה צריך לבדוק אם הגנת CAPTCHA היא זו שחסמה את ההרצה.

## איך מריצים את הבדיקות?

### 1. מתקינים ספריות Python

```bash
python -m pip install pytest playwright allure-pytest
python -m playwright install chromium
```

הקובץ `conftest.py` הנוכחי פותח **Google Chrome** באמצעות `channel="chrome"`, ולכן Chrome צריך להיות מותקן במחשב.

### 2. מגדירים זיהוי קובצי בדיקה

שמות הקבצים בפרויקט הם למשל `cart_001.py`, ולא `test_cart.py`. לכן יש לוודא שקובץ `pytest.ini` בתיקיית הפרויקט הראשית כולל:

```ini
[pytest]
testpaths = tests
python_files = *_001.py *_002.py *_003.py *_004.py
python_classes = Test*
python_functions = test_*
addopts = --alluredir=allure-results
```

### 3. מריצים את כל הבדיקות

```bash
python -m pytest tests/ -v
```

הרצת קובץ אחד:

```bash
python -m pytest tests/cart_page_tests/cart_001.py -v
```

בדיקה אילו טסטים Pytest מזהה:

```bash
python -m pytest --collect-only -q
```

### 4. פותחים דוח Allure

```bash
allure serve allure-results
```

צריך להתקין בנפרד **Allure Commandline**. צילומי מסך יוצגו בדוח אם הוגדרה הצמדת תמונות בקובץ `conftest.py`.

## איך תשתית האוטומציה עובדת?

- `BasePage` מכיל פעולות משותפות כמו לחיצה, הקלדה וקריאת טקסט.
- Page Objects מכילים פעולות של עמודי האתר השונים.
- `BaseTest` מאפשר גישה לאובייקטים של העמודים מתוך הטסטים.
- `conftest.py` פותח וסוגר דפדפנים באמצעות Fixtures.
- קובצי הבדיקות מכילים שלבים ו־Assertions לבדיקת התוצאה.

## מטרת הפרויקט

זהו פרויקט לימודי ופרויקט פורטפוליו שמציג ניסיון מעשי ב־**אוטומציה ל־Web, בדיקות פונקציונליות, בדיקות E2E, בדיקות מבוססות נתונים, תיעוד STD ודוחות בדיקה**.
