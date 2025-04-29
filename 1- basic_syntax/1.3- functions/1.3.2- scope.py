# 变量作用域

# 全局变量
global_var = "I'm global"

def outer_function():
    # 外层函数变量
    outer_var = "I'm in outer function"
    
    def inner_function():
        # 内层函数变量
        inner_var = "I'm in inner function"
        # 使用nonlocal修改外层变量
        nonlocal outer_var
        outer_var = "Modified in inner function"
        print(inner_var)
    
    inner_function()
    print(outer_var)

# 修改全局变量
def modify_global():
    global global_var
    global_var = "Modified globally"

# 作用域示例
print("Before modification:", global_var)
modify_global()
print("After modification:", global_var)
outer_function()