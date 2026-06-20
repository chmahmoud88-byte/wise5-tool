
class WISE5Scorer:
    def score(self,data):
        waste=data.get('waste_mL_run',10)
        energy=data.get('kWh_run',0.1)
        time=data.get('runtime_min',10)
        R=0.8
        G=max(0,1-waste/50)
        E=max(0,1-energy/0.3)
        B=max(0,1-time/60)
        C=0.7
        return {"pillars":{"R":R,"G":G,"E":E,"B":B,"C":C},
                "whiteness":(R+G+E+B+C)/5}
