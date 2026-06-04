#!/usr/bin/env python3
import argparse
import urllib.request
import urllib.error
import time
import json
from statistics import mean, median
VERSION = "1.0.0"

def test_endpoint(url, times=10):
    results = []
    for i in range(times):
        start = time.time()
        try:
            req = urllib.request.Request(url, method='GET')
            with urllib.request.urlopen(req) as response:
                response.read()
            elapsed = (time.time() - start) * 1000
            results.append({'status': response.status, 'time_ms': elapsed})
        except urllib.error.HTTPError as e:
            results.append({'status': e.code, 'time_ms': (time.time() - start) * 1000})
        except Exception as e:
            results.append({'status': 'error', 'time_ms': (time.time() - start) * 1000})
        time.sleep(0.1)
    times_list = [r['time_ms'] for r in results]
    return {'url': url, 'requests': times, 'avg_ms': round(mean(times_list), 2), 'median_ms': round(median(times_list), 2), 'min_ms': round(min(times_list), 2), 'max_ms': round(max(times_list), 2)}

def main():
    parser = argparse.ArgumentParser(description='API Speed Test')
    parser.add_argument('url')
    parser.add_argument('-n', '--requests', type=int, default=10)
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    result = test_endpoint(args.url, args.requests)
    output = json.dumps(result, indent=2)
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)
if __name__ == '__main__':
    main()
