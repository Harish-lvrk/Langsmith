from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['LANGCHAIN_PROJECT'] ='REACT_AGENT'
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """
    url = f'https://api.weatherstack.com/current?access_key=f07d9636974c4120025fadf60678771b&query={city}'
    response = requests.get(url)
    return response.json()

# Create agent using the new create_agent function
from langchain.agents import create_agent
agent = create_agent(
    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0),
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant.",
    
)



# # What is the release date of Dhadak 2?
# # What is the current temp of gurgaon
# # Identify the birthplace city of Kalpana Chawla (search) and give its current temperature.

# Invoke the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the capital city of Andhra pradesh and its temparature"}]},
    config={"verbose": True, "run_name": "weather_query"})
print(response)