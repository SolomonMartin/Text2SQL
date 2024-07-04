# Text2SQL

Text2SQL is a LangChain and Streamlit application that converts natural language queries into SQL commands to query a database. It allows users to input their queries in plain English and returns the results from the database.

## Features

- **Natural Language to SQL:** Converts user queries in natural language into SQL commands.
- **Database Query Execution:** Executes the generated SQL commands on a predefined SQLite database.
- **User-Friendly Interface:** Built with Streamlit, providing a simple and intuitive user experience.

## Technologies Used

- **LangChain:** Integrates various language processing tasks such as text conversion and natural language understanding.
- **Streamlit:** Creates interactive web applications directly from Python scripts.
- **Google Generative AI:** Provides advanced text generation capabilities for converting natural language queries into SQL.
- **SQLite:** Manages the database and handles SQL query execution.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Text2SQLApp.git
   cd Text2SQLApp
2. Install the required dependencies:

   ```bash
    pip install -r requirements.txt
3. Set up your Google API key:

    Create a .env file in the root directory of the project.
    Add your Google API key to the .env file:
    ```makefile
    GOOGLE_API_KEY=your_api_key_here
4. Ensure you have an SQLite database named student.db with a table STUDENT containing columns NAME, CLASS, SECTION, MARKS (sql.py).

5. Run the Streamlit app:

   ```bash
    streamlit run app.py
Usage
```
Open the app in your browser.
Enter a query in natural language (e.g., "How many entries of records are present").
Click on "Execute" to see the SQL command and the results from the database.
