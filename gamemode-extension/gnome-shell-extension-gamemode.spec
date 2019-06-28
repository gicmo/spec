Name:           gnome-shell-extension-gamemode
Version:        1
Release:        1%{?dist}
Summary:        GameMode integration for GNOME Shell
License:        LGPLv2
URL:            https://github.com/gicmo/gamemode-extension
Source0:        %{url}/archive/v%{version}/gamemode-extension-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gettext >= 0.19.6
Requires:       gnome-shell >= 3.32
Suggests:       gamemode
BuildArch:      noarch

%description
GNOME Shell extension to integrate with GameMode. Can display
an icon when GameMode is active and also emit notifications
when the global GameMode status changes.


%prep
%autosetup -p0 -n gamemode-extension-%{version}%{?prerelease:-%{prerelease}}


%build
%meson
%meson_build


%install
%meson_install

%find_lang gamemode-extension


%files -f gamemode-extension.lang
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/gamemode*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gamemode.gschema.xml


%changelog
* Fri Jun 28 2019 Christian Kellner <christian@kellner.me> - 1-1
- Initial package

