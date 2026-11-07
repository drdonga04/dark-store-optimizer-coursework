# 🏬 Chennai Dark Store Network Optimizer

An Operations Research (OR) and geospatial platform for quick-commerce dark store location-allocation, capacity planning, and multi-objective trade-off optimization in Chennai, India.

---

## 🌟 Key Features

- **Capacitated Facility Location (MIP)**: Solves location-allocation to optimality using the SCIP solver via Google OR-Tools with capacity constraints, service radius limits, and customer demand assignment.
- **Sensitivity Analysis & Pareto Frontier**: Explores trade-offs between fixed facility lease overhead and delivery transportation costs across facility limits ($P$).
- **Interactive Geospatial Intelligence**: Leaflet-based map with customer demand heatmaps, store markers, isochrones, coverage gap polygons, and camera lock-on.
- **Executive KPI Dashboard**: Metrics for Net Profit, Total Revenue, Operating Costs, Fixed Lease Costs, Transport Costs, Utilization, and an interactive Store Directory.
- **Dual Themes**: Complete Dark and Light mode styling across UI controls, maps, and Plotly charts.

---

## 📁 Project Structure

```text
├── app.py                     # Streamlit web application entrypoint
├── requirements.txt           # Python dependencies
├── src/                       # Core algorithms & mathematical models
│   ├── optimization_model.py  # OR-Tools SCIP MIP model & distance calculations
│   ├── sensitivity_analysis.py# Multi-scenario solver & Pareto frontier engine
│   ├── coverage_geometry.py   # Shapely coverage polygons & gap analysis
│   ├── data_validation.py     # CSV validation schemas & Chennai boundaries
│   └── routing_provider.py    # OpenRouteService road routing & isochrones
├── data/
│   └── examples/              # Pre-loaded customer & store example CSVs
├── sample_test_datasets/      # 8 pre-validated test pairs (15 to 10,000 customers)
├── benchmarks/                # Performance benchmarking scripts & results
├── tests/                     # Automated unit test suite (54 tests)
├── legacy/                    # Archived Cartesian prototype files
└── .streamlit/                # Streamlit UI & theme configuration
```

---

## 💻 Quickstart

### Prerequisites
- Python 3.10, 3.11, or 3.12

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/drdonga04/dark-store-optimizer.git
cd dark-store-optimizer

# Set up virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### 3. Run Automated Tests
```bash
python -m unittest discover -s tests -t . -v
```

---

## 🚀 Cloud Deployment

This app is configured for instant deployment on [Streamlit Community Cloud](https://share.streamlit.io):
- **Main file path**: `app.py`
- Continuous deployment is enabled: any push to the `main` branch automatically redeploys the live application.
- *(Optional)* Add `ORS_API_KEY = "your-api-key"` in **App Settings** -> **Secrets** for road routing features, or enter it directly in the sidebar.

---

## 📄 License
MIT License.
