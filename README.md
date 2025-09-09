# End-to-End Data Pipeline and Dashboard Project

This repository showcases a complete data workflow that includes **Python ETL scripts**, **Airflow orchestration**, **dbt transformations**, **Docker containerization**, and a **Power BI dashboard** for visualization.

---

## 📁 Project Structure
project-root/
├── dags/ # Airflow DAG files
├── dbt/ # dbt project
│ ├── models/
│ ├── dbt_project.yml
│ └── ...
├── scripts/ # Python ETL scripts
├── plugins/ # Airflow plugins
├── docker/ # Docker and docker-compose files
├── requirements/ # Python dependencies
├── reports/ # Power BI dashboard
│ ├── dashboard.pbix
│ └── screenshots/
├── .env.example # Example environment variables
└── README.md
---

## Technologies Used

- **Python** – ETL scripts and data processing
- **Airflow** – DAG orchestration for automated pipelines
- **dbt** – Data transformations and modeling
- **Docker & docker-compose** – Containerized development environment
- **Power BI** – Interactive dashboards for reporting

---

setup_instructions:
  step_1:
    description: "Clone the repository"
    commands:
      - "git clone https://github.com/yourusername/your-repo.git"
      - "cd your-repo"

  step_2:
    description: "Create your .env file"
    instructions:
      - "Copy .env.example to .env"
      - "Edit .env to add your local secrets paths and Airflow Fernet key"
    commands:
      - "cp .env.example .env"

  step_3:
    description: "Start the environment with Docker"
    commands:
      - "docker-compose up"
    notes:
      - "Airflow webserver will be available at http://localhost:8080"
      - "DAGs will automatically load from dags/"
      - "dbt models are mounted into the container and can be run inside Airflow tasks"

  step_4:
    description: "Power BI Dashboard"
    instructions:
      - "Open reports/dashboard.pbix in Power BI Desktop"
      - "Use the screenshots in reports/screenshots/ as a preview of the pages"
