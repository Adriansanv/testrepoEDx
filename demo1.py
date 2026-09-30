# passing a string name "a" to a parameter named "a"
def scope_test(a):
    a = a + "Twenty"
    print(f"a inside function: {a}")

a = "Ten"
scope_test(a)
print(f"a after function: {a}")