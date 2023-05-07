#!/bin/bash

sudo nmcli con add type wifi ifname wlan0 con-name Hotspot autoconnect yes ssid Hotspot;
sudo nmcli con modify Hotspot 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared;
sudo nmcli con modify Hotspot wifi-sec.key-mgmt wpa-psk;
sudo nmcli con modify Hotspot wifi-sec.psk "Plik est grand";
UUID=$(grep uuid /etc/NetworkManager/system-connections/Hotspot | cut -d= -f2);
nmcli con up uuid $UUID;
