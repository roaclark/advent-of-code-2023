def add_vectors(*vectors):
  return tuple([sum(vals) for vals in zip(*vectors)])