def newly_created_wrapper_function(func):
  print(func)
  def wrapper():
    print("Bella")
    res_1 = func()
    print("Ciao")
    print(res_1)
    return res_1 + "there"
  return wrapper

@newly_created_wrapper_function
def greet():
  print("Ahem")
  return "Howdy"

res = greet
print(res)



