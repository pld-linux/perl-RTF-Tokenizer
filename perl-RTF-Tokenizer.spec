#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	RTF
%define		pnam	Tokenizer
Summary:	RTF::Tokenizer - tokenize RTF
Summary(pl.UTF-8):	RTF::Tokenizer - rozkład RTF
Name:		perl-RTF-Tokenizer
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RTF/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b9cfb25f338349df6ad675356226d2d
URL:		http://search.cpan.org/dist/RTF-Tokenizer/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
Requires:	perl-Text-Diff
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RTF::Tokenizer Perl module is an object-orientated low-level RTF
reader.  If you're looking to render RTF, or want a higher-level RTF
processor, this is not the module for you - you want RTF::Reader. 
This release of RTF::Tokenizer - it's faster, higher quality, and
implements the RTF standard better than any previous release.

%description -l pl.UTF-8
Moduł Perla RTF::Tokenizer jest obiektowym niskopoziomowym czytnikiem
RTF. Nie jest to moduł służący do wyświetlania RTF-u ani wysokiego
poziomu procesor RTF-u. Tzn., jeśli ktoś tego potrzebuje, to powinien
posłużyć się modułem RTF::Reader. Ta wersja RTF::Tokenizer jest
szybsza, lepszej jakości i lepiej implementuje standard RTF niż wersje
wcześniejsze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install eg/*.rtf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install eg/rtf* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/rtf*
%{perl_vendorlib}/RTF/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
%{_mandir}/man3/*
