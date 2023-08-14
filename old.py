if a0_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.0 and hand.landmark[8].x < 0.1 and hand.landmark[8].y < 0.2:
    a0.play()
    a0_played = True

# H0  
if h0_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.11 and hand.landmark[8].x < 0.21 and hand.landmark[8].y < 0.2:
    h0.play()
    h0_played = True

# C1  
if c1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.22 and hand.landmark[8].x < 0.32 and hand.landmark[8].y < 0.2:
    c1.play()
    c1_played = True

# D1  
if d1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.33 and hand.landmark[8].x < 0.43 and hand.landmark[8].y < 0.2:
    d1.play()
    d1_played = True

# E1  
if e1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.44 and hand.landmark[8].x < 0.54 and hand.landmark[8].y < 0.2:
    e1.play()
    e1_played = True

# F1  
if f1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.55 and hand.landmark[8].x < 0.65 and hand.landmark[8].y < 0.2:
    f1.play()
    f1_played = True

# G1  
if g1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.66 and hand.landmark[8].x < 0.76 and hand.landmark[8].y < 0.2:
    g1.play()
    g1_played = True

# A1  
if a1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.77 and hand.landmark[8].x < 0.87 and hand.landmark[8].y < 0.2:
    a1.play()
    a1_played = True


# A0 released
if a0_played == True and hand.landmark[8].z > -0.08:
    a0_played = False

# H0 released
if h0_played == True and hand.landmark[8].z > -0.08:
    h0_played = False

# C1 released    
if c1_played == True and hand.landmark[8].z > -0.08:
    c1_played = False

# D1 released    
if d1_played == True and hand.landmark[8].z > -0.08:
    d1_played = False

# E1 released    
if e1_played == True and hand.landmark[8].z > -0.08:
    e1_played = False

# F1 released    
if f1_played == True and hand.landmark[8].z > -0.08:
    f1_played = False

# G1 released    
if g1_played == True and hand.landmark[8].z > -0.08:
    g1_played = False

# A1 released    
if a1_played == True and hand.landmark[8].z > -0.08:
    a1_played = False