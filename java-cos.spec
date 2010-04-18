%include	/usr/lib/rpm/macros.java
%define		srcname		cos
Summary:	"must have" class library for servlet developers
Summary(pl.UTF-8):	Niezbędnik programisty servletów
Name:		java-cos
Version:	2008.12.26
Release:	1
License:	Free for non-commercial use, "buy my book" for commercial
Group:		Libraries/Java
Source0:	http://servlets.com/cos/cos-26Dec2008.zip
# Source0-md5:	d7e6ee62b8e92c9d7cb0bdf016e2a815
URL:		http://servlets.com/cos
BuildRequires:	java(jsp)
BuildRequires:	java(servlet)
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java(jsp)
Requires:	java(servlet)
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The com.oreilly.servlet package is the "must have" class library for
servlet developers. There are classes to help servlets parse
parameters, handle file uploads, generate multipart responses (server
push), negotiate locales for internationalization, return files,
manage socket connections, and act as RMI servers, as well as a class
to help applets communicate with servlets. Since the first edition,
there are also new classes to help servlets send email messages, cache
responses, and auto-detect servlet API support.

%description -l pl.UTF-8
Pakiet com.oreilly.servlet to biblioteka stanowiąca niezbędnik
programisty servletów. W skład biblioteki wchodzą klasy
  - ułatwiające analizę parametrów servletu
  - obsługujące wysyłanie/pobieranie plików
  - generujące wieloczęściowe odpowiedzi (server push)
  - negocjujące język
  - zarządzające połączeniami sieciowymi
  - działające jako serwery RMI
  - ułatwiające komunikację między appletami a servletami
  - wysyłające wiadomości e-mail
  - buforujące odpowiedzi
  - wykrywające wsparcie dla API servletów.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -qc

%build
export JAVA_HOME="%{java_home}"

required_jars="servlet-api jsp-api"
CLASSPATH=$(build-classpath $required_jars)

%javac -cp $CLASSPATH $(find -name '*.java')
cd src
%jar cf ../%{srcname}-%{version}.jar $(find -name '*.class')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
