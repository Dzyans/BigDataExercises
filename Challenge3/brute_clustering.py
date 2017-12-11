
def loopOfDoom(hashdict):
    start_loop = timeit.default_timer()
    cluster_lookup = dict()
    clusters = dict()
    completed_keys = []
    cluster_nr = 0
    outer_loop_counter = 0
    hit_lookup = dict()
    cluster = []
    cluster_counter = 0
    print (len(hashdict))
    for key1 in hashdict:
        outer_loop_counter += 1
        if outer_loop_counter % 100 == 0:
            print(outer_loop_counter)
        if key1 in cluster_lookup:            
            cluster_nr = cluster_lookup[key1]
            cluster = clusters[cluster_nr]
            
        else:
            cluster_nr = cluster_counter
            cluster = []
            cluster.append(key1)
            
            clusters[cluster_nr] = cluster
            cluster_lookup[key1] = cluster_nr
            cluster_counter += 1
        
        for key2 in hashdict:
            
            hit_counter = 0
            if(key1 == key2 or key2 in completed_keys):
                
                continue
            
            for th in hashdict[key1]:
                for ch in hashdict[key2]:                    
                    if th == ch:
                        
                        hit_counter += 1
            if(hit_counter > 2):
                #match found
                
                if key2 not in clusters[cluster_nr]:
                    if key2 in hit_lookup and hit_counter > hit_lookup[key2]:
                        #we is moving the key from the old cluster
                        clusters[cluster_lookup[key2]].remove(key2)
                   
                    if key2 not in hit_lookup or hit_counter > hit_lookup[key2]:
                        clusters[cluster_nr].append(key2) 
                        cluster_lookup[key2] = cluster_nr
                        hit_lookup[key2] = hit_counter
        completed_keys.append(key1)
            
            
    
    elapsed = timeit.default_timer() - start_loop
    print ("loops of doom done in: " + str(elapsed) + " seconds")
         
    writeToFile(clusters, "results_final_doom.txt")