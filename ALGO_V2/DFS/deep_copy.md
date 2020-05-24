
### what is deep copy
aka hard copy, clone
soft copy: reference copy
```commandline
results.append(list(S)) # S is another list
```

不使用 Deep copy 会怎样呢？
我们来看看不使用 Deep copy 会怎样：
```commandline
subset = []
subset.append(1) # 此时subset是[1]

results = []
results.append(subset)  # 此时results是[[1]]

subset.append(2)  # 此时subset是[1, 2]
results.append(subset)  # 此时你以为results是[[1], [1,2]]而事实上他是[[1,2], [1,2]]

subset.append(3)  # 此时results里是[[1,2,3], [1,2,3]]
```

参数中引用传递
```commandline
def func(subset):  # subset is a list
    subset.append(1)

def main():
    subset = []
    # 此时subset是[]
    func(subset)
    # 此时subset就是[1]了

```
可能你会奇怪，不是说修改参数不会影响到函数之外的参数么？也就是：
```commandline
def func(x):
    x = x+1
		
def main():
    int x = 0
    func(x)
    # 此时x仍然是0
```
上面两者的区别在于，人们习惯性的认为 subset.add 和 x = x + 1 都是对参数进行了修改。而事实上，x = x + 1 确实是对参数进行了修改，这个修改只在函数func的局部有效，出了func回到main就失效了。而 subset.add 并没有修改 subset 这个参数本身，而只是在 subset 所指向的内存空间中增加了一个新的元素，这个操作是永久性的，不是临时的，是全局有效的，不是局部有效的。那么怎么样才是对 subset 这个参数进行了修改呢？比如：
