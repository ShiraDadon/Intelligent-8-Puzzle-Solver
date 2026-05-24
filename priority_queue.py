"""
Priority queue wrapper used by A* to expand the lowest-priority node first.
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.heap_entries = []
        self.active_entries = {}
        self.insertion_counter = 0

    def add_or_update_priority(self, item, priority):
        """Add a new item or update an existing item with a better priority."""
        if item in self.active_entries:
            self.mark_removed(item)

        insertion_order = self.insertion_counter
        self.insertion_counter += 1

        # insertion_order breaks ties when two nodes have the same priority.
        queue_entry = [priority, insertion_order, item]
        self.active_entries[item] = queue_entry
        heapq.heappush(self.heap_entries, queue_entry)

    def mark_removed(self, item):
        # heapq cannot efficiently delete an arbitrary entry, so the entry is marked and skipped later.
        queue_entry = self.active_entries.pop(item)
        queue_entry[-1] = None

    def pop_lowest_priority_item(self):
        """Remove and return the active item with the lowest priority."""
        while self.heap_entries:
            priority, insertion_order, item = heapq.heappop(self.heap_entries)
            if item is not None:
                del self.active_entries[item]
                return item
        raise KeyError("pop from an empty priority queue")

    def is_empty(self):
        return not self.active_entries
