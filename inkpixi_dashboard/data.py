import pyodbc
from contextlib import closing

def connect_sqlserver(database):
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=SQLSERVER; DATABASE='+database+'; Trusted_Connection=yes')
    db = conn.cursor()
    
    return db
    
def connect_sqlrptserver():
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=SQLRPTSERVER\SQLREPORTS; DATABASE=Reporting; Trusted_Connection=yes')
    db = conn.cursor()    
    
    return db

def get_list_types():
    cur = connect_sqlrptserver()
    
    with closing(cur) as db:
        db.execute("EXEC dbo.uspGetListTypes")
        ds = db.fetchall()
        
        ls_types = []
        for i in ds:
            ls_types.append(i[0])
        
    return ls_types

def get_list_subtypes():
    cur = connect_sqlrptserver()
    
    with closing(cur) as db:
        db.execute("EXEC dbo.uspGetListSubTypes")
        ds = db.fetchall()
        
        ls_subtypes = []
        for i in ds:
            ls_subtypes.append(i[0])
            
    return ls_subtypes

def get_categories():
    cur = connect_sqlrptserver()
    
    with closing(cur) as db:
        db.execute("EXEC dbo.uspGetCategories")
        ds = db.fetchall()
        
        ls_cats = []
        for i in ds:
            ls_cats.append(i[0])
            
    return ls_cats

def get_vendors():
    cur = connect_sqlrptserver()
    
    with closing(cur) as db:
        db.execute("EXEC dbo.uspGetVendors")
        ds = db.fetchall()
        
        ls_vendor = []
        for i in ds:
            ls_vendor.append(i[0])
            
    return ls_vendor

def get_campaign_year():
    cur = connect_sqlrptserver()
    
    with closing(cur) as db:
        db.execute("EXEC dbo.uspGetCampaignYear")
        ds = db.fetchall()
        
        ls_year = []
        for i in ds:
            ls_year.append(str(i[0]))
            
    return ls_year

def get_campaign_qtr():
    cur = connect_sqlrptserver()
    
    with closing(cur) as db:
        db.execute("EXEC dbo.uspGetCampaignQuarter")
        ds = db.fetchall()
        
        ls_year = []
        for i in ds:
            ls_year.append("Q" + str(i[0]))
            
    return ls_year

def get_report(qtrs, yrs, lst_type, lst_cat, lst_sub, vendor):
    cur = connect_sqlserver('Reporting')
    
    where = " WHERE "
        
    # grab years, should never be empty
    #strYrs = ','.join(yrs)
    yr = "campaign_year IN (" + yrs + ")" 
    
    # grab Quarters, should never be empty    
    #strQtrs = ','.join(qtrs)
    qtr = "campaign_quarter IN (" + qtrs.replace("Q", "") + ")"
    
    #build the final where clause with the parameters
    qry = ''
    
    if lst_type != None:
        qry += " AND list_type = '" + lst_type + "'"
        
    if lst_cat != None:
        qry += " AND list_category = '" + lst_cat + "'"
        
    if lst_sub != None:
        qry += " AND list_subtype = '" + lst_sub + "'"
        
    if vendor != None:
        qry += " AND list_vendor = '" + vendor + "'"
    

    with closing(cur) as db:
        sql = """SELECT
                    h.source_code, 
                    h.root_sku,
                    h.featured_product,
                    CONVERT(VARCHAR(20), h.drop_date, 101) drop_date,
                    CONVERT(VARCHAR(20), h.cut_off_date, 101) cut_off_date,    
                    h.list_vendor,
                    h.list_selection,
                    h.model_tier_rank,
                    h.unit_cost_per_thousand,
                    h.printed_quantity,
                    CAST(r.response_rate AS DECIMAL(10,4)) response_rate,
                    p.product_total / h.printed_quantity product_total_per_card,
                    CAST(p.product_total / o.orders AS DECIMAL(10,2)) product_total_per_order,
                    g.gross_revenue / h.printed_quantity gross_revenue_per_card,
                    CAST(g.gross_revenue / o.orders AS DECIMAL(10,2)) gross_revenue_per_order,
                    CONVERT(VARCHAR, CAST(g.gross_revenue - (p.product_total * .25) - h.list_invoice_amount - (h.printed_quantity * .00714) - (h.printed_quantity * .245) - (h.printed_quantity * .085) - (o.orders * 7.5) AS MONEY), 1) contribution_margin,
                    CONVERT(VARCHAR, CAST((g.gross_revenue - (p.product_total * .25) - h.list_invoice_amount - (h.printed_quantity * .00714) - (h.printed_quantity * .245) - (h.printed_quantity * .085) - (o.orders * 7.5)) * 1.2 AS MONEY), 1) twenty_percent   
                FROM
                    dbo.PostcardCampaignHistory h
                JOIN
                    dbo.vwResponsRatePerCampaign r ON r.source_code = h.source_code    
                JOIN
                    dbo.vwProductTotalPerCampaign p ON p.source_code = h.source_code    
                JOIN
                    dbo.vwGrossRevenuePerCampaign g ON g.source_code = h.source_code    
                JOIN    
                    dbo.vwTotalOrdersPerCampaign o ON o.source_code = h.source_code""" + where + qtr + """ AND """ + yr + qry + """ 
                ORDER BY
                    h.source_code"""
        db.execute(sql)
        ds = db.fetchall()
        
        cur_avg = connect_sqlserver('Reporting')        
        with closing(cur_avg) as db:
            sql_avg = """SELECT 
                            CAST(AVG(response_rate) AS DECIMAL(10,4)) avg_response_rate,
                            CAST(AVG((p.product_total) / (h.printed_quantity)) AS DECIMAL(10,4)) avg_product_total_per_card,
                            CAST(AVG((p.product_total) / (o.orders)) AS DECIMAL(10,2)) avg_product_total_per_order,
                            CAST(AVG(g.gross_revenue / h.printed_quantity) AS DECIMAL(10,4)) avg_gross_revenue_per_card,
                            CAST(AVG(g.gross_revenue / o.orders) AS DECIMAL(10,2)) avg_gross_revenue_per_order,
                            CONVERT(VARCHAR, CAST(SUM(g.gross_revenue - (p.product_total * .25) - h.list_invoice_amount - (h.printed_quantity * .00714) - (h.printed_quantity * .245) - (h.printed_quantity * .085) - (o.orders * 7.5)) AS MONEY), 1) sum_contribution_margin
                        FROM
                            SQLSERVER.Reporting.dbo.PostcardCampaignHistory h
                        JOIN
                            SQLSERVER.Reporting.dbo.vwResponsRatePerCampaign r ON r.source_code = h.source_code    
                        JOIN
                            SQLSERVER.Reporting.dbo.vwProductTotalPerCampaign p ON p.source_code = h.source_code    
                        JOIN    
                            SQLSERVER.Reporting.dbo.vwTotalOrdersPerCampaign o ON o.source_code = h.source_code        
                        JOIN
                            SQLSERVER.Reporting.dbo.vwGrossRevenuePerCampaign g ON g.source_code = h.source_code""" + where + qtr + """ AND """ + yr + qry 
            db.execute(sql_avg)
            ds_avg = db.fetchall()
        
        return ds, ds_avg
    
def insert_search_history(search_type, search_params):
    cur = connect_sqlrptserver()
    with closing(cur) as db:
        db.execute("EXEC dbo.insSearchHistory '" + search_type + "'," + "'" + search_params + "'")
        db.commit()
        
def get_search_history(search_type):
    cur = connect_sqlrptserver()  
    with closing(cur) as db:
        db.execute("EXEC dbo.getSearchHistory '" + search_type + "'")
        ds = db.fetchall()
        
    ls_history = []
    for row in ds:
        ls_history.append(row[0].replace('^^^', ' - '))
    
    
    return ls_history