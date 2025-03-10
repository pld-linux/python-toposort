#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Topological sort algorithm
Summary(pl.UTF-8):	Algorytm sortowania topologicznego
Name:		python-toposort
Version:	1.7
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/toposort/
Source0:	https://files.pythonhosted.org/packages/source/t/toposort/toposort-%{version}.tar.gz
# Source0-md5:	0cf6b3efe4d2dc046cede074f8e44099
URL:		https://pypi.org/project/toposort/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:42
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools >= 1:42
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a topological sort algorithm.

Topological sort (topsort, toposort) or topological ordering of a
directed graph is a linear ordering of its vertices such that for
every directed edge uv from vertex u to vertex v, u comes before v in
the ordering.

%description -l pl.UTF-8
Ten moduł implementuje algorytm sortowania topologicznego.

Sortowanie topologiczne (topsort, toposort), inaczej porządek
topologiczny grafu skierowanego to porządek liniowy wierzchołków tego
grafu taki, że dla każdej skierowanej krawędzi uv od wierzchołka u do
wierzchołka v, u występuje przed v.

%package -n python3-toposort
Summary:	Topological sort algorithm
Summary(pl.UTF-8):	Algorytm sortowania topologicznego
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-toposort
This module implements a topological sort algorithm.

Topological sort (topsort, toposort) or topological ordering of a
directed graph is a linear ordering of its vertices such that for
every directed edge uv from vertex u to vertex v, u comes before v in
the ordering.

%description -n python3-toposort -l pl.UTF-8
Ten moduł implementuje algorytm sortowania topologicznego.

Sortowanie topologiczne (topsort, toposort), inaczej porządek
topologiczny grafu skierowanego to porządek liniowy wierzchołków tego
grafu taki, że dla każdej skierowanej krawędzi uv od wierzchołka u do
wierzchołka v, u występuje przed v.

%prep
%setup -q -n toposort-%{version}

# stub for setuptools
cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m test.test_toposort
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m test.test_toposort
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt NOTICE README.txt
%{py_sitescriptdir}/toposort.py[co]
%{py_sitescriptdir}/toposort-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-toposort
%defattr(644,root,root,755)
%doc CHANGES.txt NOTICE README.txt
%{py3_sitescriptdir}/toposort.py
%{py3_sitescriptdir}/__pycache__/toposort.cpython-*.py[co]
%{py3_sitescriptdir}/toposort-%{version}-py*.egg-info
%endif
