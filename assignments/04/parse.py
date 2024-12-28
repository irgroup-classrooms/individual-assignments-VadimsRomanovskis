import re
from collections import Counter


def main():
    # Read the CSV file with the product orders
    with open('C:/Users/User1/Desktop/DataModelling/individual-assignments-VadimsRomanovskis/assignments/04/csv/orders.csv') as f_in:
        text = f_in.read()

    # 1. Extract all order numbers
    order_numbers = re.findall(r'Order #\d+', text)
    print("Order Numbers:", order_numbers)

    # 2. Extract all product names
    product_names = re.findall(r'Product: ([a-zA-Z\s]+),', text)
    print("Product Names:", product_names)

    # 3. Extract all prices
    prices = re.findall(r'Price: \$(\d+\.\d{2})', text)
    print("Prices:", prices)

    # 4. Extract all order dates
    dates = re.findall(r'Date: (\d{4}-\d{2}-\d{2})', text)
    print("Order Dates:", dates)

    # 5. Find all orders for products priced over $500
    expensive_orders = [match.group(0) for match in re.finditer(r'Order #\d+: .*?Price: \$(\d+\.\d{2})', text) if float(match.group(1)) > 500]
    print("Orders Priced Over $500:", expensive_orders)

    # 6. Change the date format to DD/MM/YYYY
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in dates]
    print("Formatted Dates (DD/MM/YYYY):", formatted_dates)

    # 7. Extract product names that have more than 6 characters
    long_product_names = [name for name in product_names if len(name) > 6]
    print("Product Names with More Than 6 Characters:", long_product_names)

    # 8. Count the occurrence of each product
    product_count = Counter(product_names)
    print("Product Occurrences:", product_count)

    # 9. Extract the orders with prices ending in .99
    orders_with_99_prices = [match.group(0) for match in re.finditer(r'Order #\d+: .*?Price: \$(\d+\.99)', text)]
    print("Orders with Prices Ending in .99:", orders_with_99_prices)

    # 10. Find the cheapest product
    min_price = min(map(float, prices))
    cheapest_product = next(match.group(0) for match in re.finditer(r'Order #\d+: .*?Price: \$(\d+\.\d{2})', text) if float(match.group(1)) == min_price)
    print("Cheapest Product:", cheapest_product)


if __name__ == '__main__':
    main()
