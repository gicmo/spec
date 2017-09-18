%global vswig    modified-1
Name:           renderdoc
Version:        0.91
Release:        1%{?dist}
Summary:        RenderDoc is a stand-alone graphics debugging tool.

License:        MIT
URL:            https://renderdoc.org
Source0:        https://github.com/baldurk/renderdoc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/baldurk/swig/archive/renderdoc-%{vswig}/swig-%{vswig}.tar.gz

# for the local swig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel

# for the renderdoc itself
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  vulkan-devel
BuildRequires:  bison
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  mesa-libGL-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       hicolor-icon-theme


%description
RenderDoc is a free MIT licensed stand-alone graphics debugger that
allows quick and easy single-frame capture and detailed introspection
of any application using Vulkan, D3D11, OpenGL or D3D12 across Windows
7 - 10, Linux.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p build
cd build
%cmake .. \
       -DQMAKE_QT5_COMMAND=qmake-qt5 \
       -DRENDERDOC_SWIG_PACKAGE=%{SOURCE1} \
       -DENABLE_GL=ON \
       -DENABLE_VULKAN=ON \
       -DENABLE_VULKAN=ENABLE_RENDERDOCCMD \
       -DENABLE_QRENDERDOC=ON \
       -DBUILD_VERSION_STABLE=ON \
       -DBUILD_VERSION_DIST_NAME="fedora" \
       -DBUILD_DISTRIBUTION_VERSION="%{version}-%{release}" \
       -DBUILD_VERSION_DIST_CONTACT="https://copr.fedorainfracloud.org/coprs/gicmo/devel/" \
       -DCMAKE_INSTALL_PREFIX=/usr \
       -DCMAKE_BUILD_TYPE=Release

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_datadir}/menu/renderdoc

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
/sbin/ldconfig

touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%postun
/sbin/ldconfig

update-desktop-database &> /dev/null ||:
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :

  touch --no-create %{_datadir}/mime/packages &> /dev/null || :
  update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%license LICENSE.md
%doc README.md CODE_OF_CONDUCT.md
%{_bindir}/qrenderdoc
%{_bindir}/renderdoccmd
%{_datadir}/applications/%{name}.desktop
%{_libdir}/lib%{name}.so
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/icons/hicolor/*/mimetypes/application-x-renderdoc-capture.*
%{_datadir}/mime/packages/renderdoc-capture.xml
%{_datadir}/pixmaps/%{name}-icon-*.xpm

#maybe should be in doc package ?
%doc %{_docdir}/%{name}/

# maybe should be in devel package ?
%{_includedir}/%{name}.h

# should be in -vulkan package ?
%{_sysconfdir}/vulkan/implicit_layer.d/%{name}_capture.json

%changelog
* Mon Sep 18 2017 Christian Kellner <ckellner@redhat.com> - 0.91-1
- New upstream version
- Dropped patches, replaced by cmake options.

* Mon Jun 19 2017 Christian Kellner <ckellner@redhat.com>
- Initial packaging
