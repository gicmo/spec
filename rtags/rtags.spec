Name:		rtags
Version:	2.14
Release:	1%{?dist}
Summary:	A indexer for the c language family with Emacs integration

License:	GPLv3+
URL:		https://github.com/Andersbakken/rtags
# Source tarball is created from the git repository
# with make package_source and not taken from the
# github releases, due to git submodules that are
# missing from the latter.
#  git clone --recursive https://github.com/Andersbakken/rtags.git
#  cd rtags && git checkout v<version>
#  mkdir build && cd build && cmake -DRTAGS_ENABLE_DEV_OPTIONS=1 ..
#  make package_source
Source0:	%{name}-%{version}.tar.gz
Source1:	rtags.service
Source2:	rtags.socket

BuildRequires:	cmake, llvm-devel, clang-devel
BuildRequires:	emacs
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(bash-completion)
%{?systemd_requires}
BuildRequires: systemd
Requires:	emacs-filesystem >= %{_emacs_version}

%description
RTags is a client/server application that indexes C/C++ code and keeps
a persistent file-based database of references, declarations,
definitions, symbolnames etc. There’s also limited support for
ObjC/ObjC++. It allows you to find symbols by name (including nested
class and namespace scope). Most importantly we give you proper
follow-symbol and find-references support.

%prep
%setup -q

%build
mkdir -p build
cd build
%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_userunitdir}
install -p -m644 -t %{buildroot}%{_userunitdir} %{SOURCE1} %{SOURCE2}

%preun
%systemd_user_preun %{name}.service

%post
%systemd_user_post %{name}.service

%files
%license LICENSE.txt
%doc	 README.org

%{_bindir}/*
%{_mandir}/man7/rc.7*
%{_mandir}/man7/rdm.7*
%{_emacs_sitelispdir}/rtags
%{_datadir}/bash-completion/
%{_userunitdir}/rtags.service
%{_userunitdir}/rtags.socket

%changelog
* Thu Sep 14 2017 Christian Kellner <ckellner@redhat.com> - 2.14-1
- New upstream release
- Proper suppport for systemd unit files
- Fix some packaging issues

* Wed Aug  2 2017 Christian Kellner <ckellner@redhat.com> - 2.12-3
- Add systemd service/socket files

* Tue Aug  1 2017 Christian Kellner <ckellner@redhat.com> - 2.12-1
- New upstream release

* Tue May 23 2017 Christian Kellner <ckellner@redhat.com> - 2.9-2
- Package bash completions

* Mon Mar 27 2017 Christian Kellner <ckellner@redhat.chom> - 2.9-1
- New upstream release

* Wed Mar  1 2017 Chrisian Kellner <ckellner@redhat.com> - 2.8-4.git37eef28
- Package systemd socket/unit files

* Fri Feb 24 2017 Chrisian Kellner <ckellner@redhat.com> - 2.8-3.git37eef28
- Add gcc7.patch to fix compilation on gcc 7.0 (rawhide)

* Fri Jan 13 2017 Chrisian Kellner <ckellner@redhat.com>
- Initial revision.
