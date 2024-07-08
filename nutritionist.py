# -*- coding: utf-8 -*-


!pip install -qU crewai crewai_tools langchain_community

!pip -q install groq
!pip -q install langchain-groq

!pip install -qU 'crewai[tools]'

from crewai import Crew, Process, Agent, Task

from google.colab import userdata
import os
os.environ["SERPER_API_KEY"]=userdata.get('serper')
os.environ["GROQ_API_KEY"]=userdata.get('groq')
from langchain_groq import ChatGroq
llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

manager_model = ChatGroq(temperature=0, model_name="llama3-70b-8192")

from crewai_tools import ScrapeWebsiteTool, SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

senior_doctor = Agent(
    role="Senior doctor",
    goal="As per that diseases the patient has,finds out what items benefit him and what harm him.Takes utmost care while  ",
    backstory="Specialized in suggesting items that are harmful and items that are beneficial in the health condition of the patient as per given health conditions of the patient.It suggests a list of items that the patient must and must not consume keeping in mind his/her health condition",
    verbose=True,

    tools = [search_tool],
    llm=manager_model,
)

senior_nutritionist = Agent(
    role="Senior nutritionist",
    goal="Given the set of products the patient can consume and cannot consume,device a list of dishes from those items that the patient can consume.Also include their calorie values per serving.",
    backstory="Specializes in creating a list of dishes the patient can consume with their calorie values per serving",
    verbose=True,

    tools = [search_tool,scrape_tool],
    llm=llm
)

senior_diet_planner=Agent(
    role="senior diet planner",
    goal="You are provided with the list of dishes the patient can have,now arrange them to make a 1 week plan having 3 meals a day keeping in mind that daily calorie requirement of patient is almost same as what the patient consumes each day",
    backstory="highly qualified diet planner who can suggest diet plan for a week with 3 meals a day with given dishes and calorie counts",
    verbose=True,

    tools = [search_tool],
    llm=llm,
)

doctor_task = Task(
    description=(
        "Given that the patient sufferes from {patient},find out a list of items that are benefical and that are harmful for the patient."
    ),
    expected_output=(
        "List of products good for patient and harmful for patient"
    ),
    agent=senior_doctor,
)

nutritionist_task=Task(
    description=(
        "the doctor gives you an information about what things the patient can and cannot consume.First calculate how many calories the patient must consume in a day as per the give age-{age},height-{height},weight-'{weight}',sex-'{gender}'.You can use mayoclinic's calorie calculator for this purpose assuming the patient is somewhat active.Now ask the doctor for the list of items beneficial and harmful for the patient.Now as per what items the doctor told,and keeping in mind the patient is {veg},device a list of dishes from those items and their calorie values in 1 serving and data to next agent for prepairing schedule"
    ),
    expected_output=(
        "list of products that the patient can consume, along with their calories in 1 serving  and keep the list enough big to keep good options and also satisfy patient requirements.Also output the amount of calories the patient must consume in a single day"
    ),
    agent=senior_nutritionist,
)

dietician_task=Task(
    description=(
        "given the dishes the patient can consume,arrange them properly to make a whole week plan with 3 meals a day .Keep in mind that they are approximately totalling up to similar calorie count what the patient must consume in each day.Prepare the schedule in a presentable format."
    ),
    expected_output=(
        "diet plan for the patient for whole week keeping 3 meals a day "
    ),
    agent=senior_diet_planner,
)

from crewai import Crew, Process
nutrionist_crew = Crew(
    agents=[senior_doctor,senior_nutritionist,
            senior_diet_planner,],

    tasks=[
        doctor_task,nutritionist_task,

           dietician_task,],
    process=Process.heirarcical,
    manager_llm=manager_model,
    verbose=True,

)

patient_details={
    'age':'24 year',
    'gender':'female',
    'height':'155 cm',
    'weight':'52 kg',
    'veg':'non-vegetarian',
    'patient':'acute gastroentritis'
}

result=nutrionist_crew.kickoff(inputs=patient_details)

result
