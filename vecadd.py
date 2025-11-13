import concurrent.futures


def dot_product_for_loop(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must also have the same length.")
    
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


def dot_product_chunk(v1_chunk, v2_chunk):
    return sum(x * y for x, y in zip(v1_chunk, v2_chunk))


def dot_product_parallel(v1, v2, num_workers=2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must also also have the same length.")
    
   
    chunk_size = len(v1) // num_workers
    chunks = [(v1[i*chunk_size:(i+1)*chunk_size], v2[i*chunk_size:(i+1)*chunk_size]) 
              for i in range(num_workers)]
    

    if len(v1) % num_workers != 0:
        chunks.append((v1[num_workers*chunk_size:], v2[num_workers*chunk_size:]))
    
   
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = executor.map(lambda args: dot_product_chunk(*args), chunks)
    
    return sum(results)


vector1 = [1, 2, 3]
vector2 = [4, 5, 6]


print("Sequential Dot Product:", dot_product_for_loop(vector1, vector2))


print("Parallel Dot Product:", dot_product_parallel(vector1, vector2, num_workers=2))


