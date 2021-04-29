# TODO:
# - deviced plugin (BR: libdeviced-devel >= 3.27.4)
#
# Conditional build:
%bcond_without	sysprof		# sysprof system profiler plugin
%bcond_without	apidocs		# Sphinx based help + gtk-doc API documentation
#
Summary:	IDE for writing GNOME-based software
Summary(pl.UTF-8):	IDE do tworzenia oprogramowania opartego na GNOME
Name:		gnome-builder
Version:	3.40.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-builder/3.40/%{name}-%{version}.tar.xz
# Source0-md5:	bf59feea441b0915cd1a5ac7e715b50e
URL:		https://wiki.gnome.org/Apps/Builder
BuildRequires:	appstream-glib
BuildRequires:	clang-devel >= 3.5
BuildRequires:	desktop-file-utils
BuildRequires:	devhelp-devel >= 3.26.0
BuildRequires:	enchant2-devel >= 2
BuildRequires:	flatpak-devel >= 0.8.0
# -std=gnu11 for C
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gjs-devel >= 1.42.0
BuildRequires:	glade-devel >= 3.22.0
BuildRequires:	glib2-devel >= 1:2.65.0
BuildRequires:	gobject-introspection-devel >= 1.48.0
BuildRequires:	gspell-devel >= 1.2.0
BuildRequires:	gtk+3-devel >= 3.22.26
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.11}
BuildRequires:	gtk-webkit4-devel >= 2.26
BuildRequires:	gtksourceview4-devel >= 4.0.0
BuildRequires:	json-glib-devel >= 1.2.0
BuildRequires:	jsonrpc-glib-devel >= 3.30.0
BuildRequires:	libdazzle-devel >= 3.37.0
BuildRequires:	libgit2-glib-devel >= 0.25.0
BuildRequires:	libpeas-devel >= 1.22.0
BuildRequires:	libportal-devel >= 0.3
BuildRequires:	libsoup-devel >= 2.52.0
# C++11
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	llvm-devel >= 3.5
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja >= 1.5
BuildRequires:	ostree-devel
BuildRequires:	pango-devel >= 1:1.38.0
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.2.3
BuildRequires:	python3-pygobject3-devel >= 3.22.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
%{?with_apidocs:BuildRequires:	sphinx-pdg-3}
%{?with_sysprof:BuildRequires:	sysprof-ui-devel >= 3.37.1}
BuildRequires:	tar >= 1:1.22
BuildRequires:	template-glib-devel >= 3.28.0
BuildRequires:	vala >= 2:0.30.0.55
BuildRequires:	vala-gtksourceview4 >= 4.0.0
BuildRequires:	vala-libdazzle >= 3.37.0
BuildRequires:	vala-libgit2-glib >= 0.25.0
BuildRequires:	vala-template-glib >= 3.28.0
BuildRequires:	vala-vte >= 0.46
BuildRequires:	vte-devel >= 0.46
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.65.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	ctags
Requires:	devhelp-libs >= 3.26.0
Requires:	enchant2 >= 2
Requires:	flatpak-libs >= 0.8.0
Requires:	gjs >= 1.42.0
Requires:	glade-libs >= 3.22.0
Requires:	glib2 >= 1:2.65.0
Requires:	gspell >= 1.2.0
Requires:	gtk+3 >= 3.22.26
Requires:	gtk-webkit4 >= 2.26
Requires:	gtksourceview4 >= 4.0.0
Requires:	hicolor-icon-theme
Requires:	json-glib >= 1.2.0
Requires:	jsonrpc-glib >= 3.30.0
Requires:	libdazzle >= 3.37.0
Requires:	libgit2-glib >= 0.25.0
Requires:	libpeas >= 1.22.0
Requires:	libportal >= 0.3
Requires:	libsoup >= 2.52.0
Requires:	libxml2 >= 1:2.9.0
Requires:	pango >= 1:1.38.0
Requires:	python3-modules >= 1:3.2.3
Requires:	python3-pygobject3 >= 3.22.0
%{?with_sysprof:Requires:	sysprof-ui-libs >= 3.37.1}
Requires:	template-glib >= 3.28.0
Requires:	vte >= 0.46
Suggests:	python3-jedi
Suggests:	python3-lxml
Obsoletes:	gnome-builder-mm < 3.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	3.40

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
Requires:	glib2-devel >= 1:2.65.0
Requires:	gtk+3-devel >= 3.22.26
Requires:	gtksourceview4-devel >= 4.0.0
Requires:	jsonrpc-glib-devel >= 3.30.0
Requires:	libdazzle-devel >= 3.37.0
Requires:	libpeas-devel >= 1.22.0
Requires:	pango-devel >= 1:1.38.0
Requires:	template-glib-devel >= 3.28.0
Requires:	vte-devel >= 0.46
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

grep -rl /usr/bin/env src/plugins src/libide | xargs sed -i -e '1{
	s,^#!.*bin/env python3,#!%{__python3},
	s,^#!.*bin/env python$,#!%{__python},
}'

%build
%meson build \
%if %{with apidocs}
	-Ddocs=true \
	-Dhelp=true \
%endif
	-Dplugin_rls=true \
	-Dplugin_sysprof=%{__true_false sysprof} \
	-Dplugin_vagrant=true
# -Dplugin_deviced=true

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%if %{with apidocs}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnome-builder/en/{.buildinfo,_sources,objects.inv}
%endif

%find_lang %{name} --with-gnome

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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-builder
%dir %{_libdir}/gnome-builder
%dir %{_libdir}/gnome-builder/girepository-1.0
%{_libdir}/gnome-builder/girepository-1.0/Ide-%{apiver}.typelib
%dir %{_libdir}/gnome-builder/plugins
%attr(755,root,root) %{_libexecdir}/gnome-builder-clang
%attr(755,root,root) %{_libexecdir}/gnome-builder-git
%dir %{_datadir}/gnome-builder
%{_datadir}/gnome-builder/fonts
%{_datadir}/gnome-builder/icons

%{_libdir}/gnome-builder/plugins/cargo.plugin
%{_libdir}/gnome-builder/plugins/cargo_plugin.py

%{_libdir}/gnome-builder/plugins/copyright.plugin
%{_libdir}/gnome-builder/plugins/copyright_plugin.py
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.copyright.gschema.xml

%{_libdir}/gnome-builder/plugins/eslint.plugin
%{_libdir}/gnome-builder/plugins/eslint_plugin.py
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.eslint.gschema.xml

%{_libdir}/gnome-builder/plugins/find-other-file.plugin
%{_libdir}/gnome-builder/plugins/find_other_file.py

%{_libdir}/gnome-builder/plugins/gjs_symbols.plugin
%{_libdir}/gnome-builder/plugins/gjs_symbols.py

%{_libdir}/gnome-builder/plugins/go-langserv.plugin
%{_libdir}/gnome-builder/plugins/go_langserver_plugin.py

%{_libdir}/gnome-builder/plugins/gvls.plugin
%{_libdir}/gnome-builder/plugins/gvls_plugin.py

%{_libdir}/gnome-builder/plugins/html_preview.gresource
%{_libdir}/gnome-builder/plugins/html-preview.plugin
%{_libdir}/gnome-builder/plugins/html_preview.py

%{_libdir}/gnome-builder/plugins/jedi.plugin
%{_libdir}/gnome-builder/plugins/jedi_plugin.py

%{_libdir}/gnome-builder/plugins/jhbuild.plugin
%{_libdir}/gnome-builder/plugins/jhbuild_plugin.py

%{_libdir}/gnome-builder/plugins/make.plugin
%{_libdir}/gnome-builder/plugins/make_plugin.gresource
%{_libdir}/gnome-builder/plugins/make_plugin.py

%{_libdir}/gnome-builder/plugins/meson-templates.plugin
%{_libdir}/gnome-builder/plugins/meson_templates.gresource
%{_libdir}/gnome-builder/plugins/meson_templates.py

%{_libdir}/gnome-builder/plugins/mono.plugin
%{_libdir}/gnome-builder/plugins/mono_plugin.py

%{_libdir}/gnome-builder/plugins/npm.plugin
%{_libdir}/gnome-builder/plugins/npm_plugin.py

%{_libdir}/gnome-builder/plugins/phpize.plugin
%{_libdir}/gnome-builder/plugins/phpize_plugin.py

%{_libdir}/gnome-builder/plugins/python-gi-imports-completion.plugin
%{_libdir}/gnome-builder/plugins/python_gi_imports_completion.py

%{_libdir}/gnome-builder/plugins/gradle.plugin
%{_libdir}/gnome-builder/plugins/gradle_plugin.py

%{_libdir}/gnome-builder/plugins/maven.plugin
%{_libdir}/gnome-builder/plugins/maven_plugin.py

%{_libdir}/gnome-builder/plugins/rls.plugin
%{_libdir}/gnome-builder/plugins/rls_plugin.py

%{_libdir}/gnome-builder/plugins/stylelint.plugin
%{_libdir}/gnome-builder/plugins/stylelint_plugin.py
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.stylelint.gschema.xml

%{_libdir}/gnome-builder/plugins/waf.plugin
%{_libdir}/gnome-builder/plugins/waf_plugin.py

%if %{with sysprof}
# not installed since 3.28
#%{_libdir}/gnome-builder/plugins/sysprof.plugin
%endif

%{_libdir}/gnome-builder/plugins/vala-pack.plugin
%{_libdir}/gnome-builder/plugins/vala_pack_plugin.py

%{_libdir}/gnome-builder/plugins/valgrind.plugin
%{_libdir}/gnome-builder/plugins/valgrind_plugin.gresource
%{_libdir}/gnome-builder/plugins/valgrind_plugin.py

%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.clang.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gnome-code-assistance.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.rust-analyzer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%{_datadir}/gtksourceview-4/styles/Adwaita*.style-scheme.xml
%{_datadir}/gtksourceview-4/styles/builder*.style-scheme.xml
%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
%{_desktopdir}/org.gnome.Builder.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Builder-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Builder.svg
%{py3_sitedir}/gi/overrides/Ide.py

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-builder
%{_includedir}/gnome-builder-%{apiver}
%dir %{_datadir}/gnome-builder/gir-1.0
%{_datadir}/gnome-builder/gir-1.0/Ide-%{apiver}.gir
%dir %{_libdir}/gnome-builder/pkgconfig
%{_libdir}/gnome-builder/pkgconfig/gnome-builder-%{apiver}.pc

%if %{with apidocs}
%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/gnome-builder
%{_docdir}/gnome-builder/en

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libide
%endif
