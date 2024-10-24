%define	modname	File-Slurp-Tiny

Summary:	Simple perl module to slurp a file (use File::Slurper instead)
Name:		perl-%{modname}
Version:	0.004
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		https://metacpan.org/pod/File::Slurp::Tiny
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/File-Slurp-Tiny-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Simple perl module to slurp a file

This module is obsolete and provided for compatibility with
legacy applications only. Use File::Slurper instead.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*
