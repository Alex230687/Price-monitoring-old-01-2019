# Price monitoring
# Old version 01-2019


Daily price monitoring program. Program has simple desktop interface.

Subject.
There are three types of production blocks:
- production with special price (production list relevent during month, set on the first day of each month);
- new production (production list relevant during 30 days, set irregularly every 7-14 days);
- bestsellers (production list relevent until new list, set inrregulary every 2-3 months);

As a result we have three reports. Each report has three types of production price:
- normal price (base price in online store);
- action price (action price in online store);
- shop price (price in offlice store);

There ara few additional actions for special price production block:
- if one of prices less then special price 
- add this position to warning list
- make screenshot with open page of this position and system calendar.

Program.
- button#1 > run price search. write price information to DB. start in the morning;
- button#2 > run link search. works only for empy links field. write new links to DB. start in the evening;
- button#3 > create base dir /dd.mm.yyyy/. create three edited excel files;
- button#4 > create dirs /<customer name>/ with excel file for price violation;
- buttom#5 > make print screen of price violation in .pgn formate and also consl docx file with print screens;
