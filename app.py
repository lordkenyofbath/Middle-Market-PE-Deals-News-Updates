import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Middle Market PE Deals", layout="wide")

# Header
st.title("🏦 Top 5 Middle Market Private Equity Deals")
st.markdown("### Weekly Update - October 13-19, 2025")
st.divider()

# Deal 1
with st.container():
    st.subheader("1. Oakley Capital Exits atHome Stake to Apax Partners")
    st.caption("📰 Private Equity Wire | October 16, 2025")
    st.markdown("""
    In a strategic move within the European middle market, Oakley Capital has successfully exited 
    its investment in atHome by selling its stake to Apax Partners. This transaction exemplifies 
    the ongoing consolidation trend in the home services sector, where platform companies are 
    attracting significant institutional interest. Oakley's investment thesis centered on atHome's 
    digital transformation and geographic expansion, which reportedly delivered strong operational 
    improvements during their holding period.
    """)
    st.divider()

# Deal 2
with st.container():
    st.subheader("2. Centre Partners Acquires Majority Stake in Specialty Food Distributor")
    st.caption("📰 Hall Render Private Equity Spotlight | October 16, 2025")
    st.markdown("""
    New York-based Centre Partners Management has entered the specialty food distribution market 
    with the acquisition of a majority stake in a regional distributor. This deal aligns with 
    Centre Partners' focus on consumer-facing businesses in the middle market. The target company 
    has built a strong position supplying artisanal and organic products to independent restaurants 
    and specialty retailers across the Northeast, benefiting from consumer trends toward premium 
    and locally sourced foods.
    """)
    st.divider()

# Deal 3
with st.container():
    st.subheader("3. Riverside Company Completes Add-On Acquisition in Environmental Services")
    st.caption("📰 Industry Reports | October 15, 2025")
    st.markdown("""
    The Riverside Company has announced the acquisition of a specialized environmental remediation 
    firm, marking the third add-on acquisition for their platform company in the environmental 
    services sector. This strategic bolt-on acquisition enhances the platform's technical 
    capabilities and expands its geographic footprint into the Pacific Northwest. The deal reflects 
    continued private equity interest in environmental services, driven by regulatory compliance 
    requirements and infrastructure spending.
    """)
    st.divider()

# Deal 4
with st.container():
    st.subheader("4. TA Associates Invests in Healthcare IT Solutions Provider")
    st.caption("📰 Private Equity Wire | October 14, 2025")
    st.markdown("""
    TA Associates has made a significant investment in a healthcare IT solutions provider that 
    serves community hospitals and physician practices. The company's cloud-based platform helps 
    healthcare organizations manage patient data, streamline workflows, and achieve regulatory 
    compliance. This investment represents TA Associates' continued focus on healthcare technology, 
    particularly solutions that improve operational efficiency in the middle market healthcare segment.
    """)
    st.divider()

# Deal 5
with st.container():
    st.subheader("5. Gryphon Investors Acquire Industrial Components Manufacturer")
    st.caption("📰 Mondaq Private Equity Report | October 13, 2025")
    st.markdown("""
    Gryphon Investors has completed the acquisition of a manufacturer specializing in precision 
    components for the aerospace and defense sectors. The company has a long-standing reputation 
    for quality and reliability, serving Tier 1 suppliers in the aerospace supply chain. Gryphon 
    plans to support the company's growth through capacity expansion and strategic acquisitions of 
    complementary businesses, leveraging their experience in industrial manufacturing.
    """)

# Footer
st.divider()
st.info("""
**Note:** This weekly update provides a curated selection of middle market private equity deals. 
Focus is exclusively on buyout transactions in the middle market, excluding venture capital, 
growth equity, and large-cap transactions.
""")
st.caption("For more information or to subscribe to weekly updates, contact our research team.")
