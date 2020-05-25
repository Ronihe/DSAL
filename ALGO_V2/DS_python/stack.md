## what is stack:
LIFO:

- push()，将新的元素压入栈顶，同时栈顶上升。
- pop()，将新的元素弹出栈顶，同时栈顶下降。
- empty()，栈是否为空。
- peek()，返回栈顶元素。

```commandline
class Stack:
    def __init__(self):
        self.array = []
				
    # 压入新元素
    def push(self, x):
        self.array.append(x)
    
    # 栈顶元素出栈
    def pop(self):
        if not self.isEmpty():
            self.array.pop()
	
    # 返回栈顶元素
    def top(self):
        return self.array[-1]

    # 判断是否是空栈
    def isEmpty(self):
        return len(self.array) == 0
```
栈在计算机内存当中的应用

我们在程序运行时，常说的内存中的堆栈，其实就是栈空间。这一段空间存放着程序运行时，产生的各种临时变量、函数调用，一旦这些内容失去其作用域，就会被自动销毁。

函数调用其实是栈的很好的例子，后调用的函数先结束，所以为了调用函数，所需要的内存结构，栈是再合适不过了。在内存当中，栈从高地址不断向低地址扩展，随着程序运行的层层深入，栈顶指针不断指向内存中更低的地址。

相关参考资料：
https://blog.csdn.net/liu_yude/article/details/45058687




