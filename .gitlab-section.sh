#!/bin/sh
set -o errexit
set -o nounset
IFS=$(printf '\n\t')

section() {
    [ $# -ge 2 ] || return 1
    tag="$1" id="$2" title="${3:-}" opts="${4:-}"
    printf "\e[0Ksection_%s:%s:%s%s\r\e[0K%s" "$tag" "$(date +%s)" "$id" "$opts" "$title"
}

section "$@"

