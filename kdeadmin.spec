
%define         _state          snapshots
%define         _ver		3.1.93
%define		_snap		031105

Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	%{_ver}.%{_snap}
Release:	3
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	7c93ded2807dbd77898a92c92d7da88e
Patch0:		%{name}-vcategories.patch
Icon:		kde-icon.xpm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	lilo
BuildRequires:	pam-devel
BuildRequires:	rpm-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon
- KDat - Tape backup tool
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
- KDat - Narzêdzie do wykonywania kopii zapasowych na ta¶mie.
- KUser - Program do zarz±dzania kontami u¿ytkowników
- KSYSV - Program do konfiguracji startu systemu
- KPackage - Program do zarz±dzania pakietami
- Kwuftpd - Demon FTP dla KDE
- Kcmlinuz - Konfigurator j±dra Linuxa dla KDE

%package kcmlilo
Summary:	LILO Configurator
Summary(pl):	Konfigurator LILO
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	lilo
Obsoletes:	%{name}-kcmlinuz < 8:3.1.93.031105-3

%description kcmlilo
LILO configurator for KDE.

%description kcmlilo -l pl
Konfigurator LILO dla KDE.

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuksa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kcmlinuz
A Linux kernel configurator for KDE.

%description kcmlinuz -l pl
Program do konfiguracji j±dra Linuksa.

%description kcmlinuz -l pt_BR
Configurador do Kernel Linux.

%package kdat
Summary:	Tape backup tool
Summary(pl):	Narzêdzie do wykonywania kopii zapasowych na ta¶mie
Group:		X11/Applications
Requires:       kdebase-core >= 9:%{version}
Obsoletes:	kdat

%description kdat
Tape backup tool.

%description kdat -l pl
Narzêdzie do wykonywania kopii zapasowych na ta¶mie.

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kcron
Kde version of "CRON".

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
Package front-end for KDE.

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
A simple tool for adding/removing users from system and changing user
information.

%description kuser -l pl
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR
Ferramenta para administração de usuários do sistema.

%package kwuftpd
Summary:	KDE FTP daemon
Summary(pl):	Wu-FTP daemon for KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Requires:	wu-ftpd

%description kwuftpd
Wu-FTP daemon for KDE.

%description kwuftpd -l pl
Zamiennik demona wu-ftp dla KDE.

%description kwuftpd -l pt_BR
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build

for f in `find . -name *.desktop` ; do
	sed -i 's/\[nb\]/\[no\]/g' $f
done

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
 	--with-pam=yes \
	--with-shadow

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kcron	--with-kde
%find_lang kdat		--with-kde
%find_lang kpackage	--with-kde
%find_lang ksysv	--with-kde
%find_lang kuser	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files kcmlilo
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_lilo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_lilo.so
%{_desktopdir}/kde/lilo.desktop

%files kcmlinuz
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_linuz.la
%attr(755,root,root) %{_libdir}/kde3/kcm_linuz.so
%{_datadir}/apps/kcmlinuz
%{_desktopdir}/kde/linuz.desktop

%files kcron -f kcron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_desktopdir}/kde/kcron.desktop
%{_iconsdir}/*/*/*/kcron.png

%files kdat -f kdat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat
%{_datadir}/apps/kdat
%{_desktopdir}/kde/kdat.desktop
%{_iconsdir}/[!l]*/*/*/kdat*

%files kpackage -f kpackage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
%{_libdir}/kde3/kfile*.la
%attr(755,root,root) %{_libdir}/kde3/kfile*.so
%{_datadir}/apps/kpackage
%{_datadir}/mimelnk/application/x-debian-package.desktop
%{_datadir}/services/kfile*
%{_desktopdir}/kde/kpackage.desktop
%{_iconsdir}/*/*/*/kpackage.png

%files ksysv -f ksysv.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv
%{_datadir}/apps/ksysv
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_desktopdir}/kde/ksysv.desktop
%{_iconsdir}/*/*/*/ksysv.png
%{_iconsdir}/*/*/*/toggle_log.png

%files kuser -f kuser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_desktopdir}/kde/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png
