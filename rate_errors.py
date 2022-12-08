#! /usr/bin/python3
#
# From the error table, it calculates the error rates, and print in the screen
# and a file this information
#
# IN:
# -------
# 1. Rectangular matrix starting in the second line.
#    The first column are the h (size of the mesh).
#    First row is not read because it has titles or comments (not numbers).
# 2. col array are the columns where we will calculate the rate. Ex: col=[2,3]
#
# OUT:
# -------
# - The same input matrix, but without the first line (titles), and with the
#   ratios of the columns indicated in col array
#   Tip: Copy and paste the output file in calc to give the format
#
# Ramiro Rebolledo Cormack
# https://github.com/ramrebol/
#
# Created: 17/07/2017
# Last edition: 08/12/2022
#
import numpy as np

fin = input('Input filename with the error table:\n(ex: example_in.dat)\n')
#fin = 'example_in.dat'
fout= 'rate_'+fin # Output file name

Tin     = np.loadtxt(fin,comments='#',skiprows=1)
#Tin     = np.loadtxt('example_in.dat')
col = input('Columns for which the rate is calculated: \n(ex:  2 3 4):\n')
col = [int(i) for i in col.split(' ')]
#col = [2,3]
col = np.array(col)

Taux = np.log( Tin[:,col-1] )
Oaux = np.zeros( ( Taux.shape[0]-1 , Taux.shape[1] ) )
for i in range(1,Taux.shape[0]):
    hlog        = np.log( Tin[i,0] ) - np.log( Tin[i-1,0] )
    Oaux[i-1,:] = ( Taux[i,:]-Taux[i-1,:] )/hlog


nrow = Tin.shape[0]                # rows ...
ncol = Tin.shape[1]+col.size       # ... and the columns with the out array
Tout = np.zeros( ( nrow , ncol ) )

c = 0
for j in range( len(Tin[1,:]) ):
    Tout[:,j+c] = Tin[:,j]
    if j in col-1:
        Tout[0 ,j+c+1] = np.nan
        Tout[1:,j+c+1] = Oaux[:,c]
        c = c + 1

# ------------------------------------------------------------------------------
#print('----------------')
#print('Rate error table')
#print(' ----------------')
#print(Tout)
np.savetxt(fout, Tout)
print('\n')
print('>  It was printed' , fout , 'with the output')
print('>  Remark: nan in the first row it is ok')
print('>  Tip   : Copy and paste the output file in calc to give the format')

