"""
    you can also create agensts with LANGCHAIN, but with crewai, you can communicate with agents.

"""

from crewai import Agent 
from dotenv import load_dotenv 
import os
load_dotenv() 
from tools import tool 

from langchain_google_genai import ChatGoogleGenerativeAI

# call the gemini model  

from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
# llm.invoke("Write me a ballad about LangChain")

try:
    llm = ChatGoogleGenerativeAI(
        model='gemini-1.5-flash',
        provider='google',  # Specify the provider
        verbose=True,
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    print("$$$$$$$$$$$$ LLM initialized successfully.")
except Exception as e:
    print(f"LLM Initialization Error: {e}")

# Test calling LLM directly with the invoke method
# try:
#     # Use the invoke method instead of the __call__ method
#     response = llm.invoke("What is Natural Language Processing?")
#     print("LLM Response:", response)
# except Exception as e:
#     print(f"Error calling LLM: {e}")




# creating a researcher agent 

researcher = Agent(
    role="Senior Researcher",
    goal="Uncover the advances in the Natural Language Processing.",
    verbose=True,
    memory = True,
    backstory = (
                "Explore research papers and technical blogs to provide me with the latest insights on subjects such as AI agents,"
                "large language models, and other related advancements in the field."
    ),
    llm=llm,
    tools =[tool],
    
    # allows the researcher agent to communicate with other agents
    allow_delegation=True
) 

# creating writer agent, responsible in writing the article. 

writer = Agent(
    role="Editor",
    goal="Narrate the stories about Natural Language Processing.",
    verbose=True,
    memory = True,
    backstory = (
            "Summarize and classify the topics into their respective categories, highlight with a heading"
    ),
    tools =[tool],
    llm=llm,
    # allows the researcher agent to communicate with other agents
    allow_delegation=False 
)

# Example execution block
# def run_agents(topic):
#     # Research the topic
#     researcher_response = researcher.invoke({"topic": topic})
#     print("Researcher Response:", researcher_response)

#     # Write about the topic
#     writer_response = writer.invoke({"topic": topic})
#     print("Writer Response:", writer_response)

# # Run the agents with a specific topic
# if __name__ == "__main__":
#     run_agents("AI advancements")