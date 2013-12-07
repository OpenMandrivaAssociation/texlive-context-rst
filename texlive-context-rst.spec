# revision 29575
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-rst
# catalog-date 2011-10-03 11:06:20 +0200
# catalog-license other-free
# catalog-version 0.4
Name:		texlive-context-rst
Version:	0.4
Release:	5
Summary:	Process reStructuredText with ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-rst
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-rst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-rst.doc.tar.xz
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
%{_texmfdistdir}/scripts/context/lua/third/rst/mtx-t-rst.lua
%{_texmfdistdir}/tex/context/interface/third/t-rst.xml
%{_texmfdistdir}/tex/context/third/rst/rst_context.lua
%{_texmfdistdir}/tex/context/third/rst/rst_directives.lua
%{_texmfdistdir}/tex/context/third/rst/rst_helpers.lua
%{_texmfdistdir}/tex/context/third/rst/rst_parser.lua
%{_texmfdistdir}/tex/context/third/rst/rst_setups.lua
%{_texmfdistdir}/tex/context/third/rst/t-rst.mkiv
%doc %{_texmfdistdir}/doc/context/third/rst/COPYING
%doc %{_texmfdistdir}/doc/context/third/rst/README.rst
%doc %{_texmfdistdir}/doc/context/third/rst/documentation.rst
%doc %{_texmfdistdir}/doc/context/third/rst/hybridtest.tex
%doc %{_texmfdistdir}/doc/context/third/rst/inc-first.rst
%doc %{_texmfdistdir}/doc/context/third/rst/inc-second.rst
%doc %{_texmfdistdir}/doc/context/third/rst/inc-third.rst
%doc %{_texmfdistdir}/doc/context/third/rst/inc.tex
%doc %{_texmfdistdir}/doc/context/third/rst/manual.bib
%doc %{_texmfdistdir}/doc/context/third/rst/manual.pdf
%doc %{_texmfdistdir}/doc/context/third/rst/manual.tex
%doc %{_texmfdistdir}/doc/context/third/rst/moduletest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
