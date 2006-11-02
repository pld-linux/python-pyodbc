%define		module	pyodbc
Summary:	DB API 2.0 Module for ODBC
Name:		python-%{module}
Version:	2.0.30
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyodbc/%{module}-%{version}.zip
# Source0-md5:	348a7481c615c2db6d2f10a002e8a93a
Patch0:		%{name}-py25.patch
URL:		http://pyodbc.sourceforge.net/
BuildRequires:	unixODBC-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyodbc is a Python module that allows you to access ODBC databases. It
implements the Python Database API Specification v2.0.
Some notable features include:
 - The library is free for commercial and personal use.
 - It conforms to the DB API standard.
 - No 3rd party libraries are required. Only native Python datatypes are used,
   such as decimal and datetime.
 - Additional features have been added to simplify database programming with
   Python.

%prep
%setup -q -n %{module}-%{version}
%patch -p1

%build
python setup.PY build

%install
rm -rf $RPM_BUILD_ROOT

python setup.PY install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.egg-info
