#!/bin/bash

tag_name=Jarvis

set -x

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=kodi-platform
branch=Jarvis
name=kodi-platform

pushd ${tmp}
git clone -b ${tag_name} https://github.com/xbmc/kodi-platform.git
cd ${package}
git checkout ${branch}
tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
#version=`git describe --tags | cut -d '-' -f 1`
version=16.0
cd ${tmp}
tar Jcf "$pwd"/${name}-${version}-${date}-${tag}.tar.xz ${package}



