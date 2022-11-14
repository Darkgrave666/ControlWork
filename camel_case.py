def to_camel_case(n: str, capitalize_first: int):
    new = n.title().replace(" ", "")
    if capitalize_first == 1:
        return new
    elif capitalize_first == 0:
        new = new[0].lower() + new[1:]
        return new


if __name__ == "__main__":
    print(to_camel_case("to camel case", 0))
