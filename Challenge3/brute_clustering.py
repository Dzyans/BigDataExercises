
def loopOfDoom(hashdict):
    start_loop = timeit.default_timer()
    cluster_lookup = dict() ## to know which cluster a video belongs to
    clusters = dict() ## the actual clusters
    completed_keys = []
    cluster_nr = 0
    outer_loop_counter = 0
    hit_lookup = dict() ## dict to look up the how well matched a video was when it was added to a cluster
    cluster = []
    cluster_counter = 0
    print (len(hashdict))
    for key1 in hashdict:
        
        ##counter for status print out
        outer_loop_counter += 1
        
        if outer_loop_counter % 100 == 0:
            print(outer_loop_counter)
        ####
        
        ##set up the cluster_nr
        if key1 in cluster_lookup: ## the key has already been added to a cluster by previous iteration
            cluster_nr = cluster_lookup[key1]
            cluster = clusters[cluster_nr]            
        else:                   ## starting a new cluster because the key is yet un clustered
            cluster_nr = cluster_counter
            cluster = []
            cluster.append(key1)
            
            clusters[cluster_nr] = cluster
            cluster_lookup[key1] = cluster_nr
            cluster_counter += 1
        
        for key2 in hashdict: ## loop through the hash lists of the rest of the set
            
            hit_counter = 0
            if(key1 == key2 or key2 in completed_keys): ## we skip it if we have already matched these two keys                
                continue
            
            for th in hashdict[key1]:
                for ch in hashdict[key2]:                    
                    if th == ch:                        
                        hit_counter += 1 ## if two hashes match then they have a LSH-hashed picture frame in common
            if(hit_counter > 2): ## we have a low threshhold because we reorganize if we find a better match later
                #match found
                
                if key2 not in clusters[cluster_nr]: ##if they has not yet been added to the current cluster
                    if key2 in hit_lookup and hit_counter > hit_lookup[key2]: ## if the other video has already been added to a cluster, but it matches this better
                        #we is moving the key from the old cluster
                        clusters[cluster_lookup[key2]].remove(key2)
                   
                    if key2 not in hit_lookup or hit_counter > hit_lookup[key2]: ## add the video to the current cluster, and update the lookup dicts
                        clusters[cluster_nr].append(key2) 
                        cluster_lookup[key2] = cluster_nr
                        hit_lookup[key2] = hit_counter
        completed_keys.append(key1)
            
            
    
    elapsed = timeit.default_timer() - start_loop
    print ("loops of doom done in: " + str(elapsed) + " seconds")
         
    writeToFile(clusters, "results_final_doom.txt")