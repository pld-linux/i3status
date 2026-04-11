Summary:	Status bar generator for i3bar, dzen2, xmobar or similar programs
Summary(pl.UTF-8):	Generator paska stanu dla programów i3bar, dzen2, xmobar i podobnych
Name:		i3status
Version:	2.15
Release:	2
License:	BSD
Group:		X11/Window Managers
Source0:	https://i3wm.org/i3status/%{name}-%{version}.tar.xz
# Source0-md5:	51f19cbb0dc91c831b2e0f1bd3c8448f
URL:		https://i3wm.org/i3status/
BuildRequires:	alsa-lib-devel
BuildRequires:	asciidoc
BuildRequires:	bash
BuildRequires:	libconfuse-devel
BuildRequires:	libnl-devel >= 3.0
BuildRequires:	meson >= 0.45.0
BuildRequires:	ninja >= 1.5
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

%description -l pl.UTF-8
i3status to program do generowania paska stanu dla programów i3bar,
dzen2, xmobar i podobnych. Wykonuje niewielką liczbę wywołań
systemowych, żeby móc uaktualniać linie stanu w każdej sekundzie,
nawet przy dużym obciążeniu. Oszczędza trochę energii, będąc
jednocześnie bardziej wydajnym niż polecenia powłoki.

%prep
%setup -q

%build
%meson \
	-Dmans=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i3status.conf
%attr(755,root,root) %{_bindir}/i3status
%{_mandir}/man1/i3status.1*
