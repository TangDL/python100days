# 编程题汇总

## 排序：
### 1.冒泡排序：
~~~
def Bubble_sort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(1, l-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums
data_test=[10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = Bubble_sort(data_test)
print(sorted_list)
~~~

### 2.选择排序：
~~~
def Select_sort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(i, l):
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums
~~~

### 3.插入排序：
~~~
def Insert_sort(nums):
    l = len(nums)
    for i in range(1, l):
        temp = nums[i]                          # 注意这个赋值很关键
        for j in range(i-1, -1, -1):
            if nums[j] <= temp:
                break
            else:
                nums[j+1], nums[j] = nums[j], temp
    return nums
~~~

### 4.归并排序：
~~~
def Merge_sort(nums):
    def Merge(left, right):
        len_l = len(left)
        len_r = len(right)
        res = []
        i, j =0, 0
        while i < len_l and j < len_r:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res

    l = len(nums)
    if l <= 1:
        return nums
    else:
        mid = l // 2
    left = Merge_sort(nums[:mid])
    right = Merge_sort(nums[mid:])
    return Merge(left, right)
~~~

### 5.快速排序：
~~~
def Quick_sort(nums, low, high):
    def Partition(nums, low, high):
        i = low - 1
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1

    if low < high:
        pivot = Partition(nums, low, high)
        Quick_sort(nums, low, pivot-1)
        Quick_sort(nums, pivot+1, high)
    return nums
2
6
3 6 9 66 66 99
2
10 1 1
10 4 2
6
3 6 9 66 66 99
2
1 1 1
10 4 3






data_test=[10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = Quick_sort(data_test, 0, len(data_test)-1)
print(sorted_list)
~~~
**复杂度分析**：
排序算法|      平均时间复杂度|     最坏时间复杂度|     最好时间复杂度|     空间复杂度|     稳定性   
冒泡排序|        O(n^2)              O(n^2)              O(n)            O(1)            稳定   
选择排序|        O(n^2)              O(n^2)              O(n)            O(1)           不稳定   
插入排序|       O(n^2)              O(n^2)              O(n)             O(1)            稳定   
快速排序|        O(nlog(n))          O(n^2)              O(nlog(n))      O(nlog(n))     不稳定   
归并排序|        O(nlog(n))          O(nlog(n))          O(nlog(n))      O(nlog(n))      稳定   
堆排序|          O(nlog(n))          O(nlog(n))          O(nlog(n))      O(1)           不稳定   
希尔排序|        O(nlog(n))          O(ns)               O(n)            O(1)           不稳定  
计数排序|        O(n+k)              O(n+k)              O(n+k)          O(n+k)          稳定   
基数排序|        O(N*M)              O(N*M)              O(N*M)          O(M)            稳定   

### 1. 
在vivo产线上，每位职工随着对手机加工流程认识的熟悉和经验的增加，日产量也会不断攀升。
假设第一天量产1台，接下来2天(即第二、三天)每天量产2件，接下来3天(即第四、五、六天)每天量产3件 ... ... 
以此类推，请编程计算出第n天总共可以量产的手机数量。
输入例子：11
输出例子：35

~~~
class Solution:
    def solution(self , n ):
        # write code here
        k = [1]
        total = 0
        for i in range(1, n+1):
            if i > sum(k):
                k.append(k[-1]+1)
            total += k[-1]
        return total
~~~
## dfs
### 1.
现有一个 3x3 规格的 Android 智能手机锁屏程序和两个正整数 m 和 n ，请计算出使用最少m 个键和最多 n个键可以解锁该屏幕的所有有效模式总数。
其中有效模式是指：
1、每个模式必须连接至少m个键和最多n个键；
2、所有的键都必须是不同的；
3、如果在模式中连接两个连续键的行通过任何其他键，则其他键必须在模式中选择，不允许跳过非选择键（如图）；
4、顺序相关，单键有效（这里可能跟部分手机不同）。

输入：m,n
代表允许解锁的最少m个键和最多n个键
输出：
满足m和n个键数的所有有效模式的总数
~~~
class Solution:
    def solution(self, m , n ):
        # write code here
        if n <=0 :
            return 0
        di = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1), (-1, 1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1)]
        ds = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, -1)]
        nodes = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

        def dfs(x, y, visited, count):
            visited.add((x, y))
            count -= 1
            ans = 0
            if count == 0:
                ans += 1
            else:
                for (xi, yi) in di:
                    if (x+xi, y+yi) in nodes:
                        if (x+xi, y+yi) in visited :
                            if (xi, yi) not in ds:
                                continue
                            else:
                                if (x+2*xi, y+2*yi) in nodes and (x+2*xi, y+2*yi) not in visited:
                                    ans += dfs(x+2*xi, y+2*yi, visited, count)
                        else:
                            ans += dfs(x+xi, y+yi, visited, count)
            visited.remove((x, y))
            return ans

        anss = 0
        for k in range(m, n+1):
            for i in range(3):
                for j in range(3):
                    visited = set()
                    anss += dfs(i, j, visited, k)
        return anss

S = Solution()
print(S.solution(1,2))
~~~

### 2.
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
~~~
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        info = 'Info'
        def get_depth(node, depth):
            if not node:
                return depth
            left_depth = get_depth(node.left, depth)
            if left_depth == info: return info
            right_depth = get_depth(node.right, depth)
            if right_depth == info: return info
            dif = abs(left_depth - right_depth)
            if dif > 1:
                return info
            else:
                return max(left_depth, right_depth)+1
            
        return get_depth(root, 0) != info
~~~

### 3.
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

输入: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

~~~
class Solution:   
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        di = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        r, c = len(board), len(board[0])
        x, y = click
        if board[x][y] == 'M':
             board[x][y] = 'X'
        elif board[x][y] == 'E':
            def dfs(x, y):
                boom = 0
                for d in di:
                    if 0<=x+d[0]<r and 0<=y+d[1]<c:
                        if board[x+d[0]][y+d[1]] == 'M':
                            boom += 1
                    
                if boom != 0:
                    board[x][y] = str(boom)
                
                else:
                    board[x][y] = 'B'

                    for d in di:
                        if 0<=x+d[0]<r and 0<=y+d[1]<c and board[x+d[0]][y+d[1]]=='E':
                            dfs(x+d[0], y+d[1])                                          # 注意，确保这个dfs中的参数每次递归都确保被更新

            dfs(click[0], click[1])
        return board
~~~