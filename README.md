# ArchiGen AI
### Autonomous Architecture Blueprint Generation for Intelligent SDLC

ArchiGen AI is a Python-based project that aims to simplify software architecture planning by analyzing application requirements and generating architecture recommendations.

## Project Overview

Designing software architecture manually can be time-consuming and requires knowledge of different technologies and architectural components.

ArchiGen AI addresses this challenge through a requirement-driven approach that identifies application needs and recommends suitable architecture components using a structured knowledge base.

## Key Features

- Requirement analysis from user-provided application descriptions.
- Identification of requirements such as high traffic, product search, shopping cart, and online payment.
- Rule-based architecture recommendations.
- JSON-based knowledge base for storing architecture information.
- Architecture component recommendations based on identified requirements.
- Architecture visualization using HTML.

## Technology Stack

- **Programming Language:** Python
- **Knowledge Representation:** JSON
- **Frontend / Visualization:** HTML
- **Architecture Visualization:** HTML-based architecture diagram

## Project Structure

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

## How It Works

1. The user provides application requirements.
2. The system analyzes the input.
3. Relevant requirements are identified.
4. The agent refers to the structured JSON knowledge base.
5. Suitable architecture components and technology recommendations are generated.
6. Architecture information can be visualized through an HTML diagram.

## Example Use Case

**Input:**

Build an e-commerce application with high traffic, product search, shopping cart, and online payment.

**Identified Requirements:**
- High Traffic
- Product Search
- Shopping Cart
- Online Payment

**Example Architecture Recommendations:**
- Redis – Caching and session management
- Kafka – Event streaming
- Kubernetes – Container orchestration
- OpenSearch – Product search
- PostgreSQL – Transactional database
- OAuth 2.0 – Authorization

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rajharshithab92-web/ArchiGen-AI-Autonomous-Blueprint-Generation-for-Intelligent-SDLC.git
```

### 2. Navigate to the project directory

```bash
cd ArchiGen-AI-Autonomous-Blueprint-Generation-for-Intelligent-SDLC
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

## Project Domain

Artificial Intelligence | Software Architecture | Intelligent SDLC

## Future Enhancements

- Generate detailed High-Level Design (HLD) and Low-Level Design (LLD).
- Expand the knowledge base to support Healthcare and BFSI domains.
- Add advanced architecture visualization.
- Generate downloadable architecture blueprint reports.
- Integrate Retrieval-Augmented Generation (RAG) for knowledge-based recommendations.

## Author

**Harshitha B Raj**

Department of Information Science and Engineering  
Nagarjuna College of Engineering and Technology