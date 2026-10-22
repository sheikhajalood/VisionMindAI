# VisionMindAI
# VisionMind AI 🧠
### An AI Business Co-Pilot for Smart Retail using Computer Vision

**Computer Vision • Business Intelligence • Actionable Decisions**

VisionMind AI is a student project focused on developing an AI-powered business co-pilot for smart retail. It aims to transform computer vision observations and retail business data into meaningful insights, explainable recommendations, and intelligent business decisions.

Instead of simply displaying data, the long-term goal is to help retailers understand what is happening in their stores, why it matters, and what actions they could take.

## 🎯 Project Objectives

- Analyze retail sales data to understand revenue, product performance, and sales trends.
- Use computer vision to detect and track people in retail video footage.
- Develop footfall analysis to understand customer movement and store visits.
- Combine visual observations with business context to generate actionable insights.
- Explore forecasting and AI-powered recommendations to support business decision-making.

## 💡 Key Features

### 1. Sales Analytics
- Process sales data from CSV files.
- Calculate total revenue and units sold.
- Summarize product-wise performance.
- Generate daily revenue reports and visualizations.

### 2. Computer Vision
- Detect people in video footage using YOLO.
- Track detected people across video frames.
- Develop entry and exit event counting using a virtual line.

### 3. Business Insights
- Identify high-revenue products.
- Generate basic business insights from sales summaries.
- Build toward explainable recommendations based on sales performance and computer vision observations.

### 4. AI Business Co-Pilot — Planned Development
- Integrate computer vision observations with retail business data.
- Explore customer activity and sales trend analysis.
- Develop forecasting and AI-assisted decision support.
- Investigate queue monitoring and store occupancy analysis.
- Generate recommendations with clear reasoning and relevant business context.

## 🛠️ Technology Stack

- **Programming Language:** Python 3.10
- **Computer Vision:** OpenCV, Ultralytics YOLO
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## 🏗️ System Workflow

1. **Data Input:** Retail sales CSV files and video footage.
2. **Data Processing:** Analyze sales records and process video frames.
3. **Computer Vision Analysis:** Detect and track people and develop footfall event counting.
4. **Business Intelligence:** Summarize product performance and revenue trends.
5. **Decision Support:** Progress toward connecting observations with business context to generate explainable recommendations.

The complete integrated co-pilot workflow is a development goal; not all stages have been implemented or validated yet.

## 📂 Project Structure

```text
VisionMindAI/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── sales_analytics.py
│   ├── business_insights.py
│   ├── detect_objects.py
│   ├── detect_video.py
│   ├── track_people.py
│   ├── footfall_counter.py
│   └── inspect_doorway.py
├── tests/
├── docs/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above describes the intended/current project organization; individual files and outputs may evolve during development.*

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible Python environment
- Git
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/sheikhajalood/VisionMindAI.git
cd VisionMindAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows Command Prompt:**

```bat
.venv\Scripts\activate.bat
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the sales analytics pipeline

```bash
python main.py
```

This runs the current sales analytics and basic business insights workflow, provided the required dependencies and input CSV are available.

**Note:** Video processing scripts may require a separate input video and model weights. Their execution depends on the script configuration and available files.

## 📊 Current Implementation Status

### Implemented or demonstrated

- Sales CSV processing and product-wise summaries.
- Daily revenue reporting and chart generation.
- Basic business insights from sales results.
- Initial YOLO-based people detection and tracking development.
- Preliminary footfall event-counting implementation.

### In progress

- Validating footfall counting accuracy.
- Improving tracking consistency and entry/exit detection.
- Testing with suitable retail video footage.
- Strengthening the connection between visual observations and business insights.

### Planned

- Integrating computer vision and business analytics into one workflow.
- Forecasting and more advanced decision support.
- AI-generated, explainable business recommendations.
- Queue and occupancy analysis.

Features are not considered complete merely because code exists; testing and validation are needed to establish reliability.

## 🔮 Future Scope

VisionMind AI aims to evolve into a practical retail decision-support system that helps business owners interpret store activity, understand business performance, identify potential issues, and evaluate recommended actions.

Future development will focus on improving model reliability, integrating data sources, and generating recommendations supported by observable evidence and business context.

## 👩‍💻 Project Team

- Sheikha V
- Mohammed Rizwan N.K
- Nandhana K
- Revath Kishor K

**Department of Computer Science and Engineering**  
Vidya Academy of Science & Technology, Thrissur, Kerala

## 📌 Project Status

**Academic Project — Phase 1 Development**

This repository documents the ongoing development of VisionMind AI. Implementation details, evaluation results, and project capabilities will be updated as development and validation progress.

---

*VisionMind AI — Turning computer vision observations into intelligent business decisions.*
