if __package__:
    from . import log
else:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import CalculatorTool as ct
    import CalculatorTool.log as log

logger = log.logging.getLogger('CalculatorTool.main')

if __package__:
    import importlib

    ct = importlib.import_module(__package__)
def main():
    # Example usage of the CalculatorTool package
    try:
        result_add = ct.add(10, 5, 3)
        print(f"Addition Result: {result_add}")

        result_sub = ct.sub(10, 5, 3)
        print(f"Subtraction Result: {result_sub}")

        result_mul = ct.mul(10, 5, 3)
        print(f"Multiplication Result: {result_mul}")

        result_div = ct.div(10, 2)
        print(f"Division Result: {result_div}")

        result_percentage = ct.percentage(200, 15)
        print(f"Percentage Result: {result_percentage}")

        result_mean = ct.mean(10, 20, 30)
        print(f"Mean Result: {result_mean}")

        result_c_to_f = ct.celsius_to_fahrenheit(25)
        print(f"Celsius to Fahrenheit: {result_c_to_f}")

        result_f_to_c = ct.fahrenheit_to_celsius(77)
        print(f"Fahrenheit to Celsius: {result_f_to_c}")

    except Exception as e:
        logger.error(f"An error occurred in main: {e}")

    # 1. Handling Division by Zero
    try:
        result=  ct.div(10, 0)
    except ZeroDivisionError as e:
            print(f"Caught expected error: {e}")
            
        # 2. Handling Custom InvalidOperationError
    try:
            result= ct.percentage(150, -5)
    except ValueError as e:
            print(f"Caught expected custom error: {e}")
            
        # 3. Handling Incorrect Data Types
    try:
            result=     ct.add("ten", 5)
    except TypeError as e:
            print(f"Caught expected type error: {e}")
            
        # 4. Handling Invalid Values (Statistics/Empty list)
    try:
            result= ct.mean([])
    except ValueError as e:
            print(f"Caught expected value error: {e}")    

if __name__ == "__main__":
    main()