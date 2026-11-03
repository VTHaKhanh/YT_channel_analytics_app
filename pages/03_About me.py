import streamlit as st

# Configure the page
st.set_page_config(page_title="About Me | Khanh Vu", page_icon="📊", layout="wide")

# Header Section
st.title("Khanh Vu")
st.subheader("Operational Data Analytics & Business Intelligence Professional")
st.write("📍 Berlin, Germany")

# Social and contact links
st.markdown("""
Contact me: [vutohakhanh@gmail.com](mailto:vutohakhanh@gmail.com) | 
 [LinkedIn Profile](https://www.linkedin.com/in/vutohakhanh)  
""")

st.divider()

# Summary
st.header("Summary")
st.info("""
Hi, I am a Operational Data Analytics and Business Intelligence professional with over 5 years of experience bridging technical data pipelines and executive decision-making. 
I have a proven track record of translating complex consumer and operational datasets into decision-ready insights using Power BI, SQL, Snowflake, Python, and Qlik Sense. 
My background includes hands-on experience establishing self-service analytics frameworks, funnel/NPS optimization, and partner-facing reporting for global enterprises (Kesko, ABB), as well as leading cross-functional test-and-learn initiatives to drive data-informed strategy.
I am passionate about leveraging data to uncover actionable insights, optimize business processes, and drive strategic decision-making. I thrive in collaborative environments where I can apply my analytical skills to solve complex business challenges and contribute to organizational growth.
As a lifelong learner, I continuously seek opportunities to expand my knowledge in data analytics, business intelligence, and emerging technologies. I am eager to connect with like-minded professionals and explore new opportunities to make a meaningful impact through data-driven decision-making.
""")

# Competencies
st.header("Competencies")

st.markdown("**Analytics & BI Tools:**")
st.write("Microsoft Power BI, SQL, Snowflake, Python, Qlik Sense, Excel")

st.markdown("**Data Engineering & Architecture:**")
st.write("ETL Data Pipelines, Snowflake Data Warehousing, SAP BW, Databricks, Data Modeling & Governance")

st.markdown("**Commercial & Operational Analytics:**")
st.write("Funnel Performance, E-Commerce & Digital Behavior, Voice of Customer (NPS), Campaign and Promotion Analysis, Supply Chain and Logistics, Financial Budgeting, Customer Segmentation, Workforce Analytics")

st.markdown("**Business Partnering & Leadership:**")
st.write("Translating Ambiguous Business Questions into KPI Frameworks, Data Storytelling, Cross-Functional Stakeholder Management")

st.divider()

# Professional Experience
st.header("Professional Experience")

# Kesko
st.subheader("Business Intelligence Analyst | Kesko Corporation")
st.caption("Sep 2022 – Jun 2026 | Helsinki, Finland")
st.markdown("""
* Technical owner of analytics domains across operational data including Digital Assisted Sales, E-Commerce, Customer Segmentation, Supply chain logistics and Finance within Finland’s leading €12B+ retail enterprise.
* Acted as the primary data and analytics contact between operational stakeholders and central IT/Data Engineering, translating ambiguous business objectives into structured KPI frameworks, ETL Data pipelines and semantic data models.
* Managed, maintained and optimized end-to-end data pipelines and modeled enterprise datasets (billions of transactional sales receipts, customers, stores, products and finance data) utilizing SQL, Snowflake, SAP BW, Databricks, Qlik Sense.
* Built, optimized, and maintained self-service analytics applications adopted by 150+ directors, managers, and specialists.
* Promoted the integration of Generative AI tools and automated SQL workflows into daily BI operations to accelerate data modeling, query optimization, and led the team to improve data governance and stakeholder engagement.
""")

# ABB Thesis
st.subheader("Master Thesis Researcher | ABB Group (Motion Division)")
st.caption("Jan 2022 – Sep 2022 | Helsinki, Finland")
st.markdown("""
* Promoted advanced analytics initiative within the Global Motion Service division to optimize B2B service sales using Salesforce CRM sales pipeline data.
* Developed and deployed a predictive machine learning classification model (LightGBM in Python) to evaluate win/loss probabilities across complex global service sales opportunities.
* Synthesized predictive model outputs into an interactive Microsoft Power BI self-service tool, providing global and regional sales managers with prescriptive recommendations to prioritize high-yield opportunities.
""")

# ABB Trainee
st.subheader("Global Operations Analyst Trainee | ABB Group")
st.caption("Dec 2019 – Jan 2022 | Helsinki, Finland")
st.markdown("""
* Collaborated with the Global Planning & Fulfillment leadership team to establish operational metric frameworks and automated reporting across the global value chain.
* Developed executive Power BI dashboards and automated data integration workflows across enterprise systems (SAP, Celonis process mining, Relex), reducing manual reporting overhead.
* Optimized data ETL pipeline and data models for operational and financial KPIs (Productivity, P&L, Customer care response, On-time deliveries, Manufacturing defects rate, inventory turnover).
* Recommended data-driven process improvements and trained global analytics dashboard users on utilizing self-service analytics for daily decision-making.
""")

st.divider()

# Education and Certifications
st.header("Education & Certifications")

st.markdown("Education")
st.markdown("""
**Master of Science (M.Sc.) in Economics and Business Administration**  
*Aalto University School of Business | Helsinki, Finland*  
Major: Strategy | Minor: Information Systems Management (ISM)

**Bachelor of Business Administration (BBA)**  
*Haaga-Helia University of Applied Sciences | Helsinki, Finland*
""")

st.write("") # Add a little vertical space for visual separation

st.markdown("Certifications & Badges")
st.markdown("""
* Azure AI Fundamentals (AI-900)
* Databricks Academy: Generative AI Fundamentals
* Lean Six Sigma: Yellow Belt Certification
""")