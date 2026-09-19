import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from findex.stats import collect_stats_streaming

if __name__ == "__main__":
    result = collect_stats_streaming("data")
    print(result)