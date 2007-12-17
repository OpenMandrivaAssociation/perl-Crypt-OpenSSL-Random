%define name	perl-Crypt-OpenSSL-Random
%define module  Crypt-OpenSSL-Random
%define version	0.04
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Crypt-OpenSSL-Random module for perl 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.gz
Requires:	openssl
Buildrequires: perl-devel
Buildrequires: openssl-devel

%description
Crypt-OpenSSL-Random module for perl

%prep
%setup -q -n %{module}-%{version} 
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} </dev/null
%{__make}
%{__make} test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/Random.so
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/autosplit.ix
%{perl_vendorlib}/*/Crypt/OpenSSL/Random.pm
%{_mandir}/*/*

