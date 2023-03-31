Name:		texlive-labels4easylist
Version:	51124
Release:	2
Summary:	Add reference labels to easylist items
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/labels4easylist
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labels4easylist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labels4easylist.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the \itemLabel macro for adding
configurable reference labels to easylist items.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/labels4easylist
%doc %{_texmfdistdir}/doc/latex/labels4easylist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
