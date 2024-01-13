# README.md for CrewAI Example Project

## Introduction

This repository serves as an example project demonstrating the capabilities of CrewAI, a multi-agent AI framework. It includes two example scripts, `talent_search.py` and `financial_analysis.py`, which illustrate how CrewAI can be employed in different contexts - recruitment and financial analysis, respectively. This README provides guidance on setting up and running the example project.

My blog post with more detail on this project can be found [here](https://stephencollins.tech/posts/how-to-automate-processes-with-crewai).

## Project Structure

This example project contains the following key files:

- `talent_search.py`: An example script for a recruitment use case.
- `financial_analysis.py`: An example script for financial analysis.
- `.env.example`: A template for setting up your environment variables.

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- pip, the Python package manager.
- OpenAI API key and a SERPAPI API key.

### Installation Steps

1. **Clone the Example Project**:

   - Clone or download this repository to your local machine.

2. **Install Dependencies**:

   - Navigate to the project directory and install the required packages:

     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**:
   - Rename `.env.example` to `.env`.
   - Fill in your OpenAI API key and SERPAPI API key in the `.env` file.

## Running the Examples

### Talent Search Example

`talent_search.py` showcases a recruitment scenario using CrewAI. To run this script:

1. Navigate to the directory containing `talent_search.py`.
2. Execute the script:

   ```bash
   python talent_search.py
   ```

### Financial Analysis Example

`financial_analysis.py` demonstrates financial analysis using CrewAI. To run this script:

1. Navigate to the directory containing `financial_analysis.py`.
2. Execute the script:

   ```bash
   python financial_analysis.py
   ```

## Understanding the Code

Each script demonstrates the instantiation of AI agents with specific roles and goals, the assignment of tasks to these agents, and how they interact within the CrewAI framework to accomplish the tasks.

## Conclusion

This example project provides a practical illustration of how CrewAI can be utilized in different domains. By exploring and running these examples, you can gain insights into integrating CrewAI into your own projects.
