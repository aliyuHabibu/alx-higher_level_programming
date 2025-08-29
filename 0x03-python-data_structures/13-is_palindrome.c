#include "lists.h"

/**
 * is_palindrome - Function to check for palindrome in a given linked list
 * @head: Double to the head of the linked list
 * Return: 1 if palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *check;
	int n, i, num;

	n = count_list(*head);

	current = *head;
	i = 0;
	num = 0;
	while (i < n / 2)
	{
		i++;
		check = address(head, n, i);
		if (current->n == check->n)
			num++;
		current = current->next;
	}
	if (n / 2 == num)
		return (1);
	else
		return (0);
}

/**
 * count_list - function to count nodes
 * @head: pointer to the head of the list
 * Return: Number counted.
 */
int count_list(listint_t *head)
{
        listint_t *current;
        int n;

        n = 0;
        current = head;
        while (current != NULL)
        {
                n++;
                current = current->next;
        }
        return (n);
}

/**
 * address - Function to get and return the address of a node
 * @head: Double pointer to the head address
 * @total: Total number of linked list
 * @getThere: Where to stop
 * Return: Address of the node
 */
listint_t *address(listint_t **head, int total, int getThere)
{
        listint_t *get;
        int s;

        get = *head;
        s = 0;
        while (s < (total - getThere))
        {
                get = get->next;
                s++;
        }
        return (get);
}
