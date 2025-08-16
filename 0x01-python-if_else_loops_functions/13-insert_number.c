#include "lists.h"

/**
 * insert_node - Function to insert a node into the list
 * @head: double pointer to the head of the list
 * @number: number to be inserted into the list
 * Return: Address of the new node if successful
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	
	current = *head;
	while (current != NULL)
	{
		if (current->next != NULL)
		{
			if ((number > current->n) && (number < current->next->n))
			{
				new->next = (current)->next;
				current->next = new;
				return (new);
			}
		}
		current = current->next;
	}
	current = new;
	return (new);
}
