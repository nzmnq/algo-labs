def solve_ijones():
    with open('in_ijones.txt', 'r') as f:
        lines = f.readlines()
        
    if not lines:
        print ("File is blank")
        return
    else:
        print("File is ready, (check out_ijones.txt) file")
    
    w_str, h_str = lines[0].split()
    W, H = int(w_str), int(h_str)

    grid = [line.strip() for line in lines[1:H+1]]
    dp = [1] * H
    
    sums = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    
    for i in range(H):
        char = grid[i][0]
        sums[char] += dp[i]

    for j in range(1, W):
        new_dp = [0] * H
        
        for i in range(H):
            char = grid[i][j]
            left_char = grid[i][j-1]
            
            if char == left_char:
                new_dp[i] = sums[char]
            else:
                new_dp[i] = sums[char] + dp[i]
        
        for i in range(H):
            char = grid[i][j]
            sums[char] += new_dp[i]
            
        dp = new_dp

    if H == 1:
        answer = dp[0]
    else:
        answer = dp[0] + dp[H-1]

    with open('out_ijones.txt', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    solve_ijones()