Summary:	Thai word separator program
Name:		cttex
Version:	1.23
Release:	23
License:	Distributable
Group:		System/Internationalization
Url:		http://linux.thai.net/pub/thailinux/cvs/software/cttex/
Source0:	%{name}_%{version}.tar.bz2
Patch0:		ctte-121-cflags.patch
Requires:	locales-th

%description
The main part of Cttex is a Thai word separator algorithm using
a dictionary. A wrapper for formatting Thai LaTeX document file is provided
to demonstrate the use of this word-sep routine. The program can also
be used as a simple word-sep filter. 

%prep
%setup -q
%autopatch -p1

%build
PATH=$PATH:. %make

%install
install -m 755 %{name} -D %{buildroot}%{_bindir}/%{name}

%files
%doc README* testfile 
%{_bindir}/%{name}

