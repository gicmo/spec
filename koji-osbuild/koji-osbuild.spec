%global         forgeurl https://github.com/osbuild/koji-osbuild

Name:           koji-osbuild
Version:        1
Release:        0%{?dist}
Summary:        Koji integration for osbuild composer

%forgemeta

License:        ASL 2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(setuptools)

%description
Koji integration for osbuild composer.

%package        hub
Summary:        Koji hub plugin for osbuild composer integration
Requires:       %{name} = %{version}-%{release}
Requires:       koji-hub

%description    hub
Koji hub plugin for osbuild composer integration.

%package        builder
Summary:        Koji hub plugin for osbuild composer integration
Requires:       %{name} = %{version}-%{release}
Requires:       koji-builder
Requires:       python3-requests

%description    builder
Koji builder plugin for osbuild composer integration.

%package        cli
Summary:        Koji client plugin for osbuild composer integration
Requires:       %{name} = %{version}-%{release}
Requires:       koji

%description    cli
Koji client plugin for osbuild composer integration.

%prep
%forgesetup

%build
# no op

%install
install -d %{buildroot}/%{_prefix}/lib/koji-hub-plugins
install -p -m 0755 plugins/hub/osbuild.py %{buildroot}/%{_prefix}/lib/koji-hub-plugins/
%py_byte_compile %{__python3} %{buildroot}/%{_prefix}/lib/koji-hub-plugins/osbuild.py

install -d %{buildroot}/%{_prefix}/lib/koji-builder-plugins
install -p -m 0755 plugins/builder/osbuild.py %{buildroot}/%{_prefix}/lib/koji-builder-plugins/
%py_byte_compile %{__python3} %{buildroot}/%{_prefix}/lib/koji-builder-plugins/osbuild.py

install -d %{buildroot}%{python3_sitelib}/koji_cli_plugins
install -p -m 0644 plugins/cli/osbuild.py %{buildroot}%{python3_sitelib}/koji_cli_plugins/osbuild.py
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/koji_cli_plugins/osbuild.py

%files
%license LICENSE
%doc README.md

%files hub
%{_prefix}/lib/koji-hub-plugins/osbuild.py
%{_prefix}/lib/koji-hub-plugins/__pycache__/osbuild.*

%files builder
%{_prefix}/lib/koji-builder-plugins/osbuild.py
%{_prefix}/lib/koji-builder-plugins/__pycache__/osbuild.*

%files cli
%{python3_sitelib}/koji_cli_plugins/osbuild.py
%{python3_sitelib}/koji_cli_plugins/__pycache__/osbuild.*


%changelog
* Mon Nov  2 2020 Christian Kellner <christian@kellner.me> - 1-0
- Initial import
