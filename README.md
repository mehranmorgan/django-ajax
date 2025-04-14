
# django-ajax

`django-ajax` is a simple and efficient library for using Ajax in Django projects. This library allows you to easily manage Ajax requests in your Django projects without complex coding.

## Features

- **Simple and User-friendly:** Using Ajax in Django projects without complexity
- **Easy Request Management:** Sending and receiving data from the server without reloading the page
- **Supports Multiple Data Formats:** JSON and other data formats supported
- **Flexible:** Can be used in any type of Django project
- **CSRF Support:** Ensures request security using CSRF Token

## Prerequisites

To use `django-ajax`, you need the following:

- Python 3.6 or higher
- Django 3.0 or higher

## Installation

To install this library, use the following command:

```bash
pip install django-ajax
```

## Setup and Usage

### 1. Initial Setup

After installation, add the library to `INSTALLED_APPS` in your Django project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'django_ajax',
    ...
]
```

### 2. Using Ajax in Views

In your `views.py` file, you can use Ajax to send data and receive responses:

```python
from django_ajax.decorators import ajax

@ajax
def my_ajax_view(request):
    # Process the data
    data = {'message': 'Ajax request was successful!'}
    return data
```

### 3. Sending Ajax Request from the Client Side

In your HTML file, you can use jQuery to send an Ajax request to the server:

```html
<button id="ajaxButton">Send Request</button>

<script>
    $(document).ready(function() {
        $('#ajaxButton').click(function() {
            $.ajax({
                url: '{% url "my_ajax_view" %}',
                type: 'GET',
                success: function(response) {
                    alert(response.message);
                },
                error: function() {
                    alert('Error sending Ajax request!');
                }
            });
        });
    });
</script>
```

## Security and CSRF

The `django-ajax` library uses CSRF Token by default to ensure the security of Ajax requests. To ensure the CSRF Token is sent correctly in the requests, you can set it up in your Django templates:

```html
<script type="text/javascript">
    const csrfToken = '{{ csrf_token }}';
</script>
```

## Documentation and Resources

For full documentation and additional guidance, please refer to the [official Django website](https://www.djangoproject.com/) and [Ajax documentation in Django](https://docs.djangoproject.com/en/stable/ref/request-response/#ajax).

## Contributing

Contributions to open-source projects are always welcome! If you have an idea to improve this library or encounter any issues, please open a new issue or submit a pull request.

## License

This project is licensed under the MIT License. For more details, please check the [LICENSE](LICENSE) file.

---

**Developer:** [Mehran Morgan](https://github.com/mehranmorgan)
