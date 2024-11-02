y = "Jawad" # Global

def my_function():
    y = 10  # local
    print(y)
    print(x)
    def nested_function():
        x = 10
        print(y, "nested variable")

    nested_function()
my_function()
print(y)

# 