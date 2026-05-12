def build_transition_table(needle):
    """
    Creating transition table for DFA
    """
    m = len(needle)
    alphabet = set(needle)
    
    TF = [{c: 0 for c in alphabet} for _ in range(m + 1)]
    
    if m == 0:
        return TF
    
    TF[0][needle[0]] = 1
    lps = 0 
    
    for i in range(1, m + 1):
        for c in alphabet:
            TF[i][c] = TF[lps].get(c, 0)
            
        if i < m:
            TF[i][needle[i]] = i + 1
            lps = TF[lps].get(needle[i], 0)
            
    return TF

def dfa_search(haystack, needle):
    """
    Searching all insertion needle into haystack by DFA
    """
    if not needle:
        return []
        
    m = len(needle)
    n = len(haystack)

    TF = build_transition_table(needle)
    
    state = 0
    result_indices = []
    
    for i in range(n):
        char = haystack[i]
        state = TF[state].get(char, 0)
        
        if state == m:
            start_index = i - m + 1
            result_indices.append(start_index)
            
    return result_indices

if __name__ == "__main__":
    haystack_text = "AABAACAADAABAABA"
    needle_text = "AABA"
    
    indices = dfa_search(haystack_text, needle_text)
    
    print(f"Haystack text: '{haystack_text}'")
    print(f"Needle text: '{needle_text}'")
    print(f"Finded on: {indices}")