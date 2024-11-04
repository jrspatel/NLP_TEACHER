# For every agent we need to create task 

from crewai import Task 
from tools import tool 
from agents import researcher, writer

research_task = Task(
    description=(
        " dive into each research paper, blogs & articles to find what are they trying to solve"
        "and what type of methods the researchers are using to solve those problems."
    ),  
    expected_output='A title of the research paper, with a short description. Limit each category by 4 reports.', 
    tools=[tool],
    agent=researcher,
)

writer_task = Task(
    description=(
            "This article should be easy to understand."
            "Focus on important topics where i can build projects on those to build my budding carrer in this field and gain internships and full time opputinities."
    ),
    expected_output='A para for each report you recive from the researcher agent, which includes every thing and be clear on what i should work on.', 
    tools=[tool],
    agent=writer,
    output_file = 'nlp_blog.md'
)