#!/usr/bin/env bash
# Regenerates the ANTLR4 lexer/parser/visitor from grammar/PLC.g4
# Requires Java and antlr-4.13.2-complete.jar (downloaded into tools/ on first run).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JAR="$ROOT/tools/antlr-4.13.2-complete.jar"

if [ ! -f "$JAR" ]; then
  echo "Downloading ANTLR 4.13.2 jar..."
  curl -sSL -o "$JAR" https://www.antlr.org/download/antlr-4.13.2-complete.jar
fi

java -jar "$JAR" \
  -Dlanguage=Python3 \
  -visitor \
  -no-listener \
  -o "$ROOT/generated" \
  "$ROOT/grammar/PLC.g4"

# Make the generated dir importable as a package
touch "$ROOT/generated/__init__.py"

echo "Parser regenerated into $ROOT/generated"
