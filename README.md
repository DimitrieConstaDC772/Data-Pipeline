# End-to-End Data Pipeline and Dashboard Project

This repository showcases a complete data workflow that includes **Python ETL scripts**, **Airflow orchestration**, **dbt transformations**, **Docker containerization**, and a **Power BI dashboard** for visualization.

---

## 📁 Project Structure
-
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

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/DimitrieConstaDC772/Data-Pipeline.git
cd your-repo


2. Create your .env file
Copy .env.example and fill in your local paths and Airflow Fernet key:

cp .env.example .env
# Then edit .env to add your local secrets paths and Fernet key

3. Start the environment with Docker

docker-compose up


Airflow webserver will be available at http://localhost:8080.

DAGs will automatically load from dags/.

dbt models are mounted into the container and can be run inside Airflow tasks.

4. Power BI Dashboard

Open reports/dashboard.pbix in Power BI Desktop.

Use the screenshots in reports/screenshots/ as a preview of the pages
