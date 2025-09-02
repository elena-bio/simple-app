def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Mini calculator (add/sub)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add two integers")
    p_add.add_argument("a", type=int)
    p_add.add_argument("b", type=int)

    p_sub = sub.add_parser("sub", help="Subtract two integers")
    p_sub.add_argument("a", type=int)
    p_sub.add_argument("b", type=int)

    args = parser.parse_args()

    if args.cmd == "add":
        print(add_numbers(args.a, args.b))
    else:
        print(subtract_numbers(args.a, args.b))
