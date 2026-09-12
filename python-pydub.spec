Name:		python-pydub
Version:	0.25.1
Release:	1
Summary:	Manipulate audio with a simple high-level interface
License:	MIT
Group:		Development/Python
URL:		https://github.com/jiaaro/pydub
Source0:	https://files.pythonhosted.org/packages/source/p/pydub/pydub-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Recommends:	ffmpeg

%description
pydub lets you manipulate audio with a simple high-level interface.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/pydub
%{py_sitedir}/pydub-*.*-info
