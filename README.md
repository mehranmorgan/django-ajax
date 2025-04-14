
# Home Page Data Fetching

This project is a simple HTML page that uses two different methods to fetch data from the server. The data is displayed as `<ul>` lists on the page. The project uses Django for the backend and jQuery for client-side interactions.

## Features

- GET method used to fetch data
- Two different methods for sending GET requests:
  - Using `$.get()`
  - Using `$.ajax()`
- Data is displayed in two separate lists named "First Get Method" and "Second Get Method"
- A button to send the requests and fetch data

## Prerequisites

1. **Django** for the backend
2. **jQuery** for sending AJAX requests
3. The static file `home.css` for styling the page

## Installation and Setup

### 1. Install prerequisites

Make sure Django and jQuery are installed.

- To install Django:
  ```bash
  pip install django
  ```

- To include jQuery in your project, add the following code to the `<head>` of your HTML file:
  ```html
  <script src="https://code.jquery.com/jquery-3.5.1.min.js" crossorigin="anonymous"></script>
  ```

### 2. Set up the Django project

Create a new Django project and a `product` app.
The `product/` path in the code above refers to a view in Django that fetches the product data from the database. You need to create a `Product` model in the `models.py` file and return the data as JSON via a view.

### 3. Create a View in Django

In `views.py`, create a view to send the data as JSON:

```python
from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    data = [{"name": product.name} for product in products]
    return JsonResponse(data, safe=False)
```

In `urls.py`, add the path for this view:

```python
from django.urls import path
from .views import product_list

urlpatterns = [
    path('product/', product_list, name='product-list'),
]
```

### 4. Styling the Page

The `home.css` file should be placed in the static folder of the project, and it should contain the necessary styles for the HTML page.

## Usage

1. Load the HTML page in your browser.
2. Click on the "Get Data" button to fetch data using two different methods, and display it in the lists.
3. GET requests are sent to the server, and products from the database are displayed as a list on the page.

## Example

### Method 1 (using `$.get()`):
Data is displayed in a list of products under "First Get Method".

### Method 2 (using `$.ajax()`):
Data is displayed in another list under "Second Get Method".

## Project Structure

```
project/
│
├── product/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── static/
│   └── home.css
├── templates/
│   └── home.html
└── manage.py
```

## Acknowledgments

This project was created for educational purposes. Please credit the original author if you use this code in commercial or public projects.

## Help and Support

If you encounter any issues or have questions, please feel free to open an issue in the project repository.
