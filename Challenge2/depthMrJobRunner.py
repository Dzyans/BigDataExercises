
from depthMrJobGraph import Graphs
from depthMrJobPrep import Prep

intermediate = None


mr_job = Prep(args=['graph3'])
with mr_job.make_runner() as runner:
    runner.run()
    #for line in runner.stream_output():
    #    print line

mr_job = Graphs(args=['graph4'])
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        print line

        
        

    
