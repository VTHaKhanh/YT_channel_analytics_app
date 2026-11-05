import streamlit as st

# Configure the page
st.set_page_config(page_title="About Me | Khanh Vu", page_icon="📊", layout="wide")

# Header Section
st.title("Khanh Vu")
st.subheader("Commercial, Marketing & Operational Data Analytics and BI Professional")
st.write("📍 Berlin, Germany")

# Social and contact links
st.markdown("""
Contact me: [vutohakhanh@gmail.com](mailto:vutohakhanh@gmail.com) | 
[LinkedIn Profile](https://www.linkedin.com/in/vutohakhanh) | 
[Data Analysis Work Example](https://ytchannelanalyticsapp.streamlit.app/)
""")

st.divider()

# Summary
st.header("Summary")
st.info("""
I am a Commercial, marketing and Operational Data Analytics and Business Intelligence professional with almost 7 years of experience translating complex data into actionable recommendations for stakeholders at all levels of organizations including senior leadership. 

I have a proven track record of translating complex operational, marketing, supply chain, digital consumer behavior, e-commerce and commercial data into decision-ready insights using Snowflake, Databricks, Qlik sense, Power BI, advanced SQL, and Python in global HQ/international matrix environment (Kesko, ABB Group) with hands-on experience in establishing scalable self-service analytics, KPI frameworks. I partner across the organization to align requirement, apply AI to continuously improve business, marketing investment and resource allocation.
""")

# Competencies
st.header("Competencies")

st.markdown("**Analytics & Business Intelligence BI Tools:**")
st.write("Qlik sense, Microsoft Power BI, SQL, Python, Databricks, Snowflake, Celonis process mining, SAP BW, Excel.")

st.markdown("**Operational Analytics:**")
st.write("Commercial and Digital Marketing Analytics, Customers Funnel Performance, E-Commerce Sales & Digital Behavior, Customer Lifetime Value (CLV), Retention and Churn, Voice of Customer (NPS), Marketing and Campaign ROI, Test-and-Learn / A/B Testing, Customer Care Response Process, Product Analytics, Pricing & Promotion Analysis, Customer Segmentation, Financial Analytics and Budgeting, Supply Chain Logistics Analytics, Customer Reclamation, Productivity and Workforce, Health Safety and Sustainability.")

st.markdown("**Data Engineering & Architecture:**")
st.write("ETL/ELT Data Pipelines, Snowflake Cloud Data Warehousing, SAP ERP (MM,SD,PP), Databricks, Data Modeling, Star schema, Data Governance and Documentation.")

st.markdown("**Business Partnering & Leadership & Tools:**")
st.write("AI (Claude), Github and Git workflow, Jira and Confluence, Cross-Functional Stakeholder Management, Leading cross-functional initiatives, Translating Ambiguous and Complex Business Questions/processes into aligned KPI Frameworks, Data Storytelling, Promoting data governance and responsible AI usage.")

st.divider()

# Professional Experience
st.header("Professional Experience")

# Kesko
st.subheader("Business Intelligence Analyst - Commercial, E-Commerce & Grocery Trade Analytics | Kesko Corporation")
st.caption("Sep 2022 – Jun 2026 | Helsinki, Finland")
st.markdown("""
- Kesko is among the largest operators in trading sector in Northern Europe, and is Finland’s leading €12B+ retail enterprise. I work for its Grocery trade division under Data and Business Intelligence organization, directly collaborate with operational stakeholders in Marketing, Supply Chain Logistic, Finance business stakeholders and Data Engineer, central IT teams to drive analytics initiatives.
- Act as the technical owner of analytics applications and solutions across key operational and strategic domains such as Marketing and Digital targets, Digital Assisted Sales via online web stores and mobile application, Digital customer behavior, E-Commerce and Customer Segmentation, B2B Customer reclamation, Supply chain logistics on-time deliveries and Turnover rates, Financial budgeting and targets.
- Act as the bridge between commercial, business, marketing, operational stakeholders and central IT/Data Engineering team, translating business objectives into structured KPI frameworks, data pipelines, data models and self-service analytics solutions, constantly improve and communicate releases, insights toward users across organization.
- Manage end-to-end ETL/ELT data pipelines, understand, own, model and improve enterprise datasets (billions of transactional sales receipts, product SKUs, customer segmentation) utilizing advanced SQL, Snowflake, SAP BW, Qlik Sense and Power BI.
- Build and maintain 100+ self-service analytics applications adopted by business stakeholders at all levels of organizations including marketing, finance, supply chain and operational specialists and leaders.
- Suggest on improvements towards operational business domain by actively involve in strategic projects on digital consumer behavior, funnel performance, Voice of Customer (NPS), marketing ROI, resource allocation and customer purchasing journeys.
- Actively work on knowledge sharing, promote and advocate integration of Generative AI tools and automated SQL workflows into daily BI operations to accelerate documentation, data modeling, query optimization, and dashboard delivery.
""")

# ABB Trainee
st.subheader("Global Operations Analyst Trainee | ABB Group (Motion / System Drives Division)")
st.caption("Dec 2019 – Jan 2022 | Helsinki, Finland")
st.markdown("""
- Build, maintain and constantly improve executive Motion Global Division analytical dashboards and reports in Microsoft Power BI to minimize downtime, improve ETL backend data pipeline for monthly and weekly business steering group at regional and global operational levels (360 degree operational KPIs and dashboard across Financial, Workforce, Customer, Productivity figures).
- Collaborate with the Global Planning & Fulfillment leadership team to align operational KPI metric frameworks and automated reporting across the global value chain using ERP systems such as Relex, Celonis process mining tool, SAP BW to reduce manual reporting overhead and improve data quality.
- Promote improvement and data-first culture across global and regional operation by organizing end-users’ updates and platforms for communications towards analytical workflows and data topics.
- Closely monitor operational KPIs and targets, recommend data-driven process improvements, and train international business users on utilizing self-service analytics for daily decision-making.
""")

# ABB Thesis
st.subheader("Master Thesis Researcher - Advanced Analytics & Salesforce Sales Pipeline Strategy | ABB Group")
st.caption("Jan 2022 – Sep 2022 | Helsinki, Finland")
st.markdown("""
- Promoted advanced analytics initiative within the Global Motion Service division to optimize B2B service sales using Salesforce CRM sales pipeline data.
- Researched on improvements towards service sales process and pipelines using commercial and pricing data, open, closed sales opportunities, and customer CRM data.
- Developed and deployed a predictive machine learning classification model (LightGBM in Python) to evaluate win/loss probabilities across complex global service sales opportunities.
- Synthesized predictive model outputs into an interactive Power BI self-service tool, providing regional and global sales teams with prescriptive recommendations to prioritize high-yield opportunities.
""")

st.divider()

# Education and Certifications
st.header("Certifications & Badges")
st.markdown("""
- Microsoft Azure AI Fundamentals (AI-900)
- Databricks Academy: Generative AI Fundamentals
- Lean Six Sigma: Yellow Belt Certification (Operational excellence, Continuous Improvement Project)
""")

st.write("") # Add a little vertical space for visual separation

st.header("Education")
st.markdown("""
**Master of Science (M.Sc.) in Economics and Business Administration**  
*Aalto University | Helsinki, Finland*  
Major: Strategy | Minor: Information Systems Management (ISM)

**Bachelor of Business Administration (BBA)**  
*Haaga-Helia University of Applied Sciences | Helsinki, Finland*
""")