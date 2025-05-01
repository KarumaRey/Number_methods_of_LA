def mul_matrices(a, b):
  N = len(a)
  M = len(b[0])
  L = len(b)

  c = [[0] * N for i in range(M)]
  for i in range(N):
    for j in range(M):
      for k in range(L):
        c[i][j] += a[i][k] * b[k][j]
  return c

def mul_matrix_vec(a, b):
  N = len(a)
  M = len(b)

  c = [0] * N
  for i in range(N):
    for j in range(M):
      c[i] += a[i][j] * b[j]
  return c

def norm(a):
  return np.sqrt(sum(x ** 2 for x in a))

def scalar_product(a, b):
  if len(a) != len(b):
    print(f"different length of vectors: {a}, {b}")
    return
  sum = 0;
  for i in range(len(a)):
    sum += a[i] * b[i]
  return sum


def copyM(M):
  n = len(M)
  M1 = [[0] * n for i in range(n)]
  for i in range(n):
    for j in range(n):
      M1[i][j] = M[i][j]
  return M1


import numpy as np
import copy
import matplotlib.pyplot as plt

def drawGraph(func, x_graph):
  #x = np.linspace(-100, 100, 50)
  plt.plot(x_graph, func(x_graph))
  plt.grid()
  plt.show()

lmbda = []
eps = 10e-5
#n = len(arr)
p = []

def f(x):
  n = len(p) - 1
  sum = 0
  for i in range (len(p)):
    sum += - (-1)**n * p[i] * x**(n-i)
  '''print(x, sum)
  print(p)'''
  return sum


def find0(a, b):
  if f(a) < eps:
    lmbda.append(a)
    return
  if f(b) < eps:
    lmbda.append(b)
    return
  x1 = (a + b) / 2
  if f(x1)*f(a) <= 0:
    find0(a, x1)
  if f(x1)*f(b) <= 0:
    find0(x1, b)

def resolveEq(A, B):
  print("собств знач:")
  n = 10000
  delta = (B-A) / n
  a = A
  for i in range(n):
    b = a + delta
    if f(a)*f(b) <= 0:
      find0(a, b)
    a = b

def comp_less(a,b):
  if a + 10e-5 < b:
    return True
  return False

def getGershgorin(M):
  n = len(M)
  left = 1000
  right = -1000
  for i in range(n):
    r = 0;
    z = M[i][i]
    for j in range(n):
      if j != i:
        r += abs(M[i][j])
    left = (z - r) if left > z-r else left
    right = (z + r) if right < z+r else right

  return left, right

def checkGershgorin(left, right):
  for l in lmbda:
    #l = round(l_, 4)
    if comp_less(l ,left):
      return False
    if comp_less(right ,l):
      return False
  return True


def Krylov(M):
  n = len(M)
  D = copyM(M)
  y = []
  A = []
  y.append([1]*n)
  for i in range(1, n+1):
    y.append(np.dot(D, y[i-1]))

  for i in range(n-1, -1, -1):
    A.append(y[i])
  A = np.transpose(np.array(A))
  f = y[n]
  res_p = np.linalg.solve(A, f)
  p.append(1)
  for p_i in res_p:
    p.append(-p_i)
  return y

def findVectors(y):
  xs = []
  q = []
  n = len(p) - 1
  for i in range(n):
    x = np.array(y[n-1])
    q_i = []
    q_i.append(1)
    for j in range(1, n):
      q_i.append(lmbda[i] * q_i[j-1] + p[j])
      x = x + np.dot(q_i[j], y[n-1-j])
    xs.append(x)
  return xs

def ortonorm(xs):
  for x in xs:
    x_norm = norm(x)
    for i in range(len(x)):
      x[i] = x[i]/x_norm
    print(np.array(x), "  norm:", round(norm(x),2))
  return xs

def checkortog(xs):
  for i in range(len(xs)):
    for j in range(i+1, len(xs)):
      print("ortog check:", f"x{i}", f"x{j}", round(scalar_product(xs[i], xs[j]), 2))

def EQ(a, b):
  if abs(a-b)<10e-2:
    return True
  return False

def viet():
  n = len(p) - 1
  mul = 1
  for x in lmbda:
    mul *= x

  if not EQ(sum(-x for x in lmbda), p[1] / p[0]):
    return False
  if not EQ(mul, (-1)**(n) * p[n] / p[0]):
    return False
  return True

def main(arr, x_graph):
  print("матрица:")
  print(np.array(arr))
  print()
  ''' p[0] = -1
  p[1] = arr[0][0] + arr[1][1] + arr[2][2]
  p[2] = - (Det2(arr[0][0], arr[0][1], arr[1][0], arr[1][1]) + Det2(arr[1][1], arr[1][2], arr[2][1], arr[2][2]) + Det2(arr[0][0], arr[0][2], arr[2][0], arr[2][2]))
  p[3] = Det3(arr)'''

  lmbda.clear()
  p.clear()
  y = Krylov(arr)
  print(p)

  l, r = getGershgorin(arr)
  resolveEq(l, r)
  print(np.array(lmbda))
  print()
  print("Viet:", viet())
  print()
  print("Gershgorin:", checkGershgorin(l, r))
  x = findVectors(y)
  print()
  print("собств в-ра:")
  print(np.array(x))
  print()
  print("ортонорм собств в-ра:")
  x = ortonorm(x)
  print()
  checkortog(x)


  drawGraph(f, x_graph)


arr = [[2.2, 1, 0.5, 2], [1, 1.3, 2, 1], [0.5, 2, 0.5, 1.6], [2, 1, 1.6, 2]]
x_graph = np.arange(-2, 6.01, 0.01)
main(arr, x_graph)

arr2 = [[0,1,0],[1,1,-1],[0,-1,0]]
x_graph2 = np.arange(-2, 3.01, 0.01)
main(arr2, x_graph2)
