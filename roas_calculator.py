import streamlit as st
import pandas as pd
from dataclasses import dataclass
from typing import Optional

@dataclass
class Campaign:
    revenue: float
    ad_spend: float
    new_buyer_share: float  # percentage of new buyers (0-100)
    discount_percentage: float  # discount percentage (0-100)
    
    @property
    def discount_amount(self) -> float:
        """Calculate total discount amount based on new buyer share"""
        # Calculate ad spend attributed to new buyers
        new_buyer_ad_spend = self.ad_spend * (self.new_buyer_share / 100)
        # Calculate discount amount based on new buyer ad spend
        return new_buyer_ad_spend * (self.discount_percentage / 100)
    
class ROASCalculator:
    @staticmethod
    def calculate_traditional_roas(campaign: Campaign) -> float:
        """Calculate traditional ROAS (Revenue / Ad Spend)"""
        if campaign.ad_spend == 0:
            return 0.0
        return campaign.revenue / campaign.ad_spend
    
    @staticmethod
    def calculate_adjusted_roas(campaign: Campaign) -> float:
        """Calculate adjusted ROAS including discount (Revenue / (Ad Spend + Discount))"""
        total_cost = campaign.ad_spend + campaign.discount_amount
        if total_cost == 0:
            return 0.0
        return campaign.revenue / total_cost

def main():
    st.set_page_config(page_title="Shop Campaign ROAS Calculator", layout="wide")
    
    st.title("Shop Campaign ROAS Calculator")
    st.markdown("""
    This calculator helps compare ROAS (Return on Ad Spend) between different advertising platforms,
    accounting for Shop Campaign's unique discount structure for new buyers.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Campaign Details")
        revenue = st.number_input("Total Revenue ($)", min_value=0.0, value=1000.0, step=100.0)
        ad_spend = st.number_input("Ad Spend ($)", min_value=0.0, value=100.0, step=10.0)
        
        st.subheader("New Buyer Details")
        new_buyer_share = st.slider("Share of New Buyers (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
        discount_percentage = st.slider("Discount Percentage for New Buyers (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
        
        campaign = Campaign(
            revenue=revenue,
            ad_spend=ad_spend,
            new_buyer_share=new_buyer_share,
            discount_percentage=discount_percentage
        )
        
        calculator = ROASCalculator()
        traditional_roas = calculator.calculate_traditional_roas(campaign)
        adjusted_roas = calculator.calculate_adjusted_roas(campaign)
    
    with col2:
        st.subheader("ROAS Comparison")
        
        # Cost Breakdown
        st.markdown("### Cost Breakdown")
        st.markdown(f"""
        - Ad Spend: ${campaign.ad_spend:.2f}
        - New Buyer Ad Spend (based on {campaign.new_buyer_share:.1f}% share): ${campaign.ad_spend * (campaign.new_buyer_share/100):.2f}
        - Discount Amount ({campaign.discount_percentage:.1f}% on new buyer spend): ${campaign.discount_amount:.2f}
        - Total Cost: ${campaign.ad_spend + campaign.discount_amount:.2f}
        """)
        
        # Traditional ROAS
        st.metric(
            label="Traditional ROAS (like Meta/Google)",
            value=f"{traditional_roas:.2f}x",
            help="Traditional ROAS = Revenue / Ad Spend"
        )
        
        # Adjusted ROAS
        st.metric(
            label="Shop Campaign Adjusted ROAS",
            value=f"{adjusted_roas:.2f}x",
            help="Adjusted ROAS = Revenue / (Ad Spend + Discount Amount)"
        )
        
        # Difference explanation
        st.markdown("### Why the difference?")
        st.markdown("""
        - **Traditional ROAS** (used by Meta/Google) only considers direct ad spend in the denominator
        - **Shop Campaign Adjusted ROAS** includes both ad spend and new buyer discounts, providing a more
          accurate picture of total campaign cost
        - The discount is only applied to the portion of ad spend attributed to new buyers
        - This adjusted ROAS helps make fair comparisons between different advertising platforms by
          accounting for upfront discounts in Shop Campaigns
        """)

if __name__ == "__main__":
    main() 