"""
DB 간단 소개
postgres 설치
table plus 설치
DB 생성, 테스트 테이블 생성



SQL은 DB를 직접 조작할수 있는만큼 강력하지만,
에러검출이 하나도 안됩니다.


SELECT              <- 3
*
FROM t_test1 as t1  <- 1
WHERE t1.id=1       <- 2


t_test1
1	id	int4	NO	id	"nextval('t_test1_id_seq'::regclass)"		NULL
2	title	varchar	YES	title	"''''''::character varying"		NULL
3	content	varchar	YES	content	"''''''::character varying"		NULL
4	created_dt	timestamptz	YES	created_dt	now()		NULL

t_test1_child
1	id	int4	NO	id	"nextval('t_test1_child_id_seq'::regclass)"		NULL
2	comment	varchar	YES	comment	"''''''::character varying"		NULL
3	created_dt	timestamptz	YES	created_dt	now()		NULL
4	test1_id	int4	YES	test1_id	NULL	 public.t_test1(id)	NULL

FK 는 무조건 자식 테이블에 있어야 한다(test1_id).
test1_id 이건 부모 테이블의 id를 뜻한다

FK 는 무조건 부모 테이블의 id 를 가져야한다


SELECT <- 4
t1.id
,t1.title
FROM t_test1 as t1  <- 1
LEFT JOIN t_test1_child as t1c <- 2  ON t1c.test1_id = t1.id  <-3
;

부모 테이블과 자식 테이블의 관계는 쉽게 생각하면 게시글이나
인터넷 쇼핑몰의 상품을 상객하면 된다.

부모테이블이 게시글, 자식 테이블이 댓글, 이런식이다.
1:N 관계를 뜻한다


JOIN := 꼭 부모와 자식 테이블에 둘다 데이터가 있을때만 가져와라
LEFT JOIN := 부모테이블꺼 다 가져오는데,
             자식 테이블에 데이터가 없으면, NULL로 표시해라.
"""