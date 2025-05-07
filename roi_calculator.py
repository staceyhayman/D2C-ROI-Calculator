import streamlit as st
import pandas as pd
from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum

class GrowthScenario(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

@dataclass
class MerchantMetrics:
    annual_gmv: float
    aov: float
    annual_transactions: int
    profit_margin: float  # as percentage
    ad_spend: float
    retargeting_budget_allocation: float  # as percentage
    retargeting_cpa: float
    prospecting_cpa: float
    ltv: float
    payments_profile_online: float  # as percentage
    orders_on_payments: float  # as percentage
    current_conversion_rate: float  # as percentage
    shop_pay_usage: float  # as percentage

@dataclass
class UpgradeMetrics:
    checkout_customization_cost: Dict[GrowthScenario, float]
    checkout_upsell_cost: Dict[GrowthScenario, float]
    plus_support_cost: Dict[GrowthScenario, float]
    audiences_cost: Dict[GrowthScenario, float]

class ROICalculator:
    def __init__(self, merchant_metrics: MerchantMetrics, upgrade_metrics: UpgradeMetrics):
        self.merchant_metrics = merchant_metrics
        self.upgrade_metrics = upgrade_metrics

    def calculate_checkout_customization_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Checkout Customization with API"""
        conversion_increase = {
            GrowthScenario.LOW: 0.01,  # 1%
            GrowthScenario.MEDIUM: 0.03,  # 3%
            GrowthScenario.HIGH: 0.05  # 5%
        }
        
        new_conversion_rate = self.merchant_metrics.current_conversion_rate * (1 + conversion_increase[scenario])
        additional_orders = self.merchant_metrics.annual_transactions * conversion_increase[scenario]
        revenue_impact = additional_orders * self.merchant_metrics.aov
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'Conversion Rate Increase': f"{conversion_increase[scenario] * 100:.1f}%",
            'New Conversion Rate': f"{new_conversion_rate:.2f}%",
            'Additional Orders': f"{additional_orders:,.0f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

    def calculate_checkout_upsell_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Checkout Upsell with 3P apps"""
        aov_increase = {
            GrowthScenario.LOW: 0.05,  # 5%
            GrowthScenario.MEDIUM: 0.10,  # 10%
            GrowthScenario.HIGH: 0.20  # 20%
        }
        
        new_aov = self.merchant_metrics.aov * (1 + aov_increase[scenario])
        revenue_impact = self.merchant_metrics.annual_transactions * (new_aov - self.merchant_metrics.aov)
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'AOV Increase': f"{aov_increase[scenario] * 100:.1f}%",
            'New AOV': f"${new_aov:.2f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

    def calculate_plus_support_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Plus Support Help"""
        conversion_increase = {
            GrowthScenario.LOW: 0.005,  # 0.5%
            GrowthScenario.MEDIUM: 0.01,  # 1%
            GrowthScenario.HIGH: 0.015  # 1.5%
        }
        
        new_conversion_rate = self.merchant_metrics.current_conversion_rate * (1 + conversion_increase[scenario])
        additional_orders = self.merchant_metrics.annual_transactions * conversion_increase[scenario]
        revenue_impact = additional_orders * self.merchant_metrics.aov
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'Conversion Rate Increase': f"{conversion_increase[scenario] * 100:.1f}%",
            'New Conversion Rate': f"{new_conversion_rate:.2f}%",
            'Additional Orders': f"{additional_orders:,.0f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

    def calculate_audiences_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Increased Retargeting with Audiences"""
        conversion_increase = {
            GrowthScenario.LOW: 0.02,  # 2%
            GrowthScenario.MEDIUM: 0.04,  # 4%
            GrowthScenario.HIGH: 0.06  # 6%
        }
        
        new_conversion_rate = self.merchant_metrics.current_conversion_rate * (1 + conversion_increase[scenario])
        additional_orders = self.merchant_metrics.annual_transactions * conversion_increase[scenario]
        revenue_impact = additional_orders * self.merchant_metrics.aov
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'Conversion Rate Increase': f"{conversion_increase[scenario] * 100:.1f}%",
            'New Conversion Rate': f"{new_conversion_rate:.2f}%",
            'Additional Orders': f"{additional_orders:,.0f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

    def calculate_shop_pay_conversion_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Increased Conversion with Shop Pay"""
        conversion_increase = {
            GrowthScenario.LOW: 0.03,  # 3%
            GrowthScenario.MEDIUM: 0.05,  # 5%
            GrowthScenario.HIGH: 0.07  # 7%
        }
        
        new_conversion_rate = self.merchant_metrics.current_conversion_rate * (1 + conversion_increase[scenario])
        additional_orders = self.merchant_metrics.annual_transactions * conversion_increase[scenario]
        revenue_impact = additional_orders * self.merchant_metrics.aov
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'Conversion Rate Increase': f"{conversion_increase[scenario] * 100:.1f}%",
            'New Conversion Rate': f"{new_conversion_rate:.2f}%",
            'Additional Orders': f"{additional_orders:,.0f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

    def calculate_shop_pay_aov_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Increased AOV with Shop Pay"""
        aov_increase = {
            GrowthScenario.LOW: 0.05,  # 5%
            GrowthScenario.MEDIUM: 0.10,  # 10%
            GrowthScenario.HIGH: 0.20  # 20%
        }
        
        new_aov = self.merchant_metrics.aov * (1 + aov_increase[scenario])
        revenue_impact = self.merchant_metrics.annual_transactions * (new_aov - self.merchant_metrics.aov)
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'AOV Increase': f"{aov_increase[scenario] * 100:.1f}%",
            'New AOV': f"${new_aov:.2f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

    def calculate_non_shop_pay_conversion_impact(self, scenario: GrowthScenario) -> Dict:
        """Calculate impact of Increased Conversion without Shop Pay influence"""
        conversion_increase = {
            GrowthScenario.LOW: 0.01,  # 1%
            GrowthScenario.MEDIUM: 0.02,  # 2%
            GrowthScenario.HIGH: 0.03  # 3%
        }
        
        new_conversion_rate = self.merchant_metrics.current_conversion_rate * (1 + conversion_increase[scenario])
        additional_orders = self.merchant_metrics.annual_transactions * conversion_increase[scenario]
        revenue_impact = additional_orders * self.merchant_metrics.aov
        margin_impact = revenue_impact * (self.merchant_metrics.profit_margin / 100)
        
        return {
            'Conversion Rate Increase': f"{conversion_increase[scenario] * 100:.1f}%",
            'New Conversion Rate': f"{new_conversion_rate:.2f}%",
            'Additional Orders': f"{additional_orders:,.0f}",
            'Revenue Impact': f"${revenue_impact:,.2f}",
            'Margin Impact': f"${margin_impact:,.2f}"
        }

def create_growth_summary_table(calculator: ROICalculator) -> pd.DataFrame:
    """Create the Growth from Upgrading summary table"""
    data = {
        'Feature': [
            'Checkout Customization with API',
            'Checkout Upsell with 3P apps',
            'Plus Support Help',
            'Increased Retargeting with Audiences',
            'Increased Conversion with Shop Pay',
            'Increased AOV with Shop Pay',
            'Increased Conversion without Shop Pay'
        ],
        'Low Growth': [
            f"${float(calculator.calculate_checkout_customization_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_checkout_upsell_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_plus_support_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_audiences_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_shop_pay_conversion_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_shop_pay_aov_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_non_shop_pay_conversion_impact(GrowthScenario.LOW)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}"
        ],
        'Medium Growth': [
            f"${float(calculator.calculate_checkout_customization_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_checkout_upsell_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_plus_support_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_audiences_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_shop_pay_conversion_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_shop_pay_aov_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_non_shop_pay_conversion_impact(GrowthScenario.MEDIUM)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}"
        ],
        'High Growth': [
            f"${float(calculator.calculate_checkout_customization_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_checkout_upsell_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_plus_support_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_audiences_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_shop_pay_conversion_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_shop_pay_aov_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}",
            f"${float(calculator.calculate_non_shop_pay_conversion_impact(GrowthScenario.HIGH)['Margin Impact'].replace('$', '').replace(',', '')):,.2f}"
        ]
    }
    return pd.DataFrame(data)

def main():
    st.set_page_config(page_title="Merchant ROI Calculator", layout="wide")
    
    st.title("Merchant ROI Calculator")
    st.markdown("""
    This calculator helps estimate the ROI of upgrading your merchant plan based on various growth scenarios.
    """)

    # Input section
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Merchant Metrics")
        merchant_metrics = MerchantMetrics(
            annual_gmv=st.number_input("Annual GMV ($)", min_value=0.0, value=1000000.0, step=10000.0),
            aov=st.number_input("Average Order Value ($)", min_value=0.0, value=70.0, step=1.0),
            annual_transactions=st.number_input("Annual Number of Transactions", min_value=0, value=35000, step=1000),
            profit_margin=st.number_input("Profit Margin (%)", min_value=0.0, max_value=100.0, value=15.0, step=0.1),
            ad_spend=st.number_input("Ad Spend ($)", min_value=0.0, value=50000.0, step=1000.0),
            retargeting_budget_allocation=st.number_input("Retargeting Budget Allocation (%)", min_value=0.0, max_value=100.0, value=15.0, step=1.0),
            retargeting_cpa=st.number_input("Retargeting CPA ($)", min_value=0.0, value=75.0, step=1.0),
            prospecting_cpa=st.number_input("Prospecting CPA ($)", min_value=0.0, value=100.0, step=1.0),
            ltv=st.number_input("LTV ($)", min_value=0.0, value=200.0, step=1.0),
            payments_profile_online=st.number_input("Payments Profile Online (%)", min_value=0.0, max_value=100.0, value=100.0, step=1.0),
            orders_on_payments=st.number_input("Orders on Payments (%)", min_value=0.0, max_value=100.0, value=100.0, step=1.0),
            current_conversion_rate=st.number_input("Current Conversion Rate (%)", min_value=0.0, max_value=100.0, value=3.0, step=0.1),
            shop_pay_usage=st.number_input("Shop Pay Usage (%)", min_value=0.0, max_value=100.0, value=40.0, step=1.0)
        )

    with col2:
        st.subheader("Upgrade Costs")
        upgrade_metrics = UpgradeMetrics(
            checkout_customization_cost={
                GrowthScenario.LOW: st.number_input("Checkout Customization Cost - Low ($)", min_value=0.0, value=125.0, step=10.0),
                GrowthScenario.MEDIUM: st.number_input("Checkout Customization Cost - Medium ($)", min_value=0.0, value=378.75, step=10.0),
                GrowthScenario.HIGH: st.number_input("Checkout Customization Cost - High ($)", min_value=0.0, value=650.19, step=10.0)
            },
            checkout_upsell_cost={
                GrowthScenario.LOW: st.number_input("Checkout Upsell Cost - Low ($)", min_value=0.0, value=1531.25, step=100.0),
                GrowthScenario.MEDIUM: st.number_input("Checkout Upsell Cost - Medium ($)", min_value=0.0, value=3062.50, step=100.0),
                GrowthScenario.HIGH: st.number_input("Checkout Upsell Cost - High ($)", min_value=0.0, value=6125.00, step=100.0)
            },
            plus_support_cost={
                GrowthScenario.LOW: st.number_input("Plus Support Cost - Low ($)", min_value=0.0, value=16.13, step=1.0),
                GrowthScenario.MEDIUM: st.number_input("Plus Support Cost - Medium ($)", min_value=0.0, value=70.95, step=1.0),
                GrowthScenario.HIGH: st.number_input("Plus Support Cost - High ($)", min_value=0.0, value=408.50, step=1.0)
            },
            audiences_cost={
                GrowthScenario.LOW: st.number_input("Audiences Cost - Low ($)", min_value=0.0, value=68.0, step=1.0),
                GrowthScenario.MEDIUM: st.number_input("Audiences Cost - Medium ($)", min_value=0.0, value=898.0, step=10.0),
                GrowthScenario.HIGH: st.number_input("Audiences Cost - High ($)", min_value=0.0, value=2746.0, step=100.0)
            }
        )

    # Calculate results
    calculator = ROICalculator(merchant_metrics, upgrade_metrics)
    
    # Display Growth Summary Table
    st.markdown("## Growth from Upgrading")
    growth_summary_df = create_growth_summary_table(calculator)
    st.dataframe(growth_summary_df, hide_index=True)

    # Display individual feature impact tables
    st.markdown("## Feature Impact Analysis")
    
    # Checkout Customization with API
    st.markdown("### Checkout Customization with API")
    checkout_customization_data = {
        'Metric': list(calculator.calculate_checkout_customization_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_checkout_customization_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(checkout_customization_data), hide_index=True)

    # Checkout Upsell with 3P apps
    st.markdown("### Checkout Upsell with 3P apps")
    checkout_upsell_data = {
        'Metric': list(calculator.calculate_checkout_upsell_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_checkout_upsell_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(checkout_upsell_data), hide_index=True)

    # Plus Support Help
    st.markdown("### Plus Support Help")
    plus_support_data = {
        'Metric': list(calculator.calculate_plus_support_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_plus_support_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(plus_support_data), hide_index=True)

    # Increased Retargeting with Audiences
    st.markdown("### Increased Retargeting with Audiences")
    audiences_data = {
        'Metric': list(calculator.calculate_audiences_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_audiences_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(audiences_data), hide_index=True)

    # Increased Conversion with Shop Pay
    st.markdown("### Increased Conversion with Shop Pay")
    shop_pay_conv_data = {
        'Metric': list(calculator.calculate_shop_pay_conversion_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_shop_pay_conversion_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(shop_pay_conv_data), hide_index=True)

    # Increased AOV with Shop Pay
    st.markdown("### Increased AOV with Shop Pay")
    shop_pay_aov_data = {
        'Metric': list(calculator.calculate_shop_pay_aov_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_shop_pay_aov_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(shop_pay_aov_data), hide_index=True)

    # Increased Conversion without Shop Pay
    st.markdown("### Increased Conversion without Shop Pay")
    non_shop_pay_data = {
        'Metric': list(calculator.calculate_non_shop_pay_conversion_impact(GrowthScenario.MEDIUM).keys()),
        'Value': list(calculator.calculate_non_shop_pay_conversion_impact(GrowthScenario.MEDIUM).values())
    }
    st.dataframe(pd.DataFrame(non_shop_pay_data), hide_index=True)

if __name__ == "__main__":
    main() 