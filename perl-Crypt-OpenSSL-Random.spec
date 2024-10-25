# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname Crypt-OpenSSL-Random
%define modver 0.15

Summary:	Crypt-OpenSSL-Random module for perl 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
Patch0:		Crypt-OpenSSL-Random-0.04-link.patch
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:  perl(Crypt::OpenSSL::Guess)

%description
Crypt-OpenSSL-Random module for perl.

%prep
%autosetup -n %{modname}-%{modver} -p1

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} </dev/null
%make_build

%install
%make_install

%files
%doc Changes  META.yml
%{perl_vendorarch}/auto/Crypt/OpenSSL/Random/Random.so
%{perl_vendorarch}/Crypt/OpenSSL/Random.pm
%doc %{_mandir}/*/*
