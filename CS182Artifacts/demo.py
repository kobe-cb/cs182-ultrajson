import atheris
import sys

with atheris.instrument_imports():
    import ujson

@atheris.instrument_func
def TestOneInput(data):

    # loads = JSON to pythonObj
    # dumps = pythonObj to JSON

    # * data comes in bytes *
    # * we convert the bytes into (unicode) of length __ *
    fdp = atheris.FuzzedDataProvider(data)
    converted_data = fdp.ConsumeUnicode(sys.maxsize)
    try:
        print(f'Data:', converted_data)
        pass
    except:
        print("null")
        pass


    try:
        curr_data = ujson.loads(converted_data)
    # * Different errors exist, we're checking specifically for Value Errors
    # which are ? *
    except ValueError:
        return
    except Exception as e:
        print(f'Error Found: {e}')
        raise RuntimeError("*dies of input*")
    

    

    #raise RuntimeError("Solved RegEx")

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

"""
except Exception as e:
    #print("Error:", e)
    print(f'Error: {e}')
"""