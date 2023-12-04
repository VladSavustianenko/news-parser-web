#!/bin/sh

/app/tailscaled --tun=userspace-networking --socks5-server=localhost:1055 &
/app/tailscale up --authkey=${TAILSCALE_AUTHKEY} --hostname=tailf3a03.ts.net
echo Tailscale started
ALL_PROXY=socks5://localhost:1055/ /app/my-app