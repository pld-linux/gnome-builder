Summary:	IDE for writing GNOME-based software
Summary(pl.UTF-8):	IDE do tworzenia oprogramowania opartego na GNOME
Name:		gnome-builder
Version:	3.18.1
Release:	3
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-builder/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	9d8c049b867a150a483ad92bd5408bc7
Patch0:		%{name}-link.patch
URL:		https://wiki.gnome.org/Apps/Builder
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	clang-devel >= 3.5
BuildRequires:	devhelp-devel >= 3.16.0
# -std=gnu11 for C
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.42.0
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	gtk-webkit4-devel >= 2.8.4
BuildRequires:	gtksourceview3-devel >= 3.18.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgit2-glib-devel >= 0.23.4
BuildRequires:	libpeas-devel >= 1.14.1
# C++11
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	llvm-devel >= 3.5
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.522
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.30
BuildRequires:	vala-libgit2-glib >= 0.23.4
BuildRequires:	vte-devel >= 0.40.2
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.46.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	devhelp-libs >= 3.16.0
Requires:	gjs >= 1.42.0
Requires:	glib2 >= 1:2.46.0
Requires:	gtk+3 >= 3.18.0
# TODO: for html-preview
#Requires:	gtk-webkit4 >= 2.8.4
Requires:	gtksourceview3 >= 3.18.0
Requires:	hicolor-icon-theme
Requires:	libgit2-glib >= 0.23.4
Requires:	libpeas >= 1.14.1
Requires:	libxml2 >= 1:2.9.0
Requires:	python3-pygobject3 >= 3.0.0
Requires:	vte >= 0.40.2
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
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.46.0
Requires:	gtk+3-devel >= 3.18.0
Requires:	gtksourceview3-devel >= 3.18.0

%description devel
This package provides development files for GNOME Builder.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne GNOME Buildera.

%package -n vala-gnome-builder
Summary:	Vala API for GNOME Builder
Summary(pl.UTF-8):	API języka Vala dla GNOME Buildera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.30
# included in vala (0.30)
#Requires:	vala-gtksourceview >= 3.18.0
Requires:	vala-libgit2-glib >= 0.23.4
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-gnome-builder
Vala API for GNOME Builder.

%description -n vala-gnome-builder -l pl.UTF-8
API języka Vala dla GNOME Buildera.

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
%patch0 -p1

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-builder/*.la \
	$RPM_BUILD_ROOT%{_libdir}/gnome-builder/plugins/*.la
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
%attr(755,root,root) %{_libdir}/gnome-builder/libegg-private.so.*.*.*
%attr(755,root,root) %{_libdir}/gnome-builder/libegg-private.so.0
%attr(755,root,root) %{_libdir}/gnome-builder/libgnome-builder.so.*.*.*
%attr(755,root,root) %{_libdir}/gnome-builder/libgnome-builder.so.0
%attr(755,root,root) %{_libdir}/gnome-builder/libide-1.0.so
%attr(755,root,root) %{_libdir}/gnome-builder/librg.so.*.*.*
%attr(755,root,root) %{_libdir}/gnome-builder/librg.so.0
%attr(755,root,root) %{_libdir}/gnome-builder/libsearch.so.*.*.*
%attr(755,root,root) %{_libdir}/gnome-builder/libsearch.so.0
%dir %{_libdir}/gnome-builder/girepository-1.0
%{_libdir}/gnome-builder/girepository-1.0/Builder-1.0.typelib
%{_libdir}/gnome-builder/girepository-1.0/Egg-1.0.typelib
%{_libdir}/gnome-builder/girepository-1.0/Ide-1.0.typelib
%attr(755,root,root) %{_libdir}/gnome-builder/ide-build
%attr(755,root,root) %{_libdir}/gnome-builder/ide-list-*
%attr(755,root,root) %{_libdir}/gnome-builder/ide-mine-projects
%attr(755,root,root) %{_libdir}/gnome-builder/ide-search
%dir %{_libdir}/gnome-builder/plugins
%dir %{_datadir}/gnome-builder
%{_datadir}/gnome-builder/fonts
%dir %{_datadir}/gnome-builder/plugins

%{_libdir}/gnome-builder/plugins/autotools.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libautotools-plugin.so

%{_libdir}/gnome-builder/plugins/c-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libc-pack-plugin.so

%{_libdir}/gnome-builder/plugins/clang.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libclang-plugin.so

%{_libdir}/gnome-builder/plugins/command-bar.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libcommand-bar.so

%{_libdir}/gnome-builder/plugins/ctags.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libctags-plugin.so

%{_libdir}/gnome-builder/plugins/devhelp.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libdevhelp-plugin.so

%{_libdir}/gnome-builder/plugins/fallback.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libfallback-plugin.so

%{_libdir}/gnome-builder/plugins/file-search.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libfile-search.so

%{_libdir}/gnome-builder/plugins/gnome-code-assistance.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libgnome-code-assistance-plugin.so

%{_libdir}/gnome-builder/plugins/html-completion.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libhtml-completion-plugin.so

%{_libdir}/gnome-builder/plugins/html-preview.plugin
%{_libdir}/gnome-builder/plugins/html_preview_plugin
%{_datadir}/gnome-builder/plugins/html_preview_plugin

%{_libdir}/gnome-builder/plugins/jedi.plugin
%{_libdir}/gnome-builder/plugins/jedi_plugin.py

%{_libdir}/gnome-builder/plugins/python-gi-imports-completion.plugin
%{_libdir}/gnome-builder/plugins/python_gi_imports_completion.py

%{_libdir}/gnome-builder/plugins/python-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libpython-pack-plugin.so

%{_libdir}/gnome-builder/plugins/symbol-tree.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libsymbol-tree.so

%{_libdir}/gnome-builder/plugins/sysmon.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libsysmon.so

%{_libdir}/gnome-builder/plugins/terminal.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libterminal.so

%{_libdir}/gnome-builder/plugins/vala-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libvala-pack-plugin.so

%{_libdir}/gnome-builder/plugins/xml-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libxml-pack-plugin.so

%{_datadir}/appdata/org.gnome.Builder.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/builder*.xml
%{_desktopdir}/org.gnome.Builder.desktop
%{_iconsdir}/hicolor/*x*/apps/builder.png
%{_iconsdir}/hicolor/scalable/apps/builder-symbolic.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-builder/libegg-private.so
%attr(755,root,root) %{_libdir}/gnome-builder/libgnome-builder.so
%attr(755,root,root) %{_libdir}/gnome-builder/librg.so
%attr(755,root,root) %{_libdir}/gnome-builder/libsearch.so
%dir %{_datadir}/gnome-builder/gir-1.0
%{_datadir}/gnome-builder/gir-1.0/Builder-1.0.gir
%{_datadir}/gnome-builder/gir-1.0/Egg-1.0.gir
%{_datadir}/gnome-builder/gir-1.0/Ide-1.0.gir
%{_pkgconfigdir}/libide-1.0.pc

%files -n vala-gnome-builder
%defattr(644,root,root,755)
%dir %{_datadir}/gnome-builder/vapi
%{_datadir}/gnome-builder/vapi/egg-private.deps
%{_datadir}/gnome-builder/vapi/egg-private.vapi
%{_datadir}/gnome-builder/vapi/gnome-builder-1.0.deps
%{_datadir}/gnome-builder/vapi/gnome-builder-1.0.vapi
%{_datadir}/gnome-builder/vapi/libide-1.0.deps
%{_datadir}/gnome-builder/vapi/libide-1.0.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libide
