# ASIC Sentry - RPM Build
This repository is all about creating rpm package for mining rig monitor software.

By default, `rpmbuild` directory should be in  `$HOME`. if you want to change it to different directory, you need to use `_topdir` rpm macro. When building rpm, this process should be in `docker` or `VM`, **thus, we follow rpm convention.**



```sh
$ git clone https://github.com/nguyenvinhlinh/ASIC-Sentry-RPM-Build ~/rpmbuild
$ sudo dnf install rpmdevtools
```




## Step 1. Prepare source code tarball
```
$ git clone https://github.com/nguyenvinhlinh/ASIC-Sentry/ asic-sentry
$ cd asic-sentry
$ git checkout v1.0.0
$ cd ..
$ mv asic-sentry asic-sentry-1.0.0
$ tar -cJvf asic-sentry-1.0.0.tar.xz asic-sentry-1.0.0
```

Now your source code tarball is ready for next step!

## Step 2. Copy source code tarball to `SOURCES`.

```sh
➜ rpmbuild (master) ✗ tree -L 3
.
├── BUILD
├── BUILDROOT
├── readme.md
├── RPMS
├── SOURCES
│   └── asic-sentry-1.0.0.tar.xz <----- your tarball here!
├── SPECS
│   ├── asic-sentry-1.0.0.spec
└── SRPMS
```
## Step 2. Create new `SPECS/.spec` file
Ignore this step if you modify existing one!

```bash
$ cd SPECS;
$ rpmdev-newspec;
```

Update:

- Version
- Release
- Source0

## Step 3. Run `rpmbuild`
```bash
$ cd SPECS;
$ rpmbuild -bb asic-sentry-1.0.0.spec
```

Gonna see error:
```
ERROR   0002: file '/opt/asic_sentry/lib/crypto-5.5/priv/lib/crypto.so' contains an invalid runpath '/usr/local/lib64'
```

`crypto` is an erlang module. I dont know how to modify it. this is a work around!
```
$ cd SPECS;
$ export QA_RPATHS=$(( 0x0001|0x0002 ))
$ rpmbuild -bb asic-sentry-1.0.0.spec
```

## Step 4. Provide `%files`
Those file would be listed after running `rpmbuild -bb asic-sentry-1.0.0.spec`. Append it and re-run `rpmbuild -bb asic-sentry-1.0.0.spec` to make rpm.
```
RPM build errors:
    Installed (but unpackaged) file(s) found:
   /opt/asic_sentry/bin/migrate
   /opt/asic_sentry/bin/migrate.bat
   /opt/asic_sentry/bin/asic_sentry
   /opt/asic_sentry/bin/asic_sentry.bat
   /opt/asic_sentry/bin/server

```

Check out `RPMS` directory! RPM should be there!

```
➜ rpmbuild (master) ✗ tree -L 3
.
├── BUILD
├── BUILDROOT
├── readme.md
├── RPMS
│   └── x86_64
│       ├── asic-sentry-1.0.0-1.fc40.x86_64.rpm <----------- your file here!
│       ├── asic-sentry-debuginfo-1.0.0-1.fc40.x86_64.rpm
│       └── asic-sentry-debugsource-1.0.0-1.fc40.x86_64.rpm
├── SOURCES
│   └── asic-sentry-1.0.0.tar.xz
├── SPECS
│   ├── asic-sentry-1.0.0.spec
└── SRPMS
```
