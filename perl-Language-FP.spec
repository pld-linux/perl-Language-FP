%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	FP
Summary:	Language::FP perl module
Summary(pl):	Modu³ perla Language::FP
Name:		perl-Language-FP
Version:	0.03
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Parse-RecDescent >= 0.01
BuildRequires:	perl-Regexp-Common >= 0.01
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Language::FP is an implementation of John Backus' FP language, a
purely functional language remarkable for its lack of named variables
- only functions have names. Note that this is not a deliberately
obfuscated language - it was designed for actual users (probably
mathematicians).

%description -l pl
Language::FP to implementacja jêzyka FP Johna Backusa, w pe³ni
funkcyjnego jêzyka znanego z braku nazwanych zmiennych - nazwy maj±
jedynie funkcje. Nie jest to celowo zaciemnony jêzyk - zosta³
zaprojektowany dla rzeczywistych u¿ytkowników (prawdopodobnie
matematyków).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Language/FP.pm
%{_mandir}/man3/*
