
# AI Usage:
# I used ChatGPT to help write and improve parts of this program.
# ChatGPT helped with pivot tables, input validation,
# monthly sales growth, and comparing two analytics.
# I reviewed the code and tested the program.

import pandas as pd
import ssl
import time


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context



def load_csv(filepath):
    """
    Load sales data from a CSV file.

    Parameters:
        filepath: The CSV file path or URL.

    Returns:
        A DataFrame, or None if loading fails.

    Test cases:
        1. Valid CSV file.
        2. Invalid file path.
        3. CSV with missing values.
    """

    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='skip')

        # Replace missing values with zero
        df = df.fillna(0)

        end_time = time.time()
        load_time = end_time - start_time

        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")

        # Display available columns
        print("\nAvailable columns:")
        print(list(df.columns))

        # Check required columns
        required_columns = [
            'sales_region',
            'order_type',
            'customer_state',
            'customer_type',
            'product_category',
            'quantity',
            'unit_price',
            'employee_id'
        ]

        missing_columns = [
            col for col in required_columns if col not in df.columns
        ]

        if missing_columns:
            print("\nWARNING: Missing required columns:")
            print(missing_columns)
            print("Some analytics may not work.")

        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None


def display_initial_rows(data):
   
    """
    Ask the user how many rows to display.

    Parameters:
        data: The sales DataFrame.

    Returns:
        None. Prints the selected rows.

    Test cases:
        1. Enter 5 to show five rows.
        2. Enter 'all' to show all rows.
        3. Enter invalid input like 'abc'.
        4. Enter 0 or a negative number.
    """

    while True:
        response = input(
            f"\nHow many initial rows would you like to see? "
            f"(1-{len(data)}, or 'all'): "
        ).strip().lower()

        if response == "all":
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid input '{response}'. Please enter a whole number or 'all'.")
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        print(data.head(num_rows))
        return


def show_employees_by_region(data):

    """
    Show the number of unique employees in each sales region.

    Parameters:
        data: The sales DataFrame.

    Returns:
        None. Prints the number of unique employees.

    Test cases:
        1. Use valid sales data.
        2. Check the employee count for each region.
        3. Use data with missing employee IDs.
    """
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())


def get_user_selection(options, prompt, required=False, single=False):
    
    """
    Ask the user to select options from a list.

    Parameters:
        options: A list of available choices.
        prompt: The message shown to the user.
        required: Whether a selection is required.
        single: Whether only one choice is allowed.

    Returns:
        A list of selected options.

    Test cases:
        1. Enter 1 to select one option.
        2. Enter 1,2 to select multiple options.
        3. Enter letters to test invalid input.
        4. Enter an invalid option number.
        5. Press Enter with no selection.
    """

    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected


def generate_custom_pivot_table(data):

    """
    Create a custom pivot table based on user selections.

    Parameters:
        data: The sales DataFrame.

    Returns:
        None. Displays a custom pivot table.

    Test cases:
        1. Select valid rows and values.
        2. Select optional columns.
        3. Test sum, mean, and count.
        4. Enter an invalid selection.
    """
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)


def show_average_sales_by_region(data):

    """
    Show average sales by region, state, and order type.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A pivot table with average sales.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check the average sales values.
    """
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))

    return pivot_table



def show_total_sales_by_region(data):

    """
    Show total sales by region and order type.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A pivot table with total sales.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check total sales for each region.
    """
    required = ["sales_region", "order_type", "quantity", "unit_price"]

    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", missing)
        return

    sales = data.copy()
    sales["total_sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        values="total_sales",
        index="sales_region",
        columns="order_type",
        aggfunc="sum",
        fill_value=0
    )

    
    print("\nTotal sales by region and order type:")
    print(pivot_table)
    return pivot_table



def show_sales_by_customer_type(data):
    """
    Show total sales by customer type, order type, and state.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A pivot table with total sales.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check the total sales values.
    """
    required = [
        "customer_state", "customer_type",
        "order_type", "quantity", "unit_price"
    ]

    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", missing)
        return

    sales = data.copy()
    sales["total_sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        values="total_sales",
        index=["customer_type", "order_type"],
        columns="customer_state",
        aggfunc="sum",
        fill_value=0
    )

    print("\nSales by customer type and order type by state:")
    print(pivot_table)


def show_sales_by_region_product(data):

    """
    Show total quantity and sales by region and product.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A pivot table with quantity and total sales.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check the total quantity and sales values.
    """
    required = ["sales_region", "produce_name", "quantity", "unit_price"]

    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", missing)
        return

    sales = data.copy()
    sales["total_sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index=["sales_region", "produce_name"],
        values=["quantity", "total_sales"],
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales quantity and price by region and product:")
    print(pivot_table)


def show_sales_by_customer_order_type(data):

    """
    Show total quantity and sales by customer type and order type.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A pivot table with quantity and total sales.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check the total quantity and sales values.
    """
    required = ["order_type", "customer_type", "quantity", "unit_price"]

    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", missing)
        return

    sales = data.copy()
    sales["total_sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index=["order_type", "customer_type"],
        values=["quantity", "total_sales"],
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales quantity and price by customer type:")
    print(pivot_table)


def show_max_min_sales_by_category(data):
    
    """
    Show maximum and minimum sales by product category.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A pivot table with maximum and minimum sales.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check the maximum and minimum sales values.
    """

    required = ["product_category", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", missing)
        return

   
    pivot_table = pd.pivot_table(
        data,
        index="product_category",
        values="unit_price",
        aggfunc=["max", "min"]
    )


    print("\nMax and min sales price by category:")
    print(pivot_table)
    return pivot_table

# AI Assistance: ChatGPT helped me calculate monthly sales growth.
# Prompt: "How can I calculate monthly sales growth using pandas?"
def show_monthly_sales_growth(data):

    """
    Show monthly sales and growth percentages.

    Parameters:
        data: The sales DataFrame.

    Returns:
        A table with monthly sales and growth rates.

    Test cases:
        1. Use valid sales data.
        2. Use data with a missing column.
        3. Check the monthly growth percentages.
    """
    required = ["order_date", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]

    if missing:
        print("Missing required columns:", missing)
        return None

    sales = data.copy()
    sales["order_date"] = pd.to_datetime(
    sales["order_date"],
    format="mixed",
    errors="coerce"
)   
    sales["quantity"] = pd.to_numeric(sales["quantity"], errors="coerce")
    sales["unit_price"] = pd.to_numeric(sales["unit_price"], errors="coerce")

    sales = sales.dropna(subset=["order_date"])
    if sales.empty:
        print("No valid dates available.")
        return None

    sales["total_sales"] = sales["quantity"] * sales["unit_price"]
    sales["month"] = sales["order_date"].dt.to_period("M")

    monthly = sales.pivot_table(
        index="month",
        values="total_sales",
        aggfunc="sum"
    ).sort_index()

    monthly["previous_month_sales"] = monthly["total_sales"].shift(1)
    monthly["growth_percent"] = (
        (monthly["total_sales"] - monthly["previous_month_sales"])
        / monthly["previous_month_sales"].replace(0, float("nan"))
        * 100
    )

    print("\nMonthly Sales Growth Analysis:")
    print(monthly.round(2))
    return monthly


# AI Assistance: ChatGPT helped me compare two pivot tables.
# Prompt: "How can I compare two sales analytics side by side?"
def compare_two_analytics(data):

    """
    Compare two sales analytics side by side.

    Parameters:
        data: The sales DataFrame.

    Returns:
        None. Prints a side-by-side comparison.

    Test cases:
        1. Enter 1,2 to compare two analytics.
        2. Enter 1,1 to test duplicate selections.
        3. Enter 1,3 to test an invalid selection.
        4. Enter letters to test invalid input.
    """

    analytics = (
        ("Total sales by region and order type", show_total_sales_by_region),
        ("Average sales by region", show_average_sales_by_region),
    )

    print("\nSelect two analytics to compare:")
    for number, (name, _) in enumerate(analytics, start=1):
        print(f"{number}. {name}")

    while True:
        choice = input("Enter two numbers separated by a comma (e.g., 1,2): ").strip()

        try:
            numbers = [int(x.strip()) for x in choice.split(",")]
        except ValueError:
            print("Invalid input. Please enter two numbers.")
            continue

        if len(numbers) != 2 or len(set(numbers)) != 2:
            print("Please select two different analytics.")
            continue

        if any(n < 1 or n > len(analytics) for n in numbers):
            print("Invalid selection. Please choose from the list.")
            continue

        break

    name1, function1 = analytics[numbers[0] - 1]
    name2, function2 = analytics[numbers[1] - 1]

    result1 = function1(data)
    result2 = function2(data)

    if result1 is None or result2 is None:
        print("Unable to compare the selected analytics.")
        return

    result1 = result1.copy()
    result2 = result2.copy()

    result1.columns = [str(col) for col in result1.columns]
    result2.columns = [str(col) for col in result2.columns]

    comparison = pd.concat(
        [result1, result2], 
        axis=1,
        keys=[name1, name2]
)

    print("\nSide-by-side comparison:")

    summary = pd.DataFrame({
    name1: result1.sum(axis=1),
    name2: result2.mean(axis=1)
})

    print(summary.round(2).to_string())
    

def exit_program(data=None):

    """
    Exit the sales dashboard program.

    Parameters:
        data: Optional sales DataFrame.

    Returns:
        None. Ends the program.

    Test cases:
        1. Select option 12 to exit.
        2. Check that the goodbye message appears.
    """

    print("Exiting the program. Goodbye!")
    raise SystemExit(0)

menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order_type", show_total_sales_by_region),
    ("Average sales by region, by state and sale type", show_average_sales_by_region),
    ("Sales by customer type and order type by state", show_sales_by_customer_type),
    ("Total sales quantity and price by region and product", show_sales_by_region_product),
    ("Total sales quantity and price by customer type", show_sales_by_customer_order_type),
    ("Max and min sales price by category", show_max_min_sales_by_category),
    ("Number of unique employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Compare two analytics side by side", compare_two_analytics),
    ("Monthly sales growth analysis", show_monthly_sales_growth),
    ("Exit the program", exit_program),
)

def display_menu():

    """
    Display the sales menu and get the user's choice.

    Parameters:
        None.

    Returns:
        The selected menu index.

    Test cases:
        1. Enter 1 to select the first option.
        2. Enter 12 to exit the program.
        3. Enter 13 to test an invalid option.
        4. Enter letters to test invalid input.
    """
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")


def main():

    """
    Run the sales dashboard program.

    Parameters:
        None.

    Returns:
        None.

    Test cases:
        1. Load a valid CSV file.
        2. Use an invalid CSV file path.
        3. Select a menu option.
        4. Exit the program.
    """

    csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA&export=download'    
    # csv_file = "junk.csv"  # Intentionally incorrect path to test error handling
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]
            action(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()