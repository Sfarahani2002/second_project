def divis(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        print("b can not be 0 ")
    except Exception as e:
        print(f"Another eroor : {e}")
        return None

print(divis(60, 4))
print(divis(1, 200))