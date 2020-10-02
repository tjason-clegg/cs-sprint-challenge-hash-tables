def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    # Loop through weights to get index and numbers

    for idx, number in enumerate(weights):

        # If numbers not in cache
        if number not in cache:
            # Add number and index to cache

            cache[number] = idx

    # Loop through weights again
    for idx, number in enumerate(weights):

        # Check if limit - number in cache
        if (limit - number) in cache:
            if idx == cache[(limit - number)]:

                # Skip
                pass
            else:
                if idx > cache[(limit - number)]:
                    return (idx, cache[(limit - number)])

                else:
                    # Return

                    return(cache[(limit - number)], idx)
