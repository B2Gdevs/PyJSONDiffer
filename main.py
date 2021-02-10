import utils
import json
from collections.abc import Sequence




# POS came back POS
# NEG came back NEG
def are_equal(test, test_against):
    return hash(json.dumps(test)) == hash(json.dumps(test_against))


def recursive_search(test: dict or list, test_key_list: list, test_value_list: list) -> None:
    if isinstance(test, dict):
        for key, value in test.items():
            recursive_search(value, test_key_list, test_value_list)
            test_key_list.append(key)
    elif isinstance(test, list):
        for item in test:
            recursive_search(item, test_key_list, test_value_list)
    if not isinstance(test, (list, tuple, dict)):
            test_value_list.append(test)


def are_in_order(test_list: list, test_against_list: list) -> bool:
    for idx, item in enumerate(test_list):
        try:
            if item != test_against_list[idx]:
                return False
        except KeyError as e:
            return False

    return True


def perform_checks(test, test_against) -> bool:

    def print_status(test_results: dict, test_case: str):
        print(f"#{test_case}: SUCCESS") if test_results[test_case] else print(f"#{test_case}: FAILURE")

    test_key_list = []
    test_value_list = []
    test_against_key_list = []
    test_against_value_list = []
    test_results = {"TEST1": None,
                    "TEST2": None,
                    "TEST3": None,
                    "TEST4": None}

    print("=============== TESTING ===============")
    print("Recursively searching both jsons and building representation")
    recursive_search(test, test_key_list, test_value_list)
    recursive_search(test_against, test_against_key_list, test_against_value_list)
    print("Representation completed")

    print("\n=============== #Test1: Check if files are completely the same")
    test_case = "TEST1"
    test_results[test_case] = are_equal(test, test_against)
    print_status(test_results, test_case)

    print("\n=============== #Test2: Check if files have same structure")
    test_case = "TEST2"
    # the keys are the stepping stones.  If this comes back true then the keys are in the same order
    test_results[test_case] = are_in_order(test_key_list, test_against_key_list) 
    print_status(test_results, test_case)

    print("\n=============== #Test3: Check if files have same key data")
    test_case = "TEST3"
    # the keys are the stepping stones.  If this comes back true then the keys are in the same order
    test_results[test_case] = are_lists_equal(test_key_list, test_against_key_list) 
    print_status(test_results, test_case)

    print("\n=============== #Test4: Check if files have same value data")
    test_case = "TEST4"
    # the keys are the stepping stones.  If this comes back true then the keys are in the same order
    test_results[test_case] = are_lists_equal(test_value_list, test_against_value_list) 
    print_status(test_results, test_case)


def are_lists_equal(test_list: list, test_against_list: list) -> bool:
    if isinstance(test_list, list) and isinstance(test_against_list, list):
        test = sorted([str(x) for x in test_list])
        test_against = sorted([str(x) for x in test_against_list])
        return are_equal(test, test_against)
    else:
        raise ValueError("All arguments should be lists")


if __name__ == "__main__":

    test = utils.load_json("test1.json")
    test_against_neg = utils.load_json("test1_neg.json")
    test_against_pos = utils.load_json("test1_pos.json")

    # print(test_against_neg)
    perform_checks(test, test_against_pos)

    # print(test_key_list)
    # print(test_against_key_list)