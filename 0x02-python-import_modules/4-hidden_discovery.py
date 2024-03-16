#!/usr/bin/python3

if __name__ == "__main__":
    import marshal
    import dis

    with open("hidden_4.pyc", "rb") as f:
        bytecodes = f.read()

    code_object = marshal.loads(bytecodes)
    instructions = dis.get_instructions(code_object)

    names = set()

    for instruction in instructions:
        if instruction.opname == 'LOAD_GLOBAL':
            name = instruction.argval
            if not name.startswith("__"):
                names.add(name)
    for name in sorted(names):
        print(name)
