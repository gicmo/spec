Name:		rtags
Version:	2.8
Release:	1%{?dist}
Summary:	A indexer for the c language family with Emacs integration

License:	GPLv3+
URL:		https://github.com/Andersbakken/rtags
# Source tarbarll was created with a patch[1] to CMakeLists.txt
# and make package_source. The 2.8 release of rtags has its version
# set to 2.5, therefore the mismatch in the versions
#
# [1] https://github.com/gicmo/rtags/commit/be5709c
Source0:	%{name}-2.5.tar.gz

BuildRequires:	cmake, llvm-devel, clang-devel
Buildrequires:	pkgconfig
BuildRequires:  emacs
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
Requires:	clang-libs, llvm-libs
Requires:       emacs-filesystem >= %{_emacs_version}

%description
RTags is a client/server application that indexes C/C++ code and keeps
a persistent file-based database of references, declarations,
definitions, symbolnames etc. There’s also limited support for
ObjC/ObjC++. It allows you to find symbols by name (including nested
class and namespace scope). Most importantly we give you proper
follow-symbol and find-references support.


%prep
%setup -q -n %{name}-2.5


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
* Fri Jan 13 2017 Chrisian Kellner <ckellner@redhat.com>
- Initial revision.
