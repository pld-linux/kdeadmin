#
%define		_state		stable
%define		_ver		3.2.3
##%define		_snap		040110

Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	%{_ver}
Release:	0.1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	4a39ce0d9abdd2dccb4531466ee7f229
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
Patch100:	%{name}-branch.diff
Patch0:		%{name}-vcategories.patch
Icon:		kde-admin.xpm
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	unsermake >= 040511
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
#BuildRequires:	lilo
BuildRequires:	pam-devel
BuildRequires:	rpm-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon,
- KDat - Tape backup tool,
- KUser - KDE user setup tool,
- KSYSV - SYS V Init configuration,
- KPackage - KDE support for RPM,
- Kwuftpd - KDE ftp daemon configuration,
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
Requires:	kdebase-core >= 9:%{version}
Requires:	lilo
Obsoletes:	%{name}-kcmlinuz < 8:3.1.93.031105-3

%description kcmlilo
LILO configuration module for KDE Control Centre.

%description kcmlilo -l pl
Konfigurator LILO dla KDE.

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuksa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kcmlinuz
A Linux kernel configuration module for KDE Control Centre.

%description kcmlinuz -l pl
Program do konfiguracji j±dra Linuksa.

%description kcmlinuz -l pt_BR
Configurador do Kernel Linux.

%package kdat
Summary:	Tape backup tool
Summary(pl):	Narzêdzie do wykonywania kopii zapasowych na ta¶mie
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdat

%description kdat
KDat is a tar-based tape archiver. It is designed to work with
multiple archives on a single tape. It was designed to provide a nice,
GUI front-end to tar that supported the fast selective extraction
features of the dds2tar program. It features:
- simple graphical interface to local filesystem and tape contents.
- multiple archives on the same physical tape.
- complete index of archives and files is stored on local hard disk.
- selective restore of files from an archive.
- backup profiles for frequently used backups.
- tape backup tool.

%description kdat -l pl
Narzêdzie do wykonywania kopii zapasowych na ta¶mie.

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron dla KDE
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kcron
KCron is an application for scheduling programs to run in the
background. It is a graphical user interface to cron, the UNIX system
scheduler.

%description kcron -l pl
Program "cron" w wersji dla KDE.

%description kcron -l pt_BR
Gerenciador/agendador de tarefas e interface para o cron.

%package kpackage
Summary:	RPM front-end KDE
Summary(pl):	Program do manipulacji pakietami
Summary(pt_BR):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Provides:	kpackage
Obsoletes:	kpackage

%description kpackage
KPackage is a GUI interface to the RPM, Debian, Slackware and BSD
package managers. KPackage is part of the K Desktop Environment and,
as a result, it is designed to integrate with the KDE file manager.

%description kpackage -l pl
Program do manipulowania pakietami w ¶rodowisku KDE.

%description kpackage -l pt_BR
Interface para gerenciamento de pacotes RPM/DEB.

%package ksysv
Summary:	KDE Sys V Init configurator
Summary(pl):	Konfigurator Sys V Init dla KDE
Summary(pt_BR):	Interface para administração da inicialização System V
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

%description kuser
A simple tool for managin system groups and user accounts from system.

%description kuser -l pl
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR
Ferramenta para administração de usuários do sistema.

%package kwuftpd
Summary:	KDE WU-FTP daemon configurator
Summary(pl):	Konfigurator demona WU-FTP dla KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Requires:	wu-ftpd

%description kwuftpd
WU-FTP daemon configurator for KDE.

%description kwuftpd -l pl
Narzêdzie do konfiguracji demona WU-FTP dla KDE.

%description kwuftpd -l pt_BR
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%prep
%setup -q
%patch100 -p1
%patch0 -p1

%build
# Do not check for lilo
rm lilo-config/configure.in.in
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
 	--with-pam=yes \
	--with-qt-libraries=%{_libdir} \
	--with-shadow

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%ifarch %{ix86}
%files kcmlilo
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_lilo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_lilo.so
%{_desktopdir}/kde/lilo.desktop
%endif

%files kcmlinuz
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_linuz.la
%attr(755,root,root) %{_libdir}/kde3/kcm_linuz.so
%{_datadir}/apps/kcmlinuz
%{_desktopdir}/kde/linuz.desktop

%files kcron
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_desktopdir}/kde/kcron.desktop
%{_iconsdir}/*/*/*/kcron.png
%{_kdedocdir}/en/kcron

%files kdat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat
%{_datadir}/apps/kdat
%{_desktopdir}/kde/kdat.desktop
%{_iconsdir}/[!l]*/*/*/kdat*
%{_kdedocdir}/en/kdat

%files kpackage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
%{_libdir}/kde3/kfile*.la
%attr(755,root,root) %{_libdir}/kde3/kfile*.so
%{_datadir}/apps/kpackage
%{_datadir}/mimelnk/application/x-debian-package.desktop
%{_datadir}/services/kfile*
%{_desktopdir}/kde/kpackage.desktop
%{_iconsdir}/*/*/*/kpackage.png
%{_kdedocdir}/en/kpackage

%files ksysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv
%{_datadir}/apps/ksysv
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_desktopdir}/kde/ksysv.desktop
%{_iconsdir}/*/*/*/ksysv.png
%{_iconsdir}/*/*/*/toggle_log.png
%{_kdedocdir}/en/ksysv

%files kuser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_desktopdir}/kde/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png
%{_kdedocdir}/en/kuser
