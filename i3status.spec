Summary:	Status bar generator for i3bar, dzen2, xmobar or similar programs
Name:		i3status
Version:	2.14
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	https://i3wm.org/i3status/%{name}-%{version}.tar.xz
# Source0-md5:	55a4bb05362947947bc93f705f5d71cd
URL:		https://i3wm.org/i3status/
BuildRequires:	alsa-lib-devel
BuildRequires:	asciidoc
BuildRequires:	bash
BuildRequires:	libconfuse-devel
BuildRequires:	libnl-devel
BuildRequires:	meson >= 0.45.0
BuildRequires:	ninja
BuildRequires:	perl-base
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
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
%meson build \
	-Dmans=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man*/%{name}.1*
