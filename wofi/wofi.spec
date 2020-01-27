Name:		wofi
Version:	1.0
Release:	1%{?dist}
Summary:	A window switcher, application launcher and dmenu replacement for wayland

License:	MIT
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:	%{URL}/archive/v%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(wayland-client)

%description
Wofi is like "rofi" a window switcher, application launcher and dmenu
replacement but for wlroots-based wayland compositors.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson -Dversion=v%{version}
%meson_build

%install
%meson_install

%files
%license COPYING.md
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Jan 27 2020 Christian Kellner <christian@kellner.me> - 1.0-1
- Initial package of v1.0


