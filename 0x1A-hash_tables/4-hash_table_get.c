#include "hash_tables.h"

/**
 * hash_table_get - retrieve the value associated with a key
 * @ht: pointer t the hash table
 * @key: key to get the value of
 * Return: if the key can't be matched - NULL
 * Otherwise - the value associated with key in ht
 */

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	hash_node_t *node;
	unsigned long int index;

	if (ht == NULL || key == NULL || *key == '\0')
		return (NULL);

	index = key_index((const unsiged char *)key, ht->size);

	if (index >= ht->size)
		return (NULL);

	node = ht->array[index];
	while (node && strcmp(node->key, key) != 0)
		node = node->next;
	return ((node == NULL) ? NULL : node->value);
}
