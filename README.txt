NEWS_COLLECTOR

    Aplikacja internetowa NEWS_COLLECTOR to imitacja strony HackerNews. Została 
stworzona przy pomocy frameworka Django. Jej zadaniem jest gromadzenie linków 
dodawanych przez użytkowników wraz z możliwością ich komentowania oraz głosowania 
na nie. 
    Aby móc korzystać ze wszystkich funkcjonalności oferowanych przez aplikację, 
użytkownik musi najpierw założyć konto oraz się zalogować. Następnie może dodać link lub
przeglądać, komentować oraz głosować na te dodane wcześniej przez inne osoby.
Głosowanie ograniczone jest do jednego głosu na użytkownika. To samo tyczy się komentarzy. 
Użytkownik niezalogowany również może korzystać ze aplikacji, ale bez możliwości
publikowania jakichkolwiek treści.
    Do umieszczania odnośnika na stronie służy przycisk POST umieszczony na górnym pasku. 
Po opublikowaniu, link pojawi się na stronie głównej. Ze strony głownej możemy 
przejść pod adres zamieszonego odnośnika lub do dyskusji na jego temat.
Wybierając opcję drugą, przechodzimy na stronę, na której mamy 
możliwość opublikowania komentarza lub przeglądania już istnejących. Posiadają one 
one strukturę drzewiastą - najpierw lista komentarzy do linku, a pod każdym 
z nich komentarze odnoszące się do nich wraz ze swoim drzewem komentarzy.