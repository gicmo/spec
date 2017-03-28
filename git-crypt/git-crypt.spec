Name:		git-crypt
Version:	0.5.0
Release:	1%{?dist}
Summary:	transparent file encryption in git

License:	GPLv3+
URL:		https://www.agwa.name/projects/git-crypt/
Source0:	https://www.agwa.name/projects/git-crypt/downloads/%{name}-%{version}.tar.gz

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
%autosetup

%build
export DOCBOOK_XSL=/usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
export ENABLE_MAN=yes
%make_build

%install
make install ENABLE_MAN=yes PREFIX=%{buildroot}/usr

%files
%license COPYING
%doc README README.md INSTALL INSTALL.md
%{_bindir}/%{name}
%{_mandir}/man1/git-crypt.1*


%changelog
* Tue Mar 28 2017 Christian Kellner <ckellner@redhat.com> - 3.15.4-0
- Initial revision
