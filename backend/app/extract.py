
import re

def extract_text(txt):
    flow=re.search(r'(\d+\.?\d*)\s*mL/min',txt)
    time=re.search(r'(\d+)\s*min',txt)
    return {
        "waste_mL_run":15,
        "kWh_run":0.1,
        "runtime_min":float(time.group(1)) if time else 15
    }
