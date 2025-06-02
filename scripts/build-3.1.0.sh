#!/bin/sh

# Change RPM_BUILD_DIR as you wish!
export RPM_BUILD_DIR=/home/nguyenvinhlinh/Projects/Mining-Rig-Monitor/asic_sentry_rpmbuild

rm -rf /tmp/asic_sentry-3.1.0.tar.xz;
rm -rf $RPM_BUILD_DIR/SOURCES/asic_sentry-3.1.0.tar.xz;


cd /tmp
git clone --depth 1 --branch release/3.1.0 git@github.com:nguyenvinhlinh/ASIC-Sentry.git asic_sentry-3.1.0;
tar -cJvf asic_sentry-3.1.0.tar.xz asic_sentry-3.1.0;


cp /tmp/asic_sentry-3.1.0.tar.xz $RPM_BUILD_DIR/SOURCES/;
cd $RPM_BUILD_DIR/SPECS/;
export QA_RPATHS=$(( 0x0001|0x0002 ))
rpmbuild --define "_topdir $RPM_BUILD_DIR" -bb asic_sentry-3.1.0.spec
