# The Funniest Toaster Error Message

[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/muhamadfajar160299-ctrl/makefun-entry-funniest-toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/muhamadfajar160299-ctrl/makefun-entry-funniest-toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

A make.fun entry for **The Funniest Toaster Error Message**: write the funniest
error message a kitchen toaster would show its owner, in 120 characters or fewer.

The entry line (73 characters):

> ERROR: Bread has unionized. Toasting suspended until its demands are met.

## How it works

`main.py` (stdlib only) copies `entry.txt` byte-identically into
`$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`, writing directly with no
temporary files. It fails loudly if `entry.txt` is missing or empty, or if
`MAKEFUN_OUTPUT_DIR` is not set.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/output python3 main.py
```
