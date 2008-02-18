%define name gwenrename
%define preversion beta3
%define version 1.1
%define release %mkrel 0.%{preversion}.1
%define qtdir   %{_prefix}/lib/qt3/%{_lib}

Name: 		%name
Version: 	%version
Release: 	%release
Summary: 	Series (batch) renaming tool
Source:  	%{name}-%{version}-%{preversion}.tar.gz
URL: 	        http://users.otenet.gr/~geosp/gwenrename/index.html
Group: 		File tools
License: 	GPL
BuildRoot: 	%_tmppath/%{name}-%{version}
BuildRequires:  kdelibs-devel 

%description
GwenRename is a series (batch) renaming tool. It was created as an external 
tool for GwenView, the image viewer for KDE, but it can be used from Konqueror
as well. As that, the files to be renamed are passed to it as command line 
parameters, through the service menus mechanism. It supports EXIF data 
extraction, file's timestamping and use of profiles.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %name-%{version}-%{preversion}

%build
QTDIR=%{qtdir}
export QTDIR
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#icons for rpmlint
mkdir -p %buildroot/{%_liconsdir,%_miconsdir,%_iconsdir}
ln -s %_datadir/icons/hicolor/64x64/apps/%name.png %buildroot/%_liconsdir
ln -s %_datadir/icons/hicolor/32x32/apps/%name.png %buildroot/%_iconsdir
ln -s %_datadir/icons/hicolor/16x16/apps/%name.png %buildroot/%_miconsdir


%find_lang %name

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog TODO INSTALL README
%_bindir/%name
%_datadir/apps/gwenview/tools/%name.desktop
%_datadir/apps/konqueror/servicemenus/konqgwenrename.desktop
%_datadir/applnk/Utilities/%name.desktop
%_datadir/apps/%name/*
%_datadir/icons/hicolor/16x16/apps/*
%_datadir/icons/hicolor/22x22/apps/*
%_datadir/icons/hicolor/32x32/apps/*
%_datadir/icons/hicolor/48x48/apps/*
%_datadir/icons/hicolor/64x64/apps/*
%_datadir/icons/locolor/16x16/apps/*
%_datadir/icons/locolor/32x32/apps/*
%_iconsdir/%{name}.png
%_miconsdir/%{name}.png
%_liconsdir/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT
