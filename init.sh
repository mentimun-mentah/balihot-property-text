#!/bin/bash
docker build -t balihot-property-text .
docker run -d -p 5002:5000 balihot-property-text
