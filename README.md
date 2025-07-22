# ClickWatch-Webtraffic-detector

|Author| Platform|
|------|----------|
|Vignesan Saravanan|YouTube: https://www.youtube.com/@vijaquick|


**ClickWatch** is a real-time web traffic analytics solution that captures, processes, and visualizes user behavior across your product pages. Built on Microsoft Fabric with Event Hubs, Delta Lake, and PySpark, this solution helps product teams measure interest in new ideas before investing heavily.

![ClickWatch Preview](https://github.com/Vijaquick/ClickWatch-Webtraffic-detector/blob/main/clickwatch%20preview.png)

---

## 🚀 Features

- 📊 Real-time user tracking (session, browser, OS, clicks, time spent)
- 🔁 Return visitor tracking using session and user ID
- 🎯 Conversion tracking (CTA clicks, form submissions)
- 📥 Streaming ingestion via Azure Event Hub
- 🧪 Behavioral event analysis: scroll, click, hover, submit
- 🌐 UTM and traffic source attribution
- 💡 Built-in Power BI Dashboard (Fabric report ready)

---

## 📂 Project Structure

📁 clickwatch/
- ├── wentraffic.json # Sample 100 user session JSONs
- ├── silverlayer_clickwatch.py # PySpark pipeline for Silver Layer in Fabric
- ├── clickwatch_product_report.pbix # Power BI report for visualization
- └── README.md


---

## 🛠️ Tech Stack

| Component         | Description                                     |
|------------------|-------------------------------------------------|
| 🧱 Microsoft Fabric | Unified data architecture (Lakehouse + Report) |
| 🔄 Azure Event Hub | Streaming data ingestion layer                  |
| 🐍 PySpark          | Transformations and aggregations                |
| 🐘 Delta Lake       | Storage and silver/gold layer representation   |
| 📊 Power BI         | Frontend visualization (ClickWatch report)     |

---

## 📈 Data Flow

1. **User event data** is streamed via Event Hub (`webtraffic` in namespace `orderstatus`)
2. **Fabric** ingests raw JSON into the Bronze table
3. `silverlayer_clickwatch.py` cleans, flattens, and prepares Silver layer
4. Delta Lake stores cleaned tables like `final_cookies`, `visit_count`
5. **Power BI** connects via DirectLake to visualize metrics in real time

---


