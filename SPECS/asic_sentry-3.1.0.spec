Name: asic_sentry
Version: 3.1.0
Release:        1%{?dist}
Summary: ASIC Sentry is a monitoring software designed to collect and send operational logs from ASIC Miners to a Mining Rig Monitor

License: GNU General Public License v3.0
URL: https://github.com/nguyenvinhlinh/ASIC-Sentry
Source0: asic_sentry-3.1.0.tar.xz

%description
ASIC Sentry is a monitoring software designed to collect and send operational logs from ASIC Miners to a Mining Rig Monitor

%global debug_package %{nil}
%define _build_id_links none

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
%dir /opt/asic_sentry
/opt/asic_sentry/*


%changelog
* Mon Jun 2 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- Receive expected asic power on/off and light indicator from Commander
- Provide API for Remote Relay Controller to read asic_expected_status and light_expected_status
- Migrate UI to use Nexus Dashboard.

* Sun May 11 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- Migrate phoenix to 1.8-rc
- Integrate with nexus dashboard

* Tue Feb 04 2025 Nguyen Vinh Linh <nguyenvinhlinh93@gmail.com>
- Support KS5L asic
