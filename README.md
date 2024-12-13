# Food Order Tracking Chatbot

### Screenshots of the Project:
1- The first look
![image](https://github.com/user-attachments/assets/5aded04b-c41d-41f9-b619-a038e0007124)

2- It is fully responsive
![image](https://github.com/user-attachments/assets/694c1309-e1c3-4df4-a3ea-91a457477240)

3- There are pre-listed relative questions for customers to ask from
![image](https://github.com/user-attachments/assets/3f0e69a2-58dc-4ac9-8f6f-4d299c97c8e6)

4- It also has some default messages set, to send when the message sent by customer is not in our database.
![image](https://github.com/user-attachments/assets/89ffd5f6-af88-4a41-bbb8-65bdeaea49e4)


## Project Overview

This Food Order Tracking Chatbot is a simple, web-based customer support chatbot designed to assist users in tracking their food orders, updating delivery addresses, cancelling orders, and answering common delivery-related queries. The chatbot uses Natural Language Processing (NLP) with NLTK to process user inputs and respond with pre-defined answers. This project is built with a Python backend and an HTML/Bootstrap frontend, with AJAX and JavaScript enabling the interaction between the user interface and backend.

## Features

- **Track orders**: Users can inquire about the status of their food orders.
- **Update delivery address**: Provides options for users to update their address for current orders.
- **Cancel orders**: Assists users in cancelling orders.
- **General FAQs**: Answers frequently asked questions, like delivery time and support contact information.
- **Prompt Suggestions**: Displays a list of predefined question prompts after every chatbot response for easy user selection.

## Technologies Used

### Languages, Libraries, and Frameworks

1. **Python**: The backend language used to handle chatbot logic.
2. **NLTK (Natural Language Toolkit)**: Python library used for natural language processing.
3. **Flask**: Web framework used to run the Python backend on a local server.
4. **HTML5**: Markup language for creating the structure of the web page.
5. **CSS3**: Styles the chatbot and creates a custom UI inspired by WhatsApp.
6. **Bootstrap 4**: CSS framework for responsive design and layout.
7. **JavaScript & AJAX**: For dynamic frontend interactions and communication with the backend.
8. **jQuery**: JavaScript library used for simplified AJAX calls and DOM manipulation.


## Installation and Setup

### Prerequisites

1. **Python**: Make sure Python 3.x is installed on your machine.
2. **pip**: Ensure `pip` is installed to manage Python packages.

### Step-by-Step Setup Instructions

Follow these steps to set up and run the chatbot on your local machine.

1. **Clone the Repository**

   Clone this repository to your local machine:
   bash
   git clone https://github.com/your-username/food-order-tracking-chatbot.git
   cd food-order-tracking-chatbot

2. **Set Up a Virtual Environment (Optional but Recommended)**

Create a virtual environment to keep dependencies organized:
python -m venv venv

Activate the virtual environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

3. **Install Required Python Libraries**

Install the required libraries from requirements.txt. If the file doesn’t exist, you can manually install the libraries:
pip install flask nltk

4. **Download NLTK Data (if not already installed)**

Open a Python shell and run the following commands to download necessary NLTK data files:
import nltk
nltk.download('punkt')

5. **Run the Application**

Start the Flask server to run the chatbot:
python app.py

6. **Access the Chatbot**

Open a web browser and go to http://127.0.0.1:5000 to interact with the chatbot.

**Usage**
Type your questions in the input box and click "Send" to interact with the chatbot.
After each response, a list of suggested prompt questions will appear. Click on these buttons to quickly ask common questions.

**Example Interactions**
"Track my order": The bot will respond with order tracking information.
"Update delivery address": The bot will guide you on how to update the delivery address.
"Cancel my order": The bot will provide information on how to cancel your order.
"How long will delivery take?": The bot will respond with typical delivery time estimates.
"Contact support": Provides options for contacting customer support.
Additional Notes
This chatbot is currently a mock-up and does not interact with a real database or backend service for order tracking. It's designed for demonstration purposes with pre-defined responses.
You can customize the chatbot by modifying app.py to add more questions and responses.

**Troubleshooting**
Issue: "Command not found" when trying to activate virtual environment.

Solution: Ensure you're in the correct directory where you created the virtual environment and use the appropriate activation command for your OS.
Issue: Cannot connect to http://127.0.0.1:5000.

Solution: Ensure the Flask server is running in your terminal.

**Future Improvements**
Add actual integration with a database or API for real-time order tracking.
Implement a more advanced NLP model for better response accuracy.
Include user authentication for personalized order tracking.

**License**
This project is licensed under the MIT License.
