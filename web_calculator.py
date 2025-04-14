import streamlit as st
from dataclasses import dataclass
import plotly.graph_objects as go

@dataclass
class Campaign:
    revenue: float
    ad_spend: float
    new_buyer_share: float  # percentage of new buyers (0-100)
    discount_percentage: float  # discount percentage (0-100)
    
    @property
    def discount_amount(self) -> float:
        """Calculate total discount amount based on new buyer share"""
        new_buyer_ad_spend = self.ad_spend * (self.new_buyer_share / 100)
        return new_buyer_ad_spend * (self.discount_percentage / 100)
    
    @property
    def new_buyer_ad_spend(self) -> float:
        """Calculate ad spend attributed to new buyers"""
        return self.ad_spend * (self.new_buyer_share / 100)

class ROASCalculator:
    @staticmethod
    def calculate_traditional_roas(campaign: Campaign) -> float:
        if campaign.ad_spend == 0:
            return 0.0
        return campaign.revenue / campaign.ad_spend
    
    @staticmethod
    def calculate_adjusted_roas(campaign: Campaign) -> float:
        total_cost = campaign.ad_spend + campaign.discount_amount
        if total_cost == 0:
            return 0.0
        return campaign.revenue / total_cost

def create_cost_breakdown_chart(campaign: Campaign):
    # Create a waterfall chart showing cost breakdown
    fig = go.Figure(go.Waterfall(
        name="Cost Breakdown",
        orientation="v",
        measure=["relative", "relative", "total"],
        x=["Base Ad Spend", "New Buyer Discount", "Total Cost"],
        text=[f"${campaign.ad_spend:,.2f}", 
              f"${campaign.discount_amount:,.2f}", 
              f"${campaign.ad_spend + campaign.discount_amount:,.2f}"],
        y=[campaign.ad_spend, campaign.discount_amount, 0],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#EF553B"}},
        increasing={"marker": {"color": "#00CC96"}},
        totals={"marker": {"color": "#636EFA"}}
    ))
    
    fig.update_layout(
        title="Campaign Cost Breakdown",
        showlegend=False,
        height=400
    )
    
    return fig

def main():
    st.set_page_config(
        page_title="Shop Campaign ROAS Calculator",
        page_icon="💰",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stMetric {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("💰 Shop Campaign ROAS Calculator")
    st.markdown("""
    Compare ROAS between different advertising platforms while accounting for Shop Campaign's 
    unique discount structure for new buyers.
    """)
    
    # Create two columns for input and results
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("### 📊 Campaign Details")
        with st.form("campaign_form"):
            revenue = st.number_input(
                "Total Revenue ($)",
                min_value=0.0,
                value=1000.0,
                step=100.0,
                help="Total revenue generated from the campaign"
            )
            
            ad_spend = st.number_input(
                "Ad Spend ($)",
                min_value=0.0,
                value=500.0,
                step=50.0,
                help="Total amount spent on advertising"
            )
            
            st.markdown("#### 🆕 New Buyer Details")
            new_buyer_share = st.slider(
                "Share of New Buyers (%)",
                min_value=0.0,
                max_value=100.0,
                value=20.0,
                step=1.0,
                help="Percentage of buyers who are new customers"
            )
            
            discount_percentage = st.slider(
                "Discount Percentage for New Buyers (%)",
                min_value=0.0,
                max_value=100.0,
                value=20.0,
                step=1.0,
                help="Discount offered to new buyers"
            )
            
            submitted = st.form_submit_button("Calculate ROAS")
    
    if submitted or 'campaign' not in st.session_state:
        campaign = Campaign(
            revenue=revenue,
            ad_spend=ad_spend,
            new_buyer_share=new_buyer_share,
            discount_percentage=discount_percentage
        )
        st.session_state.campaign = campaign
    else:
        campaign = st.session_state.campaign
    
    calculator = ROASCalculator()
    traditional_roas = calculator.calculate_traditional_roas(campaign)
    adjusted_roas = calculator.calculate_adjusted_roas(campaign)
    
    with col2:
        st.markdown("### 📈 Results")
        
        # Display cost breakdown
        fig = create_cost_breakdown_chart(campaign)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display detailed metrics
        col2_1, col2_2 = st.columns(2)
        
        with col2_1:
            st.metric(
                "Traditional ROAS",
                f"{traditional_roas:.2f}x",
                help="Revenue / Ad Spend (Meta/Google method)"
            )
            st.metric(
                "New Buyer Ad Spend",
                f"${campaign.new_buyer_ad_spend:.2f}",
                f"{campaign.new_buyer_share:.1f}% of total spend"
            )
            
        with col2_2:
            st.metric(
                "Adjusted ROAS",
                f"{adjusted_roas:.2f}x",
                f"{((adjusted_roas - traditional_roas) / traditional_roas * 100):.1f}% vs Traditional",
                help="Revenue / (Ad Spend + Discount)"
            )
            st.metric(
                "Discount Amount",
                f"${campaign.discount_amount:.2f}",
                f"{campaign.discount_percentage:.1f}% on new buyer spend"
            )
    
    # Explanation section
    st.markdown("### 📝 Understanding the Results")
    st.markdown("""
    - **Traditional ROAS** shows how platforms like Meta and Google calculate returns, considering only the direct ad spend
    - **Adjusted ROAS** includes both ad spend and new buyer discounts, showing the true cost of customer acquisition
    - The difference between these metrics helps you make fair comparisons between advertising platforms
    """)

if __name__ == "__main__":
    main() 