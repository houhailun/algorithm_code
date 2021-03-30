#!/usr/bin/env python
# encoding:utf-8


"""
题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中

方法1：利用python的 num in matrix判断
方法2：利用数组特性,从右上角开始查找，如果小于要查找的num，则往下查找(行加1)；否则往前查找(列减1)
"""
def find_integer(matrix, num):
    if not matrix:
        return False
    rows, columns = len(matrix), len(matrix[0])
    row, column = 0, columns-1  # 右上角
    while row < rows and column >= 0:
        if num == matrix[row][column]:
            return True
        elif num > matrix[row][column]:
            row += 1
        else:
            column -= 1

    return False


"""
题目：把字符串中的空格替换成'20%'
方法1：利用python的内置函数replace实现
方法2：两个指针
    1、统计空格个数，以便确定转换后最后一个字符的位置
    2、从后往前把str的字符复制到指定位置，遇到空格后p1跳过，p2写‘20%’
    3、p1到str头部或者p1==p2
"""
def replace_str(str):
    return str.replace(' ', '20%')


"""
题目: 从尾到头打印单链表
方法1：用list模拟栈
方法2：递归法
"""
def reverse_print_link_list(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


def reverse_print_link_list_v2(links):
    if links:
        reverse_print_link_list_v2(links.next)
        print(links.val)


"""
题目：重建二叉树
要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值
思路：前序遍历：根-左-右   中序遍历：左-根-右
    根据前序遍历可以得到根节点，构建根节点进而得到左子树和右子树，分别对左右子树递归构建
"""
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def rebuild_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        return False
    index = inorder.index(preorder[0])  # 在中序遍历序列中查找根节点下标
    left = inorder[: index]    # 左子树节点
    right = inorder[index+1:]  # 右子树节点
    root = TreeNode(preorder[0])  # 构建root结点
    root.left = rebuild_tree(preorder[1: 1+len(left)], left)  # 递归创建左子树
    root.left = rebuild_tree(preorder[-len(right):], right)  # 递归创建右子树


"""
题目：两个栈实现队列
要求：用两个栈实现队列，分别实现入队和出队操作
思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中
    1、入队列：直接入栈1
    2、出队列：如果栈2不为空，则栈2弹出元素；否则把栈1元素全部写到栈2；最后弹出栈2元素

"""
class Solution:
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
