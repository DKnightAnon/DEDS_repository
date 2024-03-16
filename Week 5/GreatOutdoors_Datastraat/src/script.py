
from settings import settings, logger
import pandas as pd
import pyodbc
import numpy
import sqlite3
import csv
from decimal import Decimal

def processing() :

    
    logger.info(f"Importing modules : pandas, pyodbc, numpy, sqlite3, csv, decimal")

    laptop = 'KNIGHTANON-LAPT\\SQLEXPRESS'
    local = '(localdb)\\MSSQLLocalDB'
    local2 = 'localhost'
    desktop = 'KNIGHTANON-DESK\\SQLEXPRESS'
    database = 'GreatOutdoorsDW'

    DB = {
        'servername': desktop,
        'database' : database
    }

    export_conn = pyodbc.connect('DRIVER={SQL Server};' +
                                'SERVER='+ DB['servername'] + ';'
                                'DATABASE='+DB['database'] +';'
                                +'Trusted_Connection=yes'
                                #  +'integrated security = true' 
                                )
    logger.info(f"Establishing connection with database.")
    export_cursor = export_conn.cursor()
    logger.info(f"Creating Cursor.")
    # export_cursor.execute("CREATE DATABASE GreatOutdoorsDW")
    # export_cursor.execute("USE GreatOutdoorsDW")

    export_cursor


    sales_con = None
    crm_con = None
    staff_con = None

    logger.info("Attempting to connect to source data")

    try : 
       
        sales_con = sqlite3.connect("../data/raw/go_sales.sqlite")
        print("Connected to go_sales sqlite.")
        logger.success("Connected to go_sales sqlite.")

     
        crm_con = sqlite3.connect("../data/raw/go_crm.sqlite")
        print("Connected to go_crm sqlite.")
        logger.success("Connected to go_crm sqlite.")

 
        staff_con = sqlite3.connect("../data/raw/go_staff.sqlite")
        print("Connected to go_staff sqlite.")
        logger.success("Connected to go_staff sqlite.")


    except sqlite3.Error as error: 
        print("Failed to read data from sqlite table", error)
        logger.error("Failed to read data from sqlite table", error)




    logger.info("Creating variables for database tables.")

    global go_crm_age_group
    go_crm_age_group = pd.read_sql_query("SELECT * FROM {}".format("age_group"),crm_con)
    go_crm_age_group = go_crm_age_group[go_crm_age_group.columns.drop(list(go_crm_age_group.filter(regex="TRIAL")))]


    global go_crm_country
    go_crm_country = pd.read_sql_query("SELECT * FROM {}".format("country"),crm_con)
    go_crm_country = go_crm_country[go_crm_country.columns.drop(list(go_crm_country.filter(regex="TRIAL")))]

    global go_crm_retailer
    go_crm_retailer = pd.read_sql_query("SELECT * FROM {}".format("retailer"),crm_con)
    go_crm_retailer = go_crm_retailer[go_crm_retailer.columns.drop(list(go_crm_retailer.filter(regex="TRIAL")))]

    global go_crm_retailer_contact
    go_crm_retailer_contact = pd.read_sql_query("SELECT * FROM {}".format("retailer_contact"),crm_con)
    go_crm_retailer_contact = go_crm_retailer_contact[go_crm_retailer_contact.columns.drop(list(go_crm_retailer_contact.filter(regex="TRIAL")))]

    global go_crm_retailer_headquarters
    go_crm_retailer_headquarters = pd.read_sql_query("SELECT * FROM {}".format("retailer_headquarters"),crm_con)
    go_crm_retailer_headquarters = go_crm_retailer_headquarters[go_crm_retailer_headquarters.columns.drop(list(go_crm_retailer_headquarters.filter(regex="TRIAL")))]

    global go_crm_retailer_segment
    go_crm_retailer_segment = pd.read_sql_query("SELECT * FROM {}".format("retailer_segment"),crm_con)
    go_crm_retailer_segment = go_crm_retailer_segment[go_crm_retailer_segment.columns.drop(list(go_crm_retailer_segment.filter(regex="TRIAL")))]

    global go_crm_retailer_site
    go_crm_retailer_site = pd.read_sql_query("SELECT * FROM {}".format("retailer_site"),crm_con)
    go_crm_retailer_site = go_crm_retailer_site[go_crm_retailer_site.columns.drop(list(go_crm_retailer_site.filter(regex="TRIAL")))]

    global go_crm_retailer_type
    go_crm_retailer_type = pd.read_sql_query("SELECT * FROM {}".format("retailer_type"),crm_con)
    go_crm_retailer_type = go_crm_retailer_type[go_crm_retailer_type.columns.drop(list(go_crm_retailer_type.filter(regex="TRIAL")))]

    global go_crm_sales_demographic
    go_crm_sales_demographic = pd.read_sql_query("SELECT * FROM {}".format("sales_demographic"),crm_con)
    go_crm_sales_demographic = go_crm_sales_demographic[go_crm_sales_demographic.columns.drop(list(go_crm_sales_demographic.filter(regex="TRIAL")))]

    global go_crm_sales_territory
    go_crm_sales_territory = pd.read_sql_query("SELECT * FROM {}".format("sales_territory"),crm_con)
    go_crm_sales_territory = go_crm_sales_territory[go_crm_sales_territory.columns.drop(list(go_crm_sales_territory.filter(regex="TRIAL")))]


    global go_staff_course 
    go_staff_course = pd.read_sql_query("SELECT * FROM {}".format("course"),staff_con)
    go_staff_course = go_staff_course[go_staff_course.columns.drop(list(go_staff_course.filter(regex="TRIAL")))]


    global go_staff_sales_branch 
    go_staff_sales_branch = pd.read_sql_query("SELECT * FROM {}".format("sales_branch"),staff_con)
    go_staff_sales_branch = go_staff_sales_branch[go_staff_sales_branch.columns.drop(list(go_staff_sales_branch.filter(regex="TRIAL")))]


    global go_staff_staff
    go_staff_staff = pd.read_sql_query("SELECT * FROM {}".format("sales_staff"),staff_con)
    go_staff_staff = go_staff_staff[go_staff_staff.columns.drop(list(go_staff_staff.filter(regex="TRIAL")))]


    global go_staff_satisfaction
    go_staff_satisfaction = pd.read_sql_query("SELECT * FROM {}".format("satisfaction"),staff_con)
    go_staff_satisfaction = go_staff_satisfaction[go_staff_satisfaction.columns.drop(list(go_staff_satisfaction.filter(regex="TRIAL")))]


    global go_staff_satisfaction_type
    go_staff_satisfaction_type = pd.read_sql_query("SELECT * FROM {}".format("satisfaction_type"),staff_con)
    go_staff_satisfaction_type = go_staff_satisfaction_type[go_staff_satisfaction_type.columns.drop(list(go_staff_satisfaction_type.filter(regex="TRIAL")))]


    global go_staff_training
    go_staff_training = pd.read_sql_query("SELECT * FROM {}".format("training"),staff_con)
    go_staff_training = go_staff_training = go_staff_training[go_staff_training.columns.drop(list(go_staff_training.filter(regex="TRIAL")))]


    global product
    product = pd.read_sql_query("SELECT * FROM {}".format("product"),sales_con)
    product = product[product.columns.drop(list(product.filter(regex="TRIAL")))]


    global product_type
    product_type = pd.read_sql_query("SELECT * FROM {}".format("product_type"),sales_con)
    product_type = product_type[product_type.columns.drop(list(product_type.filter(regex="TRIAL")))]

    global product_line
    product_line = pd.read_sql_query("SELECT * FROM {}".format("product_line"),sales_con)
    product_line = product_line[product_line.columns.drop(list(product_line.filter(regex="TRIAL")))]

    global sales_staff
    sales_staff = pd.read_sql_query("SELECT * FROM {}".format("sales_staff"),sales_con)
    sales_staff = sales_staff[sales_staff.columns.drop(list(sales_staff.filter(regex="TRIAL")))]

    global sales_branch
    sales_branch = pd.read_sql_query("SELECT * FROM {}".format("sales_branch"),sales_con)
    sales_branch = sales_branch[sales_branch.columns.drop(list(sales_branch.filter(regex="TRIAL")))]

    global retailer_site
    retailer_site = pd.read_sql_query("SELECT * FROM {}".format("retailer_site"),sales_con)
    retailer_site = retailer_site[retailer_site.columns.drop(list(retailer_site.filter(regex="TRIAL")))]

    global country
    country = pd.read_sql_query("SELECT * FROM {}".format("country"),sales_con)
    country = country[country.columns.drop(list(country.filter(regex="TRIAL")))]

    global order_header
    order_header = pd.read_sql_query("SELECT * FROM {}".format("order_header"),sales_con)
    order_header = order_header[order_header.columns.drop(list(order_header.filter(regex="TRIAL")))]

    global order_method
    order_method = pd.read_sql_query("SELECT * FROM {}".format("order_method"),sales_con)
    order_method = order_method[order_method.columns.drop(list(order_method.filter(regex="TRIAL")))]

    global order_details
    order_details = pd.read_sql_query("SELECT * FROM {}".format("order_details"),sales_con)
    order_details = order_details[order_details.columns.drop(list(order_details.filter(regex="TRIAL")))]

    global returned_item
    returned_item = pd.read_sql_query("SELECT * FROM {}".format("returned_item"),sales_con)
    returned_item = returned_item[returned_item.columns.drop(list(returned_item.filter(regex="TRIAL")))]

    global return_reason
    return_reason = pd.read_sql_query("SELECT * FROM {}".format("return_reason"),sales_con)
    return_reason = return_reason[return_reason.columns.drop(list(return_reason.filter(regex="TRIAL")))]

    global SALES_TARGETData
    SALES_TARGETData = pd.read_sql_query("SELECT * FROM {}".format("SALES_TARGETData"),sales_con)
    SALES_TARGETData = SALES_TARGETData[SALES_TARGETData.columns.drop(list(SALES_TARGETData.filter(regex="TRIAL")))]



    go_crm = [go_crm_age_group,go_crm_country,go_crm_retailer,go_crm_retailer_contact,go_crm_retailer_headquarters,
            go_crm_retailer_segment,go_crm_retailer_site,go_crm_retailer_type,go_crm_sales_demographic,go_crm_sales_territory]

    logger.info("Converting table columns to optimal types.")

    go_crm_age_group["AGE_GROUP_CODE"] = go_crm_age_group["AGE_GROUP_CODE"].astype(int)
    go_crm_age_group["LOWER_AGE"] = go_crm_age_group["LOWER_AGE"].astype(int)
    go_crm_age_group["UPPER_AGE"] = go_crm_age_group["UPPER_AGE"].astype(int)

    go_crm_country["COUNTRY_CODE"] = go_crm_country["COUNTRY_CODE"].astype(int)
    go_crm_country["SALES_TERRITORY_CODE"] = go_crm_country["SALES_TERRITORY_CODE"].astype(int)

    go_crm_retailer["RETAILER_CODE"] = go_crm_retailer["RETAILER_CODE"].astype(int)
    go_crm_retailer["RETAILER_CODEMR"] = go_crm_retailer["RETAILER_CODEMR"].astype(float)
    go_crm_retailer["RETAILER_TYPE_CODE"] = go_crm_retailer["RETAILER_TYPE_CODE"].astype(int)

    go_crm_retailer_contact["EXTENSION"] = go_crm_retailer_contact["EXTENSION"].astype(float)
    go_crm_retailer_contact['RETAILER_CONTACT_CODE'] = go_crm_retailer_contact["RETAILER_CONTACT_CODE"].astype(int)
    go_crm_retailer_contact["RETAILER_SITE_CODE"] = go_crm_retailer_contact["RETAILER_SITE_CODE"].astype(int)

    go_crm_retailer_headquarters["RETAILER_CODEMR"] = go_crm_retailer_headquarters["RETAILER_CODEMR"].astype(float)
    go_crm_retailer_headquarters["COUNTRY_CODE"] = go_crm_retailer_headquarters["COUNTRY_CODE"].astype(int)
    go_crm_retailer_headquarters["SEGMENT_CODE"] = go_crm_retailer_headquarters["SEGMENT_CODE"].astype(int)

    go_crm_retailer_segment["SEGMENT_CODE"] = go_crm_retailer_segment["SEGMENT_CODE"].astype(int)

    go_crm_retailer_site["RETAILER_CODE"] = go_crm_retailer_site["RETAILER_CODE"].astype(int)
    go_crm_retailer_site["RETAILER_SITE_CODE"] = go_crm_retailer_site["RETAILER_SITE_CODE"].astype(int)
    go_crm_retailer_site["COUNTRY_CODE"] = go_crm_retailer_site["COUNTRY_CODE"].astype(int)
    go_crm_retailer_site["ACTIVE_INDICATOR"] = go_crm_retailer_site["ACTIVE_INDICATOR"].astype(int)

    go_crm_retailer_type["RETAILER_TYPE_CODE"] = go_crm_retailer_type["RETAILER_TYPE_CODE"].astype(int)

    go_crm_sales_territory["SALES_TERRITORY_CODE"] = go_crm_sales_territory["SALES_TERRITORY_CODE"].astype(int)



    go_staff = [go_staff_course, go_staff_sales_branch,go_staff_staff,go_staff_satisfaction, go_staff_satisfaction_type, go_staff_training]

    go_staff_course["COURSE_CODE"] = go_staff_course["COURSE_CODE"].astype(int)

    go_staff_sales_branch["COUNTRY_CODE"] = go_staff_sales_branch["COUNTRY_CODE"].astype(int)
    go_staff_sales_branch["SALES_BRANCH_CODE"] = go_staff_sales_branch["SALES_BRANCH_CODE"].astype(int)

    go_staff_staff["SALES_STAFF_CODE"] = go_staff_staff["SALES_STAFF_CODE"].astype(int)
    go_staff_staff["SALES_BRANCH_CODE"] = go_staff_staff["SALES_BRANCH_CODE"].astype(int)
    go_staff_staff["MANAGER_CODE"] = go_staff_staff["MANAGER_CODE"].astype(int)
    go_staff_staff["EXTENSION"] = go_staff_staff["EXTENSION"].astype(float)
    go_staff_staff["DATE_HIRED"] = pd.to_datetime(go_staff_staff["DATE_HIRED"])

    go_staff_satisfaction["SALES_STAFF_CODE"] = go_staff_satisfaction["SALES_STAFF_CODE"].astype(int)
    go_staff_satisfaction["SATISFACTION_TYPE_CODE"] = go_staff_satisfaction["SATISFACTION_TYPE_CODE"].astype(int)
    # wat voor datatype for Year? Kijken naar dimensiewaardes
    # losse gedeeltes van datetimes (eg. dag, jaar) opslaan als integers
    go_staff_satisfaction["YEAR"] = go_staff_satisfaction["YEAR"].astype(int)

    go_staff_satisfaction_type["SATISFACTION_TYPE_CODE"] = go_staff_satisfaction_type["SATISFACTION_TYPE_CODE"].astype(int)

    go_staff_training["SALES_STAFF_CODE"] = go_staff_training["SALES_STAFF_CODE"].astype(int)
    go_staff_training["COURSE_CODE"] = go_staff_training["COURSE_CODE"].astype(int)
    go_staff_training["YEAR"] = go_staff_training["YEAR"].astype(int)


    for table in go_staff:
        # table = table.drop("TRIAL633", axis=1)
        table = table[table.columns.drop(list(table.filter(regex="TRIAL")))]
    #     display(table.dtypes)

    # display(go_staff_course)

    go_sales = [SALES_TARGETData,country,order_details,order_header,
                order_method,product,product_line,product_type,returned_item,
                return_reason, sales_staff,sales_branch,retailer_site]

    SALES_TARGETData["Id"] = SALES_TARGETData["Id"].astype(int)
    SALES_TARGETData["SALES_STAFF_CODE"] = SALES_TARGETData["SALES_STAFF_CODE"].astype(int)
    SALES_TARGETData["SALES_PERIOD"] = SALES_TARGETData["SALES_PERIOD"].astype(int)
    SALES_TARGETData["PRODUCT_NUMBER"] = SALES_TARGETData["PRODUCT_NUMBER"].astype(int)
    SALES_TARGETData["SALES_TARGET"] = SALES_TARGETData["SALES_TARGET"].astype(int)
    SALES_TARGETData["RETAILER_CODE"] = SALES_TARGETData["RETAILER_CODE"].astype(int)
    # datatype voor sales_year ?

    country["COUNTRY_CODE"] = country["COUNTRY_CODE"].astype(int)

    order_details["ORDER_DETAIL_CODE"] = order_details["ORDER_DETAIL_CODE"].astype(int)
    order_details["ORDER_NUMBER"] = order_details["ORDER_NUMBER"].astype(int)
    order_details["PRODUCT_NUMBER"] = order_details["PRODUCT_NUMBER"].astype(int)
    order_details["QUANTITY"] = order_details["QUANTITY"].astype(int)
    order_details["UNIT_COST"] = order_details["UNIT_COST"].apply(float)
    order_details["UNIT_PRICE"] = order_details["UNIT_PRICE"].apply(float)
    order_details["UNIT_SALE_PRICE"] = order_details["UNIT_SALE_PRICE"].apply(float)

    order_header["ORDER_NUMBER"] = order_header["ORDER_NUMBER"].astype(int)
    order_header["RETAILER_SITE_CODE"] = order_header["RETAILER_SITE_CODE"].astype(int)
    order_header["RETAILER_CONTACT_CODE"] = order_header["RETAILER_CONTACT_CODE"].astype(int)
    order_header["SALES_STAFF_CODE"] = order_header["SALES_STAFF_CODE"].astype(int)
    order_header["SALES_BRANCH_CODE"] = order_header["SALES_BRANCH_CODE"].astype(int)
    order_header["ORDER_DATE"] = pd.to_datetime(order_header["ORDER_DATE"])
    order_header["ORDER_METHOD_CODE"] = order_header["ORDER_METHOD_CODE"].astype(int)

    order_method["ORDER_METHOD_CODE"] = order_method["ORDER_METHOD_CODE"].astype(int)

    product["PRODUCT_NUMBER"] = product["PRODUCT_NUMBER"].astype(int)
    product["INTRODUCTION_DATE"] = pd.to_datetime(product["INTRODUCTION_DATE"])
    product["PRODUCT_TYPE_CODE"] = product["PRODUCT_TYPE_CODE"].astype(int)
    product["PRODUCTION_COST"] = product["PRODUCTION_COST"].astype(float)
    product["MARGIN"] = product["MARGIN"].astype(float)

    product_line["PRODUCT_LINE_CODE"] = product_line["PRODUCT_LINE_CODE"].astype(int)

    product_type["PRODUCT_LINE_CODE"] = product_type["PRODUCT_LINE_CODE"].astype(int)
    product_type["PRODUCT_TYPE_CODE"] = product_type["PRODUCT_TYPE_CODE"].astype(int)

    returned_item["RETURN_CODE"] = returned_item["RETURN_CODE"].astype(int)
    returned_item["RETURN_DATE"] = pd.to_datetime(returned_item["RETURN_DATE"], format="%d-%m-%Y %H:%M:%S")
    returned_item["ORDER_DETAIL_CODE"] = returned_item["ORDER_DETAIL_CODE"].astype(int)
    returned_item["RETURN_REASON_CODE"] = returned_item["RETURN_REASON_CODE"].astype(int)
    returned_item["RETURN_QUANTITY"] = returned_item["RETURN_QUANTITY"].astype(int)

    return_reason["RETURN_REASON_CODE"] = return_reason["RETURN_REASON_CODE"].astype(int)

    sales_staff["SALES_STAFF_CODE"] = sales_staff["SALES_STAFF_CODE"].astype(int)
    sales_staff["EXTENSION"] = sales_staff["EXTENSION"].astype(float)
    sales_staff["DATE_HIRED"] = pd.to_datetime(sales_staff["DATE_HIRED"])
    sales_staff["SALES_BRANCH_CODE"] = sales_staff["SALES_BRANCH_CODE"].astype(int) 

    sales_branch["SALES_BRANCH_CODE"] = sales_branch["SALES_BRANCH_CODE"].astype(int)
    sales_branch["COUNTRY_CODE"] = sales_branch["COUNTRY_CODE"].astype(int)

    retailer_site["RETAILER_SITE_CODE"] = retailer_site["RETAILER_SITE_CODE"].astype(int)
    retailer_site["RETAILER_CODE"] = retailer_site["RETAILER_CODE"].astype(int)
    retailer_site["COUNTRY_CODE"] = retailer_site["COUNTRY_CODE"].astype(int)
    retailer_site["ACTIVE_INDICATOR"] = retailer_site["ACTIVE_INDICATOR"].astype(int)

    # for table in go_sales:
    #     display(table.dtypes)
        




    logger.info("Creating Dimension Tables.")

    produc_types_content = pd.merge(product_type,product_line, left_on="PRODUCT_LINE_CODE", how="inner", right_on="PRODUCT_LINE_CODE")

    PRODUCT_REGISTRY = product.merge(produc_types_content, left_on="PRODUCT_TYPE_CODE", how="inner", right_on="PRODUCT_TYPE_CODE")




  
    sales_staff_combined = pd.concat([sales_staff, go_staff_staff], ignore_index=True)
    sales_staff_combined = sales_staff_combined.sort_values(by=["SALES_STAFF_CODE"])
    # inplace=False om een een nieuwe dataframe te returnen, anders gaat het sales_staff aanpassen en krijg je niks terug
    sales_staff_combined = sales_staff_combined.dropna(subset=["MANAGER_CODE"], inplace=False)


    sales_branch_combined = pd.concat([sales_branch, go_staff_sales_branch], ignore_index=True)
    sales_branch_combined = sales_branch_combined.drop_duplicates()
    sales_branch_combined["POSTAL_ADDRESS"] = sales_branch_combined[["ADDRESS1", "POSTAL_ZONE"]].agg( ", ".join, axis=1)




    # combineer de verschillende retailer_site tabellen en drop duplicates
    retailer_site_combined = pd.concat([retailer_site, go_crm_retailer_site], ignore_index=True)
    retailer_site_combined = retailer_site_combined.drop_duplicates()

    # merge pad 1 : Retailer_Site --> Country --> Sales_Territory
    country_content = pd.merge(go_crm_country, go_crm_sales_territory, left_on="SALES_TERRITORY_CODE", how="inner", right_on="SALES_TERRITORY_CODE")
    retailer = pd.merge(retailer_site_combined, country_content, left_on="COUNTRY_CODE", how="inner", right_on="COUNTRY_CODE")

    # merge pad 2 : retailer_site --> retailer_contact
    retailer = pd.merge(retailer, go_crm_retailer_contact, left_on="RETAILER_SITE_CODE", how="inner", right_on="RETAILER_SITE_CODE")

    # merge pad 3 : retailer_site --> retailer
    retailer = pd.merge(retailer, go_crm_retailer, left_on="RETAILER_CODE", how="inner", right_on="RETAILER_CODE")
    retailer = pd.merge(retailer, go_crm_retailer_type, left_on="RETAILER_TYPE_CODE", how="inner", right_on="RETAILER_TYPE_CODE")

    # Als iets een NaN value heeft, vervang met 0
    retailer["EXTENSION"] = retailer["EXTENSION"].fillna(0)
    retailer["RETAILER_CODEMR"] = retailer["RETAILER_CODEMR"].fillna(0)


    satisfaction = pd.merge(go_staff_satisfaction, go_staff_satisfaction_type, left_on="SATISFACTION_TYPE_CODE", how="inner", right_on="SATISFACTION_TYPE_CODE")




    logger.info("Creating Fact Tables.")

 
    Order_Details_Feit = None
    order_details_content = pd.merge(order_header, order_details, left_on="ORDER_NUMBER", how="inner", right_on="ORDER_NUMBER" )
    order_details_content = pd.merge(order_details_content, order_method, left_on="ORDER_METHOD_CODE", how="inner", right_on="ORDER_METHOD_CODE")
    order_details_content["TURNOVER"] = order_details_content["UNIT_SALE_PRICE"] * order_details_content["QUANTITY"]
    order_details_content["PROFIT"] = ((order_details_content["UNIT_SALE_PRICE"] * order_details_content["QUANTITY"]) - (order_details_content["UNIT_COST"] * order_details_content["QUANTITY"]))
    order_details_content["DISCOUNT_PERCENTAGE"] = ((order_details_content["UNIT_SALE_PRICE"]/order_details_content["UNIT_PRICE"]) * 100)
    order_details_content["DISCOUNT_PERCENTAGE"] = order_details_content["DISCOUNT_PERCENTAGE"].round(2)


    returned_item_combined = pd.merge(returned_item, return_reason, left_on="RETURN_REASON_CODE", how="inner", right_on="RETURN_REASON_CODE")
    returned_item_combined = pd.merge(returned_item_combined, order_details, left_on="ORDER_DETAIL_CODE", how="inner", right_on="ORDER_DETAIL_CODE")
    returned_item_combined = pd.merge(returned_item_combined, product, left_on="PRODUCT_NUMBER", how="inner", right_on="PRODUCT_NUMBER")
    returned_item_combined = returned_item_combined.loc[:,["RETURN_CODE","ORDER_DETAIL_CODE","RETURN_DATE","PRODUCT_NUMBER","RETURN_QUANTITY","RETURN_REASON_CODE","RETURN_DESCRIPTION_EN"]]




    staff_training_combined = pd.merge(go_staff_training, go_staff_course, left_on="COURSE_CODE", how="inner", right_on="COURSE_CODE")
    staff_training_combined = pd.merge(staff_training_combined, go_staff_staff, left_on="SALES_STAFF_CODE", how="inner", right_on="SALES_STAFF_CODE")
    staff_training_combined["FULL_NAME"] = staff_training_combined[["FIRST_NAME", "LAST_NAME"]].agg( ", ".join, axis=1)
    staff_training_combined = pd.merge(staff_training_combined, go_staff_satisfaction, left_on=["YEAR","SALES_STAFF_CODE"], how="inner", right_on=["YEAR","SALES_STAFF_CODE"])
    staff_training_combined = staff_training_combined.loc[:,["YEAR","SALES_STAFF_CODE", "FULL_NAME","POSITION_EN","COURSE_CODE","SATISFACTION_TYPE_CODE"]]



    global GO_SALES_PRODUCT_FORECASTData
    GO_SALES_PRODUCT_FORECASTData = pd.read_csv("../data/raw/GO_SALES_PRODUCT_FORECASTData.csv")
    GO_SALES_PRODUCT_FORECASTData = GO_SALES_PRODUCT_FORECASTData.convert_dtypes()



    global GO_SALES_INVENTORY_LEVELSData
    GO_SALES_INVENTORY_LEVELSData = pd.read_csv("../data/raw/GO_SALES_INVENTORY_LEVELSData.csv", header=0, index_col=False)
    GO_SALES_INVENTORY_LEVELSData = GO_SALES_INVENTORY_LEVELSData.convert_dtypes()

        





    logger.info("Attempting database insertion.")

    #PRODUCT
    for index, row in PRODUCT_REGISTRY.iterrows():
        try:
            query =  (
                f"INSERT INTO PRODUCT"
                f"(PRODUCT_NUMBER_PK, INTRODUCTION_DATE,PRODUCT_TYPE_CODE, PRODUCT_TYPE_EN, "
                f"PRODUCT_LINE_CODE,PRODUCT_LINE_EN,PRODUCTION_COST,MARGIN, "
                f"PRODUCT_IMAGE,PRODUCT_NAME,PRODUCT_DESCRIPTION_EN,LANUGAGE) "
                f"VALUES "
                f"({row["PRODUCT_NUMBER"]}, '{row["INTRODUCTION_DATE"]}',"
                f"{row["PRODUCT_TYPE_CODE"]}, '{row["PRODUCT_TYPE_EN"]}', {row["PRODUCT_LINE_CODE"]}, "
                f"'{row["PRODUCT_LINE_EN"]}' ,{row["PRODUCTION_COST"]}, {row["MARGIN"]}, "
                f"'{row["PRODUCT_IMAGE"]}', '{row["PRODUCT_NAME"]}', '{row["DESCRIPTION"]}', "
                f" '{row["LANGUAGE"]}' )"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in sales_branch_combined.iterrows():
        try:
            query = (
                f"INSERT INTO SALES_BRANCH"
                f"(SALES_BRANCH_CODE_PK, ADDRESS1, ADDRESS2, POSTAL_ADDRESS, COUNTRY, REGION, CITY, POSTAL_ZONE)"
                f"VALUES"
                f"({row["SALES_BRANCH_CODE"]},'{row["ADDRESS1"]}','{row["ADDRESS2"]}','{row["POSTAL_ADDRESS"]}',"
                f"'{row["COUNTRY_CODE"]}','{row["REGION"]}','{row["CITY"]}','{row["POSTAL_ZONE"]}')"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            # print(query)
            pass
    export_cursor.commit()


    for index, row in go_staff_course.iterrows():
        try:
            query = (
                f"INSERT INTO COURSE(COURSE_CODE_FK, DESCRIPTION) VALUES ({row["COURSE_CODE"]},'{row["COURSE_DESCRIPTION"]}')"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    #STAFF_TRAINING
    for index, row in staff_training_combined.iterrows():
        try:
            query = (
                f"INSERT INTO STAFF_TRAINING"
                f"(YEAR_PK, SALES_STAFF_CODE_PK,FULL_NAME,POSITION_EN,COURSE_CODE_FK,SATISFACTION_TYPE_CODE_FK)"
                f"VALUES"
                f"({row["YEAR"]}, {row["SALES_STAFF_CODE"]},'{row["FULL_NAME"]}','{row["POSITION_EN"]}',"
                f"{row["COURSE_CODE"]}, {row["SATISFACTION_TYPE_CODE"]})"
                    )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in satisfaction.iterrows():
        try:
            query = (
                f"INSERT INTO SATISFACTION"
                f"(YEAR_PK, SALES_STAFF_CODE, SATISFACTION_TYPE_CODE, SATISFACTION_TYPE_DESCRIPTION)"
                f"VALUES({row["YEAR"]},{row["SALES_STAFF_CODE"]},"
                f"{row["SATISFACTION_TYPE_CODE"]},'{row["SATISFACTION_TYPE_DESCRIPTION"]}')"
                )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in order_method.iterrows():
        try:
            query = (
                f"INSERT INTO ORDER_METHOD"
                f"(ORDER_METHOD_CODE, ORDER_METHOD_EN)"
                f"VALUES"
                f"({row["ORDER_METHOD_CODE"]},'{row["ORDER_METHOD_EN"]}')"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in return_reason.iterrows():
        try:
            query = (
                f"INSERT INTO RETURN_REASON"
                f"(RETURN_REASON_CODE, RETURN_REASON_EN)"
                f"VALUES"
                f"({row["RETURN_REASON_CODE"]},'{row["RETURN_DESCRIPTION_EN"]}')"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in GO_SALES_INVENTORY_LEVELSData.iterrows():
        try:
            query = (
                f"INSERT INTO GO_SALES_INVENTORY_LEVELSData"
                f"(INVENTORY_YEAR, INVENTORY_MONTH, PRODUCT_NUMBER, INVENTORY_COUNT)"
                f"VALUES"
                f"({row["INVENTORY_YEAR"]},{row["INVENTORY_MONTH"]},{row["PRODUCT_NUMBER"]},{row["INVENTORY_COUNT"]})"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in GO_SALES_PRODUCT_FORECASTData.iterrows():
        try:
            query = (
            f"INSERT INTO GO_SALES_PRODUCT_FORECASTData"
            f"(PRODUCT_NUMBER, YEAR, MONTH, EXPECTED_VOLUME)"
            f"VALUES"
            f"({row["PRODUCT_NUMBER"]},{row["YEAR"]},{row["MONTH"]},{row["EXPECTED_VOLUME"]})"
                    )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()

    for index, row in retailer.iterrows():
        try:
            query = (
                f"INSERT INTO RETAILER"
                f"(RETAILER_SITE_CODE, ADDRESS1, ADDRESS2, COUNTRY_CODE, COUNTRY_EN,"
                f"FLAG_IMAGE, REGION, CITY, POSTAL_ZONE, ACTIVE_INDICATOR,"
                f"SALES_TERRITORY_CODE, TERRITORY_NAME_EN, RETAILER_CODE, RETAILER_CODEMR,"
                f"COMPANY_NAME, RETAILER_TYPE_CODE, RETAILER_TYPE_EN,"
                f"RETAILER_CONTACT_CODE, FIRST_NAME, LAST_NAME, JOB_POSITION_EN,"
                f"EXTENSION, FAX, E_MAIL, GENDER)"
                f"VALUES"
                f"({row["RETAILER_SITE_CODE"]},'{row["ADDRESS1"]}','{row["ADDRESS2"]}',"
                f"{row["COUNTRY_CODE"]},'{row["COUNTRY_EN"]}','{row["FLAG_IMAGE"]}','{row["REGION"]}',"
                f"'{row["CITY"]}','{row["POSTAL_ZONE"]}',"
                f"{row["ACTIVE_INDICATOR"]},{row["SALES_TERRITORY_CODE"]},"
                f"'{row["TERRITORY_NAME_EN"]}',{row["RETAILER_CODE"]},{row["RETAILER_CODEMR"]},"
                f"'{row["COMPANY_NAME"]}',{row["RETAILER_TYPE_CODE"]},'{row["RETAILER_TYPE_EN"]}'," 
                f"{row["RETAILER_CONTACT_CODE"]},'{row["FIRST_NAME"]}','{row["LAST_NAME"]}',"
                f"'{row["JOB_POSITION_EN"]}',{row["EXTENSION"]},'{row["FAX"]}','{row["E_MAIL"]}',"
                f"'{row["GENDER"]}')"
            )
            export_cursor.execute(query)
        except pyodbc.Error:
            pass
            # print(query)
    export_cursor.commit()



    for index, row in order_details_content.iterrows():
        try:
            query = (
                f"INSERT INTO ORDER_DETAILS"
                f"(ORDER_NUMBER_PK,ORDER_DETAIL_CODE_PK,ORDER_DETAILS_QUANTITY,	ORDER_DETAILS_UNIT_COST,"
                f"ORDER_DETAILS_UNIT_PRICE,	ORDER_DETAILS_UNIT_SALE_PRICE,	ORDER_DETAILS_DISCOUNT_PERCENTAGE,"
                f"ORDER_DETAILS_TURNOVER,ORDER_DETAILS_PROFIT,ORDER_DATE,SALES_BRANCH_CODE_FK,"
                f"RETAILER_SITE_CODE,RETAILER_SITE_CONTACT)"
                f"VALUES"
                f"({row["ORDER_NUMBER"]},{row["ORDER_DETAIL_CODE"]},{row["QUANTITY"]},{row["UNIT_COST"]},"
                f"{row["UNIT_PRICE"]},{row["UNIT_SALE_PRICE"]},{row["DISCOUNT_PERCENTAGE"]},"
                f"{row["TURNOVER"]},{row["PROFIT"]},'{row["ORDER_DATE"]}',{row["SALES_BRANCH_CODE"]},"
                f"{row["RETAILER_SITE_CODE"]},{row["RETAILER_CONTACT_CODE"]})"
                    )
            export_cursor.execute(query)
        except pyodbc.Error:
            print(query)
    export_cursor.commit()

    # for index, row in sales_staff_combined.iterrows():
    #     try:
    #         query = None
    #         export_cursor.execute(query)
    #     except pyodbc.Error:
    #         print(query)
    # export_cursor.commit()

    # for index, row in sales_staff_combined.iterrows():
    #     try:
    #         query = None
    #         export_cursor.execute(query)
    #     except pyodbc.Error:
    #         print(query)
    # export_cursor.commit()

    logger.success("Insertion Complete.")

    export_cursor.close()
    
    logger.info("Data ETL complete.")



