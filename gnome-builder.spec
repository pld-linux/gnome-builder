Summary:	IDE for writing GNOME-based software
Name:		gnome-builder
Version:	3.16.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-builder/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	c7365fee143c2d4e95977e6b85dcfd7a
URL:		https://wiki.gnome.org/Apps/Builder
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	clang-devel
BuildRequires:	devhelp-devel >= 3.16.0
BuildRequires:	gjs-devel >= 1.42.0
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk+3-devel >= 3.16.1
BuildRequires:	gtksourceview3-devel >= 3.16.1
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgit2-glib-devel >= 0.22.6
BuildRequires:	libtool
BuildRequires:	llvm-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.522
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gjs >= 1.42.0
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.16.1
Requires:	gtksourceview3 >= 3.16.1
Requires:	hicolor-icon-theme
Requires:	libgit2-glib >= 0.22.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Builder attempts to be an IDE for writing software for GNOME. It does
not try to be a generic IDE, but one specialized for writing GNOME
software.

%package devel
Summary:	Development files for GNOME Builder
Group:		Development/Libraries

%description devel
This package provides development files for GNOME Builder.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnome-builder

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-builder
%attr(755,root,root) %{_libdir}/libide-1.0.so
%{_libdir}/girepository-1.0/Ide-1.0.typelib
%{_datadir}/appdata/org.gnome.Builder.appdata.xml
%{_desktopdir}/org.gnome.Builder.desktop
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.experimental.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/*.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/Ide-1.0.gir
%{_pkgconfigdir}/libide-1.0.pc
