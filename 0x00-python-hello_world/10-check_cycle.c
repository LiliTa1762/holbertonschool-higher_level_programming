#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *check_cycle - function to check cycle
 *@list: list to check
 *Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *tort;

	if (list == NULL || list->next == NULL)
		return (0);

	tort = list;
	hare = list->next;

	while (hare)
	{
		if (hare == tort)
			return (1);

		if (hare->next->next == NULL)
			return (0);

		hare = hare->next->next;
		tort = tort->next;
	}
	return (0);
}
