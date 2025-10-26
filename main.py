def isOdd(value):
    """
    判断输入是否为奇整数    
    参数:
    value - 任意类型的输入值    
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    # 检查输入是否为整数类型（排除布尔值，因bool是int子类）
    if type(value) is int:
        # 检查是否为奇数（不能被2整除）
        return value % 2 != 0
    # 非整数类型或非奇数情况均返回False
    return False
