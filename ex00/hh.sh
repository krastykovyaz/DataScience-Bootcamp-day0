#!/bin/sh

curl -k -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=data%20scientist&page=1&per_page=20' | jq -r