#!/usr/bin/env python
#encoding:utf-8

# 题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
# 思路：从左下角或者右上角开始比较
def find_interge(matrix, num):
    if not matrix:
        return False
    rows, columns = len(matrix), len(matrix[0])
    row, column = 0, columns-1  # 右上角
    while row < rows && column >= 0:
        if num == matrix[row][column]:
            return True
        elif num > matrix[row][column]:
            row++
        else:
            column--

# 题目：把字符串中的空格替换成'20%'
# 思路：利用python的内置函数replace实现
def replace_str(str):
    return str.replace(' ', '20%')
    
# 从尾到头打印单链表
# 思路：用list模拟栈
def reverse_print_linkList(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())

def reverse_print_linkList(links):
    if links:
        reverse_print_linkList(links.next)
        print(links.val)

# 题目：重建二叉树
# 要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值
# 思路：前序遍历：根-左-右   中序遍历：左-根-右
# 根据前序遍历可以得到根节点，进而得到左子树和右子树，分别对左右子树递归构建
def rebuild_tree(preorder=None, inorder=None):
    if nor preorder or not inorder:
        return False
    index = inorder.index(preorder[0]) # 在中序遍历序列中查找根节点下标
    left = inorder[: index]
    right = inorder[index+1: ]
    root = TreeNode(preorder[0])       # 构建root结点
    root.left = rebuild_tree(preorder[1: 1+len(left)], left)  # 递归创建左子树
    root.left = rebuild_tree(preorder[-len(right): ], right)  # 递归创建右子树
    
# 题目：两个栈实现队列
# 要求：用两个栈实现队列，分别实现入队和出队操作
# 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中
class myQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'


if __name__ == "__main__":
    find_interge()