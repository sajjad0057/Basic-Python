INF = 1000000000000

def min(x, y):
  if x < y:
    return x
  return y

def coin_change(money,coins):
  M = [0]*(money+1)

  for j in range(1, money+1):
    minimum = INF

    for i in range(1,len(coins)):
      if(j >= coins[i]):
        minimum = min(minimum , M[j-coins[i]]+1)
    M[j] = minimum
  return M[money]

if __name__ == '__main__':
  coins = [2, 1, 2] #coins
  print(coin_change(3,coins))