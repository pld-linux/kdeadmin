# TODO
# - unpackaged files
#   %{_pkgconfigdir}/system-tools-backends.pc
%define		_state		unstable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

%include	/usr/lib/rpm/macros.perl
Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	3.80.2
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/kde/unstable/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e0e9fe7d8d45380c44a4456d64c80805
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-knetworkconf-pld.patch
Patch2:		kde-ac260-lt.patch
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	rpm-devel >= 4.4.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	qt4-qmake
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon,
- KDat - Tape backup tool,
- KUser - KDE user setup tool,
- KSYSV - SYS V Init configuration,
- KPackage - KDE support for RPM,
- Kwuftpd - KDE FTP daemon configuration,
- Kcmlinuz - KDE Linux Kernel Configuration.

%description -l es
Herramientas administrativas para KDE. Incluidos en este paquete:
- KSYSV - editor de los archivos de iniciación sysV,
- KUser - herramienta de gestión de usuarios.

%description -l pl
Aplikacje administratorskie dla KDE. Pakiet zawiera:
- KCron - program cron,
- KDat - narzêdzie do wykonywania kopii zapasowych na ta¶mie,
- KUser - program do zarz±dzania kontami u¿ytkowników,
- KSYSV - program do konfiguracji startu systemu,
- KPackage - program do zarz±dzania pakietami,
- Kwuftpd - konfigurator demona FTP dla KDE,
- Kcmlinuz - konfigurator j±dra Linuksa dla KDE.

%package kcmlilo
Summary:	LILO Configurator
Summary(pl):	Konfigurator LILO
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
%ifarch %{ix86} %{x8664}
Requires:	lilo
%endif
Obsoletes:	kdeadmin-kcmlinuz < 8:3.4.0

%description kcmlilo
LILO configuration module for KDE Control Centre.

%description kcmlilo -l pl
Konfigurator LILO dla Centrum Sterowania KDE.

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron dla KDE
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kcron
KCron is an application for scheduling programs to run in the
background. It is a graphical user interface to cron, the UNIX system
scheduler.

%description kcron -l pl
KCron to aplikacja do planowania uruchamiania programów w tle. Jest to
graficzny interfejs do crona - systemowego programu do planowego
uruchamiania programów w systemach uniksowych.

%description kcron -l pt_BR
Gerenciador/agendador de tarefas e interface para o cron.

%package kpackage
Summary:	Package management front-end KDE
Summary(pl):	Program do manipulacji pakietami
Summary(pt_BR):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Provides:	kpackage
Obsoletes:	kpackage

%description kpackage
KPackage is a GUI interface to the RPM, Debian, Slackware and BSD
package managers. KPackage is part of the K Desktop Environment and,
as a result, it is designed to integrate with the KDE file manager.

%description kpackage -l pl
KPackage to graficzny interfejs do zarz±dców pakietów RPM, Debiana,
Slackware'a i BSD. KPackage to czê¶æ ¶rodowiska KDE, dziêki czemu
integruje siê z zarz±dc± plików KDE.

%description kpackage -l pt_BR
Interface para gerenciamento de pacotes RPM/DEB.

%package ksysv
Summary:	KDE Sys V Init configurator
Summary(pl):	Konfigurator Sys V Init dla KDE
Summary(pt_BR):	Interface para administração da inicialização System V
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description ksysv
A Sys V Init configurator for KDE.

%description ksysv -l pl
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init.

%description ksysv -l pt_BR
Interface para administração da inicialização System V, com
visualização e manipulação gráfica e facilitada dos serviços
disponíveis bem como dos níveis de execução.

%package kuser
Summary:	KDE User management tool
Summary(pl):	Administracja kontami dla KDE
Summary(pt_BR):	Ferramenta para administração de usuários
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kuser
A simple tool for managin system groups and user accounts from system.

%description kuser -l pl
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR
Ferramenta para administração de usuários do sistema.

%package knetworkconf
Summary:	KDE Network Configurator
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}

%description knetworkconf
KDE Network Configurator.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Archiving;/' \
#	kdat/kdat.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;System;/' \
#	kcron/kcron.desktop \
#	kpackage/kpackage.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;SystemSetup;/' \
#	ksysv/ksysv.desktop \
#	kuser/kuser.desktop
#for f in `find . -name '*.desktop'`; do
#	if grep -q '\[ven\]' $f; then
#		sed -i -e 's/\[ven\]/[ve]/' $f
#	fi
#done

# kill env, call interpreter directly, so rpm automatics could rule
#%{__sed} -i -e '1s,#!.*bin/env.*perl,#!%{__perl},' knetworkconf/backends/*.pl.in


%build
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang kcron	--with-kde
#%find_lang kdat	--with-kde
#%find_lang kpackage	--with-kde
#%find_lang ksysv	--with-kde
#%find_lang kuser	--with-kde
#%find_lang knetworkconf --with-kde
#%find_lang lilo-config	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files kcmlilo
%defattr(644,root,root,755)
%{_libdir}/kde4/kcm_lilo.la
%attr(755,root,root) %{_libdir}/kde4/kcm_lilo.so
%{_datadir}/services/lilo.desktop

%files kcron
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_datadir}/apps/kcron
%{_desktopdir}/kde/kcron.desktop
%{_iconsdir}/*/*/*/kcron.png

%files kpackage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
%{_libdir}/kde4/kfile*.la
%attr(755,root,root) %{_libdir}/kde4/kfile*.so
%{_datadir}/apps/kpackage
%{_datadir}/services/kfile*
%{_desktopdir}/kde/kpackage.desktop
%{_iconsdir}/*/*/*/kpackage.png

%files ksysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy

%files kuser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_datadir}/config.kcfg/kuser.kcfg
%{_desktopdir}/kde/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png

%files knetworkconf
%defattr(644,root,root,755)
%{_libdir}/kde4/kcm_knetworkconf*.la
%attr(755,root,root) %{_libdir}/kde4/kcm_knetworkconf*.so
%dir %{_datadir}/apps/knetworkconf
%dir %{_datadir}/apps/knetworkconf/backends
%attr(755,root,root) %{_datadir}/apps/knetworkconf/backends/*
%{_datadir}/apps/knetworkconf/pixmaps
%{_datadir}/services/kcm_knetworkconfmodule.desktop
%{_iconsdir}/*/*/*/knetworkconf.png
%{_iconsdir}/*/*/actions/network_*.png
%{_pkgconfigdir}/system-tools-backends.pc
