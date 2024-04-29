import frappe
from frappe.model.document import Document

from frappe import _
from frappe.query_builder.functions import IfNull, Sum
from frappe.utils import flt
# from frappe.utils.data import flt

from datetime import datetime




@frappe.whitelist()
def calc_highest_lowest_price(doc, method=None):
    frappe.msgprint("Calc Highest & Lowest Price", alert=True)


# ====================================================================
# def calculate_prices(doc, method):
#     highest_price = max(doc.price_list_rate, doc.online_rate_currency)
#     lowest_price = min(doc.price_list_rate, doc.online_rate_currency)
#     rate_of_change = 0
#     if doc.price_list_rate != 0:
#         rate_of_change = ((doc.online_rate_currency - doc.price_list_rate) / doc.price_list_rate) * 100
#
#     doc.highest_price = highest_price
#     doc.lowest_price = lowest_price
#     doc.rate_of_change = rate_of_change
#
#     # # doc.save()
#     # frappe.db.commit()
#     doc.save(ignore_permissions=True)
# ====================================================================



# # ============================================================



def calculate_prices(doc, method):
    highest_price = max(doc.price_list_rate, doc.online_rate_currency)
    lowest_price = min(doc.price_list_rate, doc.online_rate_currency)
    rate_of_change = 0
    if doc.price_list_rate != 0:
        rate_of_change = round(
            ((flt(doc.online_rate_currency) - flt(doc.price_list_rate)) / flt(doc.price_list_rate)) * 100, 2)

    doc.highest_price_data = highest_price
    doc.lowest_price_data = lowest_price
    doc.rate_of_change_data = rate_of_change

    # doc.save()

    frappe.db.sql("""
        UPDATE `tabItem Price`
        SET
            highest_price_data = %(highest_price)s,
            lowest_price_data = %(lowest_price)s,
            rate_of_change_data = ROUND(%(rate_of_change)s, 2)
        WHERE
            name = %(name)s
    """, {
        'highest_price': highest_price,
        'lowest_price': lowest_price,
        'rate_of_change': rate_of_change,
        'name': doc.name
    })



# ============================================================


# =======================   Calc  Date & Time (Update)  =====================================

def update_last_update_date_time(doc, method):
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    doc.set("date_a_0010", current_date)
    doc.set("time_a_0010", current_time)


# =================== Gap Calc. (Sell - Buy) / Buy =========================================

def gap_calc(doc, method):
    # doc.set("gap_data_a_0010", gap_calc_data)

    gap_calc_data = round(((doc.price_list_rate - doc.actual_buy_a0010) / doc.actual_buy_a0010), 2)
    doc.gap_data_a_0010 = gap_calc_data


# ============================================================








# ============================================================












# ==============================================================================
# ==============================================================================
# ==============================================================================




