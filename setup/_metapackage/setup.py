import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-account_invoice_reorder_lines',
        'odoo8-addon-partner_prepayment',
        'odoo8-addon-partner_prospect',
        'odoo8-addon-product_margin_classification',
        'odoo8-addon-sale_allotment',
        'odoo8-addon-sale_automatic_workflow',
        'odoo8-addon-sale_automatic_workflow_exception',
        'odoo8-addon-sale_cancel_reason',
        'odoo8-addon-sale_change_price',
        'odoo8-addon-sale_comment_propagation',
        'odoo8-addon-sale_delivery_split_date',
        'odoo8-addon-sale_exception_nostock',
        'odoo8-addon-sale_exceptions',
        'odoo8-addon-sale_last_price_info',
        'odoo8-addon-sale_line_price_properties_based',
        'odoo8-addon-sale_line_quantity_properties_based',
        'odoo8-addon-sale_order_add_variants',
        'odoo8-addon-sale_order_back2draft',
        'odoo8-addon-sale_order_calendar_event',
        'odoo8-addon-sale_order_line_date',
        'odoo8-addon-sale_order_line_description',
        'odoo8-addon-sale_order_line_variant_description',
        'odoo8-addon-sale_order_lot_selection',
        'odoo8-addon-sale_order_merge',
        'odoo8-addon-sale_order_price_recalculation',
        'odoo8-addon-sale_order_revision',
        'odoo8-addon-sale_order_type',
        'odoo8-addon-sale_order_type_sale_journal',
        'odoo8-addon-sale_order_unified_menu',
        'odoo8-addon-sale_order_weight',
        'odoo8-addon-sale_owner_stock_sourcing',
        'odoo8-addon-sale_packaging_price',
        'odoo8-addon-sale_partner_incoterm',
        'odoo8-addon-sale_partner_order_policy',
        'odoo8-addon-sale_payment_method',
        'odoo8-addon-sale_payment_method_automatic_workflow',
        'odoo8-addon-sale_payment_method_transaction_id',
        'odoo8-addon-sale_payment_term_interest',
        'odoo8-addon-sale_pricelist_discount',
        'odoo8-addon-sale_procurement_group_by_line',
        'odoo8-addon-sale_product_multi_add',
        'odoo8-addon-sale_product_set',
        'odoo8-addon-sale_product_set_layout',
        'odoo8-addon-sale_properties_dynamic_fields',
        'odoo8-addon-sale_properties_easy_creation',
        'odoo8-addon-sale_quick_payment',
        'odoo8-addon-sale_quotation_number',
        'odoo8-addon-sale_quotation_sourcing',
        'odoo8-addon-sale_quotation_sourcing_stock_route_transit',
        'odoo8-addon-sale_reason_to_export',
        'odoo8-addon-sale_rental',
        'odoo8-addon-sale_service_fleet',
        'odoo8-addon-sale_service_project',
        'odoo8-addon-sale_sourced_by_line',
        'odoo8-addon-sale_sourced_by_line_sale_transport_multi_address',
        'odoo8-addon-sale_start_end_dates',
        'odoo8-addon-sale_triple_discount',
        'odoo8-addon-sale_validity',
        'odoo8-addon-sales_team_security',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
