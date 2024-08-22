import mysql.connector
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate


# MySQL connection parameters
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "*******",
    "database": "yourdb",
}

# One time

# Connect to the MySQL database
try:
    global connection
    connection = mysql.connector.connect(**db_config)
except mysql.connector.Error as error:
    print("Error connecting to the database:", error)


# llm = ChatOpenAI(
#     model="gpt-3.5-turbo-0613",
#     openai_api_key="your_api_key",
# )

from langchain_openai import AzureOpenAI

llm = AzureOpenAI(model="model_name",api_key="api_key",api_version="api-preview-version",azure_endpoint = "https://endpoint.openai.azure.com/")


class sqlParser(BaseModel):
    output: str = Field(description="SQL query to be executed in database")


# repeated executions


def execute_sql_query(query):
    global connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as error:
        print("Error executing the query:", error)
        return None

class SQLGENTOOL(BaseModel):
    G: str = Field(description="user query")

def generate_sql_schema(question):
    template = """
    <<Instructions>>
    Given a user query and a sql schema and database information. Generate a sql query based on the user query,

    Here is a table called Stock in db, Stock having coulmns as itemId, ItemName(Item name containing the name of the item present in store), Quantity(Qunatity represnts the nummber of items stock presents in the store), Price(the price of the item)
    here is the ddl of the table
    -- supermarketdb.stock definition

    CREATE TABLE `stock` (
      `ItemID` int NOT NULL AUTO_INCREMENT,
      `ItemName` varchar(100) NOT NULL,
      `Quantity` int NOT NULL,
      `Price` decimal(10,2) NOT NULL,
      PRIMARY KEY (`ItemID`)
    ) 
    another table which is Transaction in DB, transaction having columns as TransactionID, CustomerName(Name of the customer who like to go and buy or return the items), Action(Action done by the customer like Buying or returning of an item), ItemID(here item iD is a foreign key from table Stock), Quantity(Customer buy how much qunatity or return how much qunatity),
    here is the ddl of the table 
    -- supermarketdb.transactions definition

    CREATE TABLE `transactions` (
      `TransactionID` int NOT NULL AUTO_INCREMENT,
      `CustomerName` varchar(100) NOT NULL,
      `Action` enum('Purchase','Return') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
      `ItemID` int DEFAULT NULL,
      `Quantity` int DEFAULT NULL,
      PRIMARY KEY (`TransactionID`),
      KEY `ItemID` (`ItemID`),
      CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`ItemID`) REFERENCES `stock` (`ItemID`)
    )


    <<Context>>
    Here is the user query - 

    User query: {question}

    <<output instruction>>
    {format_instructions}


     """

    parser = PydanticOutputParser(pydantic_object=sqlParser)
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template,
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    llm_chain = prompt | llm | parser

    res = llm_chain.invoke(input={"question": question})
    return res.output


question = "What is the total value of all items in stock"
print(execute_sql_query(generate_sql_schema(question)))
print(generate_sql_schema(question))

#Output Discussuion
