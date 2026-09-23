#sum of digits
num=int(input())
class solution:
    def sumofdigits(self,num):
      total=0
      while num>0:
          total += num%10
          num//=10
      return total

sol = solution()
print(sol.sumofdigits(num))
