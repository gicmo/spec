Name:		gamemode
Version:	1.1
Release:	1%{?dist}
Summary:	Optimise system performance for games on demand
License:	BSD
URL:		https://github.com/FeralInteractive/gamemode
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:		dbus-activatable.patch
Patch1:		version-libraries.patch

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel
BuildRequires: systemd

%description
GameMode is a daemon/lib combo for GNU/Linux that allows games to
request a set of optimisations be temporarily applied to the host OS.
GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU powersave or ondemand governors, but
is now able to launch custom user defined plugins, and is intended
to be expanded further, as there are a wealth of automation tasks
one might want to apply.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc	 README.md
%{_bindir}/gamemoded
%{_libexecdir}/cpugovctl
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_libdir}/libgamemode*.so.*
%{_userunitdir}/gamemoded.service
%{_mandir}/man1/gamemoded.1*

%files devel
%{_includedir}/gamemode_client.h
%{_libdir}/libgamemode*.so
%{_libdir}/pkgconfig/gamemode*.pc


%changelog
* Thu Jun 28 2018 Christian Kellner <christian@kellner.me>  - 1.1-1
- Initial package
- Patch for dbus auto-activation
- Patch for proper library versioning
