# AccuKnox Django Signals Assignment

## Answers to Questions

### Question 1: Are Django signals executed synchronously or asynchronously?

**Answer**: By default, Django signals are executed **synchronously**. Refer to myapp/signals.py and mpapp/views.py for code proof.

### Question 2: Do Django signals run in the same thread as the caller?

**Answer**: Yes, Django signals run in the **same thread** as the caller by default. Refer to myapp/signals.py and mpapp/views.py for code proof.

### Question 3: Do Django signals run in the same database transaction as the caller?

**Answer**: Yes, Django signals run in the **same database transaction** as the caller by default. Refer to myapp/signals.py and mpapp/views.py for code proof.

### Custom Classes in Python
#### Refer to myapp/utils.py for code implementation.
---

## Steps to Run the Code

1. **Install Django**:
    ```bash
    pip install django
    ```

2. **Clone Git Repository**:
    ```bash
    git clone https://github.com/Harshadaaaaaapawar/AccuKnox-Assignment.git
    cd AccuKnox-Assignment
    ```

3. **Migrate the Database**:
    ```bash
    python manage.py migrate
    ```

8. **Start the Django server**:
    ```bash
    python manage.py runserver
    ```
5. **Trigger the Django view**:
    ##### Visit the URL http://127.0.0.1:8000/trigger/ in your browser to trigger the signals and check the output in the server logs.

6. **Run Rectangle implementation**
    ```bash
    cd myapp
    python utils.py
    ```