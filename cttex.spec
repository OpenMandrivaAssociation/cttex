%define	name	cttex
%define	version	1.23
%define	release	%mkrel 11

Summary:	Cttex, Thai word separator program
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		System/Internationalization
Source0:	%{name}_%{version}.tar.bz2
URL:		http://linux.thai.net/pub/thailinux/cvs/software/cttex/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	locales-th
Patch0:		ctte-121-cflags.patch

%description
The main part of Cttex is a Thai word separator algorithm using
a dictionary. A wrapper for formatting Thai LaTeX document file is provided
to demonstrate the use of this word-sep routine. The program can also
be used as a simple word-sep filter. 

%prep
%setup -q
%patch0 -p1

%build
PATH=$PATH:. %make

%install
rm -rf %{buildroot}
install -m 755 %{name} -D %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* testfile 
%{_bindir}/%{name}

