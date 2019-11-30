import  math

# Asking for number of polygon points
n = float(input("Enter the number of polygon points: "))
print("\n")
if n < 4:
    n = float(input("Type a number bigger than 3: ")) # Condition for bigger than 3 polygon points


# Creating empty lists to store x and y coordinates
xlist = []
ylist = []

# Asking for x,y coordinates of polygon points
print("Enter x and y coordinates for polygon points...")

i = 1.0
while i < (n+1):
    xlist.append(int(input(f"x{i:<2.0f}: "))) # syntax for adding input coordinates to created empty lists
    ylist.append(int(input(f"y{i:<2.0f}: "))) # syntax for adding input coordinates to created empty lists
    i = i + 1

print(f"\n{'Point':<7} {'x':<7} {'y':<7}") # table header

print("-" * 20)

for t in range(0,int(n)): # printing entered coordinates
    print(f"{t+1:<6} {xlist[t]:<7.2f} {ylist[t]:<7.2f}")

#-----------------------------------------------------------------------------------------

Ai = int(1)
SAx = float(0)

# SAx is created for calculating the summation only. Ax will be related to SAx at the end.

while Ai < (n+1):
    if Ai != n:
        SAx = SAx + (xlist[Ai]+xlist[Ai-1])*(ylist[Ai]-ylist[Ai-1])
    else:
        SAx = SAx + (xlist[0]+xlist[Ai-1])*(ylist[0]-ylist[Ai-1])
    Ai = Ai + 1

Ax = (1/2) * SAx

#-----------------------------------------------------------------------------------------

Si = int(1)
SSx = float(0)

# SSx is created for calculating the summation only. Sx will be related to SSx at the end.

while Si < (n+1):
    if Si != n:
        SSx = SSx + (xlist[Si]-xlist[Si-1])*(ylist[Si]**2+ylist[Si-1]*ylist[Si]+ylist[Si-1]**2)
    else:
        SSx = SSx + (xlist[0]-xlist[Si-1])*(ylist[0]**2+ylist[Si-1]*ylist[0]+ylist[Si-1]**2)
    Si = Si + 1

Sx = -(1/6) * SSx

#-----------------------------------------------------------------------------------------

Si2 = int(1)
SSy = float(0)

# SSy is created for calculating the summation only. Sy will be related to SSy at the end.

while Si2 < (n+1):
    if Si2 != n:
        SSy = SSy + (ylist[Si2]-ylist[Si2-1])*(xlist[Si2]**2+xlist[Si2-1]*xlist[Si2]+xlist[Si2-1]**2)
    else:
        SSy = SSy + (ylist[0]-ylist[Si2-1])*(xlist[0]**2+xlist[Si2-1]*xlist[0]+xlist[Si2-1]**2)
    Si2 = Si2 + 1

Sy = (1/6) * SSy

#-----------------------------------------------------------------------------------------

Ii = int(1)
SIx = float(0)

# SIx is created for calculating the summation only. Ix will be related to SIx at the end.

while Ii < (n+1):
    if Ii != n:
        SIx = SIx + (xlist[Ii] - xlist[Ii-1]) * (ylist[Ii]**3 + ylist[Ii]**2 * ylist[Ii-1] + ylist[Ii]*ylist[Ii-1]**2 + ylist[Ii-1]**3)
    else:
        SIx = SIx + (xlist[0] - xlist[Ii-1]) * (ylist[0]**3 + ylist[0]**2 * ylist[Ii-1] + ylist[0]*ylist[Ii-1]**2 + ylist[Ii-1]**3)
    Ii = Ii + 1

Ix = -(1/12) * SIx

#-----------------------------------------------------------------------------------------

Ii2 = int(1)
SIy = float(0)

# SIy is created for calculating the summation only. Iy will be related to SIy at the end.

while Ii2 < (n+1):
    if Ii2 != n:
        SIy = SIy + (ylist[Ii2] - ylist[Ii2-1]) * (xlist[Ii2]**3 + xlist[Ii2]**2 * xlist[Ii2-1] + xlist[Ii2] * xlist[Ii2-1]**2 + xlist[Ii2-1]**3)
    else:
        SIy = SIy + (ylist[0] - ylist[Ii2-1]) * (xlist[0]**3 + xlist[0]**2 * xlist[Ii2-1] + xlist[0] * xlist[Ii2-1]**2 + xlist[Ii2-1]**3)
    Ii2 = Ii2 + 1

Iy = (1/12) * SIy

#-----------------------------------------------------------------------------------------

Ii3 = int(1)
SIxy = float(0)

# SIxy is created for calculating the summation only. Ixy will be related to SIxy at the end.

while Ii3 < (n+1):
    if Ii3 != n:
        SIxy = SIxy + (ylist[Ii3] - ylist[Ii3-1]) * (ylist[Ii3] * (3 * xlist[Ii3]**2 + 2 * xlist[Ii3] * xlist[Ii3-1] + xlist[Ii3-1]**2) + ylist[Ii3-1] * (3 * xlist[Ii3-1]**2 + 2 * xlist[Ii3] * xlist[Ii3-1] + xlist[Ii3]**2))
    else:
        SIxy = SIxy + (ylist[0] - ylist[Ii3-1]) * (ylist[0] * (3 * xlist[0]**2 + 2 * xlist[0] * xlist[Ii3-1] + xlist[Ii3-1]**2) + ylist[Ii3-1] * (3 * xlist[Ii3-1]**2 + 2 * xlist[0] * xlist[Ii3-1] + xlist[0]**2))
    Ii3 = Ii3 + 1

Ixy = -(1/24) * SIxy

#-----------------------------------------------------------------------------------------

xt = Sy / Ax

#-----------------------------------------------------------------------------------------

yt = Sx / Ax

#-----------------------------------------------------------------------------------------

Ixt = Ix - yt**2 * Ax

#-----------------------------------------------------------------------------------------

Iyt = Iy - xt**2 * Ax

#-----------------------------------------------------------------------------------------

Ixyt = Ixy + xt * yt * Ax

# Printing results
print("\nGeometric characteristics:")
print(f"Ax:    {Ax:>4.2f}")
print(f"Sx:    {Sx:>4.2f}")
print(f"Sy:    {Sy:>4.2f}")
print(f"Ix:    {Ix:>4.2f}")
print(f"Iy:    {Iy:>4.2f}")
print(f"Ixy:  {Ixy:>4.2f}")
print(f"xt:    {xt:>4.2f}")
print(f"yt:    {yt:>4.2f}")
print(f"Ixt:   {Ixt:>4.2f}")
print(f"Iyt:   {Iyt:>4.2f}")
print(f"Ixyt:  {Ixyt:>4.2f}")