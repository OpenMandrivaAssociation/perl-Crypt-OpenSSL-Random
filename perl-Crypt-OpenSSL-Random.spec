%define upstream_name    Crypt-OpenSSL-Random
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7
Summary:	Crypt-OpenSSL-Random module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Crypt-OpenSSL-Random-0.04-link.patch
Buildrequires: perl-devel
Buildrequires: openssl-devel

%description
Crypt-OpenSSL-Random module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} </dev/null
%{__make}

%check
%{__make} test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/Random.so
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/autosplit.ix
%{perl_vendorlib}/*/Crypt/OpenSSL/Random.pm
%{_mandir}/*/*

