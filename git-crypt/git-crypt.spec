Name:		git-crypt
Version:	0.6.0
Release:	2%{?dist}
Summary:	Transparent file encryption in git

License:	GPLv3+
URL:		https://www.agwa.name/projects/git-crypt
Source0:	%{URL}/downloads/%{name}-%{version}.tar.gz

BuildRequires:	openssl-devel
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
Requires:	git

%description
git-crypt enables transparent encryption and decryption of files in a
git repository. Files which you choose to protect are encrypted when
committed, and decrypted when checked out. git-crypt lets you freely
share a repository containing a mix of public and private
content. git-crypt gracefully degrades, so developers without the
secret key can still clone and commit to a repository with encrypted
files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you
to lock down your entire repository.

%prep
%setup -q

%build
export DOCBOOK_XSL=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
export ENABLE_MAN=yes
export CXXFLAGS="%{optflags}"
%make_build

%install
make install ENABLE_MAN=yes PREFIX=%{buildroot}%{_prefix}

%files
%license COPYING
%doc README README.md INSTALL INSTALL.md
%{_bindir}/%{name}
%{_mandir}/man1/git-crypt.1*


%changelog
* Sat Mar 31 2018 Christian Kellner <ckellner@redhat.com> - 0.6.0-2
- Address review comments: Fix Summary, use macros for paths.

* Sat Mar 31 2018 Christian Kellner <ckellner@redhat.com> - 0.6.0-1
- Drop gpg-from-git-config.patch (included upstream)
- Drop openssl11.patch (fixed upstream)
- Setup CXXFLAGS so we get the correct compiler flags;
  this is also needed for debuginfo extraction to work.

* Fri Jun  9 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-4
- Add patch to read gpg excutable from .git/config

* Fri Mar 31 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-3
- Only apply the patch on fedora versions > 25

* Thu Mar 30 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-2
- Add patch for openssl 1.1 changes

* Tue Mar 28 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-1
- Initial revision
