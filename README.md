# WTYCZKA QGIS

<ins> Przykładowe łącze z warstwą, na której można przetestować funkcjonalność wtyczki: https://wms.powiat.krakow.pl:1518/iip/ows. Należy je otworzyć, a następnie wybrać warstwę *Osnowa wysokościowa*.


# SPIS TREŚCI
- [Podstawowe informacje](#PODSTAWOWE-INFORMACJE)
- [Wymagania systemowe](#WYMAGANIA-SYSTEMOWE)
- [Jak korzystać z wtyczki](#JAK-KORZYSTAĆ-Z-WTYCZKI)
- [Znane błędy](#ZNANE-BŁĘDY)

***

# PODSTAWOWE INFORMACJE

Wtyczka służy do wykonywania prostych obliczeń w programie QGIS. Do jej funkcjonalności należą:
- obliczanie różnicy wysokości wybranych dwoch punktów,
- obliczanie pola powierzchni figury powstałej między zaznaczonymi punktami.


***

# WYMAGANIA SYSTEMOWE
- Windows 10 lub Windows 11
- QGIS (wersja minimum 3.22)
- python w wersji 3.9 lub 3.10
- biblioteka os
- biblioteka numpy
- biblioteka qgis.utils
- biblioteka qgis.PyQt
- biblioteka qgis.core
- biblioteka PyQt5.QtWidgets
- biblioteka PyQt5.QtGui


***

# JAK KORZYSTAĆ Z WTYCZKI

 Aby skorzystać z wtyczki należy otworzyć program QGIS, a następnie odszukać ją w zakładce "Wtyczki". Wtyczka będzie sprawnie funkcjonować tylko wtedy, kiedy nazwy atrybutów warstwy, na której chcemy wykonać obliczenia wyglądają następująco:
- współrzędna X - ***x2000***
- współrzędna Y - ***y2000***
- wysokość - ***h_plkron86nh*** lub ***h_plevrf2007nh***
  
 Po uruchomieniu wtyczki pojawi się poniższe okno dialogowe.
  
 ![Imgur](https://i.imgur.com/3Ezomqq.png)
  
 Obliczenia rozpoczynamy wyborem punktów na warstwie. Za pomocą opcji w QGIS "Zaznacz obiekty" wybieramy punkty, dla których chcemy wykonać obliczenia. Następnie w oknie dialogowym przyciskiem "Wybierz warstwę" wybieramy tę, na której znajdują się wybrane punkty. Następnie wybieramy operację, którą chcemy wykonać:
- ***Oblicz przewyższenie*** zwraca wartość różnicy wysokości w metrach dla dwóch wybranych punktów (<ins>powinny być zaznaczone tylko 2 punkty),
- ***Oblicz pole*** zwraca wartość pola powierzchni w metrach dla wybranych punktów (<ins>powinny być zaznaczone co najmniej 3 punkty)
 
 W obu przypadkach wyniki pojawiają się w oknie komunikatów programu QGIS.
  
## Wybór niepoprawnej ilości punktów 
- W przypadku jeśli użytkownik wybierze zbyt małą lub zbyt dużą ilość punktów do obliczenia różnicy wysokości otrzyma komunikat 
  
 ![Imgur](https://i.imgur.com/V3mmdwH.png)
  
- W przypadku jeśli użytkownik wybierze niepoprawną ilość punktów do obliczenia pola powierzchni otrzyma komunikat
  
 ![Imgur](https://i.imgur.com/oL895YG.png)
  
  

***

# ZNANE BŁĘDY

Funkcja "Oblicz pole powierzchni" nie zawsze daje poprawne wyniki. W przypadku, kiedy użytkownik wybierze na warstwie więcej niż 3 punkty zdarza się, że algorytm wtyczki nie zachowuje zgodności co do kierunku wykonywania obliczeń. Zaczyna przeliczenia w kierunku ruchu wskazówek zegara, a następnie zmienia na przeciwny. W efekcie tego otrzymujemy niepoprawną wartość pola powierzchni. 


