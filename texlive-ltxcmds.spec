Name:		texlive-ltxcmds
Version:	56421
Release:	1
Summary:	Some LaTeX kernel commands for general use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxcmds
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxcmds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxcmds.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxcmds.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package exports some utility macros from the LaTeX kernel
into a separate namespace and also makes them available for
other formats such as plain TeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/ltxcmds
%{_texmfdistdir}/tex/generic/ltxcmds
%doc %{_texmfdistdir}/doc/generic/ltxcmds

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
