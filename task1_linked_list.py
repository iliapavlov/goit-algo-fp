class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(elements))

    def reverse(self):

        """Реверс однозв'язного списку"""
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def merge_sort(self, head=None):

        """Сортування злиттям для однозв'язного списку"""
        if head is None: # Якщо не передано, сортуємо весь список
            head = self.head
        if head is None or head.next is None: # Базовий випадок
            return head

        def split(head):
            """Розділяє список на дві половини"""
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            """Зливає два відсортовані списки"""
            dummy = Node()
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        left, right = split(head)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return merge(left, right)

    def sort(self):
        self.head = self.merge_sort()

    @staticmethod
    def merge_sorted_lists(list1, list2):

        """Об'єднує два відсортовані однозв'язні списки в один відсортований список"""
        dummy = Node()
        tail = dummy
        a = list1.head
        b = list2.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b

        merged = LinkedList()
        merged.head = dummy.next
        return merged


def demo_linked_list():
    print("=== Демонстрація роботи з однозв'язним списком ===")

    # Створення списку
    llist = LinkedList()
    for val in [7, 3, 9, 1, 5]:
        llist.insert_at_end(val)
    print("Початковий список:")
    llist.print_list()

    # Реверс
    llist.reverse()
    print("Після реверсу:")
    llist.print_list()

    # Сортування
    llist.sort()
    print("Після сортування:")
    llist.print_list()

    # Об'єднання з іншим списком
    other = LinkedList()
    for val in [2, 4, 6, 8]:
        other.insert_at_end(val)
    print("Інший відсортований список:")
    other.print_list()

    merged = LinkedList.merge_sorted_lists(llist, other)
    print("Об'єднаний відсортований список:")
    merged.print_list()