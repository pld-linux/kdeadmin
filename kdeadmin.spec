Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Name:		kdeadmin
Version:	2.2.1
Release:	2
Epoch:		7
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Icon:		kde-icon.xpm
Requires:	kdelibs = %{version}, pam 
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pam-devel 
BuildRequires:	rpm-devel
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%description -l pt_BR
Ferramentas administrativas para o KDE.

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}

%description kcron
Kde version of "CRON".

%description -l pl kcron
Program "cron" w wersji dla KDE.

%description -l pt_BR kcron
Gerenciador/agendador de tarefas e interface para o cron.

%package kuser
Summary:	KDE User management tool
Summary(pl):	administracja kontami dla KDE
Summary(pt_BR):	Ferramenta para administração de usuários
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}

%description kuser
A simple tool for adding/removing users from system and changing user
information.

%description -l pl kuser
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description -l pt_BR kuser
Ferramenta para administração de usuários do sistema.

%package kpackage
Summary:	RPM front-end KDE
Summary(pl):	Program do manipulacji pakietami.
Summary(pt_BR):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}

%description kpackage
Package front-end for KDE.

%description -l pl kpackage
Program do manipulowania pakietami w ¶rodowisku KDE.

%description -l pt_BR kpackage
Interface para gerenciamento de pacotes RPM/DEB.

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuxa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}

%description kcmlinuz
A Linux kernel configurator for KDE.

%description -l pl kcmlinuz
Program do konfiguracji j±dra Linuxa.

%description -l pt_BR kcmlinuz
Configurador do Kernel Linux.

%package ksysv
Summary:	KDE Sys V Init configurator	
Summary(pl):	Konfigurator Sys V Init dla KDE
Summary(pt_BR):	Interface para administração da inicialização System V
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}

%description ksysv
A Sys V Init configurator for KDE.

%description -l pl ksysv
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init

%description -l pt_BR ksysv
Interface para administração da inicialização System V, com
visualização e manipulação gráfica e facilitada dos serviços
disponíveis bem como dos níveis de execução.

%package kwuftpd
Summary:	KDE FTP daemon
Summary(pl):	Wu-FTP daemon for KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs = %{version}
Requires:	wu-ftpd

%description kwuftpd
Wu-FTP daemon for KDE.

%description -l pl kwuftpd
Zamiennik demona wu-ftp dla KDE.

%description -l pt_BR kwuftpd
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%prep
%setup -q

%build
KDEDIR=%{_prefix}
CXXFLAGS="%{rpmcflags} -Wall"
CFLAGS="%{rpmcflags} -Wall"
export KDEDIR

%configure2_13 \
	--prefix=%{_prefix} \
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

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCRON
#################################################
%files kcron
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron

%{_datadir}/doc/HTML/en/kcron/*
%{_applnkdir}/System/kcron.desktop
%{_datadir}/icons/*color/*x*/apps/kcron.png

#################################################
#             KPACKAGE
#################################################
%files kpackage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage

%{_datadir}/doc/HTML/en/kpackage/*
%{_applnkdir}/System/kpackage.desktop
%{_datadir}/apps/kpackage
%{_datadir}/icons/*color/*x*/apps/kpackage.png
%{_datadir}/mimelnk/application/x-debian-package.desktop

#################################################
#             KCMLINUZ
#################################################
%files kcmlinuz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcm*
%attr(755,root,root) %{_libdir}/kde2/libkcm*

%{_applnkdir}/Settings/System/li*.desktop
%{_datadir}/apps/kcmlinuz

#################################################
#             KSYSV
#################################################
%files ksysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv

%{_datadir}/doc/HTML/en/ksysv/*
%{_datadir}/apps/ksysv
%{_datadir}/icons/*color/*x*/apps/ksysv.png
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_applnkdir}/System/ksysv.desktop

#################################################
#             KUSER
#################################################
%files kuser
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/kuser

%{_datadir}/doc/HTML/en/kuser/*
%{_applnkdir}/System/kuser.desktop
%{_datadir}/apps/kuser
%{_datadir}/icons/*color/*x*/apps/kuser.png

#################################################
#             KWUFTPD
#################################################
%files kwuftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwuftpd

%{_datadir}/doc/HTML/en/kwuftpd/*
%{_applnkdir}/System/kwuftpd.desktop
