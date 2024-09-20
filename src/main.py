from data_loader import load_car_problems
from collection_manager import get_collection, add_to_collection
from generate_response import get_solution


def main():
    car_problems = load_car_problems('data/car_problems.json')
    collection = get_collection("car_problems")
    add_to_collection(collection, car_problems)

    print("""
🚗 Welcome to the Car Diagnostics Assistant! 🚗

I'm here to help you diagnose car issues and provide solutions based on your car's error codes and symptoms.

**Here are some example questions you can ask:**
- What does P0300 mean?
- Why is my engine misfiring randomly?
- My engine is shaking. What could be causing this?
- What does error code P0171 mean regarding fuel mixture?
- What does it mean if I see error code P0420?
- I'm getting error P0700, what should I do?
- My car is having trouble shifting gears. What could be wrong?
- What does it mean if my transmission fluid is low?
- How does a faulty mass airflow sensor affect my car's performance?
- My car has poor fuel economy and rough idling, what could be the problem?

💡 **Tip**: For the best results, provide a specific error code or detailed description of the problem.

If you would like to exit, please type 'q'.
    """)
    print("-" * 50)

    user_query = input("Question: ").strip()

    while user_query.lower() != 'q':
        response = get_solution(collection, user_query)

        if response:
            print("\nResponse:")
            print(response)
            print("-" * 50)

        user_query = input("Question: ").strip()

    print("Thank you for using the Car Diagnostics Assistant! Have a great day!")


if __name__ == "__main__":
    main()
