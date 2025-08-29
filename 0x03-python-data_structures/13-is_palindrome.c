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
