#include "lists.h"

/**
 * check_cycle - Function to check for cycle in list
 * @list: pointer to head of the list
 *
 * Return: 0 if false, 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list->next;
	while (head != NULL)
	{
		if (list == head)
			return (1);
		head = head->next;
	}
	return (0);
}
