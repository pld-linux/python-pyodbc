%define		module	pyodbc
Summary:	DB API 2.0 Module for ODBC
Summary(pl):	Modu³ DB API 2.0 dla ODBC
Name:		python-%{module}
Version:	2.0.30
Release:	1
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

%description -l pl
pyodbc to modu³ Pythona pozwalaj±cy na dostêp do baz danych ODBC.
Implementuje specyfikacjê Python Database API w wersji 2.0. Niektóre
znacz±ce cechy to:
 - Biblioteka jest darmowa do u¿ytku komercyjnego i osobistego.
 - Jest zgodna ze standardem DB API.
 - Nie s± wymagane zewnêtrzne biblioteki. U¿ywane s± wy³±cznie natywne
   typy danych Pythona, takie jak decimal czy datetime.
 - Zosta³y dodane dodatkowe mo¿liwo¶ci upraszczaj±ce programowanie baz
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
