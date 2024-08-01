def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(b) != len(a[0]):
      return -1
    
    c = []
    for row in a:
      dot_product = 0;
      for i in range(len(row)):
        dot_product += row[i]* b[i]
      c.append(dot_product)   
    return c
