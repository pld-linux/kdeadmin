%define		_ver		3.0.1
#define		_sub_ver
%define		_rel		2

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Name:		kdeadmin
Version:	%{_version}
Release:	%{_release}
Epoch:		7
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Icon:		kde-icon.xpm
Requires:	kdelibs = %{version}
Requires:	pam
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
# Required by kpackage (RPM frontend). Dependency taken from librpm.la
# by libtool.
BuildRequires:	db1-devel
BuildRequires:	db3-devel
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	rpm-devel
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon
- KUser - KDE user setup tool
- KSYSV - SYS V Init configuration
- KPackage - KDE support for RPM
- Kwuftpd - KDE ftp daemon
- Kcmlinuz - KDE Linux Kernel Configuration

%description -l es
Herramientas administrativas para KDE. Incluidos en este paquete:
- KSYSV - editor de los archivos de iniciación sysV,
- KUser - herramienta de gestión de usuarios.

%description -l pl
Aplikacje administratorskie dla KDE. Pakiet zawiera:
- KCron - Program cron
- KUser - Program do zarz±dzania kontami u¿ytkowników
- KSYSV - Program do konfiguracji startu systemu
- KPackage - Przegl±darka pakietów
- Kwuftpd - Demon FTP dla KDE
- Kcmlinuz - Konfigurator j±dra Linuxa dla KDE

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kcron
Kde version of "CRON".

%description kcron -l pl
Program "cron" w wersji dla KDE.

%description kcron -l pt_BR
Gerenciador/agendador de tarefas e interface para o cron.

%package kuser
Summary:	KDE User management tool
Summary(pl):	administracja kontami dla KDE
Summary(pt_BR):	Ferramenta para administração de usuários
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kuser
A simple tool for adding/removing users from system and changing user
information.

%description kuser -l pl
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR
Ferramenta para administração de usuários do sistema.

%package kpackage
Summary:	RPM front-end KDE
Summary(pl):	Program do manipulacji pakietami.
Summary(pt_BR):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kpackage
Package front-end for KDE.

%description kpackage -l pl
Program do manipulowania pakietami w ¶rodowisku KDE.

%description kpackage -l pt_BR
Interface para gerenciamento de pacotes RPM/DEB.

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuxa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kcmlinuz
A Linux kernel configurator for KDE.

%description kcmlinuz -l pl
Program do konfiguracji j±dra Linuxa.

%description kcmlinuz -l pt_BR
Configurador do Kernel Linux.

%package ksysv
Summary:	KDE Sys V Init configurator
Summary(pl):	Konfigurator Sys V Init dla KDE
Summary(pt_BR):	Interface para administração da inicialização System V
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description ksysv
A Sys V Init configurator for KDE.

%description ksysv -l pl
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init

%description ksysv -l pt_BR
Interface para administração da inicialização System V, com
visualização e manipulação gráfica e facilitada dos serviços
disponíveis bem como dos níveis de execução.

%package kwuftpd
Summary:	KDE FTP daemon
Summary(pl):	Wu-FTP daemon for KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Requires:	kdelibs = %{version}
Requires:	wu-ftpd

%description kwuftpd
Wu-FTP daemon for KDE.

%description kwuftpd -l pl
Zamiennik demona wu-ftp dla KDE.

%description kwuftpd -l pt_BR
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%package kdat
Summary:	Tape backup tool
Summary(pl):	Narzêdzie do wykonywania kopii zapasowych na ta¶mie
Group:		X11/Applications
Requires:       kdelibs = %{version}

%description kdat
Tape backup tool.

%description kdat -l pl
Narzêdzie do wykonywania kopii zapasowych na ta¶mie.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
CXXFLAGS="%{rpmcflags} -Wall"
CFLAGS="%{rpmcflags} -Wall"
%configure \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
	--with-quota \
	--with-shadow \
	--with-rpm \
 	--with-pam="yes" \
	--with-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
KDEDIR=%{_prefix} ; export KDEDIR
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Settings/{[!K]*,KDE}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang kdat --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCRON
#################################################
%files kcron
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron

%{_htmldir}/en/kcron
%{_applnkdir}/System/kcron.desktop
%{_datadir}/pixmaps/*color/*x*/apps/kcron.png

#################################################
#             KPACKAGE
#################################################
%files kpackage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage

%{_htmldir}/en/kpackage
%{_applnkdir}/System/kpackage.desktop
%{_datadir}/apps/kpackage
%{_datadir}/pixmaps/*color/*x*/apps/kpackage.png
%{_datadir}/mimelnk/application/x-debian-package.desktop

#################################################
#             KCMLINUZ
#################################################
%files kcmlinuz
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkcm*
%attr(755,root,root) %{_libdir}/kde3/kcm_li*.??

%{_applnkdir}/Settings/KDE/System/li*.desktop
%{_datadir}/apps/kcmlinuz

#################################################
#             KSYSV
#################################################
%files ksysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv

%{_htmldir}/en/ksysv
%{_datadir}/apps/ksysv
%{_datadir}/pixmaps/*color/*x*/apps/ksysv.png
%{_datadir}/pixmaps/*color/*x*/actions/toggle_log.png
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_applnkdir}/System/ksysv.desktop

#################################################
#             KUSER
#################################################
%files kuser
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/kuser

%{_htmldir}/en/kuser
%{_applnkdir}/System/kuser.desktop
%{_datadir}/apps/kuser
%{_datadir}/pixmaps/*color/*x*/apps/kuser.png

#################################################
#             KWUFTPD
#################################################
%files kwuftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwuftpd

%{_htmldir}/en/kwuftpd
%{_applnkdir}/System/kwuftpd.desktop

#################################################
#             KWUFTPD
#################################################
%files kdat -f kdat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat
%{_datadir}/apps/kdat
%{_pixmapsdir}/*/*/*/kdat*
%{_applnkdir}/Utilities/kdat.desktop
