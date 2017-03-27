Name:		rtags
Version:	2.9
Release:	1
Summary:	A indexer for the c language family with Emacs integration

License:	GPLv3+
URL:		https://github.com/Andersbakken/rtags
# Source tarball is created with make package_source
# and not taken from the github releases, due to git
# submodules that are missing from the latter
Source0:	%{name}-2.9.tar.gz


BuildRequires:	cmake, llvm-devel, clang-devel
Buildrequires:	pkgconfig
BuildRequires:	emacs
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
Requires:	clang-libs, llvm-libs
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
%cmake .. \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

%files
%license LICENSE.txt
%doc	 README.org

%{_bindir}/*
%{_mandir}/man7/rc.7*
%{_mandir}/man7/rdm.7*
%{_emacs_sitelispdir}/rtags
# %{_datadir}/bash-completion/completions/

%changelog
* Mon Mar 27 2017 Christian Kellner <ckellner@redhat.chom> - 2.9-1
- New upstream release

* Wed Mar  1 2017 Chrisian Kellner <ckellner@redhat.com> - 2.8-4.git37eef28
- Package systemd socket/unit files

* Fri Feb 24 2017 Chrisian Kellner <ckellner@redhat.com> - 2.8-3.git37eef28
- Add gcc7.patch to fix compilation on gcc 7.0 (rawhide)

* Fri Jan 13 2017 Chrisian Kellner <ckellner@redhat.com>
- Initial revision.
