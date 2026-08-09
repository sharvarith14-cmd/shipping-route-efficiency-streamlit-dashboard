# ========================================
# NASSAU CANDY - STREAMLIT DASHBOARD
# ========================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Nassau Candy - Shipping Analysis",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ========== LOAD DATA ==========
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_shipping_data.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df['Route'] = df['Division'] + ' → ' + df['State/Province']
    return df

df = load_data()

# ========== TITLE ==========
st.title("🍬 Nassau Candy Distributor")
st.markdown("### Shipping Route Efficiency Analysis Dashboard")
st.markdown("---")

# ========== SIDEBAR FILTERS ==========
st.sidebar.header("📊 Filters")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['Order Date'].min().date(), df['Order Date'].max().date()),
    key="date_range"
)

# Region filter
selected_region = st.sidebar.multiselect(
    "Select Region(s)",
    options=sorted(df['Region'].unique()),
    default=sorted(df['Region'].unique()),
    key="region_filter"
)

# Ship mode filter
selected_ship_mode = st.sidebar.multiselect(
    "Select Ship Mode(s)",
    options=sorted(df['Ship Mode'].unique()),
    default=sorted(df['Ship Mode'].unique()),
    key="ship_mode_filter"
)

# Lead time threshold slider
lead_time_threshold = st.sidebar.slider(
    "Lead Time Threshold (Days)",
    min_value=0,
    max_value=int(df['Shipping Lead Time (Days)'].max()),
    value=7,
    key="threshold_slider"
)

# ========== APPLY FILTERS ==========
df_filtered = df[
    (df['Order Date'].dt.date >= date_range[0]) &
    (df['Order Date'].dt.date <= date_range[1]) &
    (df['Region'].isin(selected_region)) &
    (df['Ship Mode'].isin(selected_ship_mode))
].copy()

# ========== KEY METRICS (ROW 1) ==========
st.subheader("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Orders",
        len(df_filtered),
        delta=f"{len(df_filtered)} shipments"
    )

with col2:
    avg_lead = df_filtered['Shipping Lead Time (Days)'].mean()
    st.metric(
        "Avg Lead Time",
        f"{avg_lead:.1f} days",
        delta=f"Median: {df_filtered['Shipping Lead Time (Days)'].median():.1f}"
    )

with col3:
    delayed = (df_filtered['Shipping Lead Time (Days)'] > lead_time_threshold).sum()
    delay_pct = (delayed / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    st.metric(
        f"Delayed Orders (>{lead_time_threshold}d)",
        f"{delay_pct:.1f}%",
        delta=f"{delayed} orders"
    )

with col4:
    total_sales = df_filtered['Sales'].sum()
    st.metric(
        "Total Sales",
        f"${total_sales:,.0f}",
        delta="Revenue from shipments"
    )

st.markdown("---")

# ========== ROW 2: CHARTS ==========
st.subheader("📊 Performance Analysis")

col1, col2 = st.columns(2)

# Chart 1: Lead Time by Region
with col1:
    region_lead = df_filtered.groupby('Region')['Shipping Lead Time (Days)'].mean().sort_values(ascending=False)
    
    fig1 = px.bar(
        region_lead.reset_index(),