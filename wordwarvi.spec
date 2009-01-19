Summary:	Shoot 'em up '80s style arcade game
Summary(pl.UTF-8):	Strzelanka w stylu lat 80-tych
Name:		wordwarvi
Version:	0.25
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/wordwarvi/%{name}-%{version}.tar.gz
# Source0-md5:	f327d32fca05a034ac3102e833ed545b
URL:		http://wordwarvi.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libvorbis-devel
BuildRequires:	perl-base
BuildRequires:	portaudio-devel >= 19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Word War vi is your basic side-scrolling shoot 'em up '80s style
arcade game. You pilot your "vi"per craft through core memory,
rescuing lost .swp files, avoiding OS defenses, and wiping out those
memory hogging emacs processes. When all the lost .swp files are
rescued, head for the socket which will take you to the next node in
the cluster.

%description -l pl.UTF-8
Word War vi jest prostą strzelanką platformową w stylu lat 80-tych.
Zadaniem gracza jest pilotowanie statku o nazwie 'vi'per przez rdzeń
pamięci, ratowanie zagubionych plików .swp, unikanie obrony Systemu
Operacyjnego oraz czyszczenie obszarów pamięci blokowanych przez
procesy emacsa. Kiedy wszystko zostanie wyczyszczone gracz przenosi
się do kolejnego klastra pamięci.

%prep
%setup -q
%{__perl} -pi -e 's/gcc/\$(CC)/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE_FLAG="%{rpmcflags}" \
	PROFILE_FLAG="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS changelog.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
