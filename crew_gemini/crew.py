from crewai import Crew, Process 
from agents import researcher, writer 
from tasks import research_task, writer_task 
import os

#  The flow of the project starts here..
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writer_task],
    process = Process.sequential

) 

## starting the task execution 


result = crew.kickoff()
print(result)