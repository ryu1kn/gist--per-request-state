#!/bin/bash

set -euo pipefail

echo {1..3} | xargs -I % -n 1 -P 10 curl http://localhost:8010\?delay_sec\=%