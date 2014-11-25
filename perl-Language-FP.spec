%define		pdir	Language
%define		pnam	FP
%include	/usr/lib/rpm/macros.perl
Summary:	Language::FP perl module
Summary(pl.UTF-8):	Moduł perla Language::FP
Name:		perl-Language-FP
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	d272b939b074814325eb504e8cc68dc1
URL:		http://search.cpan.org/dist/Language-FP/
BuildRequires:	perl-Parse-RecDescent >= 0.01
BuildRequires:	perl-Regexp-Common >= 0.01
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Language::FP is an implementation of John Backus' FP language, a
purely functional language remarkable for its lack of named variables
- only functions have names. Note that this is not a deliberately
obfuscated language - it was designed for actual users (probably
mathematicians).

%description -l pl.UTF-8
Language::FP to implementacja języka FP Johna Backusa, w pełni
funkcyjnego języka znanego z braku nazwanych zmiennych - nazwy mają
jedynie funkcje. Nie jest to celowo zaciemniony język - został
zaprojektowany dla rzeczywistych użytkowników (prawdopodobnie
matematyków).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Language/FP.pm
%{_mandir}/man3/*
