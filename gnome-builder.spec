# TODO:
# - switch to gtk4-update-icon-cache
# - deviced plugin (BR: libdeviced-devel >= 3.27.4)
#
# Conditional build:
%bcond_without	sysprof		# sysprof system profiler plugin
%bcond_without	apidocs		# Sphinx based help + gi-docgen API documentation
#
Summary:	IDE for writing GNOME-based software
Summary(pl.UTF-8):	IDE do tworzenia oprogramowania opartego na GNOME
Name:		gnome-builder
Version:	46.3
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-builder/46/%{name}-%{version}.tar.xz
# Source0-md5:	10804c34efbc7856afe8706410e563fc
URL:		https://wiki.gnome.org/Apps/Builder
BuildRequires:	appstream-glib
BuildRequires:	clang-devel >= 3.5
BuildRequires:	cmark-devel >= 0.29.0
BuildRequires:	desktop-file-utils
BuildRequires:	dspy-devel >= 1.4.0
BuildRequires:	editorconfig-devel
BuildRequires:	enchant2-devel >= 2
BuildRequires:	flatpak-devel >= 1.11.2
# -std=gnu11 for C requires >= 4.7
# but gcc 11 is not sufficient for src/libide/terminal/ide-terminal-palettes.h, which relies of constant evaluation of sizeof-driven ?: operator
# (error: initializer element is not constant)
BuildRequires:	gcc >= 6:12
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.75.0
BuildRequires:	gobject-introspection-devel >= 1.74
BuildRequires:	gtk4-devel >= 4.10
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	gtk-webkit6-devel >= 2.40
BuildRequires:	gtksourceview5-devel >= 5.8
BuildRequires:	json-glib-devel >= 1.2.0
BuildRequires:	jsonrpc-glib-devel >= 3.43.0
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	libdex-devel >= 0.2
BuildRequires:	libgit2-glib-devel >= 1.1.0
BuildRequires:	libicu-devel
BuildRequires:	libpeas2-devel >= 2.0
BuildRequires:	libpanel-devel >= 1.5.0
BuildRequires:	libportal-gtk4-devel
BuildRequires:	libsoup3-devel >= 3.0
# -std=c++2a
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	llvm-devel >= 3.5
BuildRequires:	meson >= 0.60
BuildRequires:	ninja >= 1.5
BuildRequires:	ostree-devel
BuildRequires:	pango-devel >= 1:1.38.0
BuildRequires:	pcre2-common-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.2.3
%{?with_apidocs:BuildRequires:	python3-sphinx_rtd_theme}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	sed >= 4.0
%{?with_apidocs:BuildRequires:	sphinx-pdg-3}
%{?with_sysprof:BuildRequires:	sysprof-devel >= 45.0}
BuildRequires:	tar >= 1:1.22
BuildRequires:	template-glib-devel >= 3.36.1
BuildRequires:	vala >= 2:0.30.0.55
BuildRequires:	vala-gtksourceview5 >= 5.8
BuildRequires:	vala-libgit2-glib >= 1.1.0
BuildRequires:	vala-template-glib >= 3.36.1
BuildRequires:	vte-gtk4-devel >= 0.76.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.75.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cmark-lib >= 0.29.0
Requires:	ctags
Requires:	dspy-libs >= 1.4.0
Requires:	enchant2 >= 2
Requires:	flatpak-libs >= 1.11.2
Requires:	glib2 >= 1:2.75.0
Requires:	gtk4 >= 4.10
Requires:	gtk-webkit6 >= 2.40
Requires:	gtksourceview5 >= 5.8
Requires:	hicolor-icon-theme
Requires:	json-glib >= 1.2.0
Requires:	jsonrpc-glib >= 3.43.0
Requires:	libadwaita >= 1.5
Requires:	libdex >= 0.2
Requires:	libgit2-glib >= 1.1.0
Requires:	libpanel >= 1.5.0
Requires:	libpeas2 >= 2.0
Requires:	libportal >= 0.3
Requires:	libsoup3 >= 3.0
Requires:	libxml2 >= 1:2.9.0
Requires:	pango >= 1:1.38.0
Requires:	python3-modules >= 1:3.2.3
Requires:	template-glib >= 3.36.1
Requires:	vte-gtk4 >= 0.76.0
Suggests:	python3-jedi
Suggests:	python3-lxml
Obsoletes:	gnome-builder-mm < 3.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abiver	46
%define		apiver	46

# must comply to pygobject3 due to "..importer" import
%define		py3_gi_overridesdir	%{py3_sitedir}/gi/overrides

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
Requires:	glib2-devel >= 1:2.75.0
Requires:	gtk-webkit6-devel >= 2.40
Requires:	gtk4-devel >= 4.10
Requires:	gtksourceview5-devel >= 5.8
Requires:	libpeas2-devel >= 2.0
Requires:	template-glib-devel >= 3.36.1
Requires:	vte-gtk4-devel >= 0.76.0
Obsoletes:	gnome-builder-mm-devel < 3.24
Obsoletes:	vala-gnome-builder < 3.36

%description devel
This package provides development files for GNOME Builder.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne GNOME Buildera.

%package doc
Summary:	GNOME Builder documentation
Summary(pl.UTF-8):	Dokumentacja do GNOME Buildera
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
GNOME Builder documentation.

%description doc -l pl.UTF-8
Dokumentacja do GNOME Buildera.

%package apidocs
Summary:	API documentation for GNOME Builder libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek GNOME Buildera
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for GNOME Builder libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek GNOME Buildera.

%prep
%setup -q

# drop useless shebang
grep -q /usr/bin/env src/libide/Ide.py || exit 1
%{__sed} -i -e '1d' src/libide/Ide.py

%build
# python.purelibdir changed to place overrides file properly
# (possible only because there are no other system-wide python modules installed)
%meson build \
%if %{with apidocs}
	-Ddocs=true \
	-Dhelp=true \
%endif
	-Dplugin_clangd=true \
	-Dplugin_sysprof=%{__true_false sysprof} \
	-Dpython.bytecompile=2 \
	-Dpython.purelibdir=%{py3_sitedir}
# -Dplugin_deviced=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# for external plugins
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-builder/plugins

%if %{with apidocs}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnome-builder/en/{.buildinfo,_sources,objects.inv}

install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libide $RPM_BUILD_ROOT%{_gidocdir}
%endif

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-builder
%dir %{_libdir}/gnome-builder
%dir %{_libdir}/gnome-builder/girepository-1.0
%{_libdir}/gnome-builder/girepository-1.0/Ide-%{abiver}.typelib
%dir %{_libdir}/gnome-builder/plugins
%attr(755,root,root) %{_libexecdir}/gnome-builder-clang
%attr(755,root,root) %{_libexecdir}/gnome-builder-flatpak
%attr(755,root,root) %{_libexecdir}/gnome-builder-git
%dir %{_datadir}/gnome-builder
%{_datadir}/gnome-builder/fonts
%{_datadir}/gnome-builder/icons
%{_datadir}/gnome-builder/styles
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.clang.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.copyright.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.debug.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.flatpak.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.shellcmd.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.shellcmd.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.spelling.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.sysprof.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.valgrind.gschema.xml
%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
%{_desktopdir}/org.gnome.Builder.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Builder-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Builder.svg
%{py3_gi_overridesdir}/Ide.py
%{py3_gi_overridesdir}/__pycache__/Ide.cpython-*.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-builder-%{apiver}
%dir %{_datadir}/gnome-builder/gir-1.0
%{_datadir}/gnome-builder/gir-1.0/Ide-%{abiver}.gir
%{_pkgconfigdir}/gnome-builder-%{version}.pc

%if %{with apidocs}
%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/gnome-builder
%{_docdir}/gnome-builder/en

%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libide
%endif
