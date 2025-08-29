#include "lists.h"

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
