import requests
import json
from datetime import datetime

def get_ec2_price(region_code, instance_type, operating_system="Linux"):
    """
    Fetch EC2 pricing information using AWS Price List API
    """
    # AWS Price List API URL for EC2 pricing
    url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/{}/index.json".format(region_code)
    
    try:
        print(f"Fetching pricing data for {region_code}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        
        # Search through products and find matching instance
        for product_id, product in data.get('products', {}).items():
            attributes = product.get('attributes', {})
            
            # Check if this is the instance type we're looking for
            if (attributes.get('instanceType') == instance_type and
                attributes.get('operatingSystem', '').lower() == operating_system.lower()):
                
                # Get the price from the terms
                terms = data.get('terms', {}).get('OnDemand', {})
                for term_id, term_info in terms.items():
                    if term_id.startswith(product_id):
                        # Get the first price dimension (usually there's only one for on-demand)
                        for price_dim in term_info.values():
                            price_per_unit = float(list(price_dim['priceDimensions'].values())[0]['pricePerUnit']['USD'])
                            return price_per_unit
                            
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pricing data: {e}")
        return None

def calculate_monthly_cost(hourly_price, hours_per_month=730):
    """Calculate the monthly cost based on hourly price and usage."""
    if hourly_price is None:
        return None
    return hourly_price * hours_per_month

def format_price(price):
    """Format price with appropriate currency symbol and decimals."""
    if price is None:
        return "N/A"
    return f"${price:.3f}"

def main():
    # Define regions to check
    regions = {
        "us-east-1": "US East (N. Virginia)",
        "us-west-2": "US West (Oregon)",
        "eu-west-1": "EU (Ireland)",
        "ap-southeast-1": "Asia Pacific (Singapore)"
    }
    
    # Instance configuration
    instance_type = "t2.micro"
    operating_system = "Linux"
    
    print(f"\nEC2 Pricing Information")
    print(f"Instance Type: {instance_type}")
    print(f"Operating System: {operating_system}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 70)
    print(f"{'Region':<20} {'Region Name':<25} {'Hourly Rate':<12} {'Monthly Est.'}")
    print("-" * 70)
    
    for region_code, region_name in regions.items():
        hourly_price = get_ec2_price(region_code, instance_type, operating_system)
        monthly_cost = calculate_monthly_cost(hourly_price) if hourly_price else None
        
        print(f"{region_code:<20} {region_name:<25} {format_price(hourly_price):<12} {format_price(monthly_cost)}")

if __name__ == "__main__":
    main()