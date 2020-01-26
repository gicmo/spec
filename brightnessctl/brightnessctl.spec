Name:		brightnessctl
Version:	0.4
Release:	1%{?dist}
Summary:	Read and control device brightness

License:	MIT
URL:		https://github.com/Hummer12007/brightnessctl
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		use-systemd-logind.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(libsystemd)

%description
This program allows you read and control device brightness. Devices,
by default, include back-light and LEDs (searched for in corresponding
classes).

It can also preserve current brightness before applying the operation,
allowing for use cases like disabling back-light on lid close.

%prep
%autosetup -p1

%build
export ENABLE_SYSTEMD=1
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install INSTALL_UDEV_RULES=0 ENABLE_SYSTEMD=1 PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 26 2020 Christian Kellner <ckellner@redhat.com> - 0.4-1
- New upstream release (0.4)
- Add patch to use systemd-logind, modified from upstream PR 33 with
  modifications to not install the binary as suid.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3-1
- Upgrade to 0.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Wed Jan 18 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2-1
- Update to 0.2

* Sun Nov 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.1_p2-2
- Improvements thanks to Igor review

* Sun Nov 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.1_p2-1
- Initial packaging
