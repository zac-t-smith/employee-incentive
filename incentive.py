import streamlit as st

# Set Page Config
st.set_page_config(page_title="Incentive Plan Calculator", page_icon="💼", layout="wide")

# App Title
st.markdown("<h1 style='color:firebrick;'>Incentive Plan Calculator</h1>", unsafe_allow_html=True)
st.markdown("""
This tool helps calculate incentives for team members based on the *Best Option Restoration of Baldwin County* incentive plan.
""")
st.markdown("---")

# Sidebar Inputs
st.sidebar.header("📋 Input Job Details")

job_revenue = st.sidebar.text_input("Job Revenue ($)", value="0.00", key="job_revenue").strip()
gp_margin = st.sidebar.text_input("Gross Profit Margin (%)", value="0.0", key="gp_margin").strip()
referral_jobs = st.sidebar.text_input("Number of Jobs from Referral Source", value="0", key="referral_jobs").strip()
quarterly_revenue = st.sidebar.text_input(
    "Quarterly Revenue from Referral Jobs ($)",
    value="0.00",
    key="quarterly_revenue"
).strip()

# Helper to Convert Inputs to Float/Int
try:
    job_revenue = float(job_revenue)
    gp_margin = float(gp_margin)
    referral_jobs = int(referral_jobs)
    quarterly_revenue = float(quarterly_revenue)
except ValueError:
    st.sidebar.error("Please enter valid numbers.")

# Add Clarifications
st.sidebar.markdown("""
---
**Clarifications:**
- "Quarterly Revenue from Referral Jobs" includes all referred jobs' revenue, including the current "Job Revenue."
- Incentives will dynamically calculate as you update inputs.
""")

# Calculations
st.markdown("<h2 style='color:midnightblue;'>📊 Incentive Breakdown</h2>", unsafe_allow_html=True)

# 1. Commission Based on GP
if gp_margin >= 78:
    gp_commission_rate = 0.15
elif gp_margin >= 70:
    gp_commission_rate = 0.10
elif gp_margin >= 55:
    gp_commission_rate = 0.065
else:
    gp_commission_rate = 0.05
gp_commission = gp_commission_rate * (job_revenue * gp_margin / 100)

st.markdown("**1. Commission Based on Gross Profit:**")
st.markdown(f"  - **Rate:** `{gp_commission_rate * 100:.1f}%`")
st.markdown(f"  - **Amount:** `${gp_commission:,.2f}`")

# 2. High-Value Job Bonus
high_value_bonus = 0.01 * (job_revenue * gp_margin / 100) if job_revenue > 20000 else 0
st.markdown("**2. High-Value Job Bonus:**")
st.markdown(f"  - **Amount:** `${high_value_bonus:,.2f}`")

# 3. Referral Source Bonus
referral_bonus = 250 if referral_jobs >= 3 else 0
st.markdown("**3. Referral Source Bonus:**")
st.markdown(f"  - **Amount:** `${referral_bonus:,.2f}`")

# 4. Quarterly Revenue Milestone Bonus
milestone_bonus = (quarterly_revenue // 50000) * 1000
st.markdown("**4. Quarterly Revenue Milestone Bonus:**")
st.markdown(f"  - **Amount:** `${milestone_bonus:,.2f}`")

# Total Incentive Calculation
total_incentive = gp_commission + high_value_bonus + referral_bonus + milestone_bonus
st.markdown("---")
st.markdown("<h2 style='color:firebrick;'>💰 Total Incentive Earned</h2>", unsafe_allow_html=True)
st.markdown(f"### **${total_incentive:,.2f}**")
st.markdown("---")

# Explanation Section
st.markdown("<h2 style='color:midnightblue;'>📝 How the Calculator Works</h2>", unsafe_allow_html=True)
st.markdown("""
### **Commission Based on Gross Profit**
- **5% of GP** for all referred jobs.
- **6.5% of GP** for jobs with 55-70% GP margin.
- **10% of GP** for jobs with GP margins above 70%.
- **15% of GP** for jobs with GP margins above 78%.

### **High-Value Job Bonus**
- **1% of GP** for jobs exceeding $20,000 in revenue.

### **Referral Source Bonus**
- **$250** for each new referral source generating at least 3 jobs in a quarter.

### **Quarterly Revenue Milestone Bonus**
- **$1,000** bonus for every $50,000 in quarterly referred revenue.

This plan incentivizes team members to focus on high-margin jobs and leverage their networks effectively.
""")

# Footer
st.markdown("---")
st.caption("© 2024 Best Option Restoration of Baldwin County | Incentive Plan Calculator")
