package main

import "fmt"

type Node struct {
	data int
	next *Node
}
type LinkedList struct {
	head *Node
}

func (list *LinkedList) InsertAtBeginning(data int) {
	node := &Node{data: data}
	node.next = list.head
	list.head = node
}

func (list *LinkedList) print() {
	currentNode := list.head

	for currentNode != nil {
		fmt.Printf("%d -> ", currentNode.data)
		currentNode = currentNode.next
	}
}

func (list *LinkedList) remove(data int) {
	if list.head == nil {
		return
	}

	if list.head.data == data {
		list.head = list.head.next
		return
	}

	previousNode := list.head

	for previousNode.next != nil && previousNode.next.data != data {
		previousNode = previousNode.next
	}

	if previousNode.next == nil {
		fmt.Printf("List doesn't contains element.")
		return
	}

	previousNode.next = previousNode.next.next

}

func (list *LinkedList) find(data int) *Node {

	if list.head == nil {
		return nil
	}

	actualNode := list.head

	for actualNode != nil && actualNode.data != data {
		actualNode = actualNode.next
	}

	return actualNode
}
