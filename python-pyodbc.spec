%define		module	pyodbc
Summary:	DB API 2.0 Module for ODBC
Summary(pl.UTF-8):	Moduł DB API 2.0 dla ODBC
Name:		python-%{module}
Version:	2.0.30
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyodbc/%{module}-%{version}.zip
# Source0-md5:	348a7481c615c2db6d2f10a002e8a93a
Patch0:		%{name}-py25.patch
URL:		http://pyodbc.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
BuildRequires:	unixODBC-devel
BuildRequires:	unzip
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyodbc is a Python module that allows you to access ODBC databases. It
implements the Python Database API Specification v2.0.
Some notable features include:
 - The library is free for commercial and personal use.
 - It conforms to the DB API standard.
 - No 3rd party libraries are required. Only native Python datatypes
   are used, such as decimal and datetime.
 - Additional features have been added to simplify database
   programming with Python.

%description -l pl.UTF-8
pyodbc to moduł Pythona pozwalający na dostęp do baz danych ODBC.
Implementuje specyfikację Python Database API w wersji 2.0. Niektóre
znaczące cechy to:
 - Biblioteka jest darmowa do użytku komercyjnego i osobistego.
 - Jest zgodna ze standardem DB API.
 - Nie są wymagane zewnętrzne biblioteki. Używane są wyłącznie natywne
   typy danych Pythona, takie jak decimal czy datetime.
 - Zostały dodane dodatkowe możliwości upraszczające programowanie baz
   danych w Pythonie.

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
