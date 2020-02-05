Name:		ccls
Version:	0.20190823.5
Release:	1%{?dist}
Summary:	Full featured C/C++/ObjC language server

License:	ASL 2.0
URL:		https://github.com/MaskRay/ccls
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	llvm-devel
BuildRequires:	clang-devel
BuildRequires:	pkgconfig(RapidJSON)

%description
ccls is a language server for C/C++/Objective-C. It supports many of
the language server protocol features, including but not limited to
code completion, finding definition/references and other cross
references. Source code formatting, context aware symbol renaming,
diagnostics and code actions (clang FixIts) and semantic highlighting
and navigation.

%prep
%forgesetup

%build
mkdir -p _build
cd _build
%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags}

%install
cd _build
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Feb  5 2020 Christian Kellner <christian@kellner.me> - 0.20190823.5-1
- Initial import

