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
    title: "Clone the repository"
    description: "Get a local copy of the project."
    instructions:
      - "Clone the repository to your local machine."
      - "Navigate into the project folder."
    commands:
      - "git clone https://github.com/yourusername/your-repo.git"
      - "cd your-repo"

  step_2:
    title: "Create your .env file"
    description: "Set up environment variables for local development."
    instructions:
      - "Copy the example `.env` file to create your own `.env`."
      - "Edit `.env` to add your local secrets paths and Airflow Fernet key."
    commands:
      - "cp .env.example .env"
      - "nano .env   # or open with your preferred editor to add secrets"

  step_3:
    title: "Start the environment with Docker"
    description: "Run the full containerized environment."
    instructions:
      - "Start Docker containers using docker-compose."
      - "Airflow webserver will be available at http://localhost:8080."
      - "DAGs will automatically load from the `dags/` folder."
      - "dbt models are mounted into the container and can be run inside Airflow tasks."
    commands:
      - "docker-compose up"

  step_4:
    title: "Power BI Dashboard"
    description: "Access the reporting dashboard."
    instructions:
      - "Open `reports/dashboard.pbix` in Power BI Desktop."
      - "Use the screenshots in `reports/screenshots/` as a preview of the dashboard pages."
    commands: []

  step_4:
    description: "Power BI Dashboard"
    instructions:
      - "Open reports/dashboard.pbix in Power BI Desktop"
      - "Use the screenshots in reports/screenshots/ as a preview of the pages"
