%global commit0 fa970837020be45e1d6934b6f34a910ed04eee3c
%global githash %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20170404

Name:           gnome-battery-bench
Version:        3.15.4
Release:        7.%{gitdate}git%{githash}%{?dist}
Summary:        Measure power usage in defined scenarios

License:        GPLv2+
URL:            https://git.gnome.org/browse/%{name}
Source0:        https://git.gnome.org/browse/gnome-battery-bench/snapshot/%{name}-%{commit0}.tar.xz

BuildRequires: gnome-common
BuildRequires: asciidoc
BuildRequires: desktop-file-utils
BuildRequires: xmlto
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xtst)

%description
This application is designed for measuring power usage. It does it by
recording the reported battery statistics as it replays recorded event
logs, and then using that to estimate power consumption and total
battery lifetime.

%prep
%setup -q -n %{name}-%{commit0}

%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.BatteryBench.desktop

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gbb
%{_datadir}/%{name}
%{_datadir}/applications/org.gnome.BatteryBench.desktop
%{_datadir}/dbus-1/services/org.gnome.BatteryBench.service
%{_datadir}/dbus-1/system-services/org.gnome.BatteryBench.Helper.service
%{_datadir}/polkit-1/actions/org.gnome.BatteryBench.Helper.policy
%{_libexecdir}/gnome-battery-bench-helper
%{_mandir}/man1/gbb.1*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.gnome.BatteryBench.Helper.conf

%changelog
* Tue Apr  4 2017 Christian Kellner <ckellner@redhat.com> - 3.15.4-7.20170404gitfa97083
- New snapshot from git
  New power supply monitoring code, battery info in system information.

* Mon Mar 13 2017 Chrisian Kellner <ckellner@redhat.com> - 3.15.4-6.20170313gita1fe229
- New snapshot from git
  UUIDs for test logs, handle sudden suspend more safely, more bugfixes.

* Fri Jan 13 2017 Chrisian Kellner <ckellner@redhat.com> - 3.15.4-5.2017013gitb89dad6
- Snapshot taken from git
- Dropped Wayland patch (upstreamed)

* Mon Jan  9 2017 Chrisian Kellner <ckellner@redhat.com> - 3.15.4-4
- Add patch to not crash on Wayland

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Owen Taylor <otaylor@localhost.localdomain> - 3.15.4-1
- Fix RPM style issues (From review by Florian Lehner)

* Mon Feb 9 2015 Owen Taylor <otaylor@redhat.com> - 3.15.4-0.1
- Fix mixed use of $RPM_BUILD_ROOT and %%{buildroot} (From review by
  Florian Lehner)

* Thu Jan 29 2015 Owen Taylor <otaylor@redhat.com> - 3.15.4-0
- Initial spec version
