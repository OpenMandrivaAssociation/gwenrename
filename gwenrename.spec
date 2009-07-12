%define name gwenrename
%define preversion beta6
%define version 1.1
%define release %mkrel 0.%{preversion}.1

Name: 		%name
Version: 	%version
Release: 	%release
Summary: 	Series (batch) renaming tool
Source:  	http://members.hellug.gr/sng/gwenrename/%{name}-%{version}-%{preversion}.tar.gz
URL: 	        http://users.otenet.gr/~geosp/gwenrename/index.html
Group: 		File tools
License: 	GPLv2+
BuildRoot: 	%_tmppath/%{name}-%{version}
BuildRequires:  kdelibs4-devel 

%description
GwenRename is a series (batch) renaming tool. It was created as an external 
tool for GwenView, the image viewer for KDE, but it can be used from Konqueror
as well. As that, the files to be renamed are passed to it as command line 
parameters, through the service menus mechanism. It supports EXIF data 
extraction, file's timestamping and use of profiles.

%prep
%setup -q -n %name-%{version}-%{preversion}

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name --with-html

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root,0755)
%doc ChangeLog README
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/ServiceMenus/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT
