# python-plp-week-3


# Discounted Items Calculator

A simple Python application that calculates the final price of an item after applying a discount. The app allows the user to input the original price and the discount percentage. If the discount is 20% or higher, it applies the discount; otherwise, it returns the original price.

## Features

* **Price Calculation** : Computes the final price after applying the discount.
* **Discount Check** : Verifies that the discount is not negative and applies it only if it's 20% or higher.
* **User-friendly Interface** : Simple prompts to enter the original price and discount percentage.

## Requirements

* Python 3.x

## Installation

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/Silas-Hakuzwimana/python-plp-week-3.git
   ```
2. **Navigate to the project directory** :

```bash
   cd python-plp-week-3
```

1. **Run the application** :

```bash
   python discounted_items_calculator.py
```

## How It Works

1. The user is prompted to enter the **original price** of an item and the  **discount percentage** .
2. If the discount percentage is  **20% or higher** , the app calculates the final price after applying the discount.
3. If the discount percentage is  **less than 20%** , the app simply returns the original price.
4. If the user enters a  **negative discount** , the app notifies the user that the discount cannot be negative.

## Example Run

```
Discounted Items Calculator

Enter the original price: 100
Enter the discount for this item: 25
You're given a discount of 25.0%, you'll pay 75.00 RWF
```

```
Discounted Items Calculator

Enter the original price: 100
Enter the discount for this item: 15
You're not discounted, you'll pay 100.00 RWF
```

## Contributing

Feel free to fork this repository, submit issues, or open pull requests for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.
