#!/bin/bash
export SIMONWILLISON_ROWS=$(
  jq -n --argjson rows "$(cat simonwillison-net.json)" \
  '{ "rows": $rows, "replace": true }'
)
export DATASETTE_ROWS=$(
  jq -n --argjson rows "$(cat datasette-io.json)" \
  '{ "rows": $rows, "replace": true }'
)
curl -X POST \
  https://simon.datasette.cloud/data/hacker_news_posts/-/insert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DS_TOKEN" \
  -d "$SIMONWILLISON_ROWS"
curl -X POST \
  https://simon.datasette.cloud/data/hacker_news_posts/-/insert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DS_TOKEN" \
  -d "$DATASETTE_ROWS"
