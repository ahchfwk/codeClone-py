def getCodeFrag(filepath, start, end):
    result = ""
    with open(filepath, "r") as f:
        result = f.readlines()[start-1:end]
        result = "".join(result)
    return result


if __name__ == "__main__":
    print getCodeFrag()