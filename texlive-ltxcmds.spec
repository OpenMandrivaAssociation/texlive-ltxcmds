%global tl_name ltxcmds
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.26
Release:	%{tl_revision}.1
Summary:	Some LaTeX kernel commands for general use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/ltxcmds
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxcmds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxcmds.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxcmds.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package exports some utility macros from the LaTeX kernel into a
separate namespace and also makes them available for other formats such
as plain TeX.

