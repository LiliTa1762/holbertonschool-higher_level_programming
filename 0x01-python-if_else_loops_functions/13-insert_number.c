#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - function to insert a node in a sorted linked list
 *@head: double pointer to the head of linked list
 *@number: number inside the node to linked
 *Return: addess of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *temp = NULL;
	listint_t *first_temp = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	temp = *head;
	first_temp = *head;

	while (temp)
	{
		if (temp->n >= new->n)
		{
			if (*head ==  temp)
			{
				*head = new;
				new->next = temp;
				return (new);
			}
		first_temp->next = new;
		new->next = temp;
		return (new);
		}
		first_temp = temp;
		temp = temp -> next;
	}
	first_temp->next = new;
	return (new);
}
