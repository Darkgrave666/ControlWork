def to_snake_case(n: str):
    new = n.replace(" ", "_").lower()
    return new


if __name__ == "__main__":
    print(to_snake_case("To Snake Case"))
