# ClickWatch-Webtraffic-detector

ClickWatch is a real-time web traffic analytics solution that captures, processes, and visualizes user behavior across your product pages. Built on Microsoft Fabric with Event Hubs, Delta Lake, and PySpark, this solution helps product teams measure interest in new ideas before investing heavily.

🚀 Features
📊 Real-time user tracking (session, browser, OS, clicks, time spent)

🔁 Return visitor tracking using session and user ID

🎯 Conversion tracking (CTA clicks, form submissions)

📥 Streaming ingestion via Azure Event Hub

🧪 Behavioral event analysis: scroll, click, hover, submit

🌐 UTM and traffic source attribution

💡 Built-in Power BI Dashboard (Fabric report ready)

📂 Project Structure
text
Copy
Edit
📁 clickwatch/
├── wentraffic.json              # Sample 100 user session JSONs
├── silverlayer_clickwatch.py    # PySpark pipeline for Silver Layer in Fabric
├── clickwatch_product_report.pbix # Power BI report for visualization
└── README.md
🛠️ Tech Stack
Component	Description
🧱 Microsoft Fabric	Unified data architecture (Lakehouse + Report)
🔄 Azure Event Hub	Streaming data ingestion layer
🐍 PySpark	Transformations and aggregations
🐘 Delta Lake	Storage and silver/gold layer representation
📊 Power BI	Frontend visualization (clickwatch report)

📈 Data Flow
User event data is streamed via Event Hub (webtraffic in namespace orderstatus)

Fabric ingests events into Bronze table

silverlayer_clickwatch.py cleans and flattens the data

Final tables (final_cookies, visit_count) are created in Delta Lake

Power BI reads from Silver/Gold tables for analysis
