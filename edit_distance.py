####  Hindi-Words Edit Distance in Python  ####

####  @function editDistance takes two string as argument
####  @and returns Edit-Distance between both
# coding=utf-8
import codecs
import sys

def minimum(x,y,z):
	return min(min(x,y),z)

def editDistance(s1,s2,n,m):
	if n==0:
		return m
	if m==0:
		return n
	if s1[n-1]==s2[m-1]:
		return editDistance(s1,s2,n-1,m-1)
	return 1 + minimum(editDistance(s1,s2,n,m-1),editDistance(s1,s2,n-1,m),editDistance(s1,s2,n-1,m-1))

if __name__ == "__main__":
	fr = codecs.open('hindi-text', encoding='utf-8',mode='r')
	arg = fr.read().split()
	print arg[0],arg[1],len(arg[0]),len(arg[1])
	print editDistance(arg[0],arg[1],len(arg[0]),len(arg[1]))
