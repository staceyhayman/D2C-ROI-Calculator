from dataclasses import dataclass

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
    print("Shop Campaign ROAS Calculator")
    print("-" * 30)
    
    # Get inputs
    revenue = float(input("Enter Total Revenue ($): "))
    ad_spend = float(input("Enter Ad Spend ($): "))
    new_buyer_share = float(input("Enter Share of New Buyers (%): "))
    discount_percentage = float(input("Enter Discount Percentage for New Buyers (%): "))
    
    # Create campaign and calculate ROAS
    campaign = Campaign(
        revenue=revenue,
        ad_spend=ad_spend,
        new_buyer_share=new_buyer_share,
        discount_percentage=discount_percentage
    )
    
    calculator = ROASCalculator()
    traditional_roas = calculator.calculate_traditional_roas(campaign)
    adjusted_roas = calculator.calculate_adjusted_roas(campaign)
    
    # Print results
    print("\nCost Breakdown:")
    print(f"- Ad Spend: ${campaign.ad_spend:.2f}")
    print(f"- New Buyer Ad Spend ({campaign.new_buyer_share:.1f}% share): ${campaign.ad_spend * (campaign.new_buyer_share/100):.2f}")
    print(f"- Discount Amount ({campaign.discount_percentage:.1f}% on new buyer spend): ${campaign.discount_amount:.2f}")
    print(f"- Total Cost: ${campaign.ad_spend + campaign.discount_amount:.2f}")
    
    print("\nROAS Comparison:")
    print(f"- Traditional ROAS (like Meta/Google): {traditional_roas:.2f}x")
    print(f"- Shop Campaign Adjusted ROAS: {adjusted_roas:.2f}x")

if __name__ == "__main__":
    main() 