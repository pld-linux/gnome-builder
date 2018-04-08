# TODO:
# - fix warning: jedi not found, python auto-completion not possible.
#
# Conditional build:
%bcond_without	sysprof		# sysprof system profiler plugin
%bcond_with	vala_pack	# vala pack plugin
#
Summary:	IDE for writing GNOME-based software
Summary(pl.UTF-8):	IDE do tworzenia oprogramowania opartego na GNOME
Name:		gnome-builder
Version:	3.28.0
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-builder/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	5963331e96922e2caf6bf66b36ad4b10
URL:		https://wiki.gnome.org/Apps/Builder
BuildRequires:	appstream-glib-devel
BuildRequires:	clang-devel >= 3.5
BuildRequires:	desktop-file-utils
BuildRequires:	devhelp-devel >= 3.26.0
BuildRequires:	enchant-devel >= 1.6.0
BuildRequires:	flatpak-devel >= 0.8.0
# -std=gnu11 for C
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gjs-devel >= 1.42.0
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gobject-introspection-devel >= 1.48.0
BuildRequires:	gspell-devel >= 1.2.0
BuildRequires:	gtk+3-devel >= 3.22.1
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	gtk-webkit4-devel >= 2.12.0
BuildRequires:	gtksourceview3-devel >= 3.22.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	json-glib-devel >= 1.2.0
BuildRequires:	jsonrpc-glib-devel >= 3.28.0
BuildRequires:	libdazzle-devel
BuildRequires:	libgit2-glib-devel >= 0.25.0
BuildRequires:	libpeas-devel >= 1.22.0
BuildRequires:	libsoup-devel >= 2.52.0
# C++11
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	llvm-devel >= 3.5
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pango-devel >= 1:1.38.0
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel >= 1:3.2.3
BuildRequires:	python3-pygobject3-devel >= 3.22.0
BuildRequires:	rpmbuild(macros) >= 1.522
%{?with_sysprof:BuildRequires:	sysprof-ui-devel >= 3.28.0}
BuildRequires:	tar >= 1:1.22
BuildRequires:	template-glib-devel
BuildRequires:	vala >= 2:0.30.0.55
BuildRequires:	vala-jsonrpc-glib
BuildRequires:	vala-libgit2-glib >= 0.24.0
BuildRequires:	vala-template-glib
BuildRequires:	vte-devel >= 0.46
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildConflicts:	gd-devel
Requires(post,postun):	glib2 >= 1:2.50.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	ctags
Requires:	devhelp-libs >= 3.26.0
Requires:	enchant >= 1.6.0
Requires:	flatpak-libs >= 0.6.9
Requires:	gjs >= 1.42.0
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.22.1
Requires:	gtk-webkit4 >= 2.12.0
Requires:	gtksourceview3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	json-glib >= 1.2.0
Requires:	libgit2-glib >= 0.24.0
Requires:	libpeas >= 1.22.0
Requires:	libsoup >= 2.52.0
Requires:	libxml2 >= 1:2.9.0
Requires:	pango >= 1:1.38.0
Requires:	python3-modules >= 1:3.2.3
Requires:	python3-pygobject3 >= 3.22.0
%{?with_sysprof:Requires:	sysprof-ui-libs >= 3.28.0}
Requires:	vte >= 0.46
Suggests:	python3-lxml
Obsoletes:	gnome-builder-apidocs
Obsoletes:	gnome-builder-mm
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
Requires:	glib2-devel >= 1:2.50.0
Requires:	gtk+3-devel >= 3.22.1
Requires:	gtksourceview3-devel >= 3.22.0
Requires:	pango-devel >= 1:1.38.0
Obsoletes:	gnome-builder-mm-devel

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

%prep
%setup -q

%build
%meson build \
	-Dwith_sysprof=%{__true_false sysprof} \
	-Dwith_vala_pack=%{__true_false vala_pack}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

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
%doc AUTHORS NEWS README build/doc/en
%attr(755,root,root) %{_bindir}/dazzle-list-counters
%attr(755,root,root) %{_bindir}/gnome-builder
%attr(755,root,root) %{_bindir}/gnome-builder-cli
%attr(755,root,root) %{_libexecdir}/gnome-builder-worker
%dir %{_libdir}/gnome-builder
%attr(755,root,root) %{_libdir}/libdazzle-1.0.so.0
%attr(755,root,root) %{_libdir}/gnome-builder/libgstyle-private.so.*.*.*
%attr(755,root,root) %{_libdir}/gnome-builder/libgstyle-private.so.0
%attr(755,root,root) %{_libdir}/gnome-builder/libide-1.0.so
%attr(755,root,root) %{_libdir}/gnome-builder/libgd.so
%attr(755,root,root) %{_libdir}/gnome-builder/libtemplate_glib-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/gnome-builder/libtemplate_glib-1.0.so.0
%dir %{_libdir}/gnome-builder/girepository-1.0
%{_libdir}/gnome-builder/girepository-1.0/Dazzle-1.0.typelib
%{_libdir}/gnome-builder/girepository-1.0/Gstyle-1.0.typelib
%{_libdir}/gnome-builder/girepository-1.0/Ide-1.0.typelib
%{_libdir}/gnome-builder/girepository-1.0/Template-1.0.typelib
%dir %{_libdir}/gnome-builder/plugins
%dir %{_datadir}/gnome-builder
%{_datadir}/gnome-builder/fonts
%dir %{_datadir}/gnome-builder/plugins

%{_libdir}/gnome-builder/plugins/autotools.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libautotools-plugin.so

%{_libdir}/gnome-builder/plugins/beautifier.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libbeautifier_plugin.so
%{_datadir}/gnome-builder/plugins/beautifier_plugin

%{_libdir}/gnome-builder/plugins/c-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libc-pack-plugin.so

%{_libdir}/gnome-builder/plugins/cargo.plugin
%{_libdir}/gnome-builder/plugins/cargo_plugin.py

%{_libdir}/gnome-builder/plugins/clang.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libclang-plugin.so

%{_libdir}/gnome-builder/plugins/code-index.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libcode-index-plugin.so

%{_libdir}/gnome-builder/plugins/command-bar.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libcommand-bar.so

%{_libdir}/gnome-builder/plugins/comment-code.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libcomment-code-plugin.so

%{_libdir}/gnome-builder/plugins/create-project.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libcreate-project-plugin.so

%{_libdir}/gnome-builder/plugins/ctags.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libctags-plugin.so

%{_libdir}/gnome-builder/plugins/devhelp.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libdevhelp-plugin.so

%{_libdir}/gnome-builder/plugins/documentation-card.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libdocumentation-card-plugin.so

%{_libdir}/gnome-builder/plugins/eslint.plugin
%{_libdir}/gnome-builder/plugins/eslint_plugin
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.eslint.gschema.xml

%{_libdir}/gnome-builder/plugins/file-search.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libfile-search.so

%{_libdir}/gnome-builder/plugins/find-other-file.plugin
%{_libdir}/gnome-builder/plugins/find_other_file.py

%{_libdir}/gnome-builder/plugins/gcc.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libgcc-plugin.so

%{_libdir}/gnome-builder/plugins/gdb.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libgdb-plugin.so

%{_libdir}/gnome-builder/plugins/gettext.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libgettext-plugin.so

%{_libdir}/gnome-builder/plugins/git.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libgit-plugin.so

%{_libdir}/gnome-builder/plugins/gnome-code-assistance.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libgnome-code-assistance-plugin.so

%{_libdir}/gnome-builder/plugins/history.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libhistory-plugin.so

%{_libdir}/gnome-builder/plugins/html-completion.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libhtml-completion-plugin.so

%{_libdir}/gnome-builder/plugins/html-preview.plugin
%{_libdir}/gnome-builder/plugins/html_preview_plugin
%{_datadir}/gnome-builder/plugins/html_preview_plugin

%{_libdir}/gnome-builder/plugins/jedi.plugin
%{_libdir}/gnome-builder/plugins/jedi_plugin.py

%{_libdir}/gnome-builder/plugins/jhbuild.plugin
%{_libdir}/gnome-builder/plugins/jhbuild_plugin.py

%{_libdir}/gnome-builder/plugins/meson.plugin
%{_libdir}/gnome-builder/plugins/meson_plugin

%{_libdir}/gnome-builder/plugins/meson-templates.plugin
%{_libdir}/gnome-builder/plugins/meson_templates
%{_datadir}/gnome-builder/plugins/meson_templates

%{_libdir}/gnome-builder/plugins/mingw.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libmingw-plugin.so

%{_libdir}/gnome-builder/plugins/notification.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libnotification-plugin.so

%{_libdir}/gnome-builder/plugins/npm.plugin
%{_libdir}/gnome-builder/plugins/npm_plugin.py

%{_libdir}/gnome-builder/plugins/project-tree.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libproject-tree-plugin.so

%{_libdir}/gnome-builder/plugins/python-gi-imports-completion.plugin
%{_libdir}/gnome-builder/plugins/python_gi_imports_completion.py

%{_libdir}/gnome-builder/plugins/python-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libpython-pack-plugin.so

%{_libdir}/gnome-builder/plugins/retab.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libretab-plugin.so

%{_libdir}/gnome-builder/plugins/rust-langserv.plugin
%{_libdir}/gnome-builder/plugins/rust_langserv_plugin.py

%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libspellcheck-plugin.so
%{_libdir}/gnome-builder/plugins/spellcheck.plugin

%{_libdir}/gnome-builder/plugins/support.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libsupport-plugin.so

%{_libdir}/gnome-builder/plugins/symbol-tree.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libsymbol-tree-plugin.so

%{_libdir}/gnome-builder/plugins/sysmon.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libsysmon.so

%if %{with sysprof}
%{_libdir}/gnome-builder/plugins/sysprof.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libsysprof-plugin.so
%endif

%{_libdir}/gnome-builder/plugins/terminal.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libterminal.so

%{_libdir}/gnome-builder/plugins/todo.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libtodo-plugin.so

%if %{with vala_pack}
%{_libdir}/gnome-builder/plugins/vala-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libvala-pack-plugin.so
%endif

%{_libdir}/gnome-builder/plugins/xml-pack.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libxml-pack-plugin.so

%{_libdir}/gnome-builder/plugins/color-picker.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libcolor-picker-plugin.so

%{_libdir}/gnome-builder/plugins/flatpak.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libflatpak-plugin.so

%{_libdir}/gnome-builder/plugins/quick-highlight.plugin
%attr(755,root,root) %{_libdir}/gnome-builder/plugins/libquick-highlight-plugin.so

%{_libdir}/gnome-builder/plugins/cmake.plugin
%{_libdir}/gnome-builder/plugins/cmake_plugin

%{_libdir}/gnome-builder/plugins/make.plugin
%{_libdir}/gnome-builder/plugins/make_plugin

%{_libdir}/gnome-builder/plugins/mono.plugin
%{_libdir}/gnome-builder/plugins/mono_plugin.py

%{_libdir}/gnome-builder/plugins/phpize.plugin
%{_libdir}/gnome-builder/plugins/phpize_plugin.py

%{_libdir}/gnome-builder/plugins/rustup.plugin
%{_libdir}/gnome-builder/plugins/rustup_plugin

%{_libdir}/gnome-builder/plugins/valgrind.plugin
%{_libdir}/gnome-builder/plugins/valgrind_plugin.gresource
%{_libdir}/gnome-builder/plugins/valgrind_plugin.py

%{_datadir}/appdata/org.gnome.Builder.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gnome-code-assistance.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/builder*.xml
%{_desktopdir}/org.gnome.Builder.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Builder.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Builder-symbolic.svg
%{py3_sitedir}/gi/overrides/Ide.py

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdazzle-1.0.so
%attr(755,root,root) %{_libdir}/gnome-builder/libgstyle-private.so
%attr(755,root,root) %{_libdir}/gnome-builder/libtemplate_glib-1.0.so
%{_includedir}/gnome-builder
%dir %{_datadir}/gnome-builder/gir-1.0
%{_datadir}/gnome-builder/gir-1.0/Dazzle-1.0.gir
%{_datadir}/gnome-builder/gir-1.0/Gstyle-1.0.gir
%{_datadir}/gnome-builder/gir-1.0/Ide-1.0.gir
%{_datadir}/gnome-builder/gir-1.0/Template-1.0.gir
%dir %{_libdir}/gnome-builder/pkgconfig
%{_libdir}/gnome-builder/pkgconfig/libdazzle-1.0.pc
%{_libdir}/gnome-builder/pkgconfig/libide-1.0.pc
%{_libdir}/gnome-builder/pkgconfig/template-glib-1.0.pc

%files -n vala-gnome-builder
%defattr(644,root,root,755)
%dir %{_datadir}/gnome-builder/vapi
%{_datadir}/gnome-builder/vapi/gstyle-private.deps
%{_datadir}/gnome-builder/vapi/gstyle-private.vapi
%{_datadir}/gnome-builder/vapi/libdazzle-1.0.deps
%{_datadir}/gnome-builder/vapi/libdazzle-1.0.vapi
%{_datadir}/gnome-builder/vapi/libide-1.0.deps
%{_datadir}/gnome-builder/vapi/libide-1.0.vapi
%{_datadir}/gnome-builder/vapi/template-glib-1.0.deps
%{_datadir}/gnome-builder/vapi/template-glib-1.0.vapi
