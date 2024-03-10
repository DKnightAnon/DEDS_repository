-- Feittabellen

CREATE TABLE Order_Details (
	ORDER_NUMBER int,
	ORDER_DETAIL_CODE int,
	ORDER_DETAILS_QUANTITY int,


	ORDER_DETAILS_UNIT_COST decimal(18,2),
	ORDER_DETAILS_UNIT_PRICE decimal(18,2),
	ORDER_DETAILS_UNIT_SALE_PRICE decimal(18,2),
	ORDER_DETAILS_DISCOUNT_PERCENTAGE decimal(5,2),
	ORDER_DETAILS_TURNOVER decimal(18,2),
	ORDER_DETAILS_PROFIT decimal(18,2),

	DAY_DATE date,
	SALES_BRANCH_CODE int,
	RETAILER_SITE_CODE int,
	RETAILER_SITE_CONTACT int
);


CREATE TABLE RETURNED_ITEM(
    RETURNED ITEM CODE int,

    RETURN_DATE date,
    RETURN_QUANTITY int,

    RETURN_REASON varchar(250),
    PRODUCT_NUMBER int
);


CREATE TABLE STAFF_TRAINING(

    Year int(4),
    SALES_STAFF_CODE int(4),

    SATISFACTION varchar(250)

    Satisfaction_TYPE int,
    COURSE_CODE int

);

--Dimensiewaardes

CREATE TABLE SALES_STAFF(
    SALES_STAFF_CODE int,
    FIRST_NAME varchar,
    LAST_NAME varchar,
    FULL_NAME varchar,
    POSITION_EN varchar,
    WORK_PHONE varchar(50),
    EXTENSION int,
    FAX varchar,
    EMAIL varchar,
    DATE_HIRED date,
    SALES_BRANCH_CODE int,
    SALES_BRANCH_COUNTRY varchar,
    MANAGER_CODE int


);

CREATE TABLE SALES_BRANCH(
    SALES_BRANCH_CODE int,
    ADDRESS1 varchar(200),
    ADDRESS1 varchar(200),
    POSTAL_ADDRESS varchar(200),
    COUNTRY_CODE int,
    REGION varchar(200),
    CITY varchar(200),
    POSTAL_ZONE varchar(50)
);





CREATE TABLE PRODUCT(
    PRODUCT_NUMBER int,
    INTRODUCTION_DATE date,
    
    PRODUCT_TYPE_CODE int,
    PRODUCT_TYPE_EN varchar(200),

    PRODUCT_LINE_CODE int,
    PRODUCT_LINE_EN varchar(200),

    PRODUCTION_COST decimal(18,2),
    MARGIN decimal(4,2),
    PRODUCT_IMAGE varchar(200),
    PRODUCT_NAME varchar(200),
    PRODUCT_DESCRIPTION_EN(1000),
    LANUGAGE varchar(100)
);