Summary:	IDE for writing GNOME-based software
Summary(pl.UTF-8):	IDE do tworzenia oprogramowania opartego na GNOME
Name:		gnome-builder
Version:	3.16.3
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-builder/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	186d75c5310c37c28061bc294ed0dd15
URL:		https://wiki.gnome.org/Apps/Builder
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	clang-devel
BuildRequires:	devhelp-devel >= 3.16.0
# -std=gnu11 for C
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.42.0
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.16.1
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	gtksourceview3-devel >= 3.16.1
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgit2-glib-devel >= 0.22.6
# C++11
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	llvm-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.522
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	devhelp-libs >= 3.16.0
Requires:	gjs >= 1.42.0
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.16.1
Requires:	gtksourceview3 >= 3.16.1
Requires:	hicolor-icon-theme
Requires:	libgit2-glib >= 0.22.6
Requires:	libxml2 >= 1:2.9.0
Requires:	python3-pygobject3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Builder attempts to be an IDE for writing software for GNOME. It does
not try to be a generic IDE, but one specialized for writing GNOME
software.

%description -l pl.UTF-8
Builder jest próbą stworzenia IDE do rozwijania oprogramowania dla
GNOME. Nie próbuje być ogólnym IDE, ale wyspecjalizowanym do pisania
oprogramowania dla GNOME.

%package devel
Summary:	Development files for GNOME Builder
Summary(pl.UTF-8):	Pliki programistyczne GNOME Buildera
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.16.1
Requires:	gtksourceview3-devel >= 3.16.1

%description devel
This package provides development files for GNOME Builder.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne GNOME Buildera.

%package apidocs
Summary:	LibIDE API documentation
Summary(pl.UTF-8):	Dokumentacja API LibIDE
Group:		Documentation

%description apidocs
LibIDE API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API LibIDE.

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
	--disable-silent-rules \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-builder/*.la
#%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnome-builder

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
%dir %{_libdir}/gnome-builder
%attr(755,root,root) %{_libdir}/gnome-builder/libide-1.0.so
%dir %{_libdir}/gnome-builder/girepository-1.0
%{_libdir}/gnome-builder/girepository-1.0/Ide-1.0.typelib
%attr(755,root,root) %{_libdir}/gnome-builder/ide-build
%attr(755,root,root) %{_libdir}/gnome-builder/ide-list-*
%attr(755,root,root) %{_libdir}/gnome-builder/ide-mine-projects
%attr(755,root,root) %{_libdir}/gnome-builder/ide-search
%{_datadir}/appdata/org.gnome.Builder.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/builder*.xml
%{_desktopdir}/org.gnome.Builder.desktop
%{_iconsdir}/hicolor/*x*/apps/builder.png
%{_iconsdir}/hicolor/scalable/apps/builder-symbolic.svg

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/Ide-1.0.gir
%{_pkgconfigdir}/libide-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libide
