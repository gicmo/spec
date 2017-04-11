Name:		python3-devhelp
Version:	3.5
Release:	1%{?dist}
Summary:	Devhelp documentation for python3

License:	Python
URL:		http://www.python.org

Source:		pyhtml2devhelp.py

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-docs
BuildRequires:	gzip

Requires: python3-docs

%description
The python3-devhelp package contains devhelp documentation on the
Python 3 programming language and interpreter.

Install the python3-devhelp package if you'd like to use the
documentation for the Python 3 language from within devhelp.

%build
%{__python3} %{SOURCE0} /usr/share/doc/python3-docs/html index.html %{python3_version} > python-%{python3_version}.devhelp
gzip -9nc python-%{python3_version}.devhelp > python-%{python3_version}.devhelp.gz

%install
install -m 755 -d %{buildroot}/%{_datadir}/doc/python3-docs/html
install -t %{buildroot}/%{_datadir}/doc/python3-docs/html python-%{python3_version}.devhelp.gz
install -m 755 -d %{buildroot}/%{_datadir}/devhelp/books/
%{__ln_s} /usr/share/doc/python3-docs/html %{buildroot}/%{_datadir}/devhelp/books/python-%{python3_version}

%files
%{_datadir}/doc/python3-docs/html/python-%{python3_version}.devhelp.gz
%{_datadir}/devhelp/books/python-%{python3_version}

%changelog
* Tue Apr 11 2017 Christian Kellner <ckellner@redhat.com>
- Initial version
