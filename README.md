# PrimeTech e-commerce platform

Access the live site [here](https://primetechfnkd-382d679752d9.herokuapp.com/).

## Contents

* [MoSCoW priotisation](#moscow-prioritisation)
* [User Experience design](#user-experience-design)


## MoSCoW prioritistation and Kanban board

I used a kanban board timeline [accessed here](https://github.com/users/DanFNKD/projects/5) to track my user stories and prioritise features based on the MoSCoW prioritisation method.

Must Haves:
1. User Accounts and Authentication:
  - Registration (username, email, and password)
  - Login and logout functionality
  - User profile pages with order history and personal details
2. Product Catalogue and Navigation:
  - Viewing a list of products (with pagination or infinite scrolling)
  - Ability to filter and sort products (by price, category, rating, etc.)
  - Viewing individual product details (including multiple images, description, pricing, and related products)
3. Shopping Cart and Checkout:
  - Adding products to the basket, adjusting quantities, and removing items
  - Displaying a cart summary with a total price (including shipping calculation)
  - Secure checkout process integrated with Stripe for payment processing
  - Order confirmation email functionality
4. Basic Search Functionality:
  - Keyword search that returns matching products
5. Deployment and Code Quality:
  - A consistent, clean Django project structure with logical app separation
  - All CRUD operations for products and related models are implemented
  - The final deployed version is secure (with secret keys and credentials stored as environment variables) and free of broken links

Should Haves:
1. Wishlist Functionality:
  - Ability for authenticated users to save items to a wishlist for later purchase
2. Advanced Search and Sorting Options:
  - Combining filters and sorting (e.g., filtering by category and sorting by price or rating)
3. User Reviews and Ratings:
  - Allowing customers to submit and update reviews on products
4. Enhanced User Experience (UX):
  - Responsive design improvements and additional UX touches (e.g., subtle animations or enhanced product card layouts)

Could Haves:
1. Personalisation and Recommendations:
  - Product recommendations based on browsing history or category
  - Customisation options for user preferences (e.g., favorite brands or categories)
2. Marketing and Engagement Features:
  - Newsletter signup form
  - Links to social media platforms such as Facebook Business pages
  - Social media integration for sharing products or promotions
3. Additional Content Features:
  - Extra pages such as “FAQs” or blog articles related to technology and products

Will Not Have Now:
1. Store Access Information:
  - Detailed “About the Store” information is not included in the current user stories
2. Advanced Promotional Features:
  - Features such as dynamic discount systems, flash sales, or extensive analytics that are beyond core e-commerce functionality

## User Experience design

### Strategy design

#### User stories and epics

##### Epic: Viewing and Navigation:
- [1.1](https://github.com/DanFNKD/PrimeTech/issues/1) - As a shopper, I can view a list of products so that I can easily browse and choose items to purchase.
- [1.2](https://github.com/DanFNKD/PrimeTech/issues/2) - As a shopper, I can view a specific category of products so that I can quickly find items of interest without searching through all products.
- [1.3](https://github.com/DanFNKD/PrimeTech/issues/3) - As a shopper, I can view individual product details so that I can make an informed decision about purchasing an item.
- [1.4](https://github.com/DanFNKD/PrimeTech/issues/4) - As a shopper, I can identify deals, clearance items, and special offers so that I can take advantage of discounts.
- [1.5](https://github.com/DanFNKD/PrimeTech/issues/5) - As a shopper, I can view the total of my purchases at any time so that I can stay within my budget.
- [1.6](https://github.com/DanFNKD/PrimeTech/issues/6) - As a shopper, I can find details about the store so that I can learn about their values and policies.
- [1.7](https://github.com/DanFNKD/PrimeTech/issues/7) - As a shopper, I can find answers to questions so that I can make informed decisions before purchasing.
##### Epic: Registration and User Accounts:
- [2.1](https://github.com/DanFNKD/PrimeTech/issues/8) - As a site user, I can easily register for an account so that I can access personalised features like saved addresses and order history.
- [2.2](https://github.com/DanFNKD/PrimeTech/issues/16) - As a site user, I can easily login or logout so that I can manage my account securely.
- [2.3](https://github.com/DanFNKD/PrimeTech/issues/9) - As a site user, I can access my personalised profile so that I can view order history and save payment details.
##### Epic: Sorting and Searching:
- [3.1](https://github.com/DanFNKD/PrimeTech/issues/10) - As a shopper, I can search for products by name or description so that I can find items quickly.
- [3.2](https://github.com/DanFNKD/PrimeTech/issues/11) - As a shopper, I can sort products so that I can prioritise my preferences like best price or rating.
##### Epic: Shopping Cart Management:
- [4.1](https://github.com/DanFNKD/PrimeTech/issues/12) - As a shopper, I can add, remove, and adjust quantities in my shopping cart so that I can finalise my purchase.
##### Epic: Wishlist Management:
- [5.1](https://github.com/DanFNKD/PrimeTech/issues/13) - As a shopper, I can save items to a wishlist so that I can decide whether to purchase them later.
##### Epic: Email Communication:
- [6.1](https://github.com/DanFNKD/PrimeTech/issues/14) - As a shopper, I receive order confirmation emails so that I know my purchase was successful.
##### Epic: Admin Panel Functionality:
- [7.1](https://github.com/DanFNKD/PrimeTech/issues/15) - As an admin, I can add, update, and remove products so that the catalogue remains up to date.