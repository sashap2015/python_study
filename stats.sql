-- SELECT count(*) FROM numfrick.number_data;
-- SELECT * FROM numfrick.number_data;

select num, count(*) from numfrick.number_data group by num
order by 2 desc;

create view numfrick.v
as
select * from number_data_rng_1_10000;

select * from v where num in (10, 100, 10 + 100);

select num, a,b, sum_of_a, a/b, b/a from v where num%5=0 and num%2=1 and sum_of_num%2=1;

SELECT count(1),max(num) FROM numfrick.number_data;

# 5k
select * from number_data where num%5=0 and num%2=1 and num%11<>0 and type_algorithm=1;

select * from number_data where num%5=0 and num%2=1 and num%11<>0 and type_algorithm=0;

select * from numfrick.v where num in (85, 2033);
-- 2033 - 8/2=4 --> 8/2/2=2
2022
11

show database(); 