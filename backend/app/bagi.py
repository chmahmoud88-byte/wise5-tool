
class BAGIScorer:
    def score(self,data):
        attrs={
            "analysis":0.8,"reagents":0.6,"energy":0.7,
            "cost":0.8,"time":0.7,"waste":0.5,
            "automation":0.8,"robustness":0.7,
            "safety":0.6,"throughput":0.7
        }
        return {"attributes":attrs,"score":sum(attrs.values())/len(attrs)}
