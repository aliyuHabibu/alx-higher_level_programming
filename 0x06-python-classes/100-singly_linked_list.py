#!/usr/bin/python3

"""
    Module to define two class:
    One to define a node class and to
    retrieve it inform of a linked list
"""


class Node:
    """
        node:
            class ddefining and verifying
            the nature of a node
            """
    def __init__(self, data, next_node=None):
        """ Initialization method o the class Node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Method to get or that return the set data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Method to set the given data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Method to return the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Method to set the next_node """
        if value is None:
            self.__next_node = None
        elif self.data == value:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
        singly_linked_list:
            class to print the node in a
            linked list form
            """
    def __init__(self):
        """ Initialization method of the class singly_linked_list """
        self.head = []

    def sorted_insert(self, value):
        """ Method that collect data to be added to the node """
        node = Node(value)
        node.data = value
        node.next_node = value
        nd = node.next_node
        self.head.append(nd)

    def __repr__(self):
        """ Method that return string rep of object and prints the node """
        lst = sorted(self.head)
        i = 0
        while i < len(lst):
            if i == len(lst) - 1:
                print(lst[i], end='')
            else:
                print(lst[i])
            i = i + 1
        return ''
