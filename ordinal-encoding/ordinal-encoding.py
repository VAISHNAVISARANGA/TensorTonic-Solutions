import numpy as np
def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    values=np.array(values)
    ordering=np.array(ordering)
    dict={ ordering[i]:i for i in range(len(ordering))}
    mapping={v:i for i, v in enumerate(ordering)}
    return [mapping[v] for v in values]