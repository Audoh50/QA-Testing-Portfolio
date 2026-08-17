# E-Commerce Application Test Cases

## Test Case 1 – Successful User Login

**Test Case ID:** TC-001

**Test Scenario:** Verify that a registered user can successfully log into the application.

**Precondition:** User has an active registered account.

**Test Steps:**

1. Navigate to the login page.
2. Enter a valid email address.
3. Enter the correct password.
4. Click the Login button.

**Expected Result:**

The user should successfully log in and be redirected to their account dashboard.

**Status:** Pass


## Test Case 2 – Invalid Password

**Test Case ID:** TC-002

**Test Scenario:** Verify that the application prevents login when an incorrect password is entered.

**Precondition:** User has an active registered account.

**Test Steps:**

1. Navigate to the login page.
2. Enter a valid registered email address.
3. Enter an incorrect password.
4. Click the Login button.

**Expected Result:**

The user should remain on the login page and an appropriate error message should be displayed.

**Status:** Pass


## Test Case 3 – Empty Login Fields

**Test Case ID:** TC-003

**Test Scenario:** Verify validation when the login form is submitted without credentials.

**Test Steps:**

1. Navigate to the login page.
2. Leave the email address blank.
3. Leave the password blank.
4. Click the Login button.

**Expected Result:**

The application should display validation messages indicating that the required fields cannot be empty.

**Status:** Pass


## Test Case 4 – Add Product to Shopping Cart

**Test Case ID:** TC-004

**Test Scenario:** Verify that a customer can add a product to the shopping cart.

**Test Steps:**

1. Navigate to the product page.
2. Select a product.
3. Click Add to Cart.
4. Open the shopping cart.

**Expected Result:**

The selected product should appear in the shopping cart with the correct product name, quantity, and price.

**Status:** Pass


## Test Case 5 – Remove Product from Shopping Cart

**Test Case ID:** TC-005

**Test Scenario:** Verify that a customer can remove a product from the shopping cart.

**Precondition:** At least one product has been added to the cart.

**Test Steps:**

1. Open the shopping cart.
2. Locate the product.
3. Click Remove.
4. Review the shopping cart.

**Expected Result:**

The product should be removed and the cart total should be updated correctly.

**Status:** Pass


## Test Case 6 – Product Search

**Test Case ID:** TC-006

**Test Scenario:** Verify that the search functionality returns relevant products.

**Test Steps:**

1. Navigate to the homepage.
2. Locate the search bar.
3. Enter a valid product name.
4. Click Search.

**Expected Result:**

Products relevant to the search term should be displayed.

**Status:** Pass


## Test Case 7 – Search for Nonexistent Product

**Test Case ID:** TC-007

**Test Scenario:** Verify the application's response when searching for a nonexistent product.

**Test Steps:**

1. Navigate to the homepage.
2. Enter a product name that does not exist.
3. Click Search.

**Expected Result:**

The application should display an appropriate message indicating that no products were found.

**Status:** Pass


## Test Case 8 – Checkout Without Required Address

**Test Case ID:** TC-008

**Test Scenario:** Verify that the customer cannot complete checkout without entering required shipping information.

**Test Steps:**

1. Add a product to the shopping cart.
2. Proceed to checkout.
3. Leave required shipping address fields blank.
4. Click Continue or Place Order.

**Expected Result:**

The application should prevent checkout and display validation messages for the required fields.

**Status:** Pass
