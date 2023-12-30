# This is a simulation designed to showcase stock type settlement and 
# this is the very first exercise of the workbook

from collections import deque

def runSimulation():
    holdings = deque()
    totalRealized = 0
    currentPosition = 0
    cumulativeCashFlow = 0
    tradeSummary = []

    while True:
        try:
            currentPrice = float(input("What is the current stock price: "))
            intention = input("Would you like to sell or purchase: ")
            quantity = float(input(f"How much would you like to {intention}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if intention not in ["sell", "purchase"]:
            print("Invalid intention. Please enter 'sell' or 'purchase'.")
            continue

        if intention == "sell":
            currentPosition -= quantity
            while quantity > 0 and holdings:
                holdingsPrice, holdingsQuantity = holdings.popleft()
                tradeQuantity = min(quantity, holdingsQuantity)
                holdingsQuantity -= tradeQuantity
                quantity -= tradeQuantity
                realizedProfit = tradeQuantity * (currentPrice - holdingsPrice)
                totalRealized += realizedProfit
                if holdingsQuantity > 0:
                    holdings.appendleft((holdingsPrice, holdingsQuantity))
        else:
            currentPosition += quantity
            holdings.append((currentPrice, quantity))

        cashflow = -currentPrice * quantity if intention == "purchase" else currentPrice * quantity
        cumulativeCashFlow += cashflow

        tradeSummary.append({
            'Price': currentPrice,
            'Position': currentPosition,
            'Cash Flow': cumulativeCashFlow,
            'Realized': totalRealized,
            'Intention': intention,
            'Quantity': quantity
        })

        if input("Continue simulation? (yes/no): ").lower() != 'yes':
            break

    print("\nSimulation Summary:")
    for i, trade in enumerate(tradeSummary, 1):
        print(f"\nTrade {i}:")
        for key, value in trade.items():
            print(f"{key}: {value}")

    totalUnrealized = sum((currentPrice - price) * quantity for price, quantity in holdings)
    totalCumulative = totalUnrealized + totalRealized
    print(f"\nFinal Summary:\nPosition: {currentPosition}, "
          f"Cash Flow: {cumulativeCashFlow}, Realized: {totalRealized}, "
          f"Unrealized: {totalUnrealized}, Cumulative: {totalCumulative}")

if __name__ == "__main__":
    runSimulation()
