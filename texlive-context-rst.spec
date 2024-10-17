Name:		texlive-context-rst
Version:	47085
Release:	2
Summary:	Process reStructuredText with ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-rst
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-rst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-rst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package provides a converter and module for typesetting
reStructuredText with ConTeXt. The module uses several lua
scripts in doing its work. Documentation is supplied in rst,
which seems to be readable as text, but...

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/context/lua/third/rst
%{_texmfdistdir}/tex/context/interface/third/t-rst.xml
%{_texmfdistdir}/tex/context/third/rst
%doc %{_texmfdistdir}/doc/context/third/rst

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
