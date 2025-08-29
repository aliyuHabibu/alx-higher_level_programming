#include "lists.h"

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
