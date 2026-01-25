class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda r: r.record_id)

    # Validation
    for i, r in enumerate(records):
        if r.record_id != i:
            raise ValueError("Record id is invalid or out of order.")
        if r.record_id < r.parent_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")
        if r.record_id == r.parent_id and r.record_id != 0:
            raise ValueError("Only root should have equal record and parent id.")

    # Create all nodes
    nodes = {r.record_id: Node(r.record_id) for r in records}

    # Build relationships
    for r in records:
        if r.record_id != r.parent_id:
            nodes[r.parent_id].children.append(nodes[r.record_id])

    return nodes[0]
