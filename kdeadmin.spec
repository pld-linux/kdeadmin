#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	3.0.4
Release:	3
Epoch:		7
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-kcron.png
Patch0:		%{name}-fix-kcron-mem-leak.patch
Patch1:		%{name}-fix-mem-leak-in-kpackage.patch
Patch2:		%{name}-remove-initial-preference.patch
Patch3:		%{name}-kdat-fix-mem-leak.patch
Patch4:		%{name}-fix-ksysv-mem-leak.patch
Patch5:		%{name}-fix-kpackage-mem-leak.patch
Patch6:		%{name}-kdat-use-kintinput.patch
Patch7:		%{name}-fix-kwuftpd-fix-bug-45142.patch
Patch8:		%{name}-kuserconfig.patch
Patch9:		%{name}-desktop.patch
Icon:		kde-icon.xpm
Requires:	kdelibs = %{version}
Requires:	pam
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
BuildRequires:	bzip2-devel
# Required by kpackage (RPM frontend). Dependency taken from librpm.la
# by libtool.
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
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
Summary(pl):	Program do manipulacji pakietami
Summary(pt_BR):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Requires:	kdelibs = %{version}
Provides:	kpackage
Obsoletes:	kpackage

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
Requires:	kdelibs = %{version}

%description kdat
Tape backup tool.

%description kdat -l pl
Narzêdzie do wykonywania kopii zapasowych na ta¶mie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags} -Wall"
CFLAGS="%{rpmcflags} -Wall"
%configure \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
	--with-quota \
	--with-shadow \
	--with-rpm \
 	--with-pam="yes" \
	--disable-rpath \
	--with-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE

KDEDIR=%{_prefix} ; export KDEDIR
%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Settings/{[!K]*,KDE}

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{kdat,kpackage,ksysv,kuser}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/kcron.png

%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
# moved
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{kdat,kpackage,ksysv,kuser}.png
# resized
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/kcron.png
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

%find_lang kcmlilo	--with-kde
%find_lang kcmlinuz	--with-kde
cat kcmlilo.lang >> kcmlinuz.lang
%find_lang kcron	--with-kde
%find_lang kdat		--with-kde
%find_lang kpackage	--with-kde
%find_lang ksysctrl	--with-kde
%find_lang ksysv	--with-kde
cat ksysctrl.lang >> ksysv.lang
%find_lang kuser	--with-kde
%find_lang kwuftpd	--with-kde
%find_lang secpolicy	--with-kde
cat secpolicy.lang >> ksysv.lang

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCMLINUZ
#################################################
%files kcmlinuz -f kcmlinuz.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkcm*
%attr(755,root,root) %{_libdir}/kde3/kcm_li*.??
%{_applnkdir}/Settings/KDE/System/li*.desktop
%{_datadir}/apps/kcmlinuz

#################################################
#             KCRON
#################################################
%files kcron -f kcron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_applnkdir}/System/kcron.desktop
%{?_with_pixmapsubdirs:%{_datadir}/pixmaps/*color/*x*/apps/kcron.png}
%{_datadir}/pixmaps/kcron.png

#################################################
#             KDAT
#################################################
%files kdat -f kdat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat
%{_datadir}/apps/kdat
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/kdat.png}
%{_pixmapsdir}/kdat.png
%{_applnkdir}/Utilities/kdat.desktop

#################################################
#             KPACKAGE
#################################################
%files kpackage -f kpackage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
%{_applnkdir}/System/kpackage.desktop
%{_datadir}/apps/kpackage
%{?_with_pixmapsubdirs:%{_datadir}/pixmaps/*color/*x*/apps/kpackage.png}
%{_datadir}/pixmaps/kpackage.png
%{_datadir}/mimelnk/application/x-debian-package.desktop

#################################################
#             KSYSV
#################################################
%files ksysv -f ksysv.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv
%{_datadir}/apps/ksysv
%{?_with_pixmapsubdirs:%{_datadir}/pixmaps/*color/*x*/apps/ksysv.png}
%{_datadir}/pixmaps/ksysv.png
%{_datadir}/pixmaps/*color/*x*/actions/toggle_log.png
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_applnkdir}/System/ksysv.desktop

#################################################
#             KUSER
#################################################
%files kuser -f kuser.lang
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/kuser
%{_applnkdir}/System/kuser.desktop
%{_datadir}/apps/kuser
%{?_with_pixmapsubdirs:%{_datadir}/pixmaps/*color/*x*/apps/kuser.png}
%{_datadir}/pixmaps/kuser.png

#################################################
#             KWUFTPD
#################################################
%files kwuftpd -f kwuftpd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwuftpd
%{_applnkdir}/System/kwuftpd.desktop
