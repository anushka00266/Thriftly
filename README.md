# Thriftly

Thriftly is a platform that connects users who want to sell or buy pre-loved items. It offers an intuitive interface to list, browse, and purchase items, with a special focus on sustainability and giving items a new life. The project includes functionality for users to upload new items, manage their listings, purchase items through Cash on Delivery (COD), and communicate with sellers through a chat feature.

# Features

- User Authentication : Register, log in, and log out functionality for users.
- Item Management : Users can create, edit, and delete their item listings.
- Search Functionality : Users can search for items based on keywords (name or description).
- Purchase Flow : Users can purchase items with Cash on Delivery (COD).
- Shipping Details : Users can fill out their shipping details for COD orders.
- Order Confirmation : After a successful order, users get a confirmation of the order status.
- Contact Seller : Users can contact the seller directly by sending messages through a built-in chat feature.
- Chat Feature : A real-time messaging system that allows buyers and sellers to communicate about items in a private chat.

# Technologies Used

- Django : The backend framework to build the web application.
- Python : The programming language used to develop the app.
- Tailwind CSS : A utility-first CSS framework for building modern, responsive UI.
- SQLite : The database used for storing user and item data.
- Channels: Django Channels for real-time chat functionality.
- Redis : Used as a channel layer for real-time messaging.

# Installation

## Prerequisites

- Python 3.13 or later
- pip (Python package manager)
- Redis (for Channels)

### Steps

Step 1: Clone the Repository :
         git clone <repository-url>
         cd thriftly
         
Step 2: Create and Activate a Virtual Environment :
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Step 3: Install Dependencies :
pip install -r requirements.txt

Step 4: Apply Migrations :
python manage.py makemigrations
python manage.py migrate

Step 5: Run the Development Server :
python manage.py runserver

Step 6: Access the Application :
Open your browser and go to:http://127.0.0.1:8000/
         
   
