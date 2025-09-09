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

# Setup Instructions

---

## 1️⃣ Clone the repository

**Description:** Get a local copy of the project.

**Instructions:**
- Clone the repository to your local machine.
- Navigate into the project folder.

**Commands:**
```bash
git clone https://github.com/DimitrieConstaDC772/Data-Pipeline.git
cd your-repo
```

## 2️⃣ Create your `.env` file

**Description:** Set up environment variables for local development.

**Instructions:**
- Copy the example `.env` file to create your own `.env`.
- Edit `.env` to add your local secrets paths and Airflow Fernet key.

**Commands:**
```bash
cp .env.example .env
nano .env
```

## 3️⃣ Start the environment with Docker

**Description:** Run the full containerized environment.

**Instructions:**
- Start Docker containers using docker-compose.
- Airflow webserver will be available at [http://localhost:8080](http://localhost:8080).
- DAGs will automatically load from the `dags/` folder.
- dbt models are mounted into the container and can be run inside Airflow tasks.

**Commands:**
```bash
docker-compose up
```

## 4️⃣ Power BI Dashboard

**Description:** Access the reporting dashboard.

**Instructions:**
- Open `reports/dashboard.pbix` in Power BI Desktop.
- Use the screenshots in `reports/screenshots/` as a preview of the dashboard pages.

**Commands:**  
_None_


