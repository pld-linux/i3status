Summary:	Status bar generator for i3bar, dzen2, xmobar or similar programs
Name:		i3status
Version:	2.13
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	https://i3wm.org/i3status/%{name}-%{version}.tar.bz2
# Source0-md5:	dd9001fb9ed732142d4d7194b77486cf
URL:		https://i3wm.org/i3status/
BuildRequires:	alsa-lib-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libconfuse-devel
BuildRequires:	libnl-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	xmlto
BuildRequires:	yajl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i3status is a program for generating a status bar for i3bar, dzen2,
xmobar or similar programs. It issues a small number of system calls,
as one generally wants to update such status lines every second so
that the bar is updated even under load. It saves a bit of energy by
being more efficient than shell commands.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-builddir \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man*/%{name}.1*
