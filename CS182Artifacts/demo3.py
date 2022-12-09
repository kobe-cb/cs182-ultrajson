import atheris

with atheris.instrument_imports():
    import sys
    import ujson

def CustomMutator(data, max_size, seed):
    try:
        new_data = ujson.dumps(data)
    except TypeError:
        new_data = b'{"a": 22}'
    else:
        new_data = atheris.Mutate(new_data, len(new_data))
    return new_data


@atheris.instrument_func
def TestOneInput(data):
    try:
        decodedData = ujson.dumps(data)
    except ValueError:
        return
    except TypeError:
        return
    except Exception as e:
        print(f'!! Error found: {e}')
        return
    
def main():
    atheris.Setup(sys.argv, TestOneInput, custom_mutator=CustomMutator)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
