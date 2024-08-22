# SQL-LLM-Agent

## Overview
SQL-LLM-Agent is a cutting-edge project that leverages OpenAI's GPT-3.5, the LangChain framework, and an Agentic RAG (Retrieval-Augmented Generation) pipeline to transform the way we interact with databases. This system is designed to translate natural language queries into SQL commands, enabling seamless interaction with a MySQL database. It also includes advanced features like transaction tracking, automated actions, and future enhancements like ordering food from Zomato.

## Features
- **AI-Powered SQL Query Generation**: Translates natural language input into SQL queries using GPT-3.5.
- **Agentic RAG Pipeline**: Combines retrieval and generation techniques for accurate and context-aware responses.
- **MySQL Integration**: Securely connects to a MySQL database and executes queries.
- **User-Friendly Interaction**: Allows non-technical users to interact with databases using simple, natural language queries.
- **Error Handling**: Robust handling of errors during query execution, ensuring reliability.
- **Future Capabilities**: Transaction and wallet tracking, and potential automated actions like ordering food.
  ## Project Structure

```plaintext

SQL-LLM-Agent/
├── agents/
│   ├── __init__.py
│   ├── query_agent.py
├── db/
│   ├── __init__.py
│   ├── connection.py
│   ├── executor.py
├── models/
│   ├── llm_model.py
├── prompts/
│   ├── prompt_template.py
├── utils/
│   ├── error_handling.py
│   ├── validation.py
├── tests/
│   ├── test_agent.py
│   ├── test_db.py
│   ├── test_models.py
├── README.md
├── requirements.txt
└── main.py 
```

## Getting Started
# Prerequisites
- Python 3.10+
- MySQL: Ensure that a MySQL server is running and accessible.
- API Keys: Obtain an API key from OpenAI for GPT-3.5.
# Installation
Clone the repository:
```
git clone https://github.com/your-username/SQL-LLM-Agent.git
cd SQL-LLM-Agent
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Set up environment variables:
```
export OPENAI_API_KEY='your-openai-api-key'
export MYSQL_USER='your-mysql-username'
export MYSQL_PASSWORD='your-mysql-password'
export MYSQL_DB='your-database-name'
export MYSQL_HOST='localhost'
```
# Usage
Start the Application:
```
python utils.py
```
Interacting with the Agent:

- You can input natural language queries, like “What is the total value of all items in stock?”
- The agent will generate the corresponding SQL query, execute it, and return the results.

## Future Enhancements
- **Advanced Error Handling & Monitoring:** Implementing more granular error handling and logging for better debugging and system monitoring.
- **Sophisticated NLP Capabilities:** Enhancing natural language processing to handle a wider range of queries.
- **User-Friendly Interface:** Developing a web or desktop interface with query history, result visualization, and export options.
- **Automated Actions:** Enabling the agent to perform tasks like ordering food or managing transactions through voice or text commands.
## Contributing
- Contributions are welcome! If you’d like to help improve this project, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out to me via LinkedIn https://www.linkedin.com/in/satyam-sharma-6632a61b4/ or open an issue in this repository.

## Demo
https://www.linkedin.com/posts/satyam-sharma-6632a61b4_openai-langchain-ai-activity-7197948980297699329-zzSi?utm_source=share&utm_medium=member_desktop
