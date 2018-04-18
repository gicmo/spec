Name:          bolt
Version:       0.3
Release:       2%{?dist}
Summary:       Thunderbolt device manager
License:       LGPLv2+
URL:           https://github.com/gicmo/bolt
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        policy-normal-local-active-users-can-manage.patch

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: libudev-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(systemd)
BuildRequires: polkit-devel
BuildRequires: pygobject3-devel
BuildRequires: systemd
%{?systemd_requires}

# for the integration test (optional)
%if 0%{?fedora}
BuildRequires: pygobject3-devel
BuildRequires: python3-dbus
BuildRequires: python3-dbusmock
BuildRequires: umockdev-devel
%endif


%description
bolt is a system daemon to manage thunderbolt 3 devices via a D-BUS
API.  Thunderbolt 3 features different security modes that require
devices to be authorized before they can be used. The D-Bus API can be
used to list devices, enroll them (authorize and store them in the
local database) and forget them again (remove previously enrolled
devices). It also emits signals if new devices are connected (or
removed). During enrollment devices can be set to be automatically
authorized as soon as they are connected.  A command line tool, called
boltctl, can be used to control the daemon and perform all the above
mentioned tasks.

%prep
%setup -q
%patch0 -p1

%build
%meson -Ddb-path=%{_localstatedir}/lib/boltd
%meson_build

%check
%meson_test

%install
%meson_install
install -m0755 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/boltd


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/boltctl
%{_libexecdir}/boltd
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.bolt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.bolt.xml
%{_datadir}/polkit-1/actions/org.freedesktop.bolt.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.bolt.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.bolt.service
%{_mandir}/man1/boltctl.1*
%{_mandir}/man8/boltd.8*
%dir %{_localstatedir}/lib/boltd

%changelog
* Wed Apr 18 2018 Christian Kellner <ckellner@redhat.com> - 0.3-2
- Add policy rule patch to allow normal users to manage

* Tue Apr 10 2018 Christian Kellner <ckellner@redhat.com> - 0.3-1
- bolt 0.3 upstream release
- Update BuildRequires to include gcc
- Use forge macros

* Tue Mar  6 2018 Christian Kellner <ckellner@redhat.com> - 0.2-1
- bolt 0.2 upstream release
- Update BuildRequires dependencies.

* Sun Dec 17 2017 Christian Kellner <ckellner@redhat.com> - 0.1-2
- Set database path to /var/lib/boltd, create it during
  installation, which is needed for the service file to work.

* Thu Dec 14 2017 Christian Kellner <ckellner@redhat.com> - 0.1-1
- Initial upstream release
