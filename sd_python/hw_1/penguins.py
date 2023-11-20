pengs_slices = """   _~_    
  (o o)   
 /  V  \  
/(  _  )\ 
  ^^ ^^   """.split('\n')


def print_pengs(n):
    for p_slice in pengs_slices:
        for _ in range(n):
            print(f'{p_slice}', end='')
        print()


if __name__ == '__main__':
    n = int(input())
    print_pengs(n)
