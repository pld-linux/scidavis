Summary:	Scientific Data Analysis and Visualization
Name:		scidavis
Version:	0.2.3
Release:	0.2
License:	GPL v2
Group:		Applications/Engineering
Source0:	http://downloads.sourceforge.net/scidavis/%{name}-%{version}.tar.bz2
# Source0-md5:	30d3f7c4e3702cec0bce8e34ea6112e7
Source1:	http://downloads.sourceforge.net/scidavis/%{name}-manual-0.1_2008-02-28.tar.bz2
# Source1-md5:	3527477cb0685da3ddfb0ee398ba6303
Patch0:		%{name}-manual.patch
Patch1:		%{name}-pro.patch
URL:		http://scidavis.sourceforge.net/
BuildRequires:	QtAssistant-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	gsl-devel
BuildRequires:	muparser-devel
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-devel
#BuildRequires:	qt4-devel
BuildRequires:	qwt-devel
BuildRequires:	qwtplot3d-devel
BuildRequires:	sip
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SciDAVis is a user-friendly data analysis and visualization program
primarily aimed at high-quality plotting of scientific data. It
strives to combine an intuitive, easy-to-use graphical user interface
with powerful features such as Python scriptability.

%package manual
Summary:	Additional manual for SciDAVis
Group:		Documentation

%description manual
This package contains the manual for SciDAVis.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1

sed -i -e 's/50/100/' scidavis/scidavis.xml

%build
cd scidavis
qmake-qt4 scidavis.pro
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd scidavis
rm -rf $RPM_BUILD_ROOT
%{__make} INSTALL_ROOT="$RPM_BUILD_ROOT" install
install -d $RPM_BUILD_ROOT%{_desktopdir}
desktop-file-install --vendor fedora \
	--dir $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT/%{_desktopdir}/scidavis.desktop

rm $RPM_BUILD_ROOT/%{_desktopdir}/scidavis.desktop

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install -D -pm 644 translations/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/

mkdir $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/mimetypes/
mkdir $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/mimetypes/
cp $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/scidavis.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/mimetypes/.
cp $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/scidavis.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/mimetypes/.
mv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/mimetypes/scidavis.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/mimetypes/application-x-sciprj.png
mv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/mimetypes/scidavis.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-sciprj.png

%post
%update_icon_cache hicolor
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
%update_icon_cache hicolor
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README gpl.txt
%exclude %{_sysconfdir}/scidavisrc.pyo
%exclude %{_sysconfdir}/scidavisrc.pyc
%attr(755,root,root) %{_bindir}/scidavis
#%{_libdir}/scidavis/
%{_desktopdir}/*
%{_datadir}/mime/packages/scidavis.xml
%{_datadir}/mimelnk/application/x-sciprj.desktop
%{_iconsdir}/hicolor/*/mimetypes/application-x-sciprj*
%{_iconsdir}/hicolor/*/apps/scidavis.*
%{_iconsdir}/locolor/*/apps/scidavis.*
%{_datadir}/scidavis
%{_sysconfdir}/scidavisrc.py

%files manual
%defattr(644,root,root,755)
%doc manual/*
