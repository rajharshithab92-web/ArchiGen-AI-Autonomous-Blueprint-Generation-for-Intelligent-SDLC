# ArchiGen AI
### Autonomous Architecture Blueprint Generation for Intelligent SDLC

ArchiGen AI is a Python-based, rule-driven architecture generation system designed to simplify the early stages of software architecture planning.

The system analyzes user-provided application requirements, identifies relevant functional and non-functional needs, and recommends suitable architectural components, technologies, and design patterns using a structured JSON knowledge base.

It generates **High-Level Design (HLD)** and **Low-Level Design (LLD)** representations and provides architecture visualization through an interactive HTML interface using Mermaid.js.

The project aims to reduce manual architecture planning effort and improve the consistency of technology recommendations.

---

## 📌 Project Overview

Designing software architecture manually can be time-consuming and requires knowledge of different technologies, architectural patterns, infrastructure components, and system requirements.

ArchiGen AI addresses this challenge through a requirement-driven approach. Instead of manually selecting every architectural component, users can provide an application description, and the system analyzes the requirements to generate relevant architecture recommendations.

The current prototype focuses on the **E-Commerce domain**, using predefined architecture knowledge and rule-based decision-making.

---

## 🎯 Project Objectives

- Automate the initial stages of software architecture planning.
- Analyze application requirements from natural-language descriptions.
- Identify functional and non-functional requirements.
- Recommend suitable technologies and architectural components.
- Generate High-Level Design (HLD) and Low-Level Design (LLD).
- Visualize the generated architecture through an interactive interface.
- Provide a foundation for future security-aware architecture generation.

---

## ✨ Key Features

- **Requirement Analysis:** Analyzes user-provided application descriptions.
- **Requirement Detection:** Identifies requirements such as high traffic, product search, shopping cart, product catalog, payment, and authentication.
- **Rule-Based Recommendations:** Selects suitable technologies based on predefined architecture rules.
- **JSON-Based Knowledge Base:** Stores architectural layers, technologies, components, patterns, and selection rules.
- **Architecture Component Selection:** Recommends relevant components based on detected requirements.
- **High-Level Design (HLD):** Generates a high-level representation of the application architecture.
- **Low-Level Design (LLD):** Provides service-level implementation details.
- **Architecture Visualization:** Displays architecture diagrams through an HTML interface using Mermaid.js.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Knowledge Representation | JSON |
| Frontend | HTML, CSS, JavaScript |
| Architecture Visualization | Mermaid.js |
| Development Environment | Visual Studio Code |
| Version Control | Git and GitHub |

---

## 📂 Project Structure

```text
ArchiGen-AI/
│
├── agent/
│   ├── architect_agent.py
│   └── architect_agent_backup.py
│
├── knowledge/
│   └── ecommerce.json
│
├── architecture_diagram.html
├── main.py
├── requirements.txt
└── README.md
```

### Folder and File Description

- `agent/` – Contains the architecture generation agent.
- `architect_agent.py` – Main agent responsible for requirement analysis and architecture generation.
- `architect_agent_backup.py` – Backup copy of the agent.
- `knowledge/` – Stores the structured architecture knowledge base.
- `ecommerce.json` – Contains architectural layers, technologies, components, patterns, and selection rules for the E-Commerce domain.
- `architecture_diagram.html` – Generated HTML page for architecture visualization.
- `main.py` – Project entry point.
- `requirements.txt` – Lists the Python dependencies.
- `README.md` – Project documentation.

---

## ⚙️ How It Works

ArchiGen AI follows a requirement-driven architecture generation workflow.

1. **User Input:** The user provides a description of the application to be developed.
2. **Requirement Analysis:** The system analyzes the provided description.
3. **Requirement Detection:** Relevant application requirements are identified.
4. **Knowledge Base Retrieval:** The agent refers to the structured JSON knowledge base.
5. **Technology Recommendation:** Suitable technologies and architectural components are selected using predefined rules.
6. **Architecture Generation:** The system generates HLD and LLD representations.
7. **Visualization:** The generated architecture is displayed through an interactive HTML interface.

---

## 🔄 System Workflow

```text
        User Requirements
               |
               v
       Requirement Analysis
               |
               v
       Requirement Detection
               |
               v
      JSON Knowledge Base
               |
               v
      Rule-Based Selection
               |
               v
     Architecture Generation
               |
          +----+----+
          |         |
          v         v
         HLD       LLD
          |         |
          +----+----+
               |
               v
      Mermaid Visualization
               |
               v
       Interactive HTML Output
```

---

## 🧪 Example Use Case

### Application: E-Commerce Platform

**Sample Input:**

```text
Build an e-commerce application with high traffic,
product search, shopping cart, and online payment.
```

### Identified Requirements

- High Traffic
- Product Search
- Shopping Cart
- Payment

### Example Architecture Recommendations

| Technology | Purpose |
|---|---|
| Redis | Caching and session management |
| Kafka | Event streaming |
| Kubernetes | Container orchestration |
| OpenSearch | Product search |
| PostgreSQL | Transactional data storage |
| OAuth 2.0 | Authorization |

*These are example recommendations from the curated architecture knowledge base.*

### Generated Outputs

- Architecture component recommendations
- High-Level Design (HLD)
- Low-Level Design (LLD)
- Mermaid-based architecture diagram
- Interactive HTML visualization

---

## 🚀 Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

- Python 3.x
- Git
- Visual Studio Code (recommended)
- A web browser

### 1. Clone the Repository

```bash
git clone https://github.com/rajharshithab92-web/ArchiGen-AI-Autonomous-Blueprint-Generation-for-Intelligent-SDLC.git
```

### 2. Navigate to the Project Directory

```bash
cd ArchiGen-AI-Autonomous-Blueprint-Generation-for-Intelligent-SDLC
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

If you are running the agent directly, use:

```bash
python agent/architect_agent.py
```

### 5. View the Generated Architecture

After successful execution, open the generated `architecture_diagram.html` file in your web browser to view the architecture visualization.

---

## 🔬 Current Implementation Status

| Module | Status |
|---|---|
| Requirement analysis | Implemented |
| Requirement detection | Implemented |
| JSON knowledge base | Implemented |
| Rule-based technology selection | Implemented |
| Architecture component selection | Implemented |
| HLD generation | Implemented |
| LLD generation | Implemented |
| HTML architecture visualization | Implemented |
| Security-aware architecture generation | In progress |
| Multiple application domains | Planned |
| Downloadable blueprint reports | Planned |
| RAG-based recommendations | Planned |

---

## 🔮 Future Enhancements

- **Security-Aware Architecture Generation:** Identify security requirements and map them to appropriate architecture-level security controls.
- **Expanded Domain Support:** Extend the knowledge base to support Healthcare and Banking, Financial Services, and Insurance (BFSI) applications.
- **Advanced Architecture Visualization:** Introduce additional architecture views and improved diagram interactions.
- **Blueprint Report Generation:** Generate downloadable architecture documentation and reports.
- **Retrieval-Augmented Generation (RAG):** Integrate RAG to support knowledge-based architecture recommendations.
- **Architecture Validation:** Introduce mechanisms to identify missing or inconsistent architecture components and security controls.
- **Architecture Evaluation:** Evaluate recommendation quality, requirement coverage, and architecture consistency.

---

## 🌍 Project Domain

- Artificial Intelligence
- Software Architecture
- Requirement Engineering
- Intelligent Software Development Life Cycle (SDLC)
- Architecture Automation

---


---

## ⭐ Acknowledgement

This project is developed as part of an academic major project with the objective of exploring automation in software architecture planning and intelligent software development.

---

*ArchiGen AI – Simplifying Software Architecture Planning through Intelligent Automation.*