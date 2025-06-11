from collections import defaultdict


def sharedAccounts(customerAccounts):
    # Build customer -> accounts mapping
    cust_to_acct = defaultdict(set)
    for cust, acct in customerAccounts:
        cust_to_acct[cust].add(acct)

    # Group customers by their account sets using frozenset as key
    account_groups = defaultdict(list)
    for cust, accounts in cust_to_acct.items():
        key = frozenset(accounts)
        account_groups[key].append(cust)

    # Collect groups with multiple customers and sort
    result = []
    for _, customers in account_groups.items():
        if len(customers) > 1:
            result.append(sorted(customers))

    return sorted(result)


if __name__ == "__main__":
    customerAccounts = [
        ("1", "10"),
        ("1", "11"),
        ("2", "13"),
        ("3", "11"),
        ("4", "14"),
        ("3", "10"),
        ("4", "13"),
    ]
    print(sharedAccounts(customerAccounts))
