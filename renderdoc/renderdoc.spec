%global vswig    modified-1
Name:           renderdoc
Version:        0.91
Release:        3%{?dist}
Summary:        RenderDoc is a stand-alone graphics debugging tool

License:        MIT
URL:            https://renderdoc.org
Source0:        https://github.com/baldurk/renderdoc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/baldurk/swig/archive/renderdoc-%{vswig}/swig-%{vswig}.tar.gz

# Install the private library into a private directory
#  https://github.com/baldurk/renderdoc/issues/750
Patch0:         subfolder.patch

# plthook library, used by renderdoc is only supported on x86
ExclusiveArch: %{ix86} x86_64

# for the local swig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel

# for the renderdoc itself
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  bison
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(xcb-keysyms)
Requires:       hicolor-icon-theme

%description
A free MIT licensed stand-alone graphics debugger that allows quick
and easy single-frame capture and detailed introspection of any
application using Vulkan, OpenGL.

%package devel
Summary: Development files for renderdoc
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains headers and other files that are
required to develop applications that want to integrate with
renderdoc.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

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
       -DLIB_SUBFOLDER=renderdoc \
       -DCMAKE_BUILD_TYPE=Release

%make_build

%install
cd build
%make_install
rm %{buildroot}/%{_datadir}/menu/renderdoc

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
/sbin/ldconfig

touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
/sbin/ldconfig

if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :

%files
%license LICENSE.md
%doc README.md CODE_OF_CONDUCT.md
%{_bindir}/qrenderdoc
%{_bindir}/renderdoccmd
%{_datadir}/applications/%{name}.desktop
%{_libdir}/renderdoc/lib%{name}.so
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/icons/hicolor/*/mimetypes/application-x-renderdoc-capture.*
%{_datadir}/mime/packages/renderdoc-capture.xml
%{_datadir}/pixmaps/%{name}-icon-*.xpm

%doc %{_docdir}/%{name}/
%{_sysconfdir}/vulkan/implicit_layer.d/%{name}_capture.json

%files devel
%{_includedir}/%{name}.h


%changelog
* Wed Sep 27 2017 Christian Kellner <ckellner@redhat.com> - 0.91-3
- Split out devel package
- Address review comments

* Mon Sep 18 2017 Christian Kellner <ckellner@redhat.com> - 0.91-2
- Restrict archs to x86

* Mon Sep 18 2017 Christian Kellner <ckellner@redhat.com> - 0.91-1
- New upstream version
- Dropped patches, replaced by cmake options.

* Mon Jun 19 2017 Christian Kellner <ckellner@redhat.com>
- Initial packaging
