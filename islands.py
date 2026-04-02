from bucket_mode import flood_fill

def count_islands(ocean_map):

    rows = len(ocean_map)
    cols = len(ocean_map[0])
    islands_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if ocean_map[r][c] == 'L':
                islands_count += 1
                
                ocean_map = flood_fill(ocean_map, r, c, 'W')
                
    return islands_count

if __name__ == '__main__':
    # W - water, L - land
    satellite_map = [
        ['W', 'W', 'W', 'W', 'L', 'W', 'W'],
        ['W', 'L', 'L', 'W', 'L', 'W', 'W'],
        ['W', 'L', 'L', 'W', 'W', 'W', 'L'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L', 'W', 'W'],
        ['L', 'W', 'W', 'L', 'L', 'W', 'W']
    ]
    
    print("Satellite Map:")
    for row in satellite_map:
        print(" ".join(row))
        
    total = count_islands(satellite_map)
    
    print("\nAnalysis complete!")
    print(f"Found independent islands: {total}")