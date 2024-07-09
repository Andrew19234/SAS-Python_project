/* Pasul 1: Importarea setului de date din fișierul CSV */
proc import datafile='/home/u63881920/addata/data.csv'
    out=work.data_imported
    dbms=csv
    replace;
    getnames=yes;
run;

/* Vizualizarea setului de date importat */
proc print data=work.data_imported (obs=10);
run;

/* Pasul 2: Crearea și folosirea de formate definite de utilizator */
proc format;
    value $gender_fmt
        'Male' = 'M'
        'Female' = 'F';
    value age_fmt
        low-29 = 'Youth'
        30-49 = 'Adult'
        50-high = 'Senior';
run;

/* Aplicarea formatelor definite */
data work.data_formatted;
    set work.data_imported;
    format Gender $gender_fmt. Age age_fmt.;
run;

/* Vizualizarea setului de date cu formate aplicate */
proc print data=work.data_formatted (obs=10);
run;

/* Pasul 3: Procesarea iterativă și condițională a datelor */
data work.data_processed;
    set work.data_formatted;
    if Age < 30 then Age_Group = 1;
    else if Age >= 30 and Age < 50 then Age_Group = 2;
    else if Age >= 50 then Age_Group = 3;
run;

/* Verificarea setului de date procesat */
proc print data=work.data_processed (obs=10);
run;

/* Verificarea tipului și valorilor variabilei Age_Group */
proc freq data=work.data_processed;
    tables Age_Group;
run;

/* Pasul 4: Crearea de subseturi de date */
data work.data_youth;
    set work.data_processed;
    if Age_Group = 1;
run;

data work.data_adult;
    set work.data_processed;
    if Age_Group = 2;
run;

/* Vizualizarea subseturilor de date */
proc print data=work.data_youth (obs=10);
run;

proc print data=work.data_adult (obs=10);
run;

/* Utilizarea de funcții SAS pentru a calcula indicatori */
proc means data=work.data_processed n mean std;
    var Income;
    class Age_Group;
    output out=work.stats mean=Avg_Income std=Std_Income;
run;

/* Vizualizarea rezultatelor statistice */
proc print data=work.stats;
run;

/* Combinarea seturilor de date utilizând SAS Data Step */
data work.data_combined;
    set work.data_youth work.data_adult;
run;

/* Vizualizarea setului de date combinat */
proc print data=work.data_combined (obs=10);
run;

/* Combinarea seturilor de date utilizând PROC SQL */
proc sql;
    create table work.data_combined_sql as
    select * from work.data_youth
    union
    select * from work.data_adult;
quit;

/* Vizualizarea setului de date combinat */
proc print data=work.data_combined_sql (obs=10);
run;
