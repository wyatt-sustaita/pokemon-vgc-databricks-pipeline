# Pokémon VGC Team Builder Pipeline (Databricks)

This project builds a **data engineering pipeline and recommendation system** for competitive Pokémon VGC team building.

Using **Databricks, Apache Spark, and Delta Lake**, the pipeline ingests Pokémon metadata from PokéAPI and tournament team compositions from competitive VGC events. The processed data is used to analyze team synergy and generate AI-powered team recommendations.

---

## Project Goals

Competitive Pokémon team building often relies on analyzing **meta trends and team synergies**. This project demonstrates how a **modern data engineering pipeline** can ingest competitive data, transform it into structured datasets, and apply machine learning to identify common team compositions.

The system can:

- Analyze historical tournament teams
- Identify Pokémon that frequently appear together
- Suggest teammates based on competitive trends
- Generate teams for Pokémon with little tournament usage using similarity analysis

---

## Architecture
PokéAPI + Tournament Data
│
▼
Ingestion
(Databricks)
│
▼
Bronze Layer (Raw Data)
│
▼
Silver Layer (Cleaned Data)
│
▼
Gold Layer (Feature Engineering)
│
▼
Recommendation Model


The pipeline follows the **Databricks Medallion Architecture**:

| Layer | Description |
|------|-------------|
| Bronze | Raw ingestion from APIs and scraped tournament data |
| Silver | Cleaned and normalized Pokémon and team datasets |
| Gold | Feature engineered datasets for analytics and ML |

---

## Data Sources

### PokéAPI

Pokémon metadata including:

- base stats
- abilities
- types
- moves

API endpoint:
https://pokeapi.co/api/v2/pokemon/

---

### VGC Tournament Results

Competitive team compositions scraped from tournament standings.

Example source:
https://www.pokedata.ovh/standings/VGC/

This provides real-world competitive team data including:

- player rankings
- tournament teams
- Pokémon usage

---

## Data Pipeline

### Step 1 — Ingest Pokémon Metadata

Pokémon data is retrieved from PokéAPI and stored in **Delta Lake Bronze tables**.

Fields include:

- Pokémon name
- stats
- types
- abilities
- height / weight

---

### Step 2 — Ingest Tournament Team Data

Tournament pages are scraped to extract team compositions.

Teams are normalized into a relational dataset:

| team_id | pokemon |
|--------|---------|
| 1 | Flutter Mane |
| 1 | Urshifu |
| 1 | Amoonguss |

---

### Step 3 — Data Cleaning (Silver Layer)

Data is standardized and joined with Pokémon metadata.

Example cleaned dataset:

| team_id | pokemon | type | speed |
|--------|---------|------|------|
| 1 | flutter_mane | ghost | 135 |

---

### Step 4 — Feature Engineering (Gold Layer)

Features are prepared for machine learning models including:

- Pokémon types
- stats
- tournament usage frequency
- team composition relationships

---

## Recommendation System

The system builds a **team recommendation engine** using two approaches.

---

### Association Rule Mining (Team Synergy)

Frequent itemset mining identifies Pokémon that commonly appear on the same team.

Example rule:
Flutter Mane → Iron Hands
confidence: 0.71

This indicates that **71% of teams containing Flutter Mane also include Iron Hands**.

The model is implemented using **Spark ML FP-Growth**.

---

### Similarity-Based Team Building

For Pokémon with limited tournament data, recommendations are generated using **similarity scoring** based on:

- base stats
- typing
- abilities
- roles

Example:
Ceruledge ≈ Chandelure ≈ Gengar

The system then analyzes teams built around similar Pokémon.

---

## Example Output

Input:
Flutter Mane

Recommended teammates:
Iron Hands
Urshifu
Tornadus
Amoonguss
Landorus

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| Databricks | Data engineering platform |
| Apache Spark | Distributed data processing |
| Delta Lake | Lakehouse storage layer |
| Python | Data ingestion and transformation |
| BeautifulSoup | Web scraping tournament data |
| PokéAPI | Pokémon metadata |
| Spark ML | Team synergy modeling |

---

## Repository Structure
pokemon-vgc-databricks-pipeline

README.md
requirements.txt

notebooks/
01_ingest_pokeapi.py
02_ingest_tournament_data.py
03_transform_pokemon.py
04_build_team_dataset.py
05_feature_engineering.py

src/
pokeapi_client.py
tournament_scraper.py
data_cleaning.py

config/
pipeline_config.yaml

---

## Future Improvements

Planned enhancements include:

- Automated tournament scraping pipeline
- Graph-based Pokémon synergy analysis
- Streamlit dashboard for team building
- MLflow experiment tracking
- Real-time meta analysis

---

## Example Use Cases

This system can be used to:

- analyze VGC competitive trends
- explore Pokémon team synergies
- build competitive team suggestions
- demonstrate scalable data engineering pipelines

---

## License

This project is for educational and portfolio purposes. Pokémon data is sourced from public APIs and tournament websites.
