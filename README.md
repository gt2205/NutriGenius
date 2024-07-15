# Nutritionist Crew Project

## Overview

The Nutritionist Crew Project is an AI-driven system designed to create a personalized and detailed diet plan for patients based on their specific health conditions and dietary needs. Utilizing advanced AI tools and multiple specialized agents, the system collaborates to gather necessary information, evaluate dietary requirements, and generate a comprehensive dietary plan.

## Key Features

- **Personalized Dietary Plans**: The system generates customized diet plans based on individual patient details such as age, gender, height, weight, and specific health conditions.
- **Multi-Agent Collaboration**: The project employs multiple AI agents, each with a specialized role, to ensure comprehensive and accurate dietary recommendations.
- **Integration with External Tools**: Uses advanced AI tools like Groq and Serper to search for and scrape relevant information needed for diet planning.
- **Detailed Role Definition**: Each agent has a clearly defined role, including Senior Doctor, Senior Nutritionist, and Senior Diet Planner, ensuring a systematic approach to diet planning.

## The Big Issue It Solves

### Problem Statement

Patients with specific health conditions often face challenges in managing their diets. Incorrect dietary choices can exacerbate health issues, lead to poor recovery outcomes, and generally degrade the quality of life. Traditional diet planning requires consultation with multiple experts, such as doctors, nutritionists, and diet planners, which can be time-consuming, costly, and inaccessible to many.

### Solution Provided by Nutritionist Crew Project

The Nutritionist Crew Project addresses this issue by providing an automated, comprehensive, and accessible solution for diet planning:

1. **Accessibility**: By integrating various roles into a single AI-driven system, the project makes expert dietary advice accessible to a broader audience, including those who may not have easy access to healthcare professionals.
2. **Efficiency**: The system reduces the time and effort required to generate a personalized diet plan. Patients can receive detailed dietary recommendations quickly, which is crucial for managing health conditions effectively.
3. **Accuracy**: Leveraging advanced AI tools ensures that the dietary recommendations are accurate and tailored to the patient's specific needs. This reduces the risk of dietary errors that could negatively impact health.
4. **Comprehensiveness**: The multi-agent system covers all aspects of diet planning, from identifying beneficial and harmful items to creating balanced meal plans. This holistic approach ensures that all dietary needs are met.

## Agents and Their Roles

### Senior Doctor

- **Role**: Senior doctor
- **Goal**: Find out what items benefit and harm the patient based on their diseases.
- **Backstory**: Specialized in suggesting items that are beneficial or harmful to the patient's health condition.
- **Tools**: [search_tool]
- **LLM**: manager_model

### Senior Nutritionist

- **Role**: Senior nutritionist
- **Goal**: Devise a list of dishes from the items the patient can consume, including their calorie values per serving.
- **Backstory**: Specializes in creating a list of dishes the patient can consume with their calorie values per serving.
- **Tools**: [search_tool, scrape_tool]
- **LLM**: llm

### Senior Diet Planner

- **Role**: Senior diet planner
- **Goal**: Arrange the list of dishes to make a 1-week plan with 3 meals a day, keeping in mind the daily calorie requirement.
- **Backstory**: Highly qualified diet planner who can suggest a diet plan for a week with 3 meals a day.
- **Tools**: [search_tool]
- **LLM**: llm

## Process Flow

1. **Information Gathering**: The Senior Doctor gathers information about items that are beneficial or harmful to the patient.
2. **Diet List Creation**: The Senior Nutritionist uses this information to create a list of dishes the patient can consume, including calorie counts.
3. **Meal Plan Arrangement**: The Senior Diet Planner arranges these dishes into a balanced meal plan for the week, ensuring the daily calorie requirement is met.

## How It Works

1. **Initialization**: The system initializes multiple agents, each with a specific role and goal.
2. **Task Assignment**: Tasks are assigned to agents based on their specialization.
3. **Collaboration**: Agents collaborate to gather information, analyze dietary requirements, and generate a personalized diet plan.
4. **Output**: The final output is a detailed diet plan tailored to the patient's health conditions and dietary needs.

## Benefits

- **Accurate Recommendations**: Leveraging specialized AI agents ensures accurate and reliable dietary recommendations.
- **Comprehensive Plans**: The system provides a detailed and balanced meal plan, taking into account the patient's specific needs.
- **Efficiency**: Automating the diet planning process saves time and ensures consistency in recommendations.
