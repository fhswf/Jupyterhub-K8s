#!/usr/bin/env bash
set -xe
DISTRO=ubuntu
ARCH=$(arch | sed 's/aarch64/arm64/g' | sed 's/x86_64/amd64/g')

echo "Install Firefox"
if grep -q Jammy /etc/os-release; then
  if [ ! -f '/etc/apt/preferences.d/mozilla-firefox' ]; then
    add-apt-repository -y ppa:mozillateam/ppa
    echo '
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001
' > /etc/apt/preferences.d/mozilla-firefox
  fi
  apt-get install -y firefox p11-kit-modules
elif grep -q "ID=debian" /etc/os-release || grep -q "ID=kali" /etc/os-release || grep -q "ID=parrot" /etc/os-release; then
  echo \
    "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> \
    /etc/apt/sources.list
cat > /etc/apt/preferences.d/99pin-unstable <<EOF
Package: *
Pin: release a=stable
Pin-Priority: 900

Package: *
Pin: release a=unstable
Pin-Priority: 10
EOF
  apt-get update
  apt-get install -y -t unstable firefox p11-kit-modules
else
  apt-mark unhold firefox || :
  apt-get remove firefox
  apt-get update
  apt-get install -y firefox p11-kit-modules
fi

# Add Langpacks
FIREFOX_VERSION=$(curl -sI https://download.mozilla.org/?product=firefox-latest | awk -F '(releases/|/win32)' '/Location/ {print $2}')
RELEASE_URL="https://releases.mozilla.org/pub/firefox/releases/${FIREFOX_VERSION}/win64/xpi/"
LANGS='en-US.xpi da.xpi'
EXTENSION_DIR=/usr/lib/firefox-addons/distribution/extensions/
mkdir -p ${EXTENSION_DIR}
for LANG in ${LANGS}; do
  LANGCODE=$(echo ${LANG} | sed 's/\.xpi//g')
  echo "Downloading ${LANG} Language pack"
  curl -o ${EXTENSION_DIR}langpack-${LANGCODE}@firefox.mozilla.org.xpi -Ls ${RELEASE_URL}${LANG}
done
echo "done"

# no flash

apt-mark hold firefox
apt-get autoclean
rm -rf /var/lib/apt/lists/*  /var/tmp/*  /tmp/*


# Update firefox to utilize the system certificate store instead of the one that ships with firefox
rm -f /usr/lib/firefox/libnssckbi.so
ln /usr/lib/$(arch)-linux-gnu/pkcs11/p11-kit-trust.so /usr/lib/firefox/libnssckbi.so
# settings
preferences_file=/usr/lib/firefox/browser/defaults/preferences/firefox.js

# Disabling default first run URL for Debian based images
cat >"$preferences_file" <<EOF
pref("datareporting.policy.firstRunURL", "");
pref("datareporting.policy.dataSubmissionEnabled", false);
pref("datareporting.healthreport.service.enabled", false);
pref("datareporting.healthreport.uploadEnabled", false);
pref("trailhead.firstrun.branches", "nofirstrun-empty");
pref("browser.aboutwelcome.enabled", false);
EOF

# # Creating Default Profile
# chown -R 0:0 $HOME
# firefox -headless -CreateProfile "kasm $HOME/.mozilla/firefox/kasm"

# # Starting with version 67, Firefox creates a unique profile mapping per installation which is hash generated
# #   based off the installation path. Because that path will be static for our deployments we can assume the hash
# #   and thus assign our profile to the default for the installation

# cat >>$HOME/.mozilla/firefox/profiles.ini <<EOL
# [Install4F96D1932A9F858E]
# Default=kasm
# Locked=1
# EOL

# # Cleanup for app layer
# # chown -R 1000:0 $HOME
# #find /usr/share/ -name "icon-theme.cache" -exec rm -f {} \;
# #if [ -f $HOME/Desktop/firefox.desktop ]; then
# #  chmod +x $HOME/Desktop/firefox.desktop
# #fi
# #chown -R 1000:1000 $HOME/.mozilla