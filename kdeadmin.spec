
%define		_state		stable
%define		_ver		3.3.2

%define		_minlibsevr	9:3.3.2
%define		_minbaseevr	9:3.3.2

Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2	
# Source0-md5:	d12b12925dda1f4e6ba162e856730a5e
Icon:		kde-admin.xpm
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
BuildRequires:	rpm-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	lilo
Obsoletes:	kdeadmin-kcmlinuz < 8:3.1.93.031105-3

%description kcmlilo
LILO configuration module for KDE Control Centre.

%description kcmlilo -l pl
Konfigurator LILO dla Centrum Sterowania KDE.

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuksa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kcmlinuz
A Linux kernel configuration module for KDE Control Centre.

%description kcmlinuz -l pl
Program do konfiguracji j±dra Linuksa dla Centrum Sterowania KDE.

%description kcmlinuz -l pt_BR
Configurador do Kernel Linux.

%package kdat
Summary:	Tape backup tool
Summary(pl):	Narzêdzie do wykonywania kopii zapasowych na ta¶mie
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
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
KDat to oparty na tarze program do wykonywania kopii zapasowych na
ta¶mie. Jest przeznaczony do dzia³ania z wieloma archiwami na
jednej tasiemce. By³ projektowany, by zapewniæ mi³y, graficzny
interfejs do tara, obs³uguj±cy mo¿liwo¶ci najszybszego, selektywnego
odczytywania z programu dds2tar. Mo¿liwo¶ci programu KDat:
- prosty graficzny interfejs dla zawarto¶ci systemu plików i ta¶my
- obs³uga wielu archiwów na tej samej fizycznej ta¶mie
- pe³ny indeks archiwów i plików zapisywany na lokalnym dysku
- wybiórcze odtwarzanie plików z archiwum
- profile backupów dla czêsto u¿ywanych kopii
- narzêdzie do tworzenia kopii zapasowych na ta¶mie.

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

%package kwuftpd
Summary:	KDE WU-FTP daemon configurator
Summary(pl):	Konfigurator demona WU-FTP dla KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Requires:	wu-ftpd

%description kwuftpd
WU-FTP daemon configurator for KDE.

%description kwuftpd -l pl
Narzêdzie do konfiguracji demona WU-FTP dla KDE.

%description kwuftpd -l pt_BR
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%prep
%setup -q

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Archiving;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kdat/kdat.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;System;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kcron/kcron.desktop \
	kpackage/kpackage.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;System;X-Administration;/' \
	-e 's/Terminal=0/Terminal=false/' \
	ksysv/ksysv.desktop \
	kuser/kuser.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

# Do not check for lilo

rm lilo-config/configure.in.in

cp %{_datadir}/automake/config.sub admin

export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
 	--with-pam=yes \
	--with-qt-libraries=%{_libdir} \
	--with-shadow \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

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

%files kcron -f kcron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_desktopdir}/kde/kcron.desktop
%{_iconsdir}/*/*/*/kcron.png
%{_kdedocdir}/en/kcron

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
%{_datadir}/config.kcfg/kuser.kcfg
%{_desktopdir}/kde/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png
