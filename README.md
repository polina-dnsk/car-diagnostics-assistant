# Car Diagnostics Assistant (RAG-based System)

This project is a **Car Diagnostics Assistant** built using a **Retrieval-Augmented Generation (RAG)** architecture. The system helps users diagnose car problems by providing detailed information about car error codes, causes, and solutions based on a pre-loaded database of car issues. It combines **retrieval** from a vector database (ChromaDB) and **natural language generation** using OpenAI's GPT-4o-mini model to deliver detailed, contextual responses to user queries.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Acknowledgments](#acknowledgments)

## Features
- Quickly find detailed information about specific car error codes, including descriptions, causes, and solutions.
- Ask questions in plain language about car issues, and receive comprehensive responses.
- Supports a variety of queries, from specific error codes to general car problems and symptoms.

## Installation

### Dependencies

This project relies on the following dependencies:

- **ChromaDB**: For vector-based data storage and retrieval. [Learn more](https://www.trychroma.com/)
- **OpenAI**: For GPT-based natural language generation. This project specifically utilizes the GPT-4o-mini model. [Sign up for an API key](https://platform.openai.com/signup)
- **python-dotenv**: A module to load environment variables from a `.env` file.

### System Requirements

- **Python 3.12.3**


### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/polina-dnsk/car-diagnostics-assistant.git
    cd car-diagnostics-assistant
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root with your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. Run the project:
    ```bash
    python car_diagnostics.py
    ```

## Usage
Once the program is running, it will load a database of car error codes and problems, and prompt you to ask a question.

### Example session:
🚗 Welcome! I am your Car Diagnostics Assistant! 🚗

I am here to help you diagnose car issues and provide solutions based on your car's error codes and symptoms.

**Here are some example questions you can ask:**
- What does P0300 mean?
- Why is my engine misfiring randomly?
- My engine is shaking. What could be causing this?
- What does error code P0171 mean regarding fuel mixture?
- What does it mean if I see error code P0420?
- I'm getting error P0700, what should I do?
- My car is having trouble shifting gears. What could be wrong?
- What does it mean if my transmission fluid is low?
- How does a faulty mass airflow sensor affect my car's performance?
- My car has poor fuel economy and rough idling, what could be the problem?

💡 **Tip**: For the best results, provide a specific error code or detailed description of the problem.

If you would like to exit, please type 'q'.

---

**Question:** Hi!  
**Response:**  
Hello! How can I assist you today? If you have any questions about car diagnostics or error codes, feel free to ask!

---

**Question:** What causes the catalytic converter to malfunction?  
**Response:**  
**Relevant Error Code:** P0420

**Causes:** The catalytic converter may malfunction due to several reasons, including:
- Failing catalytic converter itself
- Faulty oxygen sensors (O2 sensors)
- Exhaust leaks
- Engine misfire

**Solutions:** To resolve issues related to the catalytic converter, you can consider the following steps:
- Replace the catalytic converter if it is found to be failing.
- Check and replace any faulty oxygen sensors to ensure proper readings and functionality.
- Repair any exhaust leaks that could affect the performance of the emissions system.
- Address any engine misfire issues, which can contribute to catalytic converter problems.

If you have any further questions or need assistance, feel free to ask!

---

**Question:** I'm getting error P0700, what should I do?  
**Response:**  
**Error Code:** P0700  
**Problem Description:** The transmission control system has detected a malfunction, which may lead to erratic shifting or the vehicle being stuck in a single gear.

**Causes:**
- Transmission control module failure
- Damaged wiring in the transmission control system
- Low transmission fluid

**Solutions:**
- Replace the transmission control module if it is determined to be faulty.
- Inspect and repair or replace any damaged wiring in the transmission control system.
- Check the transmission fluid levels and refill if they are low.

It's recommended to have a professional mechanic diagnose the issue further to determine the exact cause and perform the necessary repairs.

---

**Question:** Thank you, that was all.  
**Response:**  
You're welcome! If you have any more questions, feel free to ask!

---

**Question:** q  
**Response:**  
Thank you for using the Car Diagnostics Assistant! Have a great day!

## How It Works

### Retrieval
The system loads car problems from a JSON file (`car_problems.json`) and stores them in a vector database (ChromaDB). When the user submits a query, the system searches the collection in ChromaDB for the most relevant car problem information.

### Augmentation
The retrieved data (error code, causes, and solutions) is formatted and used to construct a detailed prompt.

### Generation
The system sends the prompt and the user query to OpenAI's GPT model, which generates a human-readable response tailored to the user's query.

## Acknowledgments

I would like to express my gratitude to the following:

- **ChromaDB Team**: For developing ChromaDB, which facilitates efficient vector-based data storage and retrieval in this project.
- **OpenAI**: For providing access to the GPT-4o-mini model, which powers the natural language generation capabilities of this application.