%include	/usr/lib/rpm/macros.perl
Summary:	Comic book archives viewer
Summary(pl.UTF-8):	Przeglądarka komiksów
Name:		cbview
Version:	0.06
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://elvine.org/code/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6f101dbcecc6d70f59a4b8cec4152446
Source1:	%{name}.desktop
URL:		http://elvine.org/code/cbview/
BuildRequires:	rpm-perlprov
BuildRequires:	unrar
BuildRequires:	unzip
Requires:	perl-Gtk2
Requires:	perl-String-ShellQuote
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CBView is a viewer/converter for CBR/CBZ comic book archives, written
with gtk2-perl.

%description -l pl.UTF-8
CBView to przeglądarka/konwerter archiwów komiksów w formacie CBR/CBZ,
napisana przy użyciu gtk2-perl.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
