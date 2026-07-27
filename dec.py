# def calculate(a, b, what_to_do):
#     def add(a,b):
#         return a + b
#     def zarb(a, b):
#         return a*b
    
#     if what_to_do == "add" :
#         return add(a, b)
#     if what_to_do == "zarb":
#         return zarb(a, b)
    
# res = calculate(3, 4, 'zarb')
# print(res)
# --------------------------------------------------------------------

def run_on_zoj(f):
    def wrapper():
        import datetime 
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0 :
            f()
        else:
            print("hiisss")
            
    return wrapper()


@run_on_zoj
def say_hello():
    print("salam, man injaaam")
    

@run_on_zoj
def say_bye():
    print("byee bye!!!")
        
        
say_hello
say_bye

    
    