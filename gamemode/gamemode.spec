Name:		gamemode
Version:	1.1
Release:	1%{?dist}
Summary:	Optimize system performance for games on demand
License:	BSD
URL:		https://github.com/FeralInteractive/gamemode
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:		manpage-section-8.patch
Patch1:		dbus-activatable.patch
Patch2:		version-libraries.patch

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel
BuildRequires: systemd

%description
GameMode is a daemon/lib combo for GNU/Linux that allows games to
request a set of optimizations be temporarily applied to the host OS.
GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU "powersave" or "ondemand" governors, but
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
%patch2 -p1

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
%{_mandir}/man8/gamemoded.8*

%files devel
%{_includedir}/gamemode_client.h
%{_libdir}/libgamemode*.so
%{_libdir}/pkgconfig/gamemode*.pc


%changelog
* Thu Jun 28 2018 Christian Kellner <christian@kellner.me>  - 1.1-1
- Initial package
  Resolves: #1596293
- Patch to move manpage to section 8
  Upstream commit 28fcb09413bbf95507788024b98b675cbf656f6c
- Patch for dbus auto-activation
  Merged PR https://github.com/FeralInteractive/gamemode/pull/62
- Patch for proper library versioning
  Merged PR https://github.com/FeralInteractive/gamemode/pull/63

