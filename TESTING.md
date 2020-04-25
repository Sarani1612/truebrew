# True Brew - Testing

1. [Manual Testing](#manual-testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Testing Features](#testing-features)
2. [Automated Testing](#automated-testing)
3. [Issues](#issues)
    1. [Resolved](#resolved)
    2. [Unresolved](#unresolved)
4. [Additional Testing](#additional-testing)

## Manual Testing
All the following testing has been carried out on smaller screens running both iOS and Android and on larger screens
running both macOS and Windows in multiple browsers. In addition, Chrome's developer tools were used extensively to test on all screen sizes
including medium size which I did not otherwise have access to.
### Testing User Stories
### Testing Features

## Automated Testing
JavaScript code was run through the [JSHint](https://jshint.com/) analysis tool to check for syntax errors.
In addition, CSS was checked in the [CSS Validator](https://jigsaw.w3.org/css-validator/) and HTML in the [HTML Validator](https://validator.w3.org/).

## Issues
### Resolved
1. I encountered a problem with my add_to_cart function where adding more of a product already in the cart would overwrite the quantity insteading of adding the new quantity to the old. In the view I added print statements to the if-else clause:
    ```python
    def add_to_cart(request, id):
        ''' adds a subscription and the quantity chosen to the cart '''
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if id in cart:
            print('Already in cart')
            cart[id] = cart[id] + quantity
        else:
            print('Not in cart')
            cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect('cart')
    ```
    I also printed the cart to see what was in it. I then added 2 of the product with the id 3 to the cart, and then tried adding another 4, so that the total should have been 6. Instead the total was 4. The 'else' print statement was printed, indicating that the product already in the cart was not recognized, and printing cart resulted in `{'3' : 2, 3 : 4}`. It was then clear that the product was not being found because its id was stored as a string while it was being added as an integer.\
    I solved the issue by removing `int:` from the paths in the urls file so that they read `path('adjust/<id>/', ...)` instead of `path('adjust/<int:id>/, ...)'`.
2. On the account page when clicking the icon to add or edit a user's address details, the DoesNotExist exception was raised. This was because no object had yet been created for that particular user in the UserInfo model where those details are stored.\
The issue was solved by using the `get_or_create()` method instead of just `get()`. This way, an object is created when the user clicks the edit icon for the first time, allowing them to add their address details.

### Unresolved

## Additional Testing
