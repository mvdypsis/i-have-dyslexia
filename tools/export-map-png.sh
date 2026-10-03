#!/usr/bin/env sh
# Export assets/strategy-map-light.svg to assets/strategy-map.png at 2x, for
# places that do not show SVG (LinkedIn, slides, chat apps). Run it after
# tools/build-visuals.py adds or removes a strategy. macOS, Google Chrome.
#
# Chrome gets its own empty profile and 40 seconds: a headless Chrome that
# shares a running profile can hang, and it sometimes hangs on exit after the
# screenshot is already written.

root=$(cd "$(dirname -- "$0")/.." && pwd)
profile=$(mktemp -d)
perl -e 'alarm 40; exec @ARGV' "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --user-data-dir="$profile" --no-first-run --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1400,830 \
  --screenshot="$root/assets/strategy-map.png" "file://$root/assets/strategy-map-light.svg" >/dev/null 2>&1
rm -rf "$profile"
[ -s "$root/assets/strategy-map.png" ] && echo "assets/strategy-map.png written"
