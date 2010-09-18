colors = ximport("colors")


def pi_digits():
    """
    Generator for digits of pi
    
    See:
    http://web.comlab.ox.ac.uk/people/Jeremy.Gibbons/publications/spigot.pdf    
    """
    
    q,r,t,k,n,l = 1,0,1,1,3,3
    while True:
        if 4*q+r-t < n*t:
            yield n
            q,r,t,k,n,l = (10*q,10*(r-n*t),t,k,(10*(3*q+r))/t-10*n,l)
        else:
            q,r,t,k,n,l = (q*k,(2*q+r)*l,t*l,k+1,(q*(7*k+2)+r*l)/(t*l),l+2)


def get_grid_index(pi_grid, i, j):
    
    try:
        up = pi_grid[i-1][j]
        down = pi_grid[i+1][j]
        left = pi_grid[i][j-1]
        right = pi_grid[i][j+1]    
    except IndexError:
        up = pi_grid[i-1][j]
        down = pi_grid[i][j]
        left = pi_grid[i][j-1]
        right = pi_grid[i][j]        
    return up + 10*down + 100*left + 1000*right
        
    
# Begin drawing
rows = 50
cols = 50

# Initialize an empty matrix
pi_grid = []
for i in range(cols):
    pi_grid.append([0]*rows)
    
# Fill the matrix with the digits of pi
digits = pi_digits()
for i in range(cols):
    for j in range(rows):
        pi_grid[i][j] = digits.next()


# Canvas size
size(50*25, 50*25)

# Black lines
stroke(0)

# Scale and width parameters in pixels
s_px = 25
w_px = 25

# Color lists
circle_clrs = colors.gradient([color(0.15, 0.1, 0.7), color(1, 1, 1)], steps=10000, spread=0.15)
square_clrs = colors.gradient([color(1, 1, 1), color(0.15, 0.1, 0.7)], steps=10000, spread=0.15)

# Draw to the canvas
for i in range(cols):
    for j in range(rows):
        x = (i)*s_px
        y = (j)*s_px        
        d = pi_grid[i][j]*w_px/10        
        idx = get_grid_index(pi_grid, i, j)
        rect(x, y, w_px, w_px, fill=square_clrs[idx])
        oval(x+(w_px/2. - d/2.), y+(w_px/2. - d/2.), d, d, fill=circle_clrs[idx])
        
canvas.save('fc.png')

        
