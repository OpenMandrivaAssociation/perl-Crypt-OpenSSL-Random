%define modname	Crypt-OpenSSL-Random
%define modver	0.04

Summary:	Crypt-OpenSSL-Random module for perl 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
Patch0:		Crypt-OpenSSL-Random-0.04-link.patch
Buildrequires:	perl-devel
Buildrequires:	pkgconfig(openssl)

%description
Crypt-OpenSSL-Random module for perl

%prep
%setup -qn %{modname}-%{modver}
%patch0 -p0
# perl path hack
find . -type f | xargs %__perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} </dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/Random.so
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/autosplit.ix
%{perl_vendorlib}/*/Crypt/OpenSSL/Random.pm
%{_mandir}/man3/*

