Name: asic_sentry
Version: 1.0.0
Release:        1%{?dist}
Summary: ASIC Sentry is a monitoring software designed to collect and send operational logs from ASIC Miners to a Mining Rig Monitor

License: GNU General Public License v3.0
URL: https://github.com/nguyenvinhlinh/ASIC-Sentry
Source0: asic_sentry-1.0.0.tar.xz

%description
ASIC Sentry is a monitoring software designed to collect and send operational logs from ASIC Miners to a Mining Rig Monitor

%global debug_package %{nil}

%prep
%autosetup

%build
cd assets;
npm install;
cd ..;
mix deps.get --only prod
MIX_ENV=prod mix compile
MIX_ENV=prod mix assets.deploy
MIX_ENV=prod mix release


%install
mkdir -p %{buildroot}/opt/asic_sentry
cp -r _build/prod/rel/asic_sentry/* %{buildroot}/opt/asic_sentry


%files
/opt/asic_sentry/*

%changelog
* Tue Feb 04 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- Support KS5L asic
