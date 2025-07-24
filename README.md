# NYC Vehicle Collisions Analysis

This project explores traffic collision data in New York City to uncover trends, contributing factors, and high-risk locations. The analysis includes both statistical summaries and visualizations to better understand when, where, and why collisions occur.

---

## **Dataset**

- **Source:** [NYC Open Data – Motor Vehicle Collisions – Crashes](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)
- **Size:** 2.1M+ records (2012–2025)
- **Note:**  
  The original CSV file exceeds GitHub's 100 MB limit, so it is not uploaded here.  
  **Download Link:** [Click here to download the dataset](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)

---

## **Key Insights**

- **Injuries vs. Fatalities:** Over **711,999 injuries** compared to **3,434 fatalities**, highlighting the need for better road safety measures.
- **Peak Collision Years:** Highest crashes between 2016–2018, with a notable decline during 2020 (pandemic effect).
- **Day vs. Night:** About **70% of crashes happen during the day**, when traffic volume is higher.
- **Boroughs with Most Collisions:** **Brooklyn and Queens** dominate collision counts, while Staten Island has the fewest.
- **Top Contributing Factors:** "Driver Inattention/Distraction" and "Failure to Yield" are leading causes of collisions.
- **High-Risk Streets:** Roads like **Broadway, Atlantic Avenue, and Belt Parkway** rank highest for crashes.

---

## **Visualizations**

### **1. Crashes by Year (Trend)**
![Crashes by Year](Images/crashes_by_year.png)

### **2. Crashes by Borough**
![Crashes by Borough](Images/crashes_by_borough.png)

### **3. Total Injuries vs Fatalities (Log Scale)**
![Injuries vs Fatalities](Images/injuries_vs_fatalities_log.png)

### **4. Top 10 Contributing Factors**
![Top 10 Contributing Factors](Images/top_10_contributing_factors.png)

### **5. Top 10 Streets & Cross Streets**
![Top 10 Streets and Cross Streets](Images/top_10_streets_cross_streets.png)

### **6. Crash Severity by Borough**
![Crash Severity by Borough](Images/crash_severity_by_borough.png)

---

## **Interactive Heatmap**

An **interactive heatmap** is included to visualize crash density across NYC.  
Open this file in your browser: **`nyc_crashes_heatmap_with_boroughs.html`**

---

## **Tech Stack**

- **Languages:** Python (Pandas, NumPy)
- **Visualization:** Matplotlib, Seaborn, Folium (for interactive maps)
- **Tools:** Jupyter Notebook, Git/GitHub

---

## **Future Improvements**

- Add predictive modeling to forecast crash hotspots.
- Integrate weather and traffic data for deeper insights.
- Create a web dashboard (e.g., Streamlit) to interactively explore trends.

---

## **Author**

**Oscar Holguin Silva**  
[LinkedIn Profile](https://www.linkedin.com/in/yashuasspear-oscar-holguin-silva/)  
#SoldiersInTech

---
