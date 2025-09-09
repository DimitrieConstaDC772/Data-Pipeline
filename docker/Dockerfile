FROM apache/airflow:2.9.1

# Install git

# Switch to root to install OS-level packages
USER root

# Install git
RUN apt-get update && apt-get install -y git

# Switch back to airflow user for safety and compatibility
USER airflow

# Install other packages

# Base Packages
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Additional packages

COPY requirements_dbt.txt .

RUN pip install --no-cache-dir -r requirements_dbt.txt